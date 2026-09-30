# Radar

연구·교육 기회를 발견하고, 공식 출처를 확인하며, 다음 행동까지 추적하는 저장소입니다. 기준 시간대는 Asia/Seoul입니다.

## 폴더 구조

```text
radar/
├─ README.md                    운영 방식과 폴더 안내
├─ AGENTS.md                    Radar 스킬의 프로젝트 실행 지침
├─ data/
│  ├─ opportunities.csv         현재 추적하는 기회의 단일 목록
│  ├─ evaluations.csv           학술 적합성·경험 가치·경쟁·준비 부담
│  └─ intake/                   과거 Radar 보고에서 수집한 원본 링크
├─ reports/
│  └─ daily/                    예약 작업의 날짜별 변경 요약
├─ docs/
│  ├─ workflow.md               조사·상태 변경·알림 기준
│  └─ automation.md             예약 작업과 Git 동기화 절차
└─ scripts/
   └─ validate.ps1              목록의 기본 형식 검사
```

## 어디부터 볼까

- [현재 기회 목록](data/opportunities.csv): 항목별 상태, 마감, 공식 링크, 다음 행동.
- [정성 평가](data/evaluations.csv): 학술 적합성과 현지 경험 가치를 별도로 평가.
- [기존 Radar 링크 84개](data/intake/2026-09-30-radar-links.csv): Student & Research Radar, CAU Daily Radar, 레이더 일정 정리에서 가져온 원본. 이 목록은 과거 보고의 링크 인덱스이며 현재 모집 상태를 보증하지 않습니다.
- [운영 규칙](docs/workflow.md): 중복 처리와 검증 기준.

상태는 `apply`(신청 검토), `watch`(공고·등록 대기), `attend`(청강·시청), `committed`(이미 확정), `closed`(종료), `review`(재확인 필요) 중 하나입니다. 과거의 날짜나 자격을 재검증하지 못한 항목은 `review`로 둡니다.

개인 신청서, 성적, 여권, 건강 정보는 이 저장소에 기록하지 않습니다.
