# 03. DC Link Condition Monitoring Method for Two-Level AC/DC/AC Converters
> Tier S · Rank 3 · **Evidence: Full text (PDF 원문 전체 확인, 2026-10-20)** — 이 파일은 2026-10-20 PDF 원문 36항목 분석으로 갱신됨(이전 Abstract-level 내용 대체). 수치는 원문 표·본문에 적힌 값만 기재했고, 없는 항목은 `Not reported (원문에 없음)`.

### 1. 정확한 제목, 저자, 연도, 저널, DOI, 저자 소속
- Title: DC Link Condition Monitoring Method for Two-Level AC/DC/AC Converters
- Authors: Piotr Lipnicki, Daniel Lewandowski (연락: piotr.lipnicki@pl.abb.com)
- Year / Journal: Power Electronics and Drives, vol. 2(37), no. 1, pp. 43–56, 2017 (manuscript received 3 Oct 2016, accepted 2 Feb 2017)
- DOI: 10.5277/PED170107
- 소속: ABB Sp. z o.o., Corporate Research Center, Starowiślna 13a, 31-038 Kraków, Poland. 관련 특허 WO2015165574 (A1) [10].

### 2. 정확한 inverter topology
- **2-Level AC/DC/AC** 컨버터(제목). 시뮬레이션: 15 kV 계통 → 결합 변압기 → **능동 정류 유닛(IGBT) + DC-link + 인버터 유닛** → 부하(견인 컨버터 예시, Fig. 3/5; DC choke 2개 포함). 다이오드 정류기 변형도 2.3절에서 다룸(계통 각도로 다이오드 도통 상태 결정, Table 1).
- 실험: 드라이브 + 유도전동기(IM) 부하 시험 리그(Fig. 7, 8). 정류단 종류(실험) 명시 없음.

### 3. Power rating, DC-link voltage, switching frequency, load/motor, modulation
- Power rating: NR (시뮬: 15 kV 계통 연결 full-scale 견인 컨버터; 실험 리그 정격 NR)
- DC-link 전압: NR / 스위칭 주파수: NR / 변조: NR (제어는 동기 좌표계 PI; FOC/scalar/DTC 어느 것이든 스위칭 신호만 있으면 됨)
- 부하: 시뮬 — 정격 전류의 30 % 부하; 실험 — 유도전동기(정격 NR).

### 4. Capacitor 종류, 정격 C, 정격 전압, ESR
- 종류: 전해 커패시터(본문 'electrolytic' 문맥) — 정격 C, 정격 전압, 정격 ESR 모두 NR.
- 실험 기준 ESR(ESR₁, 저항 미추가) 추정값 **0.15 Ω**. 수명 기준: 용량 75 % 이하이면 수명 종료([8] 인용).

### 5. 진단 task: classification / regression
- **Regression (ESR 연속 추정)** + 임계 판정: C < k_p·C_init 이면 알람·정지 명령(식 (9), k_p 는 사용자 임계).

### 6. Classification 이면 class 수와 정의
- 학습 분류 아님. 알람은 2 상태(정상 / 임계 초과).

### 7. Regression 이면 추정 대상(C / ESR / SOH)
- ESR(t) [Ω] (식 (7)) 와 이를 이용한 C(백분율, 식 (8)). 핵심 health indicator 는 **ESR 증가 추세**.

### 8. 노화 구현: 실제 aging / parameter emulation / simulation
- **Parameter emulation**: 시뮬레이션에서는 ESR 을 시간 의존 식 (11) 로 모델링하고 '정해진 저항값을 커패시터에 직렬 추가' 하는 스텝 변화로 구현; 실험에서도 **DC-link 커패시턴스에 추가 저항을 직렬 연결**(4.2절). 실제 가속 노화 없음.

### 9. Aging sample 별 실제 capacitance
- C 값 NR (C 는 바꾸지 않음; ESR 만 변화).

