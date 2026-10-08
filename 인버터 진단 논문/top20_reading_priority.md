# 인버터 커패시터 노화진단 — 핵심 논문 Top 20 읽기 우선순위

- 작성일: 2026-10-08
- 입력: 2026-09-29 문헌조사(저널 중심, 후보 약 100편)와 그 핵심 10편 평가. 새 검색은 하지 않았다.
- 방법: Harness Skill `paper-comparator` + `capacitor-aging-expert` + `npc-inverter-expert` 기준으로 재평가.
- 파일: `top20_reading_priority.md`(이 문서), `top20_inverter_capacitor_comparison.csv`(동일 내용의 표, UTF-8 BOM, Excel 호환), `core_papers/`(Tier S·A 10편 읽기 워크시트).

## 0. 근거 수준 — 반드시 먼저 읽을 것

**20편 전부 `Abstract-level only` 이다.** 조사 당시 클라우드 환경의 네트워크 정책이 IEEE Xplore·ScienceDirect·Springer·Wiley·MDPI·DOI·Crossref·Semantic Scholar 접근을 차단해 본문을 한 편도 열지 못했다. 따라서

- "같은 점/다른 점/집중할 부분" 은 초록과 검색 스니펫에 드러난 범위에서 쓴 것이며, 본문을 확인한 것처럼 쓰지 않았다. 본문에서만 알 수 있는 항목은 "미확인" 으로 적었다.
- 서지의 `(확인 필요)` 는 화면에 보이지 않아 기록하지 않은 값이다. DOI·권·쪽을 추정해 채우지 않았다.
- M4(Tier A-10)는 제목·권·쪽 자체가 검색 스니펫 추정이라 신뢰도가 낮다. IEEE Xplore 에서 실체를 확인한 뒤 유지/강등을 결정할 것.
- 서지 채우기: 로컬 PC 에서 `pwsh -File harness\tools\Search-Papers.ps1 -Query "<제목>" -Source all`.

## 1. 선정 기준과 방식

| 기준(0–2점) | 의미 |
|---|---|
| 3L-NPC/멀티레벨 관련성 | 2 = NPC/T-type 직접, 1 = 다른 멀티레벨(MMC, CHB) 또는 리뷰 포함, 0 = 2L/일반 |
| 노화·열화 직접 진단 | 2 = C/ESR/SoH 추정 또는 노화 분류가 목적, 1 = 부수적, 0 = 아님 |
| C/ESR/SOH 추정 | 2 = 둘 이상 또는 개별 추정, 1 = 하나/미확인, 0 = 없음 |
| 전류/전압 파형 사용 | 2 = 전류·전압 파형(측정 또는 재구성), 1 = 전압만/스니펫 미상, 0 = 파형 아님 |
| Harmonic/FFT/STFT/Wavelet | 2 = 스펙트럼 성분이 핵심, 1 = 리플 추출 정도, 0 = 시간영역/없음 |
| 기존 인버터 센서만 | 2 = 명시, 1 = 미확인/부분, 0 = 추가 HW |
| Online 진단 | 2 = 정상 운전 중(주입 포함), 1 = quasi-online/미확인, 0 = offline |
| AI 적용 가능성 | 2 = AI 논문 또는 바로 feature 화 가능, 1 = 간접, 0 = 낮음 |
| 타 토폴로지 이전 | 2 = 쉬움, 1 = 제한, 0 = 불가/해당 없음 |

Tier 는 점수 합계만으로 정하지 않았다. **"내 연구(3L-NPC, 무주입, 스위치/커패시터/중성점 전류 고조파, CNN, C1/C2 개별)의 경쟁 선행인가"** 와 **"내가 당장 가져다 쓸 방법·모델·AI 선례인가"** 를 먼저 보고, 점수는 투명성을 위한 보조 지표로 함께 적었다. 역할은 다음 넷 중 하나(복수 가능): **Core competitor**(같은 문제를 푼 경쟁 선행) / **Methodology donor**(방법·신호 처리·재구성 기법 공여) / **Physical-model reference**(물리·회로 모델·분류 체계) / **AI reference**(데이터 기반 설계 선례).

DC-link 와 non-DC-link 를 모두 포함했다: non-DC-link 는 MMC 서브모듈 커패시터(M28, M25, M26)와 CHB 셀 커패시터(M10) 4편이다. AC 측 필터 커패시터(E1, E2), 스너버·클램프 커패시터 논문은 초록에 방법이 거의 드러나지 않거나 저널 논문이 없어 제외했다(조사 보고서 4절).

## 2. Tier 요약

### Tier S — 가장 중요한 5편
| 순위 | Tier | ID | 제목 | 제1저자 | 연도 | 저널 | DOI | 역할 | 점수 | 근거 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | S | M3 | Online Estimation of DC-link Capacitor Parameters of Three-Level NPC Converters Using Inherent Signals Analysis | R. L. A. Ribeiro | 2025 | IEEE/CAA Journal of Automatica Sinica | 10.1109/JAS.2025.125159 | Core competitor | 16 | Abstract-level only |
| 2 | S | M1 | An Online Condition Monitoring Method for DC-Link Capacitors of Three-Level NPC Inverters Based on Charge-Discharge Profile | K. J. Min | 2026 | IEEE Transactions on Industrial Electronics | 10.1109/TIE.2026.3672764 (확인 필요) | Core competitor | 14 | Abstract-level only |
| 3 | S | M2 | Online condition monitoring for DC-link capacitors of three-level NPC converters using noninvasive signal injection | R. L. A. Ribeiro | 2024 | Computers and Electrical Engineering | 10.1016/j.compeleceng.2024.109577 | Core competitor / Methodology donor (Wavelet) | 16 | Abstract-level only |
| 4 | S | M5 | A Comprehensive Method for Online Switch Fault Diagnosis and Capacitor Condition Monitoring of Three-Level T-Type Inverters | W. Zhang | 2023 | IEEE Transactions on Power Electronics | 10.1109/TPEL.2023.3262758 | Physical-model reference / Methodology donor | 14 | Abstract-level only |
| 5 | S | P26 | Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor | M. Ghadrdan | 2022 | IEEE Transactions on Power Electronics | 10.1109/TPEL.2022.3153842 | Methodology donor | 15 | Abstract-level only |

### Tier A — 다음 5편
| 순위 | Tier | ID | 제목 | 제1저자 | 연도 | 저널 | DOI | 역할 | 점수 | 근거 |
|---|---|---|---|---|---|---|---|---|---|---|
| 6 | A | D2 | Deep learning-based estimation technique for capacitance and ESR of input capacitors in single-phase DC/AC converters | H.-J. Park | 2022 | Journal of Power Electronics | 10.1007/s43236-021-00366-x | AI reference | 14 | Abstract-level only |
| 7 | A | D3 | Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters | (저자 확인 필요) | 2025 | IEEE Transactions on Industrial Electronics | (확인 필요) | AI reference | 15 | Abstract-level only |
| 8 | A | P20 | Condition Monitoring of DC-Link Capacitors Using Goertzel Algorithm for Failure Precursor Parameter and Temperature Estimation | P. Sundararajan | 2020 | IEEE Transactions on Power Electronics | 10.1109/TPEL.2019.2951859 | Methodology donor | 14 | Abstract-level only |
| 9 | A | R3 | An Overview of Condition Monitoring Techniques for Capacitors in DC-Link Applications | Z. Zhao | 2021 | IEEE Transactions on Power Electronics | 10.1109/TPEL.2020.3023469 | Physical-model reference (분류 체계·용어) | 12 | Abstract-level only |
| 10 | A | M4 | Noninvasive Online Capacitor Monitoring Method for Three-Level Converter Based on Active Neutral-Point Current Adjustment | (저자 확인 필요) | 2024 | IEEE Transactions on Industrial Electronics | (확인 필요) | Core competitor | 15 | Abstract-level only |

