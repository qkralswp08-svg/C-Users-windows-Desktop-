# 05. Online Condition Monitoring System for DC-Link Capacitor in Industrial Power Converters

> Tier A · Rank 5 · Score 71/100 · **Evidence: Abstract-level only** (본문 미열람; 아래 `Not reported / Full text verification required` 항목은 추측으로 채우지 않았다)

### [1] 기본 논문 정보
- Title: Online Condition Monitoring System for DC-Link Capacitor in Industrial Power Converters
- Authors: P. Sundararajan et al. (전체 저자 목록 확인 필요; NTU/Rolls-Royce@NTU 그룹)
- Year: 2018
- Journal: IEEE Transactions on Industry Applications, vol. 54, no. 5, pp. 4775–4785 (Sep./Oct. 2018)
- DOI: 10.1109/TIA.2018.2845889
- Publication Type: Journal (학회판: 'Online equivalent series resistance estimation method…', Xplore 8096009)
- 식별/출처: IEEE Xplore 8378055; NTU DR-NTU 레코드; RG 325704243
- 저자 소속: Nanyang Technological University (Rolls-Royce@NTU Corporate Lab) — 리포지터리 호스팅 기준

### [2] Converter / Inverter Topology
- Topology: 전단 정류기 급전 3상 인버터(front-end rectifier-fed inverter). 맞춤 제작 인버터 + 상용 AC 드라이브(초록). 레벨 수 미명시(상용 AC 드라이브 = 2L 추정).
- Power rating: Not reported / Full text verification required / DC-link voltage: Not reported / Full text verification required / AC output voltage: Not reported / Full text verification required
- Switching frequency: NR — 방법이 유효한 '한계 스위칭 주파수' 를 규명하고 그 이하에서는 별도 해법 제안(초록) / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: Not reported / Full text verification required

### [3] Classification vs Regression
- Task: **Regression (ESR)**
- ESR 을 열화 지표로 추정. (2020 TPEL 후속: ESR + C, C 는 온도 민감 파라미터로 코어/핫스팟 온도 추정에도 사용)
- Output 단위: ESR (Ω — NR)

해당 없음(회귀/연속 지표) 또는 클래스 정의 NR.

### [4] 커패시터 기본 정보
| 항목 | 값 |
|---|---|
| Technology | Not reported / Full text verification required (전해 추정) |
| Manufacturer | Not reported / Full text verification required |
| Model | Not reported / Full text verification required |
| Rated C | Not reported / Full text verification required |
| Rated V | Not reported / Full text verification required |
| Rated ESR | Not reported / Full text verification required |
| Temperature rating | Not reported / Full text verification required |

### [5] 노화 모사 방식
- NR. 인용 문구로 고장 기준 'ESR >200 %, C <80 %' 언급(귀속 확인 필요).

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| — | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required |

논문에 나온 값이 스니펫·초록에 없어 표를 채우지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): Not reported / Full text verification required

### [7] C / ESR 변화 여부
- **ESR only (본 논문); C 변경 여부 NR**

### [8] Dataset 구성
- 해당 없음(모델 기반)

### [9] 사용 신호
- 신호: DC-link 전압과 DC-link 전류의 스위칭 주파수 성분(초록). DC-link 전류가 측정인지 재구성인지 NR.
- Sampling frequency: Not reported / Full text verification required

### [10] 센서 구성
- Existing inverter sensor only?: **Partially / NR — vdc 는 기존 센서; DC-link 전류 센서 존재 여부가 구현에 따라 다름(초록 미명시)**
- 추가 센서: NR (DC-link 전류 센서 필요 가능성)
- Derived / reconstructed: NR

### [11] 전처리 및 Feature Extraction
- 전처리: 대역통과 필터로 스위칭 주파수 성분 추출(스니펫). 2020 TPEL: Goertzel 단일 빈 DFT.
- Feature: fsw 성분 전압/전류 비 → ESR

### [12] 진단 기법
- Analytical: fsw 대역 |ΔV/ΔI| 기반 ESR 추정; 한계 fsw 이하에서 대안 해법(초록). 2020 TPEL: Goertzel 알고리즘으로 ESR·C 추출 + 온도 추정 + 자가 보정.
- Hyperparameter: 해당 없음

### [13] AI 모델 입력·출력
AI 모델 아님(분석적/모델 기반 방법).

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- 산업용 컨버터용 온라인 DC-link 커패시터 CM 시스템(제목)
- vdc·idc 의 스위칭 주파수 성분으로 ESR 추정(초록)
- 유효 한계 스위칭 주파수 규명 및 그 이하 해법(초록)
- PSpice → 맞춤 인버터 실험 → 상용 AC 드라이브 구현(초록)