### 10. Aging sample 별 실제 ESR
- Table 2(원문 표 제목 오기 'Table 1'): ESR₁ 추정 0.15 Ω(기준, 추가 0) / ESR₂ ca. 0.18 (기대 0.17) / ESR₃ ca. 0.185 (0.18) / ESR₄ ca. 0.23 (0.26) / ESR₅ ca. 0.52 (0.57).

### 11. External resistor Radd 값
- **Radd = 0, 0.02, 0.03, 0.11, 0.42 Ω** (Table 2 'Added resistance').

### 12. C only / ESR only / C+ESR simultaneous
- **ESR only** (C 고정).

### 13. 총 dataset sample 수
- 모델 기반, 데이터셋 없음. 실험 측정점 5개(ESR₁–ESR₅).

### 14. Class 별 sample 수
Not reported (원문에 없음) (분류 아님)

### 15. Train / validation / test split
Not reported (원문에 없음) (학습 없음)

### 16. Operating condition 종류
- 시뮬: 정격 전류 30 % 단일 부하, ESR 스텝(Fig. 6, ESR 스텝 상승 8단계, 약 0.005→0.18 Ω — 범례 값은 원문 그림에서 정확히 판독되지 않아 수치 인용 보류).
- 실험: 단일 운전점(부하·속도 변화 없음).

### 17. 실제 측정 신호
- DC-link 전압 U_DC(직접 측정, 전체 DC-link 양단), 3상 입력 전류 I_a, I_b, I_c(정류 유닛 측; '드라이브 앞 보호 릴레이에 이미 있는 측정' 으로 가정), 스위칭 신호 S_aREC…S_cINV(제어기 내부). Full-scale 구성에서는 인버터 측 상전류도 사용(식 (2), (10)).

### 18. 기존 inverter sensor 인지 추가 sensor 인지
- **기존 센서만** (초록·4.3절: '추가 센서 불필요, 이미 설치된 센서와 내부 신호 사용'). 실험 리그 측정보드는 LEM 전류 센서 사용.

### 19. 직접 측정 신호 vs reconstructed signal
- 직접 측정: U_DC, I_a, I_b, I_c.
- Reconstructed: I_REC = S_aREC I_aREC + S_bREC I_bREC + S_cREC I_cREC (1); I_INV = Σ S_xINV I_xINV (2); I_DC(t) = S_aREC(t) I_a(t) + … (6, 트리거 시점); full-scale: I_cap = I_REC − I_INV (10). Fig. 1: 측정 vs 재구성 정류 유닛 DC 전류 일치(재구성 신호는 1 주기 지연).

### 20. Sampling frequency
Not reported (원문에 없음)

### 21. Window length / sample length
- 인버터 영벡터 구간(S_aINV = S_bINV = S_cINV → S_TRIG = 1)의 T_on(k)~T_off(k) 창에서 적분(식 (5), (7)). 창 길이 = 영벡터 지속시간(수치 NR).

### 22. 전처리 (normalization / filtering / segmentation / phase alignment)
- 인버터 스위칭과 동기화(트리거)하여 영벡터 구간만 사용 → 필터 없이 dU_DC/dt, dI_DC/dt 로 ESR 계산. 정규화·세그먼트·위상 정렬 별도 언급 없음. 응답시간 25 ms(시뮬).

### 23. Feature extraction (FFT / PSD / harmonic / STFT / Wavelet)
- 주파수 변환 없음. 시간영역 미분·적분: ESR(t) = ∫_{T_on}^{T_off} ((dU_DC/dt − I_DC/C_init) / (dI_DC/dt)) dt (7); C = (I_DC·ESR − U_DC)² / U_DC² × 100 % (8).

### 24. 모델 또는 parameter estimation algorithm
- 해석적 시간영역 추정(식 (1)–(10)). 임피던스 근사 Z ≈ ESR (12), u_C,ac = ESR·i_C (13). 추정기(RLS/Kalman) 없음. 다이오드 정류기용 스위칭 상태 테이블(Table 1: θ∈(−60°,60°) S_a=1; (60°,180°) S_b=1; (−180°,−60°) S_c=1).