### Tier B — 나머지 10편
| 순위 | Tier | ID | 제목 | 제1저자 | 연도 | 저널 | DOI | 역할 | 점수 | 근거 |
|---|---|---|---|---|---|---|---|---|---|---|
| 11 | B | M29 | Analysis of dc-link capacitor current in three-level neutral point clamped and cascaded H-bridge inverters | G. I. Orfanoudakis et al. | 2013 | IET Power Electronics | 10.1049/iet-pel.2012.0422 | Physical-model reference | 9 | Abstract-level only |
| 12 | B | M28 | Practical Online Condition Monitoring of DC-Link Capacitors in Modular Multilevel Converters: A Comparative Approach | (저자 확인 필요) | 2024 | IEEE Open Journal of Power Electronics (Xplore 미확인; TechRxiv 프리프린트 'accepted') | 10.1109/OJPEL.2024.3387829 (확인 필요) | Methodology donor (온도 효과 분리) | 16 | Abstract-level only |
| 13 | B | M10 | Capacitor Condition Monitoring Method for Low-Capacitance StatComs: An Online Approach Using the Inherent Second-Harmonic Oscillations | E. R. Ramos | 2023 | IEEE Transactions on Power Electronics | (확인 필요) | Methodology donor (고유 고조파 → 임피던스) | 15 | Abstract-level only |
| 14 | B | P14 | Noninvasive Technique for DC-Link Capacitance Estimation in Single-Phase Inverters | M. W. Ahmad | 2018 | IEEE Transactions on Power Electronics | 10.1109/TPEL.2017.2762341 | Methodology donor (짝수 고조파 → C) | 14 | Abstract-level only |
| 15 | B | P32 | Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor in a PWM Inverter With a Six-Pulse Diode Rectifier | K. Hasegawa et al. | 2023 | IEEJ Journal of Industry Applications | (확인 필요; J-STAGE) | Methodology donor (모델 기반 전류 재구성) | 13 | Abstract-level only |
| 16 | B | P35 | Discharge-Based Condition Monitoring for Electrolytic DC-Link Capacitors | J. Baumann | 2024 | IEEE Transactions on Power Electronics | (확인 필요) | Physical-model reference (온도 의존성·SoH) | 12 | Abstract-level only |
| 17 | B | M25 | Online evaluation method for MMC submodule capacitor aging based on CapAgingNet | X. Deng | 2025 | Global Energy Interconnection | (확인 필요) | AI reference (DL 분류, 시뮬 데이터) | 11 | Abstract-level only |
| 18 | B | M26 | Neural Network-Based Submodule Capacitance Monitoring in Modular Multilevel Converters for Renewable Energy Conversion Systems | M. Asnoun | 2026 | Electronics | 10.3390/electronics15071486 | AI reference (물리 내장 NN) | 15 | Abstract-level only |
| 19 | B | P39 | Non-Intrusive Capacitor Monitoring in Photovoltaic Inverters Based on MPPT-Induced Voltage Transients | M. K. P. Muhammed Ramees | 2026 | IEEE Transactions on Power Electronics | (확인 필요) | Methodology donor (자연 여기 + 출력전류로 커패시터 전류 추정) | 13 | Abstract-level only |
| 20 | B | D6 | DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs | (저자 확인 필요; Kwak 그룹 추정) | 2023 | Journal of Electrical Engineering & Technology | 10.1007/s42835-023-01424-z | AI reference (주파수 대역 입력 DL, 3상) | 14 | Abstract-level only |

### 역할별 분포
| 역할 | 논문 |
|---|---|
| Core competitor | M3, M1, M2, M4 |
| Methodology donor | M2(Wavelet), M5, P26, P20, M28, M10, P14, P32, P39 |
| Physical-model reference | M5, R3, M29, P35 |
| AI reference | D2, D3, M25, M26, D6 |

(해석) 경쟁 선행 4편이 모두 2024–2026 년의 3L-NPC 논문이고 그중 3편이 주입형, 1편(M3)이 무주입 모델 기반이다. 데이터 기반(AI) 선례는 모두 2L·단상·MMC 이며 NPC 는 없다. 따라서 내 연구의 위치는 "M3 의 무주입 고유 성분 접근 × D2/D6 의 고조파→NN 접근 × M1 의 C1/C2 개별 진단" 의 교집합이며, 이 교집합을 다룬 저널 논문은 본 후보군에 없다.

## 3. 핵심 10편 → 20편 재평가에서 바뀐 점
- 유지: 이전 핵심 10편(R3, P20, P26, M3, M2, M1, M5, D2, D3, M25) 전부 20편 안에 포함. 다만 R3·D3·D2·P20 은 Tier A 로, M25 는 Tier B 로 내렸다(경쟁 선행·3레벨 물리 모델을 우선).
- 추가: M4(3레벨 능동 NP 전류, 경쟁 선행), M29(NPC 커패시터 전류 해석), M28(온도 분리 비교법), M10(고유 2f), P14(짝수 고조파→C), P32(전류 재구성), P35(온도·SoH), M26(물리 내장 NN), P39(자연 여기), D6(대역 입력 DL).
- 제외 이유(대표): P1/P2/P8/P9(2005–2015 주입+RLS 기반 — R3 가 요약), P34/P38(방전 프로파일 — P35 로 대표), M11–M23(MMC 모델 기반 다수 — M28 로 대표), D13/D14/D16/D17(단품 ALT·RUL — 인버터 신호 아님), E 계열(소재 메커니즘 — 설계 단계 참고용이나 진단 방법 아님).

## 4. 논문별 상세 (20편)
### [S-1] M3 — Online Estimation of DC-link Capacitor Parameters of Three-Level NPC Converters Using Inherent Signals Analysis

- 저자 / 연도 / 저널: R. L. A. Ribeiro, Han et al. (전체 저자 확인 필요) / 2025 / IEEE/CAA Journal of Automatica Sinica, vol. 12 (호/쪽 확인 필요)
- DOI: 10.1109/JAS.2025.125159
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **Core competitor** · 읽기 목록 **A** · 대상 커패시터: 3L-NPC 분할 DC-link (상·하단 구분 여부 미확인)
- 점수(0–2): 3L-NPC/멀티레벨 관련성 2 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 2 · 전류/전압 파형 사용 2 · Harmonic/FFT/STFT/Wavelet 2 · 기존 인버터 센서만 2 · Online 진단 2 · AI/ML/CNN/LSTM 적용 가능성 1 · 타 토폴로지 이전 가능성 1 → **합계 16/18**
- 서지 확인 메모: 저자·호·쪽 확인 필요. SSRN/프리프린트 없음(미확인).

**왜 읽어야 하는가** — 본 조사에서 유일하게 '주입 없이 3L-NPC 의 고유(자연 발생) 스펙트럼 성분' 으로 DC-link 커패시터 C·ESR 을 추정한 저널 논문이다. 내 연구(무주입, NPC 내부 전류·전압의 고조파)와 가장 가까우므로 신규성의 경계를 이 논문이 정한다.

**내 연구와 같은 점** — 3L-NPC · 기존 센서만 · 무주입 · 스펙트럼 성분 추적 · C 와 ESR 을 동시에 다룸 · 온라인.

**내 연구와 다른 점** — (초록 기준) 추정기는 비정수 재귀 슬라이딩 DFT + 망각계수 RLS 관측기(모델 기반)이며 데이터 기반(CNN)이 아니다. 사용하는 성분은 'PWM 전략×토폴로지 상호변조 성분' 으로 표현되어 있고, 내 연구의 스위치 전류(iSa2)·상·하단 커패시터 전류·중성점 전류 스펙트럼과 같은지 다른지는 본문에서 확인해야 한다. 상·하단 개별 진단 여부 미확인.

**집중해서 읽을 부분** — (1) 어떤 상호변조 성분을 쓰는가: 주파수 식(m·fsw ± n·f1? 3f1 측대파?)과 어느 신호(vdc? iNP? 상전류?)에서 뽑는가. (2) 그 성분의 진폭이 C, ESR 에 어떻게 종속되는지의 수식. (3) 변조지수·부하·역률 변화에 대한 민감도와 검증 조건. (4) C1 과 C2 를 구분하는지. (5) 추정 오차와 수렴 시간.

