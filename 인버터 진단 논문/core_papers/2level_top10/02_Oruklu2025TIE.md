# 02. Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters

> Tier S · Rank 2 · Score 77/100 · **Evidence: Abstract-level only** (본문 미열람; 아래 `Not reported / Full text verification required` 항목은 추측으로 채우지 않았다)

### [1] 기본 논문 정보
- Title: Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters
- Authors: Kerim Örüklü, Şener Ağalar
- Year: 2025 (온라인 2024; 출처에 따라 2024/2025 표기 상이)
- Journal: IEEE Transactions on Industrial Electronics, vol. 72, no. 4, pp. 4227–4237 (Apr. 2025)
- DOI: 10.1109/TIE.2024.3454814 (검색 결과에 DOI 문자열이 직접 표시되지 않음 — 확인 필요)
- Publication Type: Journal
- 식별/출처: IEEE Xplore 10695772; Semantic Scholar 5b474908…; RG 384386370
- 저자 소속: NR (스니펫에 소속 없음; 저자명으로 보아 튀르키예 기관 추정 — 확인 필요). First author Örüklü.

### [2] Converter / Inverter Topology
- Topology: AC/DC/AC 컨버터(정류단 + 인버터) 실험실 프로토타입. 인버터 레벨 수 미명시(일반 AC/DC/AC = 2-Level 로 추정, 확인 필요).
- Power rating: Not reported / Full text verification required / DC-link voltage: Not reported / Full text verification required / AC output voltage: Not reported / Full text verification required
- Switching frequency: Not reported / Full text verification required / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: 실험실 프로토타입 부하 NR

### [3] Classification vs Regression
- Task: **Regression (C)**
- C 를 health indicator 로 선택(초록). 연속 추정(회귀형). 분류 아님.
- Output 단위: C (µF 또는 % — 단위 NR)

해당 없음(회귀/연속 지표) 또는 클래스 정의 NR.

### [4] 커패시터 기본 정보
| 항목 | 값 |
|---|---|
| Technology | Not reported / Full text verification required (DC-link capacitor 로만 기술) |
| Manufacturer | Not reported / Full text verification required |
| Model | Not reported / Full text verification required |
| Rated C | Not reported / Full text verification required |
| Rated V | Not reported / Full text verification required |
| Rated ESR | Not reported / Full text verification required |
| Temperature rating | Not reported / Full text verification required |

### [5] 노화 모사 방식
- NR. 스니펫 의역: 시뮬레이션 + 실험실 프로토타입에서 '제어된 커패시턴스 변경' — 커패시터 교체/병렬 조합 여부 미확인.

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| — | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required |

논문에 나온 값이 스니펫·초록에 없어 표를 채우지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): Not reported / Full text verification required

### [7] C / ESR 변화 여부
- **C only (초록이 C 만 지표로 선언; ESR 변경 여부 NR)**

### [8] Dataset 구성
- NR (샘플 수·분할·운전점 종류 모두 미확인). 초록: 여러 조건에서 검증했다는 취지의 문구는 2026 TPEL 후속(GPR) 초록에 있음 — 본 논문 귀속 주의.

### [9] 사용 신호
- 신호: DC-link 전압 리플 (PSD 입력). 초록: '높은 샘플링 주파수를 요구하지 않음'.
- Sampling frequency: 수치 NR ('does not require a high sampling frequency')

### [10] 센서 구성
- Existing inverter sensor only?: **Yes (초록: 'No additional circuitry is required, as it solely relies on the available signals')**
- 추가 센서: None
- Derived / reconstructed: No (vdc 직접 사용)

### [11] 전처리 및 Feature Extraction
- 전처리: PSD(power spectral density) 계산 — 창·길이·정규화 NR
- Feature: vdc 리플 PSD (주파수 빈 선택·차원 NR)

### [12] 진단 기법
- ML 기반 회귀 — 알고리즘명 초록 미표시. 주의: 'Gaussian Process Regression-Based Condition Monitoring of DC-Link Capacitors in Three-Phase AC/DC/AC Converters' 는 같은 저자군의 2026 IEEE TPEL 후속 논문 제목으로 보이며(arXiv 2609.00218 인용 목록), '평균 예측 오차 <2 %, 저샘플링에서도 유효, 불확실성 제공' 문구는 그 후속 초록일 가능성이 큼 → 본 TIE 논문의 모델·수치로 단정하지 않음.
- Hyperparameter: Not reported / Full text verification required

### [13] AI 모델 입력·출력
| Item | Information |
|---|---|
| Input | DC-link 전압 리플 |
| Input shape | Not reported / Full text verification required |
| Preprocessing | PSD |
| Feature dimension | Not reported / Full text verification required |
| Model | ML 회귀 (명칭 NR; GPR 은 후속 논문) |
| Output | C (health indicator) |
| Loss | Not reported / Full text verification required |
| Optimizer | Not reported / Full text verification required |

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- C 를 health indicator 로, vdc 리플 PSD 를 진단 도구로 제안(초록)
- 추가 회로 없이 가용 신호만 사용(초록)
- 유사 연구와 달리 높은 샘플링 주파수 불필요(초록)
- 시뮬레이션 + 실험실 프로토타입 검증, 높은 정확도(초록)

