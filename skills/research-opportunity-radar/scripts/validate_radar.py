#!/usr/bin/env python3
"""Validate Radar CSVs without PowerShell; never modify files or access the network."""

import argparse
import csv
from datetime import date
from pathlib import Path
import sys


OPPORTUNITY_FIELDS = (
    'id name category status event_start event_end deadline location format '
    'undergraduate korean_eligible cost funding source_url last_checked next_action notes'
).split()
EVALUATION_FIELDS = (
    'id academic_fit experiential_value competition preparation_burden priority '
    'rationale last_evaluated'
).split()
STATES = {'apply', 'watch', 'attend', 'committed', 'closed', 'review'}


def read_csv(path, required):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        columns = reader.fieldnames or []
        missing = set(required) - set(columns)
        if missing:
            raise ValueError(f'{path.name}: missing columns: {", ".join(sorted(missing))}')
        if len(columns) != len(set(columns)):
            raise ValueError(f'{path.name}: duplicate columns')
        rows = list(reader)
    for line, row in enumerate(rows, 2):
        if None in row or any(value is None for value in row.values()):
            raise ValueError(f'{path.name}:{line}: column count does not match header')
    return rows


def check_date(value, context):
    if value:
        try:
            parsed = date.fromisoformat(value)
        except ValueError as error:
            raise ValueError(f'{context}: invalid ISO date: {value}') from error
        if parsed.isoformat() != value:
            raise ValueError(f'{context}: expected YYYY-MM-DD: {value}')


def validate(root):
    opportunities = read_csv(root / 'data/opportunities.csv', OPPORTUNITY_FIELDS)
    ids = set()
    for row in opportunities:
        item_id = row['id']
        if not all(row[key].strip() for key in ('id', 'name', 'source_url')):
            raise ValueError('opportunities.csv: missing id, name, or source URL')
        if item_id in ids:
            raise ValueError(f'opportunities.csv: duplicate id: {item_id}')
        ids.add(item_id)
        if row['status'] not in STATES:
            raise ValueError(f'{item_id}: invalid status: {row["status"]}')
        if not row['source_url'].startswith('https://'):
            raise ValueError(f'{item_id}: source URL must start with https://')
        for key in ('event_start', 'event_end', 'deadline', 'last_checked'):
            check_date(row[key], f'{item_id}.{key}')

    evaluations = read_csv(root / 'data/evaluations.csv', EVALUATION_FIELDS)
    evaluated_ids = set()
    for row in evaluations:
        item_id = row['id']
        if item_id not in ids:
            raise ValueError(f'evaluations.csv: unknown opportunity: {item_id}')
        if item_id in evaluated_ids:
            raise ValueError(f'evaluations.csv: duplicate id: {item_id}')
        evaluated_ids.add(item_id)
        for key in ('academic_fit', 'experiential_value', 'competition', 'preparation_burden'):
            if not row[key].strip():
                raise ValueError(f'{item_id}: missing {key}')
        check_date(row['last_evaluated'], f'{item_id}.last_evaluated')
    return len(opportunities), len(evaluations)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True, help='Existing Radar repository')
    args = parser.parse_args()
    try:
        count, evaluated = validate(args.root)
    except (OSError, ValueError, csv.Error) as error:
        print(f'Validation failed: {error}', file=sys.stderr)
        return 1
    print(f'Validated {count} opportunities and {evaluated} evaluations.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