**타 토폴로지 이전 가능성** — 상호변조 성분 자체는 NPC 에 특유하지만 '고유 성분 추적 + RLS' 틀은 T-type·ANPC 로 이전 가능.

**AI/ML/CNN 적용 가능성** — 추적한 스펙트럼 성분을 feature 벡터로 삼아 CNN/MLP 의 입력으로 쓸 수 있다. 내 연구의 차별점은 '같은 성분을 데이터 기반으로, 조건 강건성과 개별 진단까지' 가 될 수 있다.

### [S-2] M1 — An Online Condition Monitoring Method for DC-Link Capacitors of Three-Level NPC Inverters Based on Charge-Discharge Profile

- 저자 / 연도 / 저널: K. J. Min, U.-M. Choi, F. Blaabjerg / 2026 / IEEE Transactions on Industrial Electronics, vol. 73, no. 8, pp. 12452–12463 (SeoulTech Pure 기준)
- DOI: 10.1109/TIE.2026.3672764 (확인 필요)
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **Core competitor** · 읽기 목록 **A** · 대상 커패시터: 3L-NPC 상·하단 DC-link 커패시터 C1, C2 개별
- 점수(0–2): 3L-NPC/멀티레벨 관련성 2 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 2 · 전류/전압 파형 사용 2 · Harmonic/FFT/STFT/Wavelet 0 · 기존 인버터 센서만 2 · Online 진단 2 · AI/ML/CNN/LSTM 적용 가능성 1 · 타 토폴로지 이전 가능성 1 → **합계 14/18**
- 서지 확인 메모: IEEE Xplore 페이지 미확인(대학 Pure 목록 기준). DOI 재확인 필요.

**왜 읽어야 하는가** — '상·하단 커패시터를 개별로' 진단한 유일한 저널 논문(초록 기준). 내 연구가 C1/C2 개별 노화를 목표로 한다면 반드시 비교해야 할 경쟁 선행이다. 국내 그룹(SeoulTech)이라 본문 확보가 쉬울 수 있다.

**내 연구와 같은 점** — 3L-NPC · C1/C2 개별 · 추가 HW 없음 · 온라인(정상 운전 중) · vC1, vC2 사용.

**내 연구와 다른 점** — 기준전압에 오프셋을 '주입' 해 vC1−vC2 를 발산시키는 능동형이고, 시간영역 충방전 프로파일(Q=CΔv)을 쓴다. 고조파·스펙트럼을 쓰지 않으며 ESR 추정 여부 미확인. 데이터 기반 아님.

**집중해서 읽을 부분** — (1) 오프셋 주입 크기·시간과 출력전류 영향 보상 방식(내 연구의 '무주입' 주장의 대조군). (2) C 계산식과 전하 적분 방식(iNP 재구성?). (3) 실험 조건·오차 <1% 의 조건 범위. (4) C1 과 C2 가 다를 때 중성점 전압 거동 서술 — 내 '짝수 고조파' 가설의 물리 근거로 쓸 수 있는지.

**타 토폴로지 이전 가능성** — T-type 분할 DC-link 에 그대로 이전 가능. 2L 에는 해당 없음.

**AI/ML/CNN 적용 가능성** — 프로파일 자체는 ML 대상이 아니나, 노화 모사 실험 설계(C 교체·오차 기준)를 데이터셋 라벨 정의에 참고.

### [S-3] M2 — Online condition monitoring for DC-link capacitors of three-level NPC converters using noninvasive signal injection

- 저자 / 연도 / 저널: R. L. A. Ribeiro, D. K. Alves, R. P. R. de Sousa, A. C. Oliveira / 2024 / Computers and Electrical Engineering, vol. 119, art. 109577
- DOI: 10.1016/j.compeleceng.2024.109577
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **Core competitor / Methodology donor (Wavelet)** · 읽기 목록 **A** · 대상 커패시터: 3L-NPC 분할 DC-link (중성점 경로)
- 점수(0–2): 3L-NPC/멀티레벨 관련성 2 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 2 · 전류/전압 파형 사용 2 · Harmonic/FFT/STFT/Wavelet 2 · 기존 인버터 센서만 2 · Online 진단 2 · AI/ML/CNN/LSTM 적용 가능성 1 · 타 토폴로지 이전 가능성 1 → **합계 16/18**
- 서지 확인 메모: SSRN 4875339 프리프린트 확인 권장.

**왜 읽어야 하는가** — M3 의 전신으로, 중성점 전류 경로를 이용해 ESR 과 C 를 동시에 추정하며 Wavelet 분해를 쓴다. 내 연구의 'NP 경로 고조파' 와 같은 물리를 능동 주입으로 구현한 사례이므로, 무주입 접근의 차별점을 서술할 때 직접 대조 대상이다. SSRN 프리프린트(4875339)가 있어 본문 접근 가능성이 높다.

**내 연구와 같은 점** — 3L-NPC · 중성점 전류 이용 · 시간-주파수(스펙트럼) 분해 · ESR+C · HW·제어 변경 없음.

**내 연구와 다른 점** — 영상분 구형파(상호고조파)를 기준전압에 더하는 '주입형'. Wavelet(FFT 아님). 데이터 기반 아님. 전력품질 제약을 저자가 언급.

**집중해서 읽을 부분** — (1) NP 전류가 C1/C2 로 나뉘어 흐르는 모델과 각 주파수에서의 임피던스 식. (2) Wavelet 대 Fourier 비교 결과(<2% 주장)의 조건. (3) 주입 크기 결정 기준(전력품질). (4) C1/C2 분리 가능 여부. (5) 어떤 주파수에서 ESR 이, 어떤 주파수에서 C 가 잘 보이는지 — 내 feature 대역 선정에 직접 참고.

**타 토폴로지 이전 가능성** — 영상분 주입은 T-type·ANPC 에 이전 가능. 2L 에는 중성점이 없어 불가.

**AI/ML/CNN 적용 가능성** — Wavelet 계수를 CNN 입력(시간-주파수 이미지)으로 쓰는 변형이 가능.

### [S-4] M5 — A Comprehensive Method for Online Switch Fault Diagnosis and Capacitor Condition Monitoring of Three-Level T-Type Inverters

- 저자 / 연도 / 저널: W. Zhang, Y. He, X. Wang, J. Chen / 2023 / IEEE Transactions on Power Electronics, vol. 38, no. 8, pp. 10183–10195
- DOI: 10.1109/TPEL.2023.3262758
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **Physical-model reference / Methodology donor** · 읽기 목록 **B** · 대상 커패시터: 3L T-type 분할 DC-link
- 점수(0–2): 3L-NPC/멀티레벨 관련성 2 · 노화·열화 직접 진단 1 · C/ESR/SOH 추정 1 · 전류/전압 파형 사용 2 · Harmonic/FFT/STFT/Wavelet 2 · 기존 인버터 센서만 1 · Online 진단 2 · AI/ML/CNN/LSTM 적용 가능성 1 · 타 토폴로지 이전 가능성 2 → **합계 14/18**
- 서지 확인 메모: 없음

**왜 읽어야 하는가** — 3레벨 토폴로지에서 'DC-link 측 고유 고조파 성분' 을 모델로 도출하고 커패시터 전류를 재구성해 진단에 쓴 저널 논문. 내 연구가 필요로 하는 '3레벨 DC-link/NP 고조파의 해석적 모델' 을 가장 가까운 형태로 제공할 가능성이 크다.

**내 연구와 같은 점** — 3레벨(분할 DC-link, NP 전압) · 고유 고조파 모델 · 커패시터 전류 재구성 · 출력 전류 사용 · 온라인.

**내 연구와 다른 점** — T-type(NPC 와 스위치 구조·도통 경로가 다름). 스위치 OC 고장진단이 주이고 커패시터 CM 은 서브모듈. 'signal injection'·'extra hardware' 서브모듈이 언급되어 완전 센서리스가 아닐 수 있음. 추정 파라미터(C/ESR) 미확인. 데이터 기반 아님.

