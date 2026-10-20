# 08. A Transient-Modeling-Based Grey-Box Method for Online Monitoring of DC-Link Capacitors (제목 표기 VBN 레코드 기준 — 하이픈 등 정확 표기 확인 필요)

> Tier B · Rank 8 · Score 73/100 · **Evidence: Abstract-level only** (본문 미열람; 아래 `Not reported / Full text verification required` 항목은 추측으로 채우지 않았다)

### [1] 기본 논문 정보
- Title: A Transient-Modeling-Based Grey-Box Method for Online Monitoring of DC-Link Capacitors (제목 표기 VBN 레코드 기준 — 하이픈 등 정확 표기 확인 필요)
- Authors: (S.) Zhao, Hu, He, Lu, H. H. C. Iu, F. Blaabjerg, P. Davari (이름 이니셜 일부 NR)
- Year: 2023
- Journal: IEEE Transactions on Power Electronics, vol. 38, no. 11, pp. 14547–14562 (Nov. 2023)
- DOI: 10.1109/TPEL.2023.3308115
- Publication Type: Journal (2023 TPEL Second Place Prize Paper Award — VBN)
- 식별/출처: IEEE Xplore 10229504; AAU VBN(AAM PDF 547236531/FINAL_VERSION.pdf — 본 환경에서 미열람)
- 저자 소속: Southwest Jiaotong Univ., Chongqing Univ., Univ. of Western Australia, Aalborg Univ. (스니펫)

### [2] Converter / Inverter Topology
- Topology: 일반 DC-link(토폴로지 비의존). 시뮬: AC/DC 및 DC/DC 시스템; 실험: 상용 전원장치(commercial power supply). 2L 인버터 실험 아님.
- Power rating: Not reported / Full text verification required / DC-link voltage: Not reported / Full text verification required / AC output voltage: Not reported / Full text verification required
- Switching frequency: Not reported / Full text verification required / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: 상용 전원장치

### [3] Classification vs Regression
- Task: **Regression (C via damping factor α)**
- DC-link 전압 과도의 병렬 RLC 영상태 응답에서 감쇠 계수 α 를 HI 로 추출 → C 추정.
- Output 단위: α, C

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
- Not reported / Full text verification required

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| — | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required |

논문에 나온 값이 스니펫·초록에 없어 표를 채우지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): Not reported / Full text verification required

### [7] C / ESR 변화 여부
- **C (α 는 C 에 비례; ESR 변경 여부 NR)**

### [8] Dataset 구성
- 해당 없음(grey-box 모델)

### [9] 사용 신호
- 신호: DC-link 전압 과도(대신호 과도) — '극히 낮은 샘플링 주파수' 로 충분(초록)
- Sampling frequency: 수치 NR ('extremely low sampling frequency')

### [10] 센서 구성
- Existing inverter sensor only?: **Yes (전압 센서만)**
- 추가 센서: None
- Derived / reconstructed: No

### [11] 전처리 및 Feature Extraction
- 전처리: 과도 구간 분리·피팅(세부 NR)
- Feature: 감쇠 계수 α

### [12] 진단 기법
- Grey-box: 과도 등가회로 모델(TECM) + 파라미터 피팅. 토폴로지·제어 지식 최소 요구(초록).
- Hyperparameter: 해당 없음

### [13] AI 모델 입력·출력
AI 모델 아님(분석적/모델 기반 방법).

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- 과도 모델링 기반 grey-box 온라인 감시(제목)
- α 를 HI 로 하는 TECM — 토폴로지·제어 지식 최소(초록)
- 극히 낮은 샘플링 요구(초록)
- α·C 추정 오차 1 % 미만(실험, 초록)

My interpretation:
'전압 센서 하나 + 자연 과도 + 저샘플링' 으로 1 % 미만을 달성한 점이 강점. 연속 감시가 아니라 과도 이벤트가 있을 때만 갱신되므로 True Online 과는 구분해야 한다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **Quasi-Online (이벤트형: 자연 발생 대신호 과도 필요)** — 정상 운전을 멈추지는 않지만 과도가 있어야 추정(초록 취지).
- On-board implementation: Not reported / Full text verification required

