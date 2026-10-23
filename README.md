# Radar

연구·교육 기회를 발견하고, 공식 출처를 확인하며, 다음 행동까지 추적하는 저장소입니다. 기준 시간대는 Asia/Seoul입니다.

필요할 때 [research-opportunity-radar skill](skills/research-opportunity-radar/SKILL.md)로 전체 또는 분야별 기회를 탐색합니다. [AGENTS.md](AGENTS.md)와 [운영 규칙](docs/workflow.md)에 따라 찾은 기회를 기존 목록·평가·날짜별 보고서에 연결합니다. 개인 배경·지원 결정은 로컬 전용 파일에서 읽고 skill에 복제하지 않습니다.

예: “논리학·복잡도 쪽 학교나 워크숍을 찾아주세요”, “미국에서 여름에 할 만한 연구 기회를 찾아주세요”, “Lean 관련 short paper 제출처를 찾아 Radar에 정리해주세요”. 명시적으로는 `$research-opportunity-radar`를 사용할 수 있습니다.

## 폴더 구조

```text
radar/
├─ README.md                    운영 방식과 폴더 안내
├─ AGENTS.md                    Radar의 프로젝트 실행 지침
├─ data/
│  ├─ opportunities.csv         현재 추적하는 기회의 단일 목록
│  ├─ evaluations.csv           학술 적합성·경험 가치·경쟁·준비 부담
│  └─ intake/                   과거 Radar 보고에서 수집한 원본 링크
├─ reports/
│  └─ daily/                    예약 작업의 날짜별 변경 요약
├─ skills/research-opportunity-radar/  필요할 때 호출하는 탐색·평가·기록 skill 원본
├─ docs/
│  ├─ workflow.md               조사·상태 변경·알림 기준
│  ├─ automation.md             예약 작업과 Git 동기화 절차
│  └─ user-context.md           공개 가능한 적합성 판단 기준
└─ scripts/
   └─ validate.ps1              목록의 기본 형식 검사
```

## 어디부터 볼까

- [10월23일 제공 Radar 정리](reports/daily/2026-10-23.md): Lean Kernel Challenge·SODA 장학·LNCC·ICTP 신규 추적과 기존 Aalto·ESSLLI 보완.

- [10월 12·14·19일 Radar 통합 정리](reports/reviews/2026-10-19-pasted-radar.md): 17개 기회, 신규 LLNL·PriSC·Albany, 공식 재검증·마감·준비물과 확인이 남은 조건.
- [현재 기회 목록](data/opportunities.csv): 항목별 상태, 마감, 공식 링크, 다음 행동.
- [정성 평가](data/evaluations.csv): 학술 적합성과 현지 경험 가치를 별도로 평가.
- [기존 Radar 링크 84개](data/intake/2026-09-30-radar-links.csv): Student & Research Radar, CAU Daily Radar, 레이더 일정 정리에서 가져온 원본. 이 목록은 과거 보고의 링크 인덱스이며 현재 모집 상태를 보증하지 않습니다.
- [운영 규칙](docs/workflow.md): 중복 처리와 검증 기준.
- [적합성 판단 기준](docs/user-context.md): 공개 가능한 일반 원칙. 개인 맥락은 Git에서 제외한 `docs/user-private.local.md`에만 둡니다.

상태는 `apply`(신청 검토), `watch`(공고·등록 대기), `attend`(청강·시청), `committed`(이미 확정), `closed`(종료), `review`(재확인 필요) 중 하나입니다. 과거의 날짜나 자격을 재검증하지 못한 항목은 `review`로 둡니다.

개인 신청서, 성적, 여권, 건강 정보는 이 저장소에 기록하지 않습니다.