**집중해서 읽을 부분** — (1) DC-link 전류/전압 고유 고조파의 유도 과정(스위칭 함수 × 상전류)과 결과 식 — NPC 에 그대로 바꿔 쓸 수 있는지. (2) 커패시터 전류 재구성 식. (3) NP 전압 잔차 정의. (4) 커패시터 CM 서브모듈이 어떤 성분으로 무엇을 추정하는지. (5) 추가 HW 가 무엇인지.

**타 토폴로지 이전 가능성** — T-type → NPC 로 모델 이전 가능성 높음(도통 경로만 수정).

**AI/ML/CNN 적용 가능성** — 고유 고조파 모델이 주는 '이론 스펙트럼' 을 CNN 의 물리 유도 feature 로 사용 가능.

### [S-5] P26 — Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor

- 저자 / 연도 / 저널: M. Ghadrdan, S. Peyghami, H. Mokhtari, F. Blaabjerg / 2022 / IEEE Transactions on Power Electronics, vol. 37, no. 8, pp. 9733–9744
- DOI: 10.1109/TPEL.2022.3153842
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **Methodology donor** · 읽기 목록 **A** · 대상 커패시터: 2L back-to-back DC-link 전해 커패시터
- 점수(0–2): 3L-NPC/멀티레벨 관련성 0 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 2 · 전류/전압 파형 사용 2 · Harmonic/FFT/STFT/Wavelet 2 · 기존 인버터 센서만 2 · Online 진단 2 · AI/ML/CNN/LSTM 적용 가능성 1 · 타 토폴로지 이전 가능성 2 → **합계 15/18**
- 서지 확인 메모: 없음

**왜 읽어야 하는가** — '출력(상) 전류와 스위칭 상태로 커패시터 전류의 스위칭 주파수 성분을 재구성' 해 진단한 저널 논문. 내 연구가 시뮬레이션에서 iSa2, iC1, iC2 를 스위칭 상태로 만드는 것과 같은 철학이며, 실제 장치에서 커패시터 전류 센서 없이 feature 를 얻는 방법의 선례다. Aalborg VBN 에 accepted manuscript 가 있을 가능성.

**내 연구와 같은 점** — 커패시터 전류 재구성(상전류×스위칭 상태) · 스위칭 주파수 성분 · 추가 센서 없음 · 온라인 · 실험.

**내 연구와 다른 점** — 2L B2B(NPC 아님). HI 가 DF(=ωC·ESR) 하나라 C/ESR 분리 불가. 데이터 기반 아님. 스위칭 주파수·ESL·필터 영향이 정확도에 미침(저자).

**집중해서 읽을 부분** — (1) 재구성 수식(스위칭 함수 정의, 데드타임·ESL 처리). (2) fsw 성분 추출 방법과 DF 계산. (3) EoL 기준 정의. (4) 스위칭 주파수·필터·ESL 영향 분석 — 내 시뮬 설정(fsw, 필터)에 그대로 적용. (5) 실험에서 노화를 어떻게 모사했는가.

**타 토폴로지 이전 가능성** — 재구성 틀은 NPC 로 이전 가능(스위칭 함수를 3레벨로 확장).

**AI/ML/CNN 적용 가능성** — 재구성 전류의 스펙트럼을 CNN 입력으로 쓰는 전처리 단계의 근거.

### [A-6] D2 — Deep learning-based estimation technique for capacitance and ESR of input capacitors in single-phase DC/AC converters

- 저자 / 연도 / 저널: H.-J. Park, J.-C. Kim, S. Kwak / 2022 / Journal of Power Electronics, vol. 22, p. 513– (끝쪽 확인 필요)
- DOI: 10.1007/s43236-021-00366-x
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **AI reference** · 읽기 목록 **B** · 대상 커패시터: 단상 DC/AC 컨버터 입력(DC측) 커패시터
- 점수(0–2): 3L-NPC/멀티레벨 관련성 0 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 2 · 전류/전압 파형 사용 2 · Harmonic/FFT/STFT/Wavelet 2 · 기존 인버터 센서만 1 · Online 진단 1 · AI/ML/CNN/LSTM 적용 가능성 2 · 타 토폴로지 이전 가능성 2 → **합계 14/18**
- 서지 확인 메모: 같은 그룹의 D1(Machines 2022, 소스 전류 → ML, 3상)과 D6(JEET 2023, 주파수 대역 입력 DL, 3상)을 함께 볼 것.

**왜 읽어야 하는가** — 'FFT 로 뽑은 소수 고조파 성분(2·f1, fsw) → 신경망 → C, ESR' 구조를 저널에서 보인 논문. 내 연구의 '고조파 feature → CNN' 과 가장 가까운 AI 선례이며 국내 그룹(중앙대 Kwak)이라 접근성이 좋다.

**내 연구와 같은 점** — FFT 고조파 성분을 입력으로 · C 와 ESR 회귀 · 실험 파형 사용.

**내 연구와 다른 점** — 단상(3상 NPC 아님). 커패시터 전압·전류를 직접 측정. DNN(MLP)이며 CNN 아님. 온라인 여부·운전조건 범위 미확인.

**집중해서 읽을 부분** — (1) 왜 2f1 과 fsw 두 성분인가(물리적 근거 서술). (2) 입력 정규화와 데이터 범위(C, ESR 격자, 부하). (3) 네트워크 구조·오차. (4) 운전조건 변화 시 일반화 결과 유무. (5) 노화 모사 방법.

**타 토폴로지 이전 가능성** — 성분 선택 논리는 3상·NPC 로 이전 가능(2f_grid → NPC 의 3f1/측대파로 대체).

**AI/ML/CNN 적용 가능성** — 직접적인 AI 선례. 내 연구는 3상 NPC + 재구성 전류 + CNN + 조건 강건성으로 차별화.

### [A-7] D3 — Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters

- 저자 / 연도 / 저널: (저자 확인 필요) / 2025 / IEEE Transactions on Industrial Electronics, vol. 72, no. 4, pp. 4227–4237
- DOI: (확인 필요)
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **AI reference** · 읽기 목록 **B** · 대상 커패시터: 3상 AC/DC/AC(2L) DC-link
- 점수(0–2): 3L-NPC/멀티레벨 관련성 0 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 2 · 전류/전압 파형 사용 1 · Harmonic/FFT/STFT/Wavelet 2 · 기존 인버터 센서만 2 · Online 진단 2 · AI/ML/CNN/LSTM 적용 가능성 2 · 타 토폴로지 이전 가능성 2 → **합계 15/18**
- 서지 확인 메모: 저자·DOI 확인 필요(Xplore 10695772).

**왜 읽어야 하는가** — 데이터 기반 커패시터 CM 중 '다중 운전조건(부하·출력 주파수) 실험 검증 + 예측 불확실성(GPR)' 을 갖춘 드문 저널 논문. 내 연구의 강건성 검증 프로토콜과 결과 보고 형식의 벤치마크.

**내 연구와 같은 점** — 정상 운전 신호의 스펙트럼(PSD) → ML → C · 추가 HW·주입 없음 · 3상.

**내 연구와 다른 점** — 2L B2B. 입력은 DC-link 전압 리플(전류 아님). GPR(CNN 아님). 저샘플링 강조.

**집중해서 읽을 부분** — (1) PSD 계산 설정(샘플링, 창, 대역). (2) 학습/검증 조건 분할 방식(조건 외 일반화?). (3) 불확실성 활용 방식. (4) 오차 <2% 의 조건별 분포. (5) 노화 모사·데이터 수집 절차.

**타 토폴로지 이전 가능성** — 틀 자체는 토폴로지 무관.

**AI/ML/CNN 적용 가능성** — GPR 대 CNN 비교 실험의 기준선으로 적합.

### [A-8] P20 — Condition Monitoring of DC-Link Capacitors Using Goertzel Algorithm for Failure Precursor Parameter and Temperature Estimation

