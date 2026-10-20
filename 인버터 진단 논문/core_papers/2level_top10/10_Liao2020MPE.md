# 10. Fault Diagnosis of Capacitance Aging in DC Link Capacitors of Voltage Source Inverters Using Evidence Reasoning Rule

> Tier B · Rank 10 · Score 62/100 · **Evidence: Abstract-level only** (본문 미열람; 아래 `Not reported / Full text verification required` 항목은 추측으로 채우지 않았다)

### [1] 기본 논문 정보
- Title: Fault Diagnosis of Capacitance Aging in DC Link Capacitors of Voltage Source Inverters Using Evidence Reasoning Rule
- Authors: Linhao Liao, Haibo Gao, Yelan He, Xiaobin Xu, Zhiguo Lin, Yajie Chen, Fubing You
- Year: 2020
- Journal: Mathematical Problems in Engineering (Hindawi/Wiley, OA), vol. 2020, art. 5724019, pp. 1–12 (published 31 Mar 2020)
- DOI: 10.1155/2020/5724019
- Publication Type: Journal (OA)
- 식별/출처: onlinelibrary.wiley.com/doi/10.1155/2020/5724019; hindawi.com; ideas.repec.org hin/jnlmpe/5724019
- 저자 소속: Not reported / Full text verification required

### [2] Converter / Inverter Topology
- Topology: 전압형 인버터(VSI) 시뮬레이션. 레벨 수 미명시(일반 VSI = 2L 추정).
- Power rating: Not reported / Full text verification required / DC-link voltage: Not reported / Full text verification required / AC output voltage: Not reported / Full text verification required
- Switching frequency: Not reported / Full text verification required / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: Not reported / Full text verification required

### [3] Classification vs Regression
- Task: **Classification (3 ranges: normal / incipient fault / failed) — 노화 등급 판정**
- C 잔존율 구간으로 등급 정의. '등급 추정(aging fault level)' 이라 소프트 분류(증거 융합 신뢰도)일 수 있음.
- Output 단위: 등급(및 증거 융합 신뢰도)

| Class | 의미 | C | ESR |
|---|---|---|---|
| 0 | Normal | C = 초기값의 90–100 % | Not reported / Full text verification required |
| 1 | Incipient fault | C = 초기값의 80–90 % | Not reported / Full text verification required |
| 2 | Failed (no longer incipient) | C < 초기값의 80 % | Not reported / Full text verification required |

### [4] 커패시터 기본 정보
| 항목 | 값 |
|---|---|
| Technology | Not reported / Full text verification required |
| Manufacturer | 해당 없음(시뮬) |
| Model | 해당 없음 |
| Rated C | 7500 µF (시뮬레이션 초기 설정값, 본문 스니펫) |
| Rated V | Not reported / Full text verification required |
| Rated ESR | Not reported / Full text verification required |
| Temperature rating | Not reported / Full text verification required |

### [5] 노화 모사 방식
- Simulation — C 를 초기값 대비 여러 수준으로 감소. 서론 기준: C −20 % 또는 ESR ×2 = 수명 종료.

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| S1 | Normal | 초기값(7500 µF)의 90–100 % (µF 수치 NR) | 0 ~ −10 % | Not reported / Full text verification required | Not reported / Full text verification required |
| S2 | Incipient fault | 초기값의 80–90 % (µF 수치 NR) | −10 ~ −20 % | Not reported / Full text verification required | Not reported / Full text verification required |
| S3 | Failed | 초기값의 <80 % (µF 수치 NR) | < −20 % | Not reported / Full text verification required | Not reported / Full text verification required |

구간 경계(%)만 본문 스니펫에 있음. 구간 내 개별 시뮬 값·µF 환산값·ESR 설정은 논문 표기가 확인되지 않아 적지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): 해당 없음(시뮬; ESR 변경 여부 NR)

### [7] C / ESR 변화 여부
- **C only (스니펫 기준)**

### [8] Dataset 구성
- NR (샘플 수·분할 미확인; '증거' 는 vdc 특징)

### [9] 사용 신호
- 신호: DC-link 전압 특징(진단 증거)
- Sampling frequency: Not reported / Full text verification required

### [10] 센서 구성
- Existing inverter sensor only?: **Yes (vdc 만)**
- 추가 센서: None
- Derived / reconstructed: No

### [11] 전처리 및 Feature Extraction
- 전처리: Not reported / Full text verification required
- Feature: vdc 에서 추출한 특징(종류 NR) → 각 특징을 증거로 변환

### [12] 진단 기법
- Evidence Reasoning(ER) rule 융합(증거 가중치 조정 가능) vs BP 신경망 비교.
- Hyperparameter: Not reported / Full text verification required

