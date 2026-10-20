# 04. Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor Based on Analysis of a Six-Pulse Diode Rectifier Having AC and DC Inductors

> Tier A · Rank 4 · Score 76/100 · **Evidence: Abstract-level only** (본문 미열람; 아래 `Not reported / Full text verification required` 항목은 추측으로 채우지 않았다)

### [1] 기본 논문 정보
- Title: Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor Based on Analysis of a Six-Pulse Diode Rectifier Having AC and DC Inductors
- Authors: K. Hasegawa, Y. Hirose
- Year: 2024
- Journal: IEEE Transactions on Industry Applications, vol. 60, no. 6, pp. 9043–9051 (Nov./Dec. 2024)
- DOI: (확인 필요) — Kyutech 교원 목록·리포지터리에서 권/호/쪽만 확인, IEEE 페이지 미열람
- Publication Type: Journal (ECCE 2023 학회판의 저널 확장)
- 식별/출처: Kyutech repository (kyutech.repo.nii.ac.jp), 교원 업적 DB hyokadb02; 학회판 ECCE 2023
- 저자 소속: Kyushu Institute of Technology (Hasegawa 연구실). First author Hasegawa.

### [2] Converter / Inverter Topology
- Topology: 6-pulse 다이오드 정류기(AC 라인 인덕터 + DC 인덕터) + 3상 PWM 인버터 — 정류기-인버터 드라이브(보조 범위; 인버터부는 3상 PWM 인버터 = 2L 로 추정).
- Power rating: NR (2025 MR 후속: 1.5 kW) / DC-link voltage: 200 V 급 실험 시스템(초록 '200-V laboratory system') / AC output voltage: Not reported / Full text verification required
- Switching frequency: Not reported / Full text verification required / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: Not reported / Full text verification required

### [3] Classification vs Regression
- Task: **Regression (C+ESR)**
- C 와 ESR 변화를 모두 관측·추정(초록 'both ESR and capacitance changes were observed').
- Output 단위: C, ESR (단위 NR)

해당 없음(회귀/연속 지표) 또는 클래스 정의 NR.

### [4] 커패시터 기본 정보
| 항목 | 값 |
|---|---|
| Technology | Not reported / Full text verification required (전해 추정 — 리플 전류 해석 대상) |
| Manufacturer | Not reported / Full text verification required |
| Model | Not reported / Full text verification required |
| Rated C | Not reported / Full text verification required |
| Rated V | Not reported / Full text verification required |
| Rated ESR | Not reported / Full text verification required |
| Temperature rating | Not reported / Full text verification required |

### [5] 노화 모사 방식
- NR (실험에서 C·ESR 변화를 '관측' 했다고만 초록에 기재 — 커패시터 교체/저항 추가 여부 미확인)

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| — | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required |

논문에 나온 값이 스니펫·초록에 없어 표를 채우지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): Not reported / Full text verification required

### [7] C / ESR 변화 여부
- **C + ESR (둘 다 변화를 관측했으나 동시/개별 여부 NR)**

### [8] Dataset 구성
- 해당 없음(모델 기반)

### [9] 사용 신호
- 신호: 3상 AC 전원 전압, AC 라인 인덕터·DC 인덕터 값(파라미터), 인버터 출력 전력 → 커패시터 전류 계산; DC-link 전압(리플). 전류 센서 미사용.
- Sampling frequency: Not reported / Full text verification required

### [10] 센서 구성
- Existing inverter sensor only?: **Yes — 전류 센서 자체를 쓰지 않음(초록). 전원 전압 측정이 필요하므로 '인버터 기존 센서' 관점에서는 전원 전압 센서 유무에 따라 Partially 가 될 수 있음(해석).**
- 추가 센서: None (전류 센서 없음; 전원 전압 센서는 드라이브 구성에 따라 다름)
- Derived / reconstructed: Yes — 정류기 해석 모델(전원 전압 + 인덕터 + 출력 전력)로 커패시터 전류를 계산.

### [11] 전처리 및 Feature Extraction
- 전처리: 정류 리플(6f1 계열) 성분 해석 — FFT 여부 NR(관련 2019 IEEJ·2024 학회판은 FFT 사용)
- Feature: 정류 리플 전류·전압 성분 → ESR, C

### [12] 진단 기법
- Analytical: 6-pulse 정류기 리플 전류 모델 → 커패시터 전류 계산 → 리플 전압과의 관계로 ESR·C 산출.
- Hyperparameter: 해당 없음

### [13] AI 모델 입력·출력
AI 모델 아님(분석적/모델 기반 방법).

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- 전류 센서 없이 DC-link 커패시터 CM(제목·초록)
- AC·DC 인덕터를 모두 가진 6-pulse 정류기 해석으로 커패시터 전류 계산(초록)
- 200 V 실험으로 ESR·C 변화 모두 관측(초록)