### 25. AI: network architecture, input size, output, loss, optimizer
- 해당 없음(AI 아님).

### 26. 저자가 직접 주장하는 contribution / novelty
Authors' claimed contributions:
1. 추가 센서 없이 **DC-link 전압 측정 + DC-link 전류 재구성** 만으로 온라인 ESR 추정(초록, 2.1절 '기존 방법 [3,4] 보다 적은 측정').
2. 계산량이 작아 큰 연산 능력 불필요; 인버터 스위칭과 동기화해 SW·HW 를 더 단순화(2절, 특허 [10]).
3. 제어 전략(FOC/scalar/DTC)에 독립.
4. 회생 운전·AC 주입(Le et al. [12]) 없이 운전 중 ESR 결정(4.3절).
5. 시뮬(±1 %, 25 ms) + 실험(최대 상대 오차 11 %)으로 검증.

### 27. True Online / Quasi-Online / Offline
- **True Online**: 컨버터 운전 중(영벡터 구간은 PWM 에 자연 발생) 추정. 주입·시퀀스·정지 없음.

### 28. 실제 on-board 구현 여부
- **Yes**: ABB AC800PEC 제어기(PowerPC + Virtex-II FPGA)에 Simulink 설계 제어를 배포(Fig. 8 'Design Control Deployed to PEC'); 측정은 MI 보드(LEM). 데이터 수집은 MATLAB/Java SOAP. 알고리즘이 PEC 에서 실행됐는지 PC 후처리인지는 본문이 명시하지 않음 — 'implemented in an easy manner' 로만 기술.

### 29. DSP / MCU / FPGA 모델
- ABB AC800PEC (PowerPC 프로세서 + Xilinx Virtex-II FPGA), 측정보드 LEM 센서, 게이트 드라이버(광섬유 PWM).

### 30. Control frequency / inference time / execution time / memory
- 제어 주파수 NR / 실행 시간 NR / 메모리 NR. 시뮬 응답시간 25 ms.

### 31. Classification accuracy 또는 regression error
- 시뮬: ESR 스텝 추적 오차 약 ±1 %, 응답 25 ms. 실험: 기대값 대비 **최대 상대 오차 11 %**(Table 2: 0.18 vs 0.17, 0.185 vs 0.18, 0.23 vs 0.26, 0.52 vs 0.57).

### 32. Load / speed / temperature / modulation 변화 robustness
- 부하·속도·온도·변조 변화 실험 없음(단일 조건). 저자는 과전압·과전류·동적 충방전 등 '원치 않는 현상' 이 ESR 결정에 영향을 준다고 기술.

### 33. 저자가 인정한 limitation
- 노화 과정이 비선형이어서 ESR·잔여수명 정확 결정이 어려움(2절, 4.2절).
- 정확도 평가에 쓴 점이 적음(4.2절).
- 향후: DC-link 전압·전류의 외란으로부터 알고리즘 분리(decoupling) 또는 외란을 추가 지표로 활용(결론).

### 34. 내가 보는 추가 limitation
- 정격(전압·전력·fsw·C)·샘플링·실행시간이 전혀 없어 재현 조건 불명.
- C_init 을 알고 있어야 ESR 계산 가능(식 (7)) → C 가 함께 변하면 ESR 오차로 전파(C 변화 실험 없음).
- 영벡터 구간 적분은 변조지수가 높을수록 창이 짧아짐(추론) → 고변조·고속 운전에서 정확도 저하 가능.
- 실험 오차 11 % 는 EoL 기준(ESR ×2) 대비 작지만, 초기 열화(+20–30 %) 검출에는 부족할 수 있음.
- 저널 영향력 낮음, 그림 수치 판독성 낮음.

