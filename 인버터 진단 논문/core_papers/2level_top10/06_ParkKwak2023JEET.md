# 06. DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs

> Tier A · Rank 6 · Score 66/100 · **Evidence: Abstract-level only** (본문 미열람; 아래 `Not reported / Full text verification required` 항목은 추측으로 채우지 않았다)

### [1] 기본 논문 정보
- Title: DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs
- Authors: Hye-Jin Park, Sangshin Kwak
- Year: 2023
- Journal: Journal of Electrical Engineering & Technology (Springer/KIEE), vol. 18, no. 3, pp. 1841–1850 (May 2023)
- DOI: 10.1007/s42835-023-01424-z
- Publication Type: Journal
- 식별/출처: Springer; CAU ScholarWorks 2019.sw.cau/66390; RG (Feb 2023)
- 저자 소속: Chung-Ang University (곽상신 연구실). First author Park, corresponding Kwak(추정).

### [2] Converter / Inverter Topology
- Topology: 3상 DC/AC 컨버터(입력 커패시터 = DC-link). 레벨 수 미명시(2L 추정). 정격 NR.
- Power rating: Not reported / Full text verification required / DC-link voltage: Not reported / Full text verification required / AC output voltage: Not reported / Full text verification required
- Switching frequency: Not reported / Full text verification required / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: Not reported / Full text verification required

### [3] Classification vs Regression
- Task: **Regression (C+ESR)**
- 커패시터 내부 상태(C, ESR) 를 딥러닝으로 추정(회귀). 분류 아님.
- Output 단위: C, ESR (단위 NR)

해당 없음(회귀/연속 지표) 또는 클래스 정의 NR.

### [4] 커패시터 기본 정보
| 항목 | 값 |
|---|---|
| Technology | Not reported / Full text verification required |
| Manufacturer | Not reported / Full text verification required |
| Model | Not reported / Full text verification required |
| Rated C | Not reported / Full text verification required |
| Rated V | Not reported / Full text verification required |
| Rated ESR | Not reported / Full text verification required |
| Temperature rating | Not reported / Full text verification required |

### [5] 노화 모사 방식
- NR. 선행 JPE 2022(단상)는 '실험 전압·전류 파형' 을 사용 — 본 3상 논문의 실험/시뮬 여부는 미확인.

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| — | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required |

논문에 나온 값이 스니펫·초록에 없어 표를 채우지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): Not reported / Full text verification required

### [7] C / ESR 변화 여부
- **C + ESR (둘 다 추정 대상; 데이터 생성 시 동시 변화 여부 NR)**

### [8] Dataset 구성
- NR (샘플 수·분할·운전점 모두 미확인). 입력 구성은 '특정 단일 주파수 성분' vs '그 성분을 포함한 넓은 대역' 두 종류를 비교.

### [9] 사용 신호
- 신호: 주파수 성분(저주파 대역 → C, 중주파 대역 → ESR; 초록). 기반 신호는 NR — 선행 JPE 2022 는 커패시터 전압·전류의 FFT 성분(2·f1, fsw 지배 성분) 사용 → 본 논문도 유사할 가능성(추론).
- Sampling frequency: Not reported / Full text verification required

### [10] 센서 구성
- Existing inverter sensor only?: **NR (커패시터 전류를 쓴다면 'No' 에 해당 — 선행 논문 기준 추론)**
- 추가 센서: NR (커패시터 전류 센서 가능성)
- Derived / reconstructed: NR

### [11] 전처리 및 Feature Extraction
- 전처리: FFT 로 주파수 성분/대역 추출(초록 취지)
- Feature: 단일 주파수 성분(저/중) 또는 대역 스펙트럼 — 차원 NR

### [12] 진단 기법
- Deep learning: DNN, CNN, Simple RNN, LSTM 4종 비교. 결과: 단일 성분 입력엔 DNN, 광대역 입력엔 CNN 이 최선(초록).
- Hyperparameter: Not reported / Full text verification required

### [13] AI 모델 입력·출력
| Item | Information |
|---|---|
| Input | 주파수 성분(단일) 또는 대역 스펙트럼 |
| Input shape | Not reported / Full text verification required |
| Preprocessing | FFT |
| Feature dimension | Not reported / Full text verification required |
| Model | DNN / CNN / Simple RNN / LSTM |
| Output | C, ESR (회귀) |
| Loss | Not reported / Full text verification required |
| Optimizer | Not reported / Full text verification required |

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- 3상 DC/AC 컨버터 입력 커패시터 C·ESR 추정에 4종 딥러닝 비교(초록)
- 저주파 대역에 C 정보, 중주파 대역에 ESR 정보가 집중됨을 제시(초록)
- 입력 유형(단일 성분 vs 대역)에 따라 최적 모델이 다름: DNN vs CNN(초록)