My interpretation:
'vdc 리플의 PSD → ML 회귀' 는 신호 하나·센서 추가 없음이라는 구현 단순성이 핵심이다. 내 연구와의 차이는 입력 신호(상전류 재구성 전류 vs vdc)와 대상(C+ESR vs C)이며, 이 논문은 데이터 기반 벤치마크(비교군)로 가장 적합하다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **True Online** — 정상 운전 중 vdc 리플만 사용, 주입·회로 없음(초록).
- On-board implementation: Not reported / Full text verification required (실험 검증은 있으나 DSP/MCU 추론 구현 여부 미기재)

### [16] On-board Hardware Environment
| 항목 | 값 |
|---|---|
| DSP | Not reported / Full text verification required |
| MCU | Not reported / Full text verification required |
| FPGA | Not reported / Full text verification required |
| Sampling ADC | Not reported / Full text verification required |
| Memory | Not reported / Full text verification required |
| Sampling frequency | 저샘플링 강조(수치 NR) |
| Control frequency | Not reported / Full text verification required |
| Execution time | Not reported / Full text verification required |
| Inference time / model size | Not reported / Full text verification required |

### [17] Real-time 가능성
- **Real-time feasible** — 저샘플링 PSD + 경량 회귀는 제어기 탑재가 가능하나, 모델 크기·추론 시간이 미기재라 '시연' 으로 볼 수 없음(해석).

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
- NR for this paper. 후속(2026 TPEL GPR) 초록에 '여러 부하·출력 주파수' 검증 문구 — 본 논문 귀속 미확인.

### [20] 최종 성능
- 종합: 'high accuracy' (수치 NR). '<2 % 평균 예측 오차' 는 후속 논문 귀속 가능성 → 미채택.
- C error: Not reported / Full text verification required / ESR error: 해당 없음(C only) / Classification metrics: 해당 없음

### [21] Noise / Robustness
- 저샘플링 강건성 주장(초록). 노이즈·온도·미학습 운전조건 검증 NR.

### [22] 장점
- 센서·회로 추가 없음(vdc 만)
- 저샘플링 → 저가 MCU 적합(해석)
- 실험실 프로토타입 검증(초록)
- IEEE TIE 급 최신(2024–25) ML 접근

### [23] 한계
Authors' stated limitation:
- Not reported / Full text verification required

Additional limitation identified (분석자):
- C only — ESR(전해 커패시터 초기 열화 지표) 미추정
- vdc 리플은 부하·변조지수·전원 조건에 따라 변하므로 조건 정규화 없이는 일반화 위험(해석)
- 알고리즘·데이터셋·수치가 초록에 없어 재현 설계 불가(본문 필수)
- 노화 모사 방식 NR

### [24] 내 연구 목표와의 관련성
- **Very High** — 2L(추정) 3상 AC/DC/AC + 기존 센서 + True Online + ML 회귀 — 내 목표 파이프라인과 구조가 같다. 입력 신호·대상만 다름.

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | AC/DC/AC (2L 추정) | 2-Level 3-Phase |
| Capacitor | DC-link | DC-Link |
| Signal | vdc 리플 (기존 센서) | Existing inverter signal preferred |
| Aging Target | C | C / ESR |
| Diagnosis | Regression | Classification or Regression |
| Online | Yes (True Online) | Yes |
| On-board | NR | Yes |
| Extra Sensor | No | Preferably No |
| AI | Yes (ML 회귀) | Candidate |
| Real-time | 시연 NR | Required |

### [26] 재현 가능성
- **Moderate** — vdc 리플 PSD → 회귀는 MATLAB/Python 으로 바로 구성 가능. 단 저자의 PSD 설정·모델·노화 샘플을 본문에서 확인해야 동일 조건 비교가 된다.
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: vdc(리플 포함, 저·고 샘플링 2종), 부하·변조지수·f1 로그. 변화 파라미터: C 5–7 단계(−0…−30 %), 가능하면 ESR 도 교차. 데이터셋: 운전점×C 조합별 PSD 벡터 → 회귀(train/test 를 운전점 기준으로 분리해 일반화 검증).

### 선정 점수 (10 기준 × 10점)
| c1 9 | c2 10 | c3 8 | c4 10 | c5 10 | c6 8 | c7 4 | c8 7 | c9 4 | c10 7 | **Total 77** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: 기존 센서(vdc)만으로 True Online ML 회귀를 IEEE TIE 에 실은 최신 논문. 내 AI 파이프라인의 직접 비교군.
- 집중할 Figure/Table/Equation: PSD 입력 정의(주파수 범위·분해능), 사용 ML 모델과 hyperparameter, 노화 샘플 표, 실험 셋업 표, 오차 표/그림, 저샘플링 실험 절
- 동반·후속 논문: 후속(귀속 확인 필요): 'Gaussian Process Regression-Based Condition Monitoring of DC-Link Capacitors in Three-Phase AC/DC/AC Converters', IEEE TPEL 2026 (arXiv 2609.00218 인용 목록) — 평균 예측 오차 <2 %, 불확실성 제공.

---

(본 파일은 `2level_inverter_dc_link_capacitor_onboard_top10.md` 7절과 동일 내용. 본문 확보 후 `Not reported / Full text verification required` 항목을 채워 갱신한다.)