### [16] On-board Hardware Environment
| 항목 | 값 |
|---|---|
| DSP | Not reported / Full text verification required |
| MCU | Not reported / Full text verification required |
| FPGA | Not reported / Full text verification required |
| Sampling ADC | Not reported / Full text verification required |
| Memory | Not reported / Full text verification required |
| Sampling frequency | 극저 샘플링(수치 NR) |
| Control frequency | Not reported / Full text verification required |
| Execution time | Not reported / Full text verification required |
| Inference time / model size | 해당 없음 |

### [17] Real-time 가능성
- **Real-time feasible** — 저샘플링 과도 피팅은 계산량이 작다(해석). 구현 시연 NR.

### [18] 실험 환경
| Parameter | Value |
|---|---|
| DC-Link Voltage | Not reported / Full text verification required |
| Output Voltage | Not reported / Full text verification required |
| Power | Not reported / Full text verification required |
| Load | 상용 전원장치 |
| Motor | 해당 없음 |
| Motor speed | 해당 없음 |
| Torque | 해당 없음 |
| Switching Frequency | Not reported / Full text verification required |
| Fundamental Frequency | Not reported / Full text verification required |
| Modulation | Not reported / Full text verification required |
| Capacitor | Not reported / Full text verification required |
| Sampling Frequency | Not reported / Full text verification required |

### [19] Operating Condition 다양성
- Not reported / Full text verification required

### [20] 최종 성능
- 종합: α·C 오차 <1 % (실험, 초록)
- C error: <1 % / ESR error: 해당 없음 / Classification metrics: 해당 없음

### [21] Noise / Robustness
- 토폴로지·제어 지식 최소 요구(초록). 노이즈·온도 NR.

### [22] 장점
- 전압 센서만
- 저샘플링 → 저가 구현
- <1 % 실험 정확도
- 수상 논문(방법 품질)

### [23] 한계
Authors' stated limitation:
- Not reported / Full text verification required

Additional limitation identified (분석자):
- 2L 인버터 실험 아님(상용 전원장치)
- 과도 이벤트 의존 → 연속 감시 불가
- C only
- 노화 샘플 NR

### [24] 내 연구 목표와의 관련성
- **Medium** — 물리 모델·저샘플링 설계의 참고. 내 목표(연속 True Online, C+ESR, 2L)와는 구조가 다름.

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | 일반(실험: 전원장치) | 2-Level 3-Phase |
| Capacitor | DC-link | DC-Link |
| Signal | vdc 과도 | Existing inverter signal preferred |
| Aging Target | C(α) | C / ESR |
| Diagnosis | Regression | Classification or Regression |
| Online | 이벤트형 | Yes |
| On-board | NR | Yes |
| Extra Sensor | No | Preferably No |
| AI | No | Candidate |
| Real-time | 미시연 | Required |

### [26] 재현 가능성
- **Moderate** — 과도 RLC 피팅은 쉽지만 TECM 정의·과도 검출 로직은 본문 필요. AAM PDF 가 공개되어 로컬 확보 가능.
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: vdc(부하 스텝 전후), 부하 전류. 변화 파라미터: C 단계. 데이터셋: 과도 구간별 α.

### 선정 점수 (10 기준 × 10점)
| c1 5 | c2 10 | c3 8 | c4 7 | c5 10 | c6 8 | c7 3 | c8 8 | c9 8 | c10 6 | **Total 73** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: 전압 센서만으로 1 % 미만을 낸 물리 모델(과도) 기준점. 내 리플 기반 방법의 '보조 경로(과도 시 C 교정)' 로 검토.
- 집중할 Figure/Table/Equation: TECM 유도(병렬 RLC, α 정의), 샘플링 요구 분석, 실험 셋업·오차 표
- 동반·후속 논문: 같은 흐름: Dai, Zhao, Han, Sun, Chen, IEEE JESTPE 12(2):2281–2291, 2024, DOI 10.1109/JESTPE.2024.3370616 (부하 변화 과도 + 전류 적분 재구성, 저샘플링).

---

(본 파일은 `2level_inverter_dc_link_capacitor_onboard_top10.md` 7절과 동일 내용. 본문 확보 후 `Not reported / Full text verification required` 항목을 채워 갱신한다.)