My interpretation:
학술 프로토타입을 넘어 '상용 드라이브 구현' 까지 간 점이 핵심. 내 연구에서 fsw 성분 기반 ESR 추정과 Goertzel(2020) 은 경량 feature 추출기의 직접 참고가 된다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **True Online** — 정상 운전 중 스위칭 리플 성분만 사용(초록). 주입 없음.
- On-board implementation: Yes (초록: 'implemented in a commercial ac drive system') — 제어기 종류·부품 NR

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
- **Real-time demonstrated (상용 드라이브 구현 — 초록 기준)** — 초록이 상용 AC 드라이브 시스템 구현을 명시. 실행 시간 수치는 NR.

### [18] 실험 환경
| Parameter | Value |
|---|---|
| DC-Link Voltage | Not reported / Full text verification required |
| Output Voltage | Not reported / Full text verification required |
| Power | Not reported / Full text verification required |
| Load | Not reported / Full text verification required |
| Motor | 상용 AC 드라이브(전동기 종류 NR) |
| Motor speed | Not reported / Full text verification required |
| Torque | Not reported / Full text verification required |
| Switching Frequency | Not reported / Full text verification required |
| Fundamental Frequency | Not reported / Full text verification required |
| Modulation | Not reported / Full text verification required |
| Capacitor | Not reported / Full text verification required |
| Sampling Frequency | Not reported / Full text verification required |

### [19] Operating Condition 다양성
- NR (스위칭 주파수 의존성은 분석)

### [20] 최종 성능
- 종합: 'estimation error is very low' (수치 NR)
- C error: 해당 없음(본 논문) / ESR error: Not reported / Full text verification required / Classification metrics: 해당 없음

### [21] Noise / Robustness
- fsw 의존성 분석(초록). 온도는 2020 TPEL 에서 다룸(온도 추정·자가 보정).

### [22] 장점
- 상용 드라이브 구현 → On-board 실증
- True Online, 주입 없음
- fsw 성분이라는 명확한 물리 feature
- 후속(2020)에서 Goertzel 로 연산량 최소화 + 온도까지

### [23] 한계
Authors' stated limitation:
- 한계 스위칭 주파수 이하에서는 기본 방법이 유효하지 않아 별도 해법 필요(초록)

Additional limitation identified (분석자):
- DC-link 전류 센서 필요 가능성(미확인) → 센서 조건 불리할 수 있음
- ESR only(본 논문)
- 노화 샘플·오차 수치·제어기 사양이 초록에 없음
- 2020 TPEL 검증은 T-type 3L 프로토타입 — 2L 데이터로 단정 불가

### [24] 내 연구 목표와의 관련성
- **High** — fsw 성분 ESR 추정 + 상용 드라이브 구현은 내 on-board 목표의 실증 선례. 센서 조건(idc)과 ESR 단독이 차이.

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | 정류기 급전 3상 인버터(2L 추정) | 2-Level 3-Phase |
| Capacitor | DC-link | DC-Link |
| Signal | vdc + idc 의 fsw 성분 | Existing inverter signal preferred |
| Aging Target | ESR (+C, 온도: 2020) | C / ESR |
| Diagnosis | Regression | Classification or Regression |
| Online | Yes (True Online) | Yes |
| On-board | Yes (상용 드라이브) | Yes |
| Extra Sensor | idc 센서 여부 NR | Preferably No |
| AI | No | Candidate |
| Real-time | 시연(초록) | Required |

### [26] 재현 가능성
- **Moderate** — fsw 대역 추출과 ESR 비 계산은 쉽다. 한계 fsw 조건과 대안 해법, 전류 측정 방식은 본문 확인 필요.
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: vdc, idc(또는 재구성), fsw 성분. 변화 파라미터: ESR 3–5 단계, fsw 2–3 단계(한계 fsw 확인), 부하. 데이터셋: 조합별 fsw 빈 진폭(Goertzel) → ESR.

### 선정 점수 (10 기준 × 10점)
| c1 8 | c2 10 | c3 9 | c4 10 | c5 6 | c6 8 | c7 3 | c8 8 | c9 3 | c10 6 | **Total 71** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: On-board(상용 드라이브) 구현까지 보인 True Online ESR 추정의 대표. Goertzel 후속과 함께 경량 feature 추출 설계의 근거.
- 집중할 Figure/Table/Equation: fsw 성분 ESR 식, 한계 fsw 유도, 상용 드라이브 구현 절(제어기·샘플링), 오차 표; 2020 TPEL 의 Goertzel 빈 선택·온도 보정 절
- 동반·후속 논문: Sundararajan et al., 'Condition Monitoring of DC-Link Capacitors Using Goertzel Algorithm for Failure Precursor Parameter and Temperature Estimation', IEEE TPEL 35(6):6386–6396, 2020, DOI 10.1109/TPEL.2019.2951859 (Xplore 8892651; 검증은 T-type 3L 프로토타입 — 스니펫).

---

(본 파일은 `2level_inverter_dc_link_capacitor_onboard_top10.md` 7절과 동일 내용. 본문 확보 후 `Not reported / Full text verification required` 항목을 채워 갱신한다.)