- 저자 / 연도 / 저널: P. Sundararajan, M. H. M. Sathik, F. Sasongko, C. S. Tan, J. Pou, F. Blaabjerg, A. K. Gupta / 2020 / IEEE Transactions on Power Electronics, vol. 35, no. 6, pp. 6386–6396
- DOI: 10.1109/TPEL.2019.2951859
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **Methodology donor** · 읽기 목록 **B** · 대상 커패시터: 정류기 전단 3상 인버터 DC-link 전해
- 점수(0–2): 3L-NPC/멀티레벨 관련성 0 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 2 · 전류/전압 파형 사용 2 · Harmonic/FFT/STFT/Wavelet 2 · 기존 인버터 센서만 1 · Online 진단 2 · AI/ML/CNN/LSTM 적용 가능성 1 · 타 토폴로지 이전 가능성 2 → **합계 14/18**
- 서지 확인 메모: Aalborg VBN/CORE 에 accepted manuscript 존재 가능.

**왜 읽어야 하는가** — 전체 FFT 대신 Goertzel 로 '관심 빈 몇 개만' 뽑아 ESR·C·온도를 추정. 내 연구가 feature 를 소수 고조파로 줄여 임베디드 구현까지 가려면 가장 직접적인 방법론 공여자이며, 온도를 C 로 추정하는 아이디어는 온도 교란 문제의 해법 후보.

**내 연구와 같은 점** — 고조파 성분 기반 · ESR+C · 온라인 · 3상 인버터.

**내 연구와 다른 점** — 2L(정류기 전단). 커패시터 전류 측정 여부 미확인. 데이터 기반 아님. 온도 추정 포함(내 연구에는 없음).

**집중해서 읽을 부분** — (1) 어떤 주파수 빈을 쓰는가(fsw? 6f 정류 리플?). (2) ESR·C 추정식과 각 빈의 역할. (3) C 의 온도 의존성을 이용한 온도 추정 원리와 한계. (4) 아날로그 필터·FFT 대비 비용 비교. (5) 실험 조건.

**타 토폴로지 이전 가능성** — Goertzel 추출은 모든 토폴로지에 적용 가능.

**AI/ML/CNN 적용 가능성** — CNN 입력 feature 추출기(저비용) 후보. 온도 feature 추가 가능.

### [A-9] R3 — An Overview of Condition Monitoring Techniques for Capacitors in DC-Link Applications

- 저자 / 연도 / 저널: Z. Zhao, P. Davari, W. Lu, H. Wang, F. Blaabjerg / 2021 / IEEE Transactions on Power Electronics, vol. 36, no. 4, pp. 3692–3716
- DOI: 10.1109/TPEL.2020.3023469
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **Physical-model reference (분류 체계·용어)** · 읽기 목록 **A** · 대상 커패시터: DC-link 전반(전해·필름)
- 점수(0–2): 3L-NPC/멀티레벨 관련성 1 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 2 · 전류/전압 파형 사용 1 · Harmonic/FFT/STFT/Wavelet 1 · 기존 인버터 센서만 1 · Online 진단 1 · AI/ML/CNN/LSTM 적용 가능성 1 · 타 토폴로지 이전 가능성 2 → **합계 12/18**
- 서지 확인 메모: Aalborg VBN 에 author copy 존재.

**왜 읽어야 하는가** — 2021 기준의 표준 분류(ESR/C/온도, 주입/비주입, online/quasi/offline, 정확도)를 제공하는 개관. 관련연구 절의 뼈대와 용어를 여기서 가져오면 심사자가 익숙한 틀로 설명할 수 있다. 먼저 읽어 두면 나머지 19편의 위치가 보인다.

**내 연구와 같은 점** — DC-link 커패시터 CM 전반.

**내 연구와 다른 점** — 리뷰. NPC·고조파·CNN 특화 아님. 2021 이후(M1–M3 등) 미포함.

**집중해서 읽을 부분** — (1) 분류 체계와 평가 기준(정확도·구현·응용 목적) 표. (2) 리플 기반/주입/과도 방법의 수식 요약. (3) 저자들이 지적한 미해결 문제(온도, 부하, 산업 채택) — 내 Gap 서술의 인용 근거. (4) AI 방법에 대한 평가.

**타 토폴로지 이전 가능성** — —

**AI/ML/CNN 적용 가능성** — AI 방법 절의 2021 시점 평가를 내 서론에 인용.

### [A-10] M4 — Noninvasive Online Capacitor Monitoring Method for Three-Level Converter Based on Active Neutral-Point Current Adjustment

- 저자 / 연도 / 저널: (저자 확인 필요) / 2024 / IEEE Transactions on Industrial Electronics, vol. 71, no. 5, pp. 4320–4329 (서지 신뢰도 낮음, 확인 필요)
- DOI: (확인 필요)
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **Core competitor** · 읽기 목록 **B** · 대상 커패시터: 3L(ac/dc/ac) 분할 DC-link
- 점수(0–2): 3L-NPC/멀티레벨 관련성 2 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 2 · 전류/전압 파형 사용 2 · Harmonic/FFT/STFT/Wavelet 1 · 기존 인버터 센서만 2 · Online 진단 2 · AI/ML/CNN/LSTM 적용 가능성 1 · 타 토폴로지 이전 가능성 1 → **합계 15/18**
- 서지 확인 메모: 제목·권·쪽이 검색 스니펫 추정이므로 IEEE Xplore(10149200) 에서 반드시 확인. 실체가 다르면 Tier B 로 강등.

**왜 읽어야 하는가** — 중성점 전류를 '능동 조정' 해 NP 전압 리플을 만들고, 스위칭 상태×3상 전류로 주입 NP 전류를 재구성해 RLS 로 C 를 추정한 3레벨 논문. 내 연구의 신호(NP 전류 재구성, NP 전압 리플)와 동일한 양을 다루므로 경쟁 선행이자 재구성 식의 공여자.

**내 연구와 같은 점** — 3레벨 · NP 전류 재구성(스위칭 상태×상전류) · NP 전압 리플 · 추가 센서 없음 · 온라인.

**내 연구와 다른 점** — 능동 조정(주입형). RLS(모델 기반). ESR 미확인. 데이터 기반 아님.

**집중해서 읽을 부분** — (1) NP 전류 재구성 식(내 iNP 계산과 대조). (2) 조정 크기와 운전점 불변 주장의 근거. (3) NP 전압 리플 ↔ C 관계식. (4) 실험 조건·오차.

**타 토폴로지 이전 가능성** — NPC/T-type 공통.

**AI/ML/CNN 적용 가능성** — 재구성 NP 전류 스펙트럼을 CNN 입력으로 쓰는 전처리 근거.

### [B-11] M29 — Analysis of dc-link capacitor current in three-level neutral point clamped and cascaded H-bridge inverters

- 저자 / 연도 / 저널: G. I. Orfanoudakis et al. / 2013 / IET Power Electronics
- DOI: 10.1049/iet-pel.2012.0422
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **Physical-model reference** · 읽기 목록 **C** · 대상 커패시터: 3L-NPC(및 CHB) DC-link 커패시터 전류
- 점수(0–2): 3L-NPC/멀티레벨 관련성 2 · 노화·열화 직접 진단 0 · C/ESR/SOH 추정 0 · 전류/전압 파형 사용 2 · Harmonic/FFT/STFT/Wavelet 1 · 기존 인버터 센서만 1 · Online 진단 1 · AI/ML/CNN/LSTM 적용 가능성 0 · 타 토폴로지 이전 가능성 2 → **합계 9/18**
- 서지 확인 메모: 본문에서 스펙트럼을 다루는지 미확인.

**왜 읽어야 하는가** — CM 논문은 아니지만 3L-NPC DC-link 커패시터 전류를 해석한 저널 논문. 내 연구의 커패시터 전류·중성점 전류 스펙트럼(저차·측대파)에 대한 이론식의 출발점이 될 수 있다.

**내 연구와 같은 점** — 3L-NPC · 커패시터 전류 · (스펙트럼/실효값) 해석.

**내 연구와 다른 점** — 노화·진단 아님. C/ESR 변화에 따른 변화는 다루지 않을 가능성.

**집중해서 읽을 부분** — (1) 커패시터 전류 식(스위칭 함수·변조지수·역률 종속). (2) 고조파 성분(3f1, 측대파) 표현. (3) CHB 와의 비교.

