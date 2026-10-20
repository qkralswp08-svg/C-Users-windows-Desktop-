# 01. Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor

> Tier S · Rank 1 · Score 73/100 · **Evidence: Abstract-level only** (본문 미열람; 아래 `Not reported / Full text verification required` 항목은 추측으로 채우지 않았다)

### [1] 기본 논문 정보
- Title: Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor
- Authors: M. Ghadrdan, S. Peyghami, H. Mokhtari, F. Blaabjerg
- Year: 2022
- Journal: IEEE Transactions on Power Electronics, vol. 37, no. 8, pp. 9733–9744 (Aug. 2022)
- DOI: 10.1109/TPEL.2022.3153842
- Publication Type: Journal
- 식별/출처: IEEE Xplore 9721605; AAU VBN; Sharif repository; RG 358881451
- 저자 소속: Sharif University of Technology (Ghadrdan, Mokhtari) + Aalborg University (Peyghami, Blaabjerg) — 리포지터리 호스팅 기준(소속 줄 미확인). First author Ghadrdan(이후 KIT). Corresponding NR.

### [2] Converter / Inverter Topology
- Topology: Back-to-back (AC/DC/AC) 전압형 컨버터. 초록은 'back-to-back converters' 로만 기술 — 2-Level 여부는 명시되지 않음(일반 B2B VSC = 2-Level 로 추정, 확인 필요).
- Power rating: Not reported / Full text verification required / DC-link voltage: Not reported / Full text verification required / AC output voltage: Not reported / Full text verification required
- Switching frequency: 수치 NR (스위칭 주파수가 DF 정확도에 미치는 영향은 분석했다고 초록에 명시) / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: Not reported / Full text verification required

### [3] Classification vs Regression
- Task: **Regression-type indicator (DF)**
- 분류 아님. 연속 지표 DF = tanδ = ω·C·ESR 를 추정하고 EoL 기준과 비교(초록). C 와 ESR 을 개별로 출력하지는 않음(초록 기준).
- Output 단위: DF (무차원)

해당 없음(회귀/연속 지표) 또는 클래스 정의 NR.

### [4] 커패시터 기본 정보
| 항목 | 값 |
|---|---|
| Technology | Aluminum electrolytic (제목에 명시) |
| Manufacturer | Not reported / Full text verification required |
| Model | Not reported / Full text verification required |
| Rated C | Not reported / Full text verification required |
| Rated V | Not reported / Full text verification required |
| Rated ESR | Not reported / Full text verification required |
| Temperature rating | Not reported / Full text verification required |

### [5] 노화 모사 방식
- NR — 실험 검증은 언급되나 노화 구현 방식(가속/모사/시뮬) 미기재. 2차 출처(인용 리뷰): 'ESR 이 초기값의 2배가 되면 고장으로 간주하며 그 경우에도 계산 오차가 허용 범위' (귀속 주의).

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| — | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required |

논문에 나온 값이 스니펫·초록에 없어 표를 채우지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): Not reported / Full text verification required

### [7] C / ESR 변화 여부
- **Not reported / Full text verification required (DF 지표 특성상 C·ESR 모두 반영되나 실험에서 무엇을 바꿨는지는 미확인)**

### [8] Dataset 구성
- 해당 없음(모델 기반). 운전점 종류 NR.

### [9] 사용 신호
- 신호: 컨버터 출력(AC) 상전류 → 커패시터 전류의 스위칭 주파수 성분 재구성; DC-link 전압(리플). 초록: 'it is possible to estimate the switching component of the capacitor current by measuring the output currents of the converter'.
- Sampling frequency: Not reported / Full text verification required

### [10] 센서 구성
- Existing inverter sensor only?: **Yes (초록 기준: 출력 전류 측정만으로 커패시터 전류 스위칭 성분 추정; 커패시터 전류 센서 불필요)**
- 추가 센서: None (초록 기준)
- Derived / reconstructed: Yes — 출력 상전류(+스위칭 상태, 추론) → 커패시터 전류 스위칭 주파수 성분. 재구성 식 자체는 본문 확인 필요.

