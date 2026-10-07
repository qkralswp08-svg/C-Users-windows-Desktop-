# 연구 작업 기록 (항목 단위, 최신이 아래)

> 하네스 지시서의 마무리 단계에서 Claude 가 3~6줄 항목을 추가한다. 직접 적어도 된다.
> 형식: `## YYYY-MM-DD — 제목` / 요청 / Skill / 결과 / 다음
> 오래된 항목은 정리해서 `workspace/reports/` 로 옮기고 여기에는 최근 것만 남긴다 (하네스는 마지막 N개만 지시서에 포함).

## 2026-09-29 — 하네스 구축
- 요청: 캡 노화진단 프로젝트용 Research Harness 구성
- Skill: (없음)
- 결과: harness.ps1, Skill 13개, Context/논문/로그 구조 생성
- 다음: `.\harness.ps1 init` 으로 project-context.md 초안 작성

## 2026-09-29 — 인버터 커패시터 노화진단 기술 동향 문헌조사 (저널 중심)
- 요청: DC-link 에 한정하지 않은 인버터 커패시터 CM 최신 동향, Research Gap, 새 진단법 설계 근거
- Skill: literature-researcher, paper-analyzer, paper-comparator, capacitor-aging-expert, npc-inverter-expert
- 결과: 저널 논문 약 100편(리뷰 7, DC-link 44, 멀티레벨 29, 데이터 기반 22, 소재 10) 분류; 핵심 10편 선정; Gap 12개; 연구 후보 T1–T6. 보고서 `workspace/reports/2026-09-29-inverter-capacitor-condition-monitoring-survey.md`, 노트 `papers/notes/2026-09-29-core-papers-abstract-level.md`, 출처 `papers/notes/2026-09-29-survey-sources.md`, `papers/index.md` 38행 추가
- 한계: 컨테이너 네트워크 정책으로 학술 사이트 차단 → **전 논문 본문 확인 불가(초록 수준)**, 서지 일부 (확인 필요); 검색 예산 소진으로 일부 검색 미실행
- 핵심 발견: 3L-NPC CM 저널은 2024–2026 4편(M1–M4)뿐이며 주입형 우세, M3 만 무주입 고유 성분; 스위치 전류 스펙트럼·자연 NP 전류 스펙트럼·출력 짝수 고조파를 노화 feature 로 쓴 저널 없음; NPC×ML/CNN 없음
- 다음: (1) 네트워크 허용 후 M3, M1, M2, P26, M5, D3, D2, P20 정독 (2) MATLAB 민감도 실험(C1/C2/ESR vs 부하/변조 스윕, iSa2·ia·iNP·vNP 고조파) (3) Search-Papers.ps1 로 서지 (확인 필요) 채우기

## 2026-10-07 — AI 활용 보고서 + 커패시터 노화진단 AI 코드 검증 (다중 에이전트)
- 요청: 창업계획서 PDF·Python 코드 2종 기반 「AI 활용 보고서」(선행연구 조사 → 연구실 매핑 → 코드 검증 → 연구주제 제안), 산출물 01–07
- Skill: literature-researcher, paper-comparator, python-analyzer, capacitor-aging-expert, signal-analyzer, report-writer, dataviz (에이전트 A·B1·B2·C·D·E·F·G·H 병렬)
- 결과: `workspace/reports/2026-10-07-ai-utilization/` (01–07, agent_reports/, data/, figures/, verification_code/). 외부 후보 84편·연구실 29편 검증(WebSearch 스니펫 수준, 한도 200회 소진), 핵심 18편 비교. 원본 코드 무수정 실행(TF 2.21, 4모델×3조합, 합성 데이터) + 검증 도구(LOCO·라벨 뒤집기·이득·seed)
- 핵심 발견: internal VAL/TEST = 같은 녹화 인접 window(FAIL, 라벨 무관 합성에서도 95%↑); unseen 은 학습 범위 내 내삽만; 정상·노화 쌍 설계로 운전조건 shortcut 은 없으나 측정 블록·커패시터 개체 교락으로 "노화 학습" 미입증; 진폭 보존 입력 → 센서 이득 민감; 비교용 파일②는 1908행 절단본
- 주의: 업로드 코드의 데이터셋은 토폴로지(2-level/NPC)·측정 지점이 코드에 기록되지 않음 — project-context 의 3L-NPC 설정과 같은 실험인지 미확인
- 다음: (1) 실측 tek*.txt 로 검증 도구 실행(LOCO, 블록별 재집계, 이득 시험) (2) 커패시터 개체 ID·C/ESR·온도·Vdc 기록 (3) V2 서지 doi.org 확인
