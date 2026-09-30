# 예약 Radar 작업 연동

기존 주간 예약 작업 **전 세계 연구·교육 기회 탐색**을 이 저장소의 갱신 작업으로 사용합니다. 월요일 08:00 Asia/Seoul에 실행되며, 기존의 넓은 탐색 범위와 알림 기준을 유지합니다. 사용자가 설치한 ChatGPT의 `academic-opportunity-radar` 스킬을 우선 사용하고, 실행 환경에서 스킬을 직접 열 수 없으면 [AGENTS.md](../AGENTS.md)에 반영한 동일한 운영 원칙을 따릅니다.

실행 절차:

1. 작업 위치 `C:\godspell\radar`에서 최신 `origin`을 확인하고 동기화한다.
2. `AGENTS.md`, `README.md`, `docs/workflow.md`, `data/opportunities.csv`, `data/evaluations.csv`, `data/intake/`를 읽는다.
3. 공식 출처에서 새 항목과 기존 항목의 상태를 조사한다. `data/opportunities.csv`와 `data/evaluations.csv`를 갱신하고 `reports/weekly/YYYY-MM-DD.md`를 작성한다.
4. `scripts/validate.ps1`을 실행한다. 개인 정보나 인증 정보를 저장소에 넣지 않는다.
5. 변경 파일을 커밋하고 `origin`에 푸시한다. 실패하면 원인과 아직 반영되지 않은 내용을 사용자에게 알린다.

자동화의 실제 프롬프트와 대상 작업은 Codex 예약 작업 설정에서 관리합니다. 이 파일은 실행자가 저장소 안에서 따를 절차입니다.