### [13] AI 모델 입력·출력
| Item | Information |
|---|---|
| Input | vdc 특징 |
| Input shape | Not reported / Full text verification required |
| Preprocessing | Not reported / Full text verification required |
| Feature dimension | Not reported / Full text verification required |
| Model | ER rule (vs BP-NN) |
| Output | 노화 등급(3 구간) |
| Loss | 해당 없음 |
| Optimizer | 해당 없음 |

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- vdc 특징을 증거로 ER rule 로 융합해 노화 등급 추정(초록)
- BP-NN 보다 우수(초록)
- 증거별 가중치 조정 가능(초록)
- ANN 은 학습 샘플 수에 정확도가 제한됨을 지적(서론)

My interpretation:
이 조사에서 '등급 경계(90/80 %)' 를 명시한 유일한 저널 후보. 내 분류 라벨 설계(정상/초기/고장) 의 출발점으로 쓸 수 있으나, 시뮬레이션 전용·C only·특징 정의 불명이라 방법 자체보다 라벨 정의를 참고한다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **Quasi-Online/주장 Online (시뮬레이션)** — 'online monitoring method' 라 하나 시뮬레이션만, 구현 없음.
- On-board implementation: No (시뮬레이션)

### [16] On-board Hardware Environment
| 항목 | 값 |
|---|---|
| DSP | 해당 없음 |
| MCU | 해당 없음 |
| FPGA | 해당 없음 |
| Sampling ADC | 해당 없음 |
| Memory | 해당 없음 |
| Sampling frequency | Not reported / Full text verification required |
| Control frequency | Not reported / Full text verification required |
| Execution time | Not reported / Full text verification required |
| Inference time / model size | Not reported / Full text verification required |

### [17] Real-time 가능성
- **Offline post-processing only** — 시뮬레이션 데이터의 후처리.

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
| Capacitor | 7500 µF(초기) |
| Sampling Frequency | Not reported / Full text verification required |

### [19] Operating Condition 다양성
- Not reported / Full text verification required

### [20] 최종 성능
- 종합: BP-NN 대비 우수(수치 NR)
- C error: 해당 없음 / ESR error: 해당 없음 / Classification metrics: Accuracy/F1/혼동행렬 NR

### [21] Noise / Robustness
- 증거 가중치 조정으로 강건성 조절 가능(초록 취지). 노이즈·운전조건 NR.

### [22] 장점
- 등급 경계(90/80 %) 명시
- vdc 만 사용
- 소표본에서 ANN 대안(ER rule)
- OA

### [23] 한계
Authors' stated limitation:
- (서론) ANN 은 학습 샘플 수에 제한 — 저자가 ER rule 로 대체한 동기

Additional limitation identified (분석자):
- 시뮬레이션 전용, 실험 없음
- C only, ESR 미고려
- 특징·성능 수치 NR
- 저널 등급 낮음(MPE)

### [24] 내 연구 목표와의 관련성
- **Medium** — 분류 라벨 설계 참고용. 2L 실험·on-board·ESR 요소 없음.

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | VSI 시뮬(2L 추정) | 2-Level 3-Phase |
| Capacitor | DC-link | DC-Link |
| Signal | vdc 특징 | Existing inverter signal preferred |
| Aging Target | C (3 구간) | C / ESR |
| Diagnosis | Classification(3) | Classification or Regression |
| Online | 시뮬 | Yes |
| On-board | No | Yes |
| Extra Sensor | No | Preferably No |
| AI | ER rule / BP-NN | Candidate |
| Real-time | 후처리 | Required |

### [26] 재현 가능성
- **Easy** — Simulink 에서 C 를 90/80 % 경계로 바꾸고 vdc 특징을 뽑는 것은 바로 가능. ER rule 구현은 본문 수식 필요(OA).
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: vdc. 변화 파라미터: C 100→70 % 를 2.5–5 % 간격. 데이터셋: 구간별 라벨 + vdc 특징.

### 선정 점수 (10 기준 × 10점)
| c1 7 | c2 10 | c3 2 | c4 6 | c5 8 | c6 6 | c7 6 | c8 6 | c9 3 | c10 8 | **Total 62** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: 분류 등급 정의(정상 90–100 % / 초기 80–90 % / 고장 <80 %)를 명시한 유일한 후보 — 라벨 설계의 출발점.
- 집중할 Figure/Table/Equation: 등급 정의 표, 특징(증거) 정의, ER 융합 수식, BP-NN 비교 결과표
- 동반·후속 논문: 분류 참고(학회): Seferian, Bazzi, Hajj, ECCE 2020 (3 클래스 healthy/half/fully degraded, 99 %, 저가 MCU, 단상 PV 시뮬).

---

(본 파일은 `2level_inverter_dc_link_capacitor_onboard_top10.md` 7절과 동일 내용. 본문 확보 후 `Not reported / Full text verification required` 항목을 채워 갱신한다.)
