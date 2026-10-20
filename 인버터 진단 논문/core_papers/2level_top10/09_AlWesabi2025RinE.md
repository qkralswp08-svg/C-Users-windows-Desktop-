# 09. Capacitance estimation algorithm based on DC-link voltage ripples using hybrid machine learning techniques in power electronics converters

> Tier B · Rank 9 · Score 70/100 · **Evidence: Abstract-level only** (본문 미열람; 아래 `Not reported / Full text verification required` 항목은 추측으로 채우지 않았다)

### [1] 기본 논문 정보
- Title: Capacitance estimation algorithm based on DC-link voltage ripples using hybrid machine learning techniques in power electronics converters
- Authors: Ibrahim AL-Wesabi, Abdullrahman A. Al-Shamma'a, Hassan M. Hussein Farh, (Al Dawood), (Mwakipunda), (Xu) — ScienceDirect 저자 목록(일부 이름 NR)
- Year: 2025
- Journal: Results in Engineering (Elsevier, OA), vol. 27, art. 106216
- DOI: (확인 필요) PII S2590123025022881
- Publication Type: Journal (OA)
- 식별/출처: sciencedirect.com/science/article/pii/S2590123025022881
- 저자 소속: Not reported / Full text verification required

### [2] Converter / Inverter Topology
- Topology: 전력전자 컨버터 일반(풍력 터빈 컨버터 맥락 언급). 2L 여부 NR.
- Power rating: Not reported / Full text verification required / DC-link voltage: Not reported / Full text verification required / AC output voltage: Not reported / Full text verification required
- Switching frequency: Not reported / Full text verification required / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: Not reported / Full text verification required

### [3] Classification vs Regression
- Task: **Regression (C)**
- DC-link 커패시턴스 연속 추정. (한 탐색은 'C and ESR' 로 보고 — ESR 포함 여부 확인 필요)
- Output 단위: C (µF)

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
- **C only (초록 기준)**

### [8] Dataset 구성
- NR

### [9] 사용 신호
- 신호: DC-link 전압 리플; '컨버터의 접근 가능한 입·출력 단자 데이터' 만 사용(초록). 불확실 단서: 100 Hz·300 Hz 정류 리플 고조파 사용(이전 판 귀속 가능).
- Sampling frequency: Not reported / Full text verification required

### [10] 센서 구성
- Existing inverter sensor only?: **Yes (초록: 'no extra sensors or hardware')**
- 추가 센서: None
- Derived / reconstructed: No

### [11] 전처리 및 Feature Extraction
- 전처리: Not reported / Full text verification required
- Feature: vdc 리플 기반 특징(정의 NR)

### [12] 진단 기법
- ML 회귀 비교: RF, KNN, ANN, GB, DT, LR (+BR) → 하이브리드 ANN-GB-LR 제안.
- Hyperparameter: Not reported / Full text verification required

### [13] AI 모델 입력·출력
| Item | Information |
|---|---|
| Input | vdc 리플(및 단자 데이터) |
| Input shape | Not reported / Full text verification required |
| Preprocessing | Not reported / Full text verification required |
| Feature dimension | Not reported / Full text verification required |
| Model | ANN-GB-LR 하이브리드 |
| Output | C |
| Loss | Not reported / Full text verification required |
| Optimizer | Not reported / Full text verification required |

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- 접근 가능한 단자 데이터만으로 C 예측(초록)
- 하이브리드 ANN-GB-LR 이 평균 오차 0.142 %, R²≈1 (초록)
- RMSE 0.0070 µF, MAE 0.0049 µF (highlights — 단위 타당성 의문)

My interpretation:
수치는 가장 작지만 토폴로지·실험 여부·노화 방식이 불명해 '시뮬레이션 내 보간 성능' 일 가능성을 배제할 수 없다. 회귀 모델 비교 프로토콜(6종 + 하이브리드)은 참고 가치가 있다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **True Online (주장)** — 정상 운전 리플만 사용한다는 초록 취지. 실험·구현 NR.
- On-board implementation: Not reported / Full text verification required

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
- **Real-time not demonstrated** — 구현·추론 시간 언급 없음.

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
- 종합: 평균 C 오차 0.142 % (하이브리드); 비교 DT 0.624 / GB 0.586 / BR 0.182 / KNN 0.322 / RF 0.304 %; 최대 오차 1.1–1.3 %(모델별)
- C error: 0.142 % 평균, RMSE 0.0070 µF, MAE 0.0049 µF (단위 확인 필요) / ESR error: NR/해당 없음 / Classification metrics: 해당 없음

### [21] Noise / Robustness
- Not reported / Full text verification required

### [22] 장점
- 센서 추가 없음
- 정량 성능이 가장 상세(모델 비교표)
- OA

### [23] 한계
Authors' stated limitation:
- Not reported / Full text verification required

Additional limitation identified (분석자):
- 토폴로지·실험 여부·노화 방식 NR → 성능 해석 불가
- C only
- RMSE/MAE 의 µF 단위가 DC-link 용량 대비 비현실적으로 작음(단위 오기 가능)
- 저널 등급 중간

### [24] 내 연구 목표와의 관련성
- **Medium** — AI 회귀 벤치마크 수치로만 유용. 2L·on-board 조건 미확인.

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | NR | 2-Level 3-Phase |
| Capacitor | DC-link | DC-Link |
| Signal | vdc 리플(단자 데이터) | Existing inverter signal preferred |
| Aging Target | C | C / ESR |
| Diagnosis | Regression (ML) | Classification or Regression |
| Online | 주장 Yes | Yes |
| On-board | NR | Yes |
| Extra Sensor | No | Preferably No |
| AI | Yes | Candidate |
| Real-time | 미시연 | Required |

### [26] 재현 가능성
- **Easy (시뮬레이션 기준)** — vdc 리플 특징 → 회귀 비교는 즉시 가능. 저자 데이터 조건은 OA 본문에서 확인.
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: vdc, 입·출력 단자 전압·전류. 변화 파라미터: C 다단계. 데이터셋: 운전점×C 리플 특징 → 회귀 6종 비교.

### 선정 점수 (10 기준 × 10점)
| c1 5 | c2 10 | c3 4 | c4 9 | c5 9 | c6 8 | c7 4 | c8 6 | c9 9 | c10 6 | **Total 70** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: 회귀 모델 6종 + 하이브리드의 정량 비교. 내 회귀 실험의 '비교 모델 세트' 로 바로 차용.
- 집중할 Figure/Table/Equation: 특징 정의 절, 데이터 생성 조건(시뮬/실험, 운전점), 모델별 오차 표(단위 확인), 하이브리드 구조 그림
- 동반·후속 논문: 관련: Abo-Khalil et al., Energies 12(12):2369, 2019 (PSO-SVR C, 3상 B2B, 실험).

---

(본 파일은 `2level_inverter_dc_link_capacitor_onboard_top10.md` 7절과 동일 내용. 본문 확보 후 `Not reported / Full text verification required` 항목을 채워 갱신한다.)
