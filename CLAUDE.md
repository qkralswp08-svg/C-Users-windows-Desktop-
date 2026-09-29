# 캡 노화진단 — 프로젝트 지침 (Claude Code 가 자동으로 읽는 파일)

이 폴더는 **3-Level NPC 인버터의 DC-Link 커패시터 노화진단** 연구 작업공간이다.
MATLAB(시뮬레이션·신호 생성·FFT), Python(전처리·CNN), 데이터, 논문, 결과가 함께 있고,
`harness.ps1` 로 실행되는 Research Harness 가 Skill 단위 작업 지침을 제공한다.

## 프로젝트 핵심 Context
@context/project-context.md

## 작업 원칙
1. **탐색 후 작업**: 프로젝트 전체를 한 번에 읽지 말고 `Glob`/`Grep` 으로 필요한 파일만 찾아 읽는다. 하네스 폴더(`harness/`, `.claude/`, `context/`, `logs/`, `workspace/`, `papers/`)는 연구 코드가 아니다.
2. **연구 코드 보호**: MATLAB/Python 연구 코드는 분석·읽기는 자유롭게 하되, 수정은 문제·원인·영향·수정 방향을 먼저 설명하고 사용자 확인 후 최소 범위로 한다. 파일 삭제, 덮어쓰기, 폴더 이동, 대규모 리팩토링, git reset, 대량 패키지 설치는 하지 않는다 (필요하면 제안만).
3. **사실 / 해석 / 추론 구분**: 파일·논문에서 직접 확인한 것, 그 결과에 대한 물리적 해석, 스위칭 상태·수식에서 도출한 추론을 구분해 쓴다. 확인하지 못한 것은 "확인하지 못함" 이라고 쓴다. 논문의 제목/초록만 보고 세부 내용을 단정하지 않는다.
4. **한국어로 답하되** 변수명·함수명·전문용어(ESR, NPC, SVPWM, FFT 등)는 원문 그대로 쓴다.
5. **바이너리 한계**: `.mat`, `.slx`, `.fig`, 모델 가중치는 직접 읽을 수 없다. 이를 만든/읽는 코드로 추정하고 그렇게 표시한다.

## Skill 사용
- Skill 은 `.claude/skills/<이름>/SKILL.md` 에 있다. 하네스가 만든 작업 지시서(`harness/runs/*-brief.md`)에 선택된 Skill 본문이 들어 있으며, 필요하면 다른 Skill 파일도 읽어 적용한다. `/skill-name` 으로 직접 호출할 수도 있다.
- 논문 메타데이터 검색 보조 도구: `harness/tools/Search-Papers.ps1` (사용법은 `literature-researcher` Skill 참고).

## Context 유지
- 핵심 정보는 `context/project-context.md` (짧게 유지, 잘못된 내용을 발견하면 해당 항목만 수정).
- 작업 기록은 `context/research-log.md` 에 항목 단위로 추가 (지시서의 마무리 형식). 전체 대화를 저장하지 않는다.
- 용어는 `context/glossary.md`. 논문 목록은 `papers/index.md`, 논문 노트는 `papers/notes/`.
- 결과 문서는 `workspace/results/` (일회성 실행 결과), `workspace/reports/` (보고서).