**타 토폴로지 이전 가능성** — —

**AI/ML/CNN 적용 가능성** — 이론 스펙트럼을 CNN 의 물리 유도 feature·정규화 기준으로.

### [B-12] M28 — Practical Online Condition Monitoring of DC-Link Capacitors in Modular Multilevel Converters: A Comparative Approach

- 저자 / 연도 / 저널: (저자 확인 필요) / 2024 / IEEE Open Journal of Power Electronics (Xplore 미확인; TechRxiv 프리프린트 'accepted')
- DOI: 10.1109/OJPEL.2024.3387829 (확인 필요)
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **Methodology donor (온도 효과 분리)** · 읽기 목록 **C** · 대상 커패시터: MMC 서브모듈 커패시터 (non-DC-link) **(non-DC-link)**
- 점수(0–2): 3L-NPC/멀티레벨 관련성 1 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 2 · 전류/전압 파형 사용 2 · Harmonic/FFT/STFT/Wavelet 2 · 기존 인버터 센서만 2 · Online 진단 2 · AI/ML/CNN/LSTM 적용 가능성 1 · 타 토폴로지 이전 가능성 2 → **합계 16/18**
- 서지 확인 메모: OA 저널·TechRxiv 프리프린트로 본문 확보 용이할 가능성. 저널 게재 확정 여부 확인.

**왜 읽어야 하는가** — 같은 암 안의 모든 SM 커패시터 추정치를 서로 비교해 '온도로 인한 공통 변동' 과 '노화로 인한 개별 변동' 을 분리한다. NPC 의 C1 vs C2 상대 비교 feature 로 그대로 옮길 수 있는 아이디어이며, 온도 센서 없이 온도 교란을 다루는 몇 안 되는 접근.

**내 연구와 같은 점** — 주파수 성분 기반 C 추정 · 추정 전류(측정 아님) · 온라인 · 추가 센서 없음.

**내 연구와 다른 점** — MMC(SM 다수). 2개뿐인 NPC 커패시터에서는 통계적 비교력이 약함(추론).

**집중해서 읽을 부분** — (1) 비교 기준의 수식(평균 대비 편차). (2) 온도 변동이 C 추정치에 주는 크기. (3) 주파수 성분 선택.

**타 토폴로지 이전 가능성** — 비교 개념은 토폴로지 무관.

**AI/ML/CNN 적용 가능성** — C1/C2 상대 feature 설계 근거.

### [B-13] M10 — Capacitor Condition Monitoring Method for Low-Capacitance StatComs: An Online Approach Using the Inherent Second-Harmonic Oscillations

- 저자 / 연도 / 저널: E. R. Ramos, R. Leyva, Q. Liu, G. G. Farivar, J. Pou / 2023 / IEEE Transactions on Power Electronics, vol. 38, no. 9, pp. 10559–10562
- DOI: (확인 필요)
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **Methodology donor (고유 고조파 → 임피던스)** · 읽기 목록 **C** · 대상 커패시터: CHB STATCOM 셀 DC 커패시터 (non-DC-link) **(non-DC-link)**
- 점수(0–2): 3L-NPC/멀티레벨 관련성 1 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 2 · 전류/전압 파형 사용 2 · Harmonic/FFT/STFT/Wavelet 2 · 기존 인버터 센서만 1 · Online 진단 2 · AI/ML/CNN/LSTM 적용 가능성 1 · 타 토폴로지 이전 가능성 2 → **합계 15/18**
- 서지 확인 메모: Letters 형식(4쪽) 추정.

**왜 읽어야 하는가** — 주입 없이 '토폴로지가 자연히 만드는 2f 진동' 으로 ESR 과 C 를 동시에 식별. 내 연구의 '자연 발생 고조파로 진단' 논리의 멀티레벨 선례.

**내 연구와 같은 점** — 고유(무주입) 고조파 · ESR+C · 온라인 · 멀티레벨.

**내 연구와 다른 점** — CHB 셀(단상 전력 맥동 2f). NPC 의 3f1/측대파와 발생 원리 다름.

**집중해서 읽을 부분** — (1) 2f 성분에서 ESR·C 를 분리하는 식. (2) 저용량 조건에서 SNR. (3) 부하 변화 처리.

**타 토폴로지 이전 가능성** — 원리(고유 리플 임피던스)는 NPC 3f1 에 이전 가능.

**AI/ML/CNN 적용 가능성** — feature 정의 참고.

### [B-14] P14 — Noninvasive Technique for DC-Link Capacitance Estimation in Single-Phase Inverters

- 저자 / 연도 / 저널: M. W. Ahmad, P. N. Kumar, A. Arya, S. Anand / 2018 / IEEE Transactions on Power Electronics, vol. 33, no. 5, pp. 3693–3696
- DOI: 10.1109/TPEL.2017.2762341
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **Methodology donor (짝수 고조파 → C)** · 읽기 목록 **C** · 대상 커패시터: 단상 인버터 DC-link 전해
- 점수(0–2): 3L-NPC/멀티레벨 관련성 0 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 2 · 전류/전압 파형 사용 2 · Harmonic/FFT/STFT/Wavelet 2 · 기존 인버터 센서만 2 · Online 진단 2 · AI/ML/CNN/LSTM 적용 가능성 1 · 타 토폴로지 이전 가능성 1 → **합계 14/18**
- 서지 확인 메모: 짧은 논문(letter).

**왜 읽어야 하는가** — 제어용 센서만으로 2f(짝수) 성분의 v/i 비에서 C 를 추정(최대 오차 2.56%). '짝수 고조파 ↔ C' 관계를 가장 단순하게 보여주는 저널 논문이라 내 2n 고조파 가설의 비교 기준.

**내 연구와 같은 점** — 짝수 고조파 · C · 기존 센서 · 온라인.

**내 연구와 다른 점** — 단상 전력 맥동(2f_grid)이 원인이며 NPC 의 2f1 과 발생 원리가 다르다. ESR 없음.

**집중해서 읽을 부분** — (1) 2f 성분 추출 방법(SOGI?). (2) v/i 비 → C 식과 ESR 무시 조건. (3) 오차 원인 분석.

**타 토폴로지 이전 가능성** — 단상 특유. 원리는 참고.

**AI/ML/CNN 적용 가능성** — 낮음.

### [B-15] P32 — Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor in a PWM Inverter With a Six-Pulse Diode Rectifier

- 저자 / 연도 / 저널: K. Hasegawa et al. / 2023 / IEEJ Journal of Industry Applications, vol. 12, no. 3, art. 22009135
- DOI: (확인 필요; J-STAGE)
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **Methodology donor (모델 기반 전류 재구성)** · 읽기 목록 **C** · 대상 커패시터: 정류기 전단 인버터 DC-link
- 점수(0–2): 3L-NPC/멀티레벨 관련성 0 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 2 · 전류/전압 파형 사용 2 · Harmonic/FFT/STFT/Wavelet 1 · 기존 인버터 센서만 2 · Online 진단 2 · AI/ML/CNN/LSTM 적용 가능성 1 · 타 토폴로지 이전 가능성 1 → **합계 13/18**
- 서지 확인 메모: 후속: Yamasoto & Hasegawa 2025 Microelectron. Reliab. 173:115873.

**왜 읽어야 하는가** — 전류 센서 없이 전원 전압과 인덕터 모델로 커패시터 전류를 계산해 ESR·C 를 추정. '측정 대신 모델로 전류를 만든다' 는 점에서 내 시뮬→실험 전환 시 전류 확보 전략의 참고. J-STAGE OA 가능성.

**내 연구와 같은 점** — 커패시터 전류 재구성 · ESR+C · 기존 센서 · 온라인.

**내 연구와 다른 점** — 정류기 리플(6f) 기반, 2L. 고조파 대역이 다름.

**집중해서 읽을 부분** — (1) 재구성 모델과 오차 원인. (2) 어떤 리플 성분을 쓰는가. (3) 전원 불평형(후속 P37) 영향.

**타 토폴로지 이전 가능성** — 정류기 전단 구조 특유.

**AI/ML/CNN 적용 가능성** — 낮음.