### [11] 전처리 및 Feature Extraction
- 전처리: 스위칭 주파수 성분 추출(방법: 필터/FFT 여부 NR)
- Feature: fsw 대역 커패시터 전류·전압 성분 → DF 계산

### [12] 진단 기법
- Analytical: 재구성 전류·전압 리플의 fsw 성분으로 DF 계산 → EoL 임계 비교. 스위칭 주파수·ESL(capacitor series inductor)·계통 필터의 영향 분석(초록). RLS/Kalman 등 추정기 사용 여부 NR.
- Hyperparameter: 해당 없음

### [13] AI 모델 입력·출력
AI 모델 아님(분석적/모델 기반 방법).

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- DF 를 전해 커패시터 수명 지표로 제안하고 EoL 기준 제시(초록)
- 출력 전류 측정만으로 커패시터 전류 스위칭 성분 추정 → 커패시터 전류 센서 불필요(초록)
- fsw·ESL·계통 필터가 DF 측정 정확도에 미치는 영향 분석(초록)
- 실험으로 수용 가능한 정확도 검증(초록)

My interpretation:
새로운 점은 '측정 지표를 C 또는 ESR 이 아닌 DF 로 바꾼 것' 과 '출력 전류로 커패시터 전류를 재구성한 것' 의 결합이다. DF 는 C·ESR 를 분리하지 못하므로 내 연구에서는 재구성 전류 철학만 가져오고 지표는 분리형으로 바꾸는 것이 자연스럽다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **True Online** — 초록상 주입·시퀀스 없이 정상 운전 중 스위칭 성분을 이용(사실). 상세 운전조건 제약은 본문 확인 필요.
- On-board implementation: Not reported / Full text verification required (DSP/FPGA 구현 언급 없음; 실험 결과는 있음)

### [16] On-board Hardware Environment
| 항목 | 값 |
|---|---|
| DSP | Not reported / Full text verification required |
| MCU | Not reported / Full text verification required |
| FPGA | Not reported / Full text verification required |
| Sampling ADC | Not reported / Full text verification required |
| Memory | Not reported / Full text verification required |
| Sampling frequency | Not reported / Full text verification required |
| Control frequency | Not reported / Full text verification required |
| Execution time | Not reported / Full text verification required |
| Inference time / model size | 해당 없음 |

### [17] Real-time 가능성
- **Real-time feasible** — fsw 성분 추출과 DF 계산은 Goertzel/대역필터 수준의 연산이므로 제어기 탑재가 가능하다고 판단(해석). 구현 시연은 초록에 없음.

### [18] 실험 환경
| Parameter | Value |
|---|---|
| DC-Link Voltage | Not reported / Full text verification required |
| Output Voltage | Not reported / Full text verification required |
| Power | Not reported / Full text verification required |
| Load | Not reported / Full text verification required |
| Motor | 해당 없음(B2B 컨버터) |
| Motor speed | Not reported / Full text verification required |
| Torque | Not reported / Full text verification required |
| Switching Frequency | Not reported / Full text verification required |
| Fundamental Frequency | Not reported / Full text verification required |
| Modulation | Not reported / Full text verification required |
| Capacitor | Not reported / Full text verification required |
| Sampling Frequency | Not reported / Full text verification required |

### [19] Operating Condition 다양성
- NR. 초록은 fsw·ESL·필터 '요인' 영향 분석을 언급하나 부하·변조지수 변화 실험 여부는 미확인.

### [20] 최종 성능
- 종합: 수치 NR ('acceptable accuracy' 만 초록에 있음)
- C error: 해당 없음(DF 지표) / ESR error: 해당 없음(DF 지표) / Classification metrics: 해당 없음

### [21] Noise / Robustness
- fsw·ESL·계통 필터 영향 분석(초록). 측정 노이즈·온도·부하 변화 검증 여부 NR.