My interpretation:
'어느 대역이 어느 파라미터를 담는가' 를 DL 입력 설계 관점에서 정리한 점이 유용하다. 내 연구의 '재구성 전류 스펙트럼 → CNN' 은 이 논문의 광대역-CNN 결론과 맞닿지만, 신호원(상전류 재구성)과 센서 조건(기존 센서)이 다르다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **True Online (추정)** — 정상 운전 리플의 주파수 성분을 입력으로 쓰는 구조(초록)이나, 센서·운전 조건·실시간 구현은 NR.
- On-board implementation: Not reported / Full text verification required (오프라인 학습·평가로 보임 — 구현 언급 없음)

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
| Inference time / model size | Not reported / Full text verification required |

### [17] Real-time 가능성
- **Real-time not demonstrated** — 초록에 구현·추론 시간 정보 없음. DNN/CNN 크기에 따라 가능할 수 있음(해석).

### [18] 실험 환경
| Parameter | Value |
|---|---|
| DC-Link Voltage | Not reported / Full text verification required |
| Output Voltage | Not reported / Full text verification required |
| Power | Not reported / Full text verification required |
| Load | Not reported / Full text verification required |
| Motor | Not reported / Full text verification required |
| Motor speed | Not reported / Full text verification required |
| Torque | Not reported / Full text verification required |
| Switching Frequency | Not reported / Full text verification required |
| Fundamental Frequency | Not reported / Full text verification required |
| Modulation | Not reported / Full text verification required |
| Capacitor | Not reported / Full text verification required |
| Sampling Frequency | Not reported / Full text verification required |

### [19] Operating Condition 다양성
- Not reported / Full text verification required

### [20] 최종 성능
- 종합: 정성(모델 간 우열)만 초록에 있음; MAE/RMSE NR
- C error: Not reported / Full text verification required / ESR error: Not reported / Full text verification required / Classification metrics: 해당 없음

### [21] Noise / Robustness
- Not reported / Full text verification required

### [22] 장점
- C·ESR 동시 회귀 + DL 4종 비교라는 설계 정보
- 대역-파라미터 대응(저주파→C, 중주파→ESR) 명시
- 3상 컨버터 대상(단상 선행에서 확장)

### [23] 한계
Authors' stated limitation:
- Not reported / Full text verification required

Additional limitation identified (분석자):
- 센서 조건·실험 여부·정격·데이터셋·오차 모두 미확인(본문 필수)
- 커패시터 전류 센서를 쓴다면 on-board 조건 불리(추론)
- 운전조건 다양성·일반화 검증 NR
- 저널 등급 중간(JEET)

### [24] 내 연구 목표와의 관련성
- **Very High** — 3상 인버터 DC-link C+ESR 를 FFT 성분 → DL 회귀로 다룬 유일한 저널 후보. 내 AI 설계(입력 대역, 모델 선택)에 직접 참고.

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | 3상 DC/AC (2L 추정) | 2-Level 3-Phase |
| Capacitor | DC-link(입력 커패시터) | DC-Link |
| Signal | 주파수 성분(신호원 NR) | Existing inverter signal preferred |
| Aging Target | C + ESR | C / ESR |
| Diagnosis | Regression (DL) | Classification or Regression |
| Online | 추정 Yes | Yes |
| On-board | NR | Yes |
| Extra Sensor | NR | Preferably No |
| AI | Yes (DNN/CNN/RNN/LSTM) | Candidate |
| Real-time | 미시연 | Required |

### [26] 재현 가능성
- **Moderate** — FFT 성분 → DNN/CNN 회귀는 Python 으로 쉽게 구성. 저자의 대역 정의·데이터 생성 조건을 본문에서 확인해야 비교 가능.
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: vC(=vdc), iC(검증용; 내 연구는 재구성 전류로 대체), ia/ib/ic, 스위칭 상태. 변화 파라미터: C×ESR 격자(예 5×5), 부하·변조지수. 데이터셋: 조합별 FFT 저/중 대역 벡터 → C, ESR 회귀, 운전점 기준 분할.

### 선정 점수 (10 기준 × 10점)
| c1 9 | c2 10 | c3 4 | c4 8 | c5 5 | c6 10 | c7 4 | c8 6 | c9 3 | c10 7 | **Total 66** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: 3상 DC-link C+ESR 를 DL 로 회귀한 저널 논문. 입력 대역 설계와 모델 선택(DNN vs CNN) 결론을 그대로 실험 설계에 쓸 수 있다.
- 집중할 Figure/Table/Equation: 입력 대역 정의 표, 데이터 생성 조건(실험/시뮬, 노화 샘플), 4개 모델 구조·hyperparameter 표, C/ESR 오차 표, 단일 성분 vs 대역 비교 그림
- 동반·후속 논문: 선행(단상): H.-J. Park, (Kim), S. Kwak, J. Power Electron. 22:513–521, 2022, DOI 10.1007/s43236-021-00366-x — DNN, FFT 저/중주파 성분, 11개 입력 조합, 실험 파형.

---

(본 파일은 `2level_inverter_dc_link_capacitor_onboard_top10.md` 7절과 동일 내용. 본문 확보 후 `Not reported / Full text verification required` 항목을 채워 갱신한다.)