### 35. MATLAB/Simulink 재현에 필요한 신호와 parameter
- 모델: 3상 전원 + (능동 또는 다이오드) 정류기 + DC choke + C(ESR) + 2L 인버터 + IM/RL 부하. 로그: U_DC, I_a,I_b,I_c(정류 측), 필요 시 인버터 측 상전류, S_xREC, S_xINV, 검증용 I_DC·I_cap.
- 구현: 영벡터 검출(S_aINV=S_bINV=S_cINV) → 트리거 창 → 식 (6) 재구성 → 식 (7) ESR, 식 (8) C. 스윕: R_add 0/0.02/0.03/0.11/0.42 Ω(원문) + 추가로 C 변화·부하 30/60/100 %.
- 다이오드 정류기면 Table 1 각도 기반 S_x 생성(계통 각도 필요).

### 36. 실험 장치 구현에 필요한 sensor 와 hardware
- 센서: DC-link 전압 센서 1개, 정류 측 3상 전류 센서(LEM; 보호 릴레이 공용 가능), (full-scale) 인버터 측 3상 전류 센서.
- 제어기: 스위칭 신호와 측정을 동기 샘플링할 수 있는 DSP/FPGA(ABB 는 AC800PEC). 직렬 저항 삽입용 저항 세트(0.02–0.42 Ω, 전류 정격 고려).

### Aging Sample 표 (원문 값만)
| Aging Sample | C | C Change | ESR | ESR Change | Operating Condition | Label |
|---|---:|---:|---:|---:|---|---|
| ESR₁ | Not reported (원문에 없음) (C 고정) | 0 % | 0.15 Ω (추정 기준값; Radd 0) | 기준 | 실험 리그, 단일 운전점 | ESR 추정 (기준) |
| ESR₂ | 〃 | 0 % | 기대 0.17 Ω / 추정 ca. 0.18 Ω (Radd 0.02) | +13 % (기대) | 〃 | 오차 ≈ +6 % |
| ESR₃ | 〃 | 0 % | 기대 0.18 Ω / 추정 ca. 0.185 Ω (Radd 0.03) | +20 % | 〃 | 오차 ≈ +3 % |
| ESR₄ | 〃 | 0 % | 기대 0.26 Ω / 추정 ca. 0.23 Ω (Radd 0.11) | +73 % | 〃 | 오차 ≈ −11 % |
| ESR₅ | 〃 | 0 % | 기대 0.57 Ω / 추정 ca. 0.52 Ω (Radd 0.42) | +280 % | 〃 | 오차 ≈ −9 % |
원문 Table 2 값. 'ESR Change' 와 오차 % 는 기대값(0.15 + Radd) 기준 분석자 계산. C 는 변경하지 않았고 정격도 미기재.

### 원문 수식 요약 (재현용)
- (1) I_REC = S_aREC I_aREC + S_bREC I_bREC + S_cREC I_cREC ; (2) I_INV = Σ S_xINV I_xINV ; (4) 트리거: S_aINV = S_bINV = S_cINV → S_TRIG = 1
- (6) I_DC(t) = S_aREC(t) I_a(t) + S_bREC(t) I_b(t) + S_cREC(t) I_c(t)
- (7) ESR(t) = ∫_{T_on}^{T_off} [ (dU_DC/dt − I_DC(t)/C_init) / (dI_DC(t)/dt) ] dt
- (8) C = (I_DC ESR − U_DC)² / U_DC² × 100 % ; (9) C < k_p C_init → 알람 ; (10) I_cap = I_REC − I_INV
- (11) 1/ESR(t) = 1/ESR(0) · (1 − k t e^{−4700/(T−273)}) (시뮬용 ESR 성장 모델)

---
(이 파일은 `2level_top5_fulltext_comparison.md` 와 같은 원문 분석에서 생성됨. 이전 Abstract-level 워크시트의 선정 점수·Tier 는 `2level_inverter_dc_link_capacitor_onboard_top10.md` 5절 참조.)