### [22] 장점
- 커패시터 전류 센서 없이 출력 전류로 재구성 → 센서 비용 0 추가
- 주입 없음 → 전력품질·제어 영향 없음
- DF 하나로 C 감소·ESR 증가를 모두 반영
- fsw·ESL·필터 의존성을 저자가 직접 분석 → 설계 시 보정 근거

### [23] 한계
Authors' stated limitation:
- (초록 기준) fsw·ESL·계통 필터가 DF 정확도에 영향 — 영향 분석이 필요함을 저자가 인정

Additional limitation identified (분석자):
- DF 로는 C 와 ESR 을 분리할 수 없음 → 열화 메커니즘 구분 불가
- 노화 샘플 값·실험 정격·오차 수치가 초록에 없어 성능 비교 불가(본문 필요)
- 재구성이 스위칭 상태·데드타임·샘플링 동기화에 의존(추론) — 구현 오차원
- 운전조건(부하·변조지수) 다양성 검증 여부 미확인

### [24] 내 연구 목표와의 관련성
- **Very High** — 2L(추정) 3상 컨버터, 기존 센서, True Online, 커패시터 전류 재구성 — 내 목표 파이프라인의 신호 생성 단계와 가장 가깝다. 단 AI·분류 요소는 없음.

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | B2B VSC (2L 추정) | 2-Level 3-Phase |
| Capacitor | DC-link 전해 | DC-Link |
| Signal | 출력 상전류 + vdc (기존 센서) | Existing inverter signal preferred |
| Aging Target | DF (C·ESR 결합) | C / ESR |
| Diagnosis | 연속 지표(회귀형) | Classification or Regression |
| Online | Yes (True Online) | Yes |
| On-board | 구현 NR | Yes |
| Extra Sensor | No | Preferably No |
| AI | No | Candidate |
| Real-time | 시연 NR | Required |

### [26] 재현 가능성
- **Moderate** — 재구성 수식과 fsw 성분 추출은 MATLAB/Simulink 로 구현 가능하나, 본문의 ESL·필터 보정식과 EoL 기준을 확인해야 결과를 비교할 수 있다.
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: ia, ib, ic, 스위칭 함수(Sa,Sb,Sc), vdc, (검증용) iC. 변화 파라미터: C(−0 ~ −20 %), ESR(×1 ~ ×2) 독립·동시 스윕, fsw 2–3 단계, 부하·변조지수. 데이터셋: 각 조합에서 정상상태 수 주기 파형 → fsw 성분·DF.

### 선정 점수 (10 기준 × 10점)
| c1 8 | c2 10 | c3 8 | c4 10 | c5 10 | c6 7 | c7 3 | c8 8 | c9 3 | c10 6 | **Total 73** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: '출력 상전류 → 커패시터 전류 스위칭 성분 재구성 → fsw 대역 지표' 의 IEEE TPEL 선례. 내 신호 생성 단계의 근거 논문.
- 집중할 Figure/Table/Equation: 재구성 수식(출력 전류→커패시터 전류), DF 정의·EoL 기준, fsw/ESL/필터 영향 절과 해당 Figure, 실험 셋업 표
- 동반·후속 논문: 후속: Ghadrdan et al., 'Dissipation Factor as a Degradation Indicator for Electrolytic Capacitors', IEEE JESTPE 11(1):1035–1044, 2023 (VBN); 과도 기반: Ghadrdan, Abdi, Peyghami, Mokhtari, Blaabjerg, IEEE JESTPE 11(1):1132–1142, 2023, DOI 10.1109/JESTPE.2022.3163012 (스위칭 로직 일시 변경, C <1 % vs LCR).

---

(본 파일은 `2level_inverter_dc_link_capacitor_onboard_top10.md` 7절과 동일 내용. 본문 확보 후 `Not reported / Full text verification required` 항목을 채워 갱신한다.)