### [B-16] P35 — Discharge-Based Condition Monitoring for Electrolytic DC-Link Capacitors

- 저자 / 연도 / 저널: J. Baumann, Murillo Garcia, K. Papastergiou, D. Peftitsis / 2024 / IEEE Transactions on Power Electronics, vol. 39, pp. 16622–16637 (호 확인 필요)
- DOI: (확인 필요)
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **Physical-model reference (온도 의존성·SoH)** · 읽기 목록 **C** · 대상 커패시터: DC-link 전해(일반 컨버터)
- 점수(0–2): 3L-NPC/멀티레벨 관련성 0 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 2 · 전류/전압 파형 사용 2 · Harmonic/FFT/STFT/Wavelet 0 · 기존 인버터 센서만 2 · Online 진단 1 · AI/ML/CNN/LSTM 적용 가능성 1 · 타 토폴로지 이전 가능성 2 → **합계 12/18**
- 서지 확인 메모: author copy: papastergiou.web.cern.ch (미확인).

**왜 읽어야 하는가** — 정지 시 방전 프로파일로 SoH 를 구하면서 전해 커패시터의 온도 의존성과 물리적 거동을 모델에 넣어 보상한다. 내 연구가 온도 교란을 다룰 때 참고할 모델과, quasi-online 대안(보완 연구)의 대표.

**내 연구와 같은 점** — 기존 DC 전압 센서 · C/SoH · 온도 고려.

**내 연구와 다른 점** — quasi-online(정지 필요), 시간영역, 고조파 없음, 2L/일반.

**집중해서 읽을 부분** — (1) 온도-ESR/C 모델과 보상식. (2) SoH 정의. (3) 저자 웹(CERN)에 author copy 있음.

**타 토폴로지 이전 가능성** — 토폴로지 무관.

**AI/ML/CNN 적용 가능성** — 온도 보상 feature 설계 참고.

### [B-17] M25 — Online evaluation method for MMC submodule capacitor aging based on CapAgingNet

- 저자 / 연도 / 저널: X. Deng, Y. Deng, L. Qin et al. / 2025 / Global Energy Interconnection, vol. 8, no. 3, pp. 420–432
- DOI: (확인 필요)
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **AI reference (DL 분류, 시뮬 데이터)** · 읽기 목록 **C** · 대상 커패시터: MMC 서브모듈 커패시터 (non-DC-link) **(non-DC-link)**
- 점수(0–2): 3L-NPC/멀티레벨 관련성 1 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 1 · 전류/전압 파형 사용 0 · Harmonic/FFT/STFT/Wavelet 0 · 기존 인버터 센서만 2 · Online 진단 2 · AI/ML/CNN/LSTM 적용 가능성 2 · 타 토폴로지 이전 가능성 1 → **합계 11/18**
- 서지 확인 메모: OA 저널(gei-journal.com PDF 존재 가능).

**왜 읽어야 하는가** — 딥 네트워크로 노화 '등급' 을 분류한 저널 논문(Top-1 95.32%). 입력이 파형이 아닌 스위칭 상태 시퀀스이고 데이터가 시뮬레이션뿐이라, 내 연구가 피해야 할 한계(실험 부재·일반화 미검증)와 등급 라벨 설계를 동시에 보여준다.

**내 연구와 같은 점** — DL 분류 · 노화 등급 라벨 · 추가 채널 없음 · 온라인.

**내 연구와 다른 점** — MMC · 스위칭 상태 입력(고조파 아님) · 시뮬 데이터만.

**집중해서 읽을 부분** — (1) 노화 등급 라벨 정의(C 감소 구간). (2) 데이터셋 생성 조건(운전점 다양성). (3) 네트워크 구조·일반화 평가 방식.

**타 토폴로지 이전 가능성** — 라벨·평가 설계는 이전 가능.

**AI/ML/CNN 적용 가능성** — 직접 참고(분류 설계).

### [B-18] M26 — Neural Network-Based Submodule Capacitance Monitoring in Modular Multilevel Converters for Renewable Energy Conversion Systems

- 저자 / 연도 / 저널: M. Asnoun, A. Rahoui, K. Mesbah, B. Boukais, D. Frey, I. Sadli, S. Bacha / 2026 / Electronics, vol. 15, no. 7, art. 1486
- DOI: 10.3390/electronics15071486
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **AI reference (물리 내장 NN)** · 읽기 목록 **C** · 대상 커패시터: MMC 서브모듈 커패시터 (non-DC-link) **(non-DC-link)**
- 점수(0–2): 3L-NPC/멀티레벨 관련성 1 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 2 · 전류/전압 파형 사용 2 · Harmonic/FFT/STFT/Wavelet 0 · 기존 인버터 센서만 2 · Online 진단 2 · AI/ML/CNN/LSTM 적용 가능성 2 · 타 토폴로지 이전 가능성 2 → **합계 15/18**
- 서지 확인 메모: 없음

**왜 읽어야 하는가** — ADALINE 가중치를 회로 방정식에 매핑해 C 를 추정하는 '물리 내장(grey-box) 신경망'. 블랙박스 CNN 의 대안 또는 하이브리드(물리 유도 feature + CNN) 설계의 선례. MDPI OA 라 본문 확보 용이.

**내 연구와 같은 점** — NN · 암 전류·스위칭 상태·전압(파형) 입력 · C · 온라인 · 센서 추가 없음.

**내 연구와 다른 점** — MMC · 고조파 아님 · 선형 적응 필터 수준.

**집중해서 읽을 부분** — (1) 가중치↔C 매핑 식. (2) 가혹 조건·노화 시나리오 정의. (3) 수렴·오차.

**타 토폴로지 이전 가능성** — 회로식 매핑은 NPC 커패시터 전압 방정식에도 적용 가능.

**AI/ML/CNN 적용 가능성** — 하이브리드 설계 직접 참고.

### [B-19] P39 — Non-Intrusive Capacitor Monitoring in Photovoltaic Inverters Based on MPPT-Induced Voltage Transients

- 저자 / 연도 / 저널: M. K. P. Muhammed Ramees, M. W. Ahmad / 2026 / IEEE Transactions on Power Electronics, vol. 41, no. 3 (쪽 확인 필요)
- DOI: (확인 필요)
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **Methodology donor (자연 여기 + 출력전류로 커패시터 전류 추정)** · 읽기 목록 **C** · 대상 커패시터: 3상 PV 인버터 DC-link
- 점수(0–2): 3L-NPC/멀티레벨 관련성 0 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 2 · 전류/전압 파형 사용 2 · Harmonic/FFT/STFT/Wavelet 1 · 기존 인버터 센서만 2 · Online 진단 2 · AI/ML/CNN/LSTM 적용 가능성 1 · 타 토폴로지 이전 가능성 1 → **합계 13/18**
- 서지 확인 메모: 같은 저자의 리뷰 R4(IEEE Access 2023)도 참고.

**왜 읽어야 하는가** — 주입 대신 MPPT 기준 전압 전이를 '자연 여기' 로 쓰고, 인버터 출력 전류로 커패시터 전류를 추정해 C 를 구한다. 최신(2026) 무주입 흐름의 대표이며 시뮬+실험 검증.

**내 연구와 같은 점** — 무주입 · 출력 전류 → 커패시터 전류 추정 · 기존 센서 · 3상 · 시뮬+실험.

**내 연구와 다른 점** — 2L PV, 저주파 과도 성분(고조파 아님), C 만.

**집중해서 읽을 부분** — (1) 출력 전류 → 커패시터 전류 추정식. (2) 자연 여기의 발생 빈도와 추정 주기. (3) 실험 대 시뮬 결과 차이.

**타 토폴로지 이전 가능성** — MPPT 특유; 추정식은 이전 가능.

**AI/ML/CNN 적용 가능성** — 낮음.

### [B-20] D6 — DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs

