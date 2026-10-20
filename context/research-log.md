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

## 2026-10-08 — 핵심 논문 Top 20 읽기 우선순위 선정
- 요청: 후보 약 100편(2026-09-29 조사)에서 DC-link·non-DC-link 포함 20편 선정, Tier S/A/B, 역할·읽기 목록 A/B/C
- Skill: paper-comparator, capacitor-aging-expert, npc-inverter-expert (새 검색 없음)
- 결과: `인버터 진단 논문/top20_reading_priority.md`, `top20_inverter_capacitor_comparison.csv`(UTF-8 BOM), `core_papers/` 워크시트 10개. Tier S = M3, M1, M2, M5, P26 / A = D2, D3, P20, R3, M4 / B = M29, M28, M10, P14, P32, P35, M25, M26, P39, D6. 전부 Abstract-level only.
- 주의: M4 서지 신뢰도 낮음(Xplore 10149200 확인 후 유지/강등). 저장 경로는 저장소 루트의 `인버터 진단 논문/` (바탕화면 체크아웃 시 `C:\Users\windows\Desktop\인버터 진단 논문\`)
- 다음: PDF 확보 → core_papers 워크시트 8–9절 작성(M3, M1, M2 우선) → MATLAB 민감도 실험 설계

## 2026-10-14 — DC-link 커패시터 On-board/Online 진단 Top 10 (전 응용)
- 요청: NPC 에 한정하지 않고, 기존 센서·정상 운전 조건에서 DC-link 커패시터 C/ESR/SoH 를 진단하는 저널 논문 10편 선정·정밀 비교
- Skill: literature-researcher → bibliographic-verifier(신규) → capacitor-aging-expert → paper-analyzer → paper-comparator (+npc-inverter-expert); 4개 응용 영역 병렬 탐색(검색 160회)
- 결과: 후보 저널 58편 → Top 10. Tier S: Ghadrdan 2022 TPEL(DF, 출력전류 재구성), Ribeiro 2025 IEEE/CAA JAS(NPC 고유 성분, C+ESR), Hasegawa & Hirose 2024 TIA(전류 센서 없이 C+ESR) / A: Örüklü & Ağalar 2025 TIE, Sundararajan 2020 TPEL, Zhang 2023 TPEL(T-type), Min/Choi/Blaabjerg 2026 TIE(in press) / B: Zhao 2023 TPEL, Wechsler 2012 TIA, Baumann 2024 TPEL. 파일: `인버터 진단 논문/dc_link_capacitor_onboard_top10.md`, `dc_link_capacitor_onboard_top10_comparison.csv`
- 한계: 출판사·DOI 호스트 DNS 차단 → 전 논문 Abstract-level only; Min 2026 TIE 권/쪽/DOI 미확인(in press), Zhang 2023·Meng 2023·Wu 2022 서지 재확인 필요; 풍력 IJEPES 2021 후보는 커패시터 논문 아님(제외)
- 다음: PDF 확보 후 Rank 1–3 본문 확인(재구성 수식·상호변조 성분 정의·정류 리플 해석식) → 내 NPC 재구성 전류 스펙트럼 feature 설계에 반영

## 2026-10-20 — 2-Level 인버터 DC-link 커패시터 노화진단 On-board/Online Top 10 (정밀 분석)
- 요청: 2-Level 3상 인버터(보조: 단상·정류기-인버터; NPC/MMC/FC 는 Reference only)에서 기존 센서로 DC-link 커패시터 노화를 On-board/Online 진단하는 저널 논문 10편을 선정하고, 논문별로 [1]–[26] 항목(토폴로지·분류/회귀·커패시터·노화 모사·샘플별 C/ESR·데이터셋·신호·센서·전처리·알고리즘·AI I/O·주장 vs 해석·온라인 유형·HW·실시간·실험 환경·운전조건·성능·강건성·장단점·관련성·비교·재현성)을 정리
- Skill: literature-researcher → bibliographic-verifier → capacitor-aging-expert → paper-analyzer → paper-comparator; 4개 병렬 스카우트(ML/DL, 해석적 True-Online, 드라이브·EV·PV, 상세 수치 채굴; 검색 160회)
- 결과: 저널 후보 50편 + 학회·미확정 15편 + Reference only 5편 → 10개 기준(각 10점) 채점 → Top 10. Tier S: Ghadrdan 2022 TPEL(출력 전류 재구성 → DF), Örüklü & Ağalar 2025 TIE(vdc PSD → ML 회귀 C), Lipnicki & Lewandowski 2017 PED(2L AC/DC/AC, 재구성 → ESR, ABB) / A: Hasegawa & Hirose 2024 TIA(전류 센서 없이 C+ESR), Sundararajan 2018 TIA(fsw 성분 ESR, 상용 드라이브 구현), Park & Kwak 2023 JEET(FFT 대역 → DNN/CNN/RNN/LSTM C+ESR), Machines 2022(전원 전류 + DWT → 학습 추정) / B: Zhao 2023 TPEL(과도 grey-box <1 %), Al-Wesabi 2025 RinE(ML 회귀 0.142 %), Liao 2020 MPE(노화 등급 90–100/80–90/<80 %). 파일: `인버터 진단 논문/2level_inverter_dc_link_capacitor_onboard_top10.md`, `.csv`(UTF-8 BOM), `core_papers/2level_top10/01–10_*.md`
- 한계: 출판사·리포지터리 호스트 차단으로 **전 논문 Abstract-level only**. 샘플별 C/ESR·Radd·클래스별 C/ESR·데이터셋 분할·DSP/MCU 부품·샘플링·추론 시간은 10편 모두 스니펫에 없음(예외: Liao 7500 µF·90/80 % 구간, Al-Wesabi 오차 수치) → 전부 `Not reported / Full text verification required`. Örüklü 의 '<2 %·GPR·다중 조건' 은 2026 TPEL 후속 귀속 가능, Machines 2022 저자·Hasegawa 2024 DOI·Al-Wesabi DOI 미확인
- 핵심 발견: 2L 계열 True Online 은 "상전류 기반 재구성/feature" 와 "vdc 단독" 두 흐름; C+ESR 동시는 Hasegawa(정류 리플)·Park & Kwak(DL)뿐이며 인버터 스위칭 신호 기반 동시 추정 저널 0편; 분류 저널은 Liao 1편(3 구간); AI 의 DSP/MCU 추론 시연 저널 0편 → 내 연구 차별점 = 재구성 전류 스펙트럼 빈 → C·ESR 동시 회귀/등급 + 다중 운전조건 + on-board 추론
- 다음: (1) 로컬에서 Search-Papers.ps1 로 부록 A 서지 확인 (2) OA 본문 확보(Zhao 2023 VBN, Lipnicki PDF, Machines, Al-Wesabi, Liao, Amaral) → core_papers 워크시트 NR 채우기 (3) 20절 설계안대로 MATLAB C×ESR 격자 + Radd 실험 계획 수립

## 2026-10-20 — 2-Level Top 10 중 핵심 5편 PDF 원문 정밀 분석
- 요청: 사용자가 제공한 PDF(Ghadrdan 2022 TPEL, Lipnicki 2017 PED, Hasegawa & Hirose 2024 TIA, Örüklü & Ağalar 2025 TIE, Park & Kwak 2023 JEET)를 원문 기준으로 36항목(서지·토폴로지·정격·커패시터·task·노화 모사·샘플별 C/ESR·Radd·데이터셋·신호·센서·재구성·샘플링·전처리·feature·알고리즘·AI 구조·contribution·online 유형·on-board·HW·성능·강건성·한계·재현 조건) 추출, 5편 비교표, 연구 방향 A/B/C 비교
- Skill: paper-analyzer → capacitor-aging-expert → paper-comparator → paper-code-bridge(재현 조건)
- 결과: `인버터 진단 논문/core_papers/2level_top10/01,02,03,04,06_*.md` 를 원문 기준으로 갱신(Evidence: Full text), `인버터 진단 논문/2level_top5_fulltext_comparison.md` 신규. 원문 확인으로 바뀐 사실: Ghadrdan Radd 0/0.1/0.22/0.34 Ω × C 5단계 20세트·실험은 i_inv 센서 측정·FFT 는 PC; Lipnicki Radd 0/0.02/0.03/0.11/0.42 Ω·최대 오차 11 %·영벡터 트리거 시간영역; Hasegawa C 1100/1000 µF × Radd 150 mΩ·360/720 Hz 2주파수 연립·Excel 오프라인; Örüklü 단상 H-bridge 출력·GPR·975/175 샘플·MPE <1 %·50 kHz 2500점; Park & Kwak i_C 센서 사용·병렬 25쌍 122–650 µF·오차표 공개·샘플링/구조 NR
- 판단: 추천 1순위 = A+B 하이브리드(상전류+스위칭 상태 재구성 전류의 fsw/측대파/저주파 Goertzel 빈 + vdc fsw 빈 → 2주파수 임피던스 연립으로 C·ESR 초기 추정 + 운전점 변수 GPR/소형 DNN 보정, DSP 구현), 2순위 = 같은 데이터셋으로 경량 1D-CNN/DNN 회귀·3등급 분류 + MCU 추론 시간 보고; B 단독은 Örüklü 2025 와 중복
- 다음: Simulink 모델(정류기 유무 2종)로 재구성 전류 vs 측정 i_C 스펙트럼 비교(Ghadrdan Fig. 9 재현) → C 5 × Radd 4 × 운전점 데이터셋 설계서 → 나머지 Top 10 PDF 확보 시 동일 36항목 갱신
