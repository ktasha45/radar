$ErrorActionPreference = 'Stop'
$repo = Split-Path $PSScriptRoot -Parent
$path = Join-Path $repo 'data/opportunities.csv'
$rows = @(Import-Csv -LiteralPath $path)
$required = @('id','name','category','status','event_start','event_end','deadline','location','format','undergraduate','korean_eligible','cost','funding','source_url','last_checked','next_action','notes')
$columns = @((Get-Content -LiteralPath $path -TotalCount 1).Split(','))
foreach ($field in $required) {
    if ($columns -notcontains $field) { throw "Missing column: $field" }
}
$ids = @{}
$allowed = @('apply','watch','attend','committed','closed','review')
foreach ($row in $rows) {
    if (-not $row.id -or -not $row.name -or -not $row.source_url) { throw "Missing id, name, or source URL" }
    if ($ids.ContainsKey($row.id)) { throw "Duplicate id: $($row.id)" }
    $ids[$row.id] = $true
    if ($allowed -notcontains $row.status) { throw "Invalid status: $($row.id)" }
    if ($row.source_url -notmatch '^https://') { throw "Invalid URL: $($row.id)" }
    foreach ($field in @('event_start','event_end','deadline','last_checked')) {
        $value = $row.$field
        if ($value -and $value -notmatch '^\d{4}-\d{2}-\d{2}$') { throw "Invalid $field in $($row.id)" }
    }
}
Write-Output "Validated $($rows.Count) opportunities."
$evaluationPath = Join-Path $repo 'data/evaluations.csv'
$evaluations = @(Import-Csv -LiteralPath $evaluationPath)
$evaluationIds = @{}
foreach ($evaluation in $evaluations) {
    if (-not $ids.ContainsKey($evaluation.id)) { throw "Evaluation without opportunity: $($evaluation.id)" }
    if ($evaluationIds.ContainsKey($evaluation.id)) { throw "Duplicate evaluation: $($evaluation.id)" }
    $evaluationIds[$evaluation.id] = $true
    foreach ($field in @('academic_fit','experiential_value','competition','preparation_burden')) {
        if (-not $evaluation.$field) { throw "Missing $field in evaluation $($evaluation.id)" }
    }
}
Write-Output "Validated $($evaluations.Count) evaluations."