- 저자 / 연도 / 저널: (저자 확인 필요; Kwak 그룹 추정) / 2023 / Journal of Electrical Engineering & Technology
- DOI: 10.1007/s42835-023-01424-z
- 근거 수준: **Abstract-level only** (본문 미확인; 초록·검색 스니펫 기준)
- 역할: **AI reference (주파수 대역 입력 DL, 3상)** · 읽기 목록 **C** · 대상 커패시터: 3상 DC/AC 컨버터 DC 커패시터
- 점수(0–2): 3L-NPC/멀티레벨 관련성 0 · 노화·열화 직접 진단 2 · C/ESR/SOH 추정 2 · 전류/전압 파형 사용 2 · Harmonic/FFT/STFT/Wavelet 2 · 기존 인버터 센서만 1 · Online 진단 1 · AI/ML/CNN/LSTM 적용 가능성 2 · 타 토폴로지 이전 가능성 2 → **합계 14/18**
- 서지 확인 메모: D1(Machines 2022)과 함께 읽을 것. 세부가 초록에 없어 Tier B.

**왜 읽어야 하는가** — 3상 컨버터에서 '주파수 대역을 나눈 입력' 으로 DL 이 C·ESR 을 추정. 내 연구의 '저차 대역 vs 스위칭 대역 feature 분리' 설계와 직접 맞닿는 AI 선례. D2 의 3상 확장판일 가능성.

**내 연구와 같은 점** — 3상 · 주파수 대역 feature · DL · C+ESR.

**내 연구와 다른 점** — 2L(추정) · 입력 신호 종류 미확인 · 온라인 여부 미확인.

**집중해서 읽을 부분** — (1) 대역 분할 기준과 각 대역이 C/ESR 에 주는 정보. (2) 네트워크 구조. (3) 데이터 범위.

**타 토폴로지 이전 가능성** — 대역 분리 논리는 NPC 로 이전 가능.

**AI/ML/CNN 적용 가능성** — 직접 참고.


## 5. 읽기 목록

### A. 지금 당장 먼저 읽을 5편
| 순서 | ID | 제목 | 연도 | Tier | 역할 | 근거 |
|---|---|---|---|---|---|---|
| 1 | R3 | An Overview of Condition Monitoring Techniques for Capacitors in DC-Link Applications | 2021 | Tier A | Physical-model reference (분류 체계·용어) | Abstract-level only |
| 2 | M3 | Online Estimation of DC-link Capacitor Parameters of Three-Level NPC Converters Using Inherent Signals Analysis | 2025 | Tier S | Core competitor | Abstract-level only |
| 3 | M1 | An Online Condition Monitoring Method for DC-Link Capacitors of Three-Level NPC Inverters Based on Charge-Discharge Profile | 2026 | Tier S | Core competitor | Abstract-level only |
| 4 | M2 | Online condition monitoring for DC-link capacitors of three-level NPC converters using noninvasive signal injection | 2024 | Tier S | Core competitor / Methodology donor (Wavelet) | Abstract-level only |
| 5 | P26 | Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor | 2022 | Tier S | Methodology donor | Abstract-level only |

읽는 순서의 이유: R3 로 분류 체계와 용어를 잡은 뒤, 경쟁 선행 M3 → M1 → M2 로 "무주입/개별/주입" 의 세 축을 확인하고, P26 으로 전류 재구성 방법을 확보한다. 이 5편을 읽으면 내 연구의 신규성 문장을 쓸 수 있다.

### B. 그 다음 읽을 5편
| 순서 | ID | 제목 | 연도 | Tier | 역할 | 근거 |
|---|---|---|---|---|---|---|
| 1 | M5 | A Comprehensive Method for Online Switch Fault Diagnosis and Capacitor Condition Monitoring of Three-Level T-Type Inverters | 2023 | Tier S | Physical-model reference / Methodology donor | Abstract-level only |
| 2 | M4 | Noninvasive Online Capacitor Monitoring Method for Three-Level Converter Based on Active Neutral-Point Current Adjustment | 2024 | Tier A | Core competitor | Abstract-level only |
| 3 | D2 | Deep learning-based estimation technique for capacitance and ESR of input capacitors in single-phase DC/AC converters | 2022 | Tier A | AI reference | Abstract-level only |
| 4 | D3 | Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters | 2025 | Tier A | AI reference | Abstract-level only |
| 5 | P20 | Condition Monitoring of DC-Link Capacitors Using Goertzel Algorithm for Failure Precursor Parameter and Temperature Estimation | 2020 | Tier A | Methodology donor | Abstract-level only |

이유: M5 로 3레벨 고유 고조파 모델을, M4 로 NP 전류 재구성 식을 얻고(둘 다 내 MATLAB 민감도 실험의 이론 대조군), D2 → D3 로 고조파→NN 과 강건성 검증 프로토콜을, P20 으로 경량 feature 추출(Goertzel)과 온도 지표를 확보한다.

### C. 연구 설계 단계에서 참고할 10편
| 순서 | ID | 제목 | 연도 | Tier | 역할 | 근거 |
|---|---|---|---|---|---|---|
| 1 | M29 | Analysis of dc-link capacitor current in three-level neutral point clamped and cascaded H-bridge inverters | 2013 | Tier B | Physical-model reference | Abstract-level only |
| 2 | M28 | Practical Online Condition Monitoring of DC-Link Capacitors in Modular Multilevel Converters: A Comparative Approach | 2024 | Tier B | Methodology donor (온도 효과 분리) | Abstract-level only |
| 3 | M10 | Capacitor Condition Monitoring Method for Low-Capacitance StatComs: An Online Approach Using the Inherent Second-Harmonic Oscillations | 2023 | Tier B | Methodology donor (고유 고조파 → 임피던스) | Abstract-level only |
| 4 | P14 | Noninvasive Technique for DC-Link Capacitance Estimation in Single-Phase Inverters | 2018 | Tier B | Methodology donor (짝수 고조파 → C) | Abstract-level only |
| 5 | P32 | Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor in a PWM Inverter With a Six-Pulse Diode Rectifier | 2023 | Tier B | Methodology donor (모델 기반 전류 재구성) | Abstract-level only |
| 6 | P35 | Discharge-Based Condition Monitoring for Electrolytic DC-Link Capacitors | 2024 | Tier B | Physical-model reference (온도 의존성·SoH) | Abstract-level only |
| 7 | M25 | Online evaluation method for MMC submodule capacitor aging based on CapAgingNet | 2025 | Tier B | AI reference (DL 분류, 시뮬 데이터) | Abstract-level only |
| 8 | M26 | Neural Network-Based Submodule Capacitance Monitoring in Modular Multilevel Converters for Renewable Energy Conversion Systems | 2026 | Tier B | AI reference (물리 내장 NN) | Abstract-level only |
| 9 | P39 | Non-Intrusive Capacitor Monitoring in Photovoltaic Inverters Based on MPPT-Induced Voltage Transients | 2026 | Tier B | Methodology donor (자연 여기 + 출력전류로 커패시터 전류 추정) | Abstract-level only |
| 10 | D6 | DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs | 2023 | Tier B | AI reference (주파수 대역 입력 DL, 3상) | Abstract-level only |

용도: M29(커패시터 전류 이론식) → M10·P14(고유/짝수 고조파와 C·ESR 관계) → M28(C1 vs C2 상대 비교로 온도 분리) → P35(온도 모델) → P32·P39(전류 추정·자연 여기, 실험 전환 시) → M25·M26·D6(라벨 설계, 물리 내장 NN, 대역 feature).

## 6. 다음 행동
1. 네트워크 허용 또는 로컬 PC 에서 PDF 확보 후 `core_papers/` 워크시트의 8–9 절을 채운다 (우선 M3, M1, M2).
2. M4 의 실체 확인(IEEE Xplore 10149200). 실체가 다르면 Tier B 로 내리고 M5 를 Tier A 로 올린다.
3. M5·M4·M29 의 식을 바탕으로 MATLAB 민감도 실험(C1/C2/ESR 스윕 대 부하/변조 스윕; iSa2·ia·iNP·vNP·vC1/vC2 의 2f1·3f1·4f1·fsw±f1)을 설계한다.
4. D2·D3·D6 의 데이터 범위·검증 방식을 따라 Python 데이터셋과 평가 프로토콜을 정의한다.
