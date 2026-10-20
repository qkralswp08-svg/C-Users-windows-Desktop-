# 03. DC Link Condition Monitoring Method for Two-Level AC/DC/AC Converters

> Tier S · Rank 3 · Score 72/100 · **Evidence: Abstract-level only** (본문 미열람; 아래 `Not reported / Full text verification required` 항목은 추측으로 채우지 않았다)

### [1] 기본 논문 정보
- Title: DC Link Condition Monitoring Method for Two-Level AC/DC/AC Converters
- Authors: P. Lipnicki, D. Lewandowski
- Year: 2017
- Journal: Power Electronics and Drives (Sciendo / Wrocław Univ. of Science and Technology), vol. 2(37), no. 1, pp. 43–56 (online 27 Oct 2017)
- DOI: 10.5277/PED170107
- Publication Type: Journal (국내·중소 저널급; IEEE/IET 아님)
- 식별/출처: ped.pwr.edu.pl 68776; sciendo.com/article/10.5277/ped170107; RG 334696403; 공개 PDF yadda.icm.edu.pl (PED_1_2017_Lipnicki.pdf) — 본 환경에서 열지 못함
- 저자 소속: ABB Corporate Research Center, Kraków (스니펫 기준)

### [2] Converter / Inverter Topology
- Topology: 2-Level AC/DC/AC 컨버터(제목에 명시). 정격 NR.
- Power rating: Not reported / Full text verification required / DC-link voltage: Not reported / Full text verification required / AC output voltage: Not reported / Full text verification required
- Switching frequency: Not reported / Full text verification required / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: Not reported / Full text verification required

### [3] Classification vs Regression
- Task: **Regression (ESR)**
- ESR 온라인 추정; ESR 증가 추세를 고장 지표로 사용(인용 논문 문구).
- Output 단위: ESR (Ω 또는 상대값 — NR)

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
- Not reported / Full text verification required (실험 여부·노화 모사 방식 모두 미확인)

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| — | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required |

논문에 나온 값이 스니펫·초록에 없어 표를 채우지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): Not reported / Full text verification required

### [7] C / ESR 변화 여부
- **ESR only (추정 대상 기준; 실험에서 C 변경 여부 NR)**

### [8] Dataset 구성
- 해당 없음(모델 기반)

### [9] 사용 신호
- 신호: DC-link 전압 측정 + DC-link 전류 재구성(초록). 이전 조사 스니펫: 상전류 + 각 레그 스위칭 함수로 DC-link 전류 재구성 — 본문 확인 필요.
- Sampling frequency: Not reported / Full text verification required

### [10] 센서 구성
- Existing inverter sensor only?: **Yes (초록: 'does not require any additional sensors')**
- 추가 센서: None
- Derived / reconstructed: Yes — DC-link(커패시터) 전류를 상전류·스위칭 함수로 재구성(초록 'DC-link current reconstruction').

### [11] 전처리 및 Feature Extraction
- 전처리: Not reported / Full text verification required (리플 성분 추출 방법 미확인)
- Feature: 재구성 전류와 vdc 리플의 관계 → ESR

### [12] 진단 기법
- Analytical: vdc + 재구성 DC-link 전류 → ESR 추정(세부 추정기 NR).
- Hyperparameter: 해당 없음

### [13] AI 모델 입력·출력
AI 모델 아님(분석적/모델 기반 방법).

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- 2-Level AC/DC/AC 컨버터용 DC-link 상태 감시 방법 제안(제목)
- 추가 센서 없이 vdc 측정 + DC-link 전류 재구성으로 온라인 ESR 추정(초록)

My interpretation:
산업계(ABB)가 2-Level 드라이브에서 '스위칭 함수 기반 전류 재구성 → ESR' 을 실제로 다룬 드문 공개 논문. 저널 등급은 낮지만 내 신호 생성 방식과 토폴로지가 정확히 일치한다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **True Online** — 초록상 주입·시퀀스 언급 없음, 추가 센서 없음. 운전 조건 제약은 본문 확인 필요.
- On-board implementation: Not reported / Full text verification required (ABB 연구소 논문이나 제어기 구현·실험 여부 스니펫 미확인)

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
- **Real-time feasible** — 상전류×스위칭 함수 합산과 리플 대역 처리로 구성되어 제어기 주기 내 계산이 가능(해석); 시연 여부 미확인.

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
- 종합: Not reported / Full text verification required
- C error: 해당 없음 / ESR error: Not reported / Full text verification required / Classification metrics: 해당 없음

### [21] Noise / Robustness
- Not reported / Full text verification required

### [22] 장점
- 토폴로지(2L AC/DC/AC)·센서 조건(추가 없음)·재구성 철학이 내 목표와 일치
- 산업 연구소 출처 → 실용 관점
- 공개 PDF 존재(로컬에서 확보 가능)

### [23] 한계
Authors' stated limitation:
- Not reported / Full text verification required

Additional limitation identified (분석자):
- 저널 영향력 낮음 → 인용 시 보조 근거
- 실험·정격·오차·노화 방식이 모두 미확인(본문 필수)
- ESR only; 필름 커패시터에는 부적합(추론)
- 재구성 오차(데드타임·샘플링 지연) 처리 여부 미확인

### [24] 내 연구 목표와의 관련성
- **Very High** — 2-Level AC/DC/AC + 기존 센서 + 재구성 + ESR + True Online — 내 목표와 조건이 가장 많이 겹친다(AI 요소만 없음).

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | 2L AC/DC/AC | 2-Level 3-Phase |
| Capacitor | DC-link | DC-Link |
| Signal | vdc + 재구성 DC-link 전류 (기존 센서) | Existing inverter signal preferred |
| Aging Target | ESR | C / ESR |
| Diagnosis | Regression(추정) | Classification or Regression |
| Online | Yes (True Online) | Yes |
| On-board | NR | Yes |
| Extra Sensor | No | Preferably No |
| AI | No | Candidate |
| Real-time | 시연 NR | Required |

### [26] 재현 가능성
- **Moderate** — 재구성 자체는 쉽지만 ESR 추출식·대역·보정이 본문에만 있다. PDF 가 공개되어 있어 로컬에서 바로 확인 가능.
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: ia, ib, ic, Sa/Sb/Sc, vdc, 검증용 idc·iC. 변화 파라미터: ESR(Radd 0 ~ +100 %), C 고정/변경 교차, 부하 3단계. 데이터셋: 조합별 정상상태 파형 → 재구성 전류 fsw 성분 vs vdc 리플.

### 선정 점수 (10 기준 × 10점)
| c1 10 | c2 10 | c3 4 | c4 10 | c5 10 | c6 8 | c7 3 | c8 8 | c9 2 | c10 7 | **Total 72** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: 제목부터 '2-Level AC/DC/AC' 이며 추가 센서 없는 재구성 기반 ESR 추정 — 내 토폴로지·신호 조건의 직접 선례.
- 집중할 Figure/Table/Equation: DC-link 전류 재구성 식(스위칭 함수 정의), ESR 추출 대역·수식, 실험/시뮬 조건 표, 오차 그림
- 동반·후속 논문: 관련 특허(개념 비교용): US 12461138 'Circuitry and methods for monitoring power conversion circuitry' — AC 측 전류+스위칭 상태로 커패시터 전류 재구성.

---

(본 파일은 `2level_inverter_dc_link_capacitor_onboard_top10.md` 7절과 동일 내용. 본문 확보 후 `Not reported / Full text verification required` 항목을 채워 갱신한다.)