My interpretation:
'커패시터 전류를 측정하지 않고 계산한다' 는 점에서 내 재구성 접근과 같은 철학이지만, 정보원이 인버터 스위칭이 아니라 정류기 리플이다. 정류기 전단 드라이브에서는 이 방법이 가장 단순하고, 인버터 측 재구성과 결합하면 C·ESR 를 두 대역에서 교차 검증할 수 있다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **True Online** — 정상 운전 중 고유 정류 리플을 이용, 주입 없음(초록).
- On-board implementation: 본 논문 NR. 같은 그룹의 2024 학회판·2025 MR 논문은 'Leafony' 소형 MCU 에서 FFT 로 ESR 감시(스니펫; 2025 MR 판 귀속은 확인 필요).

### [16] On-board Hardware Environment
| 항목 | 값 |
|---|---|
| DSP | Not reported / Full text verification required |
| MCU | Leafony 소형 MCU (학회판/후속 논문; 본 논문 귀속 NR) |
| FPGA | Not reported / Full text verification required |
| Sampling ADC | Not reported / Full text verification required |
| Memory | Not reported / Full text verification required |
| Sampling frequency | Not reported / Full text verification required |
| Control frequency | Not reported / Full text verification required |
| Execution time | Not reported / Full text verification required |
| Inference time / model size | 해당 없음 |

### [17] Real-time 가능성
- **Real-time feasible (후속 논문에서 MCU 구현 시사)** — FFT 한 번과 대수 계산으로 구성되어 소형 MCU 에서도 가능함을 같은 그룹이 보였다(스니펫).

### [18] 실험 환경
| Parameter | Value |
|---|---|
| DC-Link Voltage | 200 V 급 |
| Output Voltage | Not reported / Full text verification required |
| Power | NR (후속 1.5 kW) |
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
- NR (본 논문). 후속 2025 MR: 전원 전압 불평형 ≈5 % 까지 유효.

### [20] 최종 성능
- 종합: Not reported / Full text verification required (초록은 '변화를 관측' 으로만 기술)
- C error: Not reported / Full text verification required / ESR error: Not reported / Full text verification required / Classification metrics: 해당 없음

### [21] Noise / Robustness
- 후속 2025 MR 에서 전원 불평형 강건성 다룸. 부하·온도 NR.

### [22] 장점
- 전류 센서 완전 배제 → 비용·설치 최소
- C 와 ESR 동시
- True Online
- 소형 MCU 구현 계열(후속)

### [23] 한계
Authors' stated limitation:
- Not reported / Full text verification required

Additional limitation identified (분석자):
- 정류기 전단(다이오드) 드라이브에 한정 — AFE·PV·배터리 입력 2L 인버터에는 적용 불가(추론)
- 인버터 출력 전력·인덕터 값 등 파라미터 의존 → 파라미터 오차가 추정 오차로 전파(추론)
- 오차 수치·노화 샘플 미확인

### [24] 내 연구 목표와의 관련성
- **High** — 방법 철학(센서 없는 커패시터 전류 계산, C+ESR 동시)은 매우 유용하나, 정보원이 정류 리플이라 내 '인버터 신호' 목표와 다르다.

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | 다이오드 정류기 + 3상 PWM 인버터 | 2-Level 3-Phase |
| Capacitor | DC-link | DC-Link |
| Signal | 전원 전압 + 출력 전력 + vdc (전류 센서 없음) | Existing inverter signal preferred |
| Aging Target | C + ESR | C / ESR |
| Diagnosis | Regression | Classification or Regression |
| Online | Yes (True Online) | Yes |
| On-board | 후속 MCU | Yes |
| Extra Sensor | No | Preferably No |
| AI | No | Candidate |
| Real-time | 후속에서 시연 시사 | Required |

### [26] 재현 가능성
- **Moderate** — 정류기 리플 모델은 Simulink 로 재현 가능. 인덕터 값·출력 전력 추정 방법이 본문에만 있음.
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: 전원 3상 전압, vdc, (검증) iC, 출력 전력(상전류·전압). 변화 파라미터: C, ESR 각 3–5 단계, 부하 3단계, 전원 불평형. 데이터셋: 조합별 정류 리플 성분.

### 선정 점수 (10 기준 × 10점)
| c1 7 | c2 10 | c3 9 | c4 10 | c5 10 | c6 10 | c7 3 | c8 8 | c9 3 | c10 6 | **Total 76** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: 전류 센서 없이 C+ESR 를 동시에 추정한 IEEE TIA 최신 논문. '측정 대신 계산' 의 오차 처리 방식을 배울 수 있다.
- 집중할 Figure/Table/Equation: 커패시터 전류 계산식(전원 전압·인덕터·출력 전력), ESR/C 산출식, 200 V 실험 셋업 표, C·ESR 변화 관측 그림
- 동반·후속 논문: K. Hasegawa, T. Kubo, Y. Hirose, IEEJ J. Ind. Appl. 2023 (DC 인덕터만); Yamasoto & Hasegawa, Microelectronics Reliability 173:115873, 2025, DOI 10.1016/j.microrel.2025.115873 (200 V 1.5 kW, 불평형 ≈5 %); Hasegawa, Nishizawa, Omura, Microelectron. Reliab. 88–90:433–437, 2018.

---

(본 파일은 `2level_inverter_dc_link_capacitor_onboard_top10.md` 7절과 동일 내용. 본문 확보 후 `Not reported / Full text verification required` 항목을 채워 갱신한다.)
