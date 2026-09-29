# papers/ — 논문 관리

- `pdf/`   : 분석할 논문 PDF 를 넣는 곳 (git 에는 올리지 않음). 파일명 권장: `<연도>-<제1저자>-<짧은제목>.pdf`
- `notes/` : `paper-analyzer` 가 만든 정독 노트 (`<연도>-<제1저자>-<짧은제목>.md`)
- `index.md` : 찾은/분석한 논문 목록 표. `literature-researcher`, `paper-comparator` 가 갱신한다.

사용 예
- `.\harness.ps1 paper "NPC inverter DC-link capacitor 노화진단에서 capacitor current harmonic 을 쓴 논문 찾아줘"`
- `.\harness.ps1 "papers/pdf/2021-Kim-xxx.pdf 논문 분석해줘"`
- `.\harness.ps1 "찾은 논문들 비교해서 내 연구와 가장 가까운 것 골라줘"`

메타데이터 검색 도구 (Claude 가 사용, 직접 써도 됨)
- `pwsh -File harness/tools/Search-Papers.ps1 -Query "NPC inverter DC-link capacitor condition monitoring" -Source all -Limit 20`
- `pwsh -File harness/tools/Search-Papers.ps1 -Citations 10.1109/xxxx` / `-References 10.1109/xxxx`
