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

## 2026-09-30 — train80.py 운전조건 3D 분포도 수정
- 요청: Train/Unseen 운전조건 3D projection 그림의 축 화살표 방향 수정 + 조건 위치 구분되게 펼치기
- Skill: (없음, matplotlib 작도)
- 결과: `workspace/results/plot_operating_conditions_3d.py` → `3d_projection.png`. 축은 nominal(60 Hz/8 kHz/100 V)에서 교차, 증가 방향 끝에만 화살표; half-axis |x|^0.6 스케일로 중심부 확장(SPREAD_GAMMA=1.0 이면 선형); nominal 의 R 10/22/47 Ω 점(ID 7, 8, 12)은 원점에 크기를 달리해 겹쳐 표시(큰 것이 뒤); 시점은 f0=30 Hz·fsw=2 kHz 사분면 쪽(azim −146°); ID·표 없는 버전 `3d_projection_clean.png` 동시 출력; 원점 3점을 리더선으로 펼친 `3d_projection_fan(_clean).png` 추가; 점 ID ↔ 우측 조건표
- 한계: 원래 plot 코드는 받지 못해 train80.py 조건 목록으로 재작성. 1조건 파일은 코드에 R 값이 없어 R1=47, R4=10, 나머지=22 Ω 로 가정 (사용자 설명·기존 그림 기준)
