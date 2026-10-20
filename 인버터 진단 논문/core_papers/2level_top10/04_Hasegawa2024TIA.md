# 04. Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor Based on Analysis of a Six-Pulse Diode Rectifier Having AC and DC Inductors
> Tier A · Rank 4 · **Evidence: Full text (PDF 원문 전체 확인, 2026-10-20)** — 이 파일은 2026-10-20 PDF 원문 36항목 분석으로 갱신됨(이전 Abstract-level 내용 대체). 수치는 원문 표·본문에 적힌 값만 기재했고, 없는 항목은 `Not reported (원문에 없음)`.

### 1. 정확한 제목, 저자, 연도, 저널, DOI, 저자 소속
- Title: Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor Based on Analysis of a Six-Pulse Diode Rectifier Having AC and DC Inductors
- Authors: Kazunori Hasegawa (Member, IEEE; corresponding), Yuto Hirose (현 Chugoku Electric Power Co.)
- Year / Journal: IEEE Transactions on Industry Applications, vol. 60, no. 6, pp. 9043–9051, Nov./Dec. 2024 (received 8 Feb 2024, accepted 15 Jul 2024, published 15 Aug 2024; paper 2024-IPCC-0225.R1, ECCE 2023 발표판 [26] 확장)
- DOI: 10.1109/TIA.2024.3443784
- 소속: Dept. of Electrical and Electronic Engineering, Kyushu Institute of Technology, Kitakyushu, Fukuoka 804-8550, Japan. 지원: NEDO JPNP20004.

### 2. 정확한 inverter topology
- **6-pulse 다이오드 정류기(AC 라인 인덕터 L_ac + DC 인덕터 L_dc) + 3상 2-Level PWM 인버터**(Fig. 1: 레그당 스위치 2개, IGBT) + 3상 RL 부하. 회생 제동 없는 범용 모터 드라이브 구조를 대상으로 함.

### 3. Power rating, DC-link voltage, switching frequency, load/motor, modulation
| 항목 | 값 (Table I) |
|---|---|
| Power rating P | 1.2 kW |
| AC 전원 전압 V_S | 200 V, f_S 60 Hz |
| DC-link 전압 V_dc | 270 V (Fig. 6 계산 조건) |
| DC 인덕터 L_dc | 0 ~ 8.2 mH (0 ~ 9.2 %) |
| AC 라인 인덕터 L_ac | 4.6 ~ 8.2 mH (5.2 ~ 9.2 %) |
| 캐리어(스위칭) 주파수 f_C | 10 kHz |
| 출력 주파수 f_O | 50 Hz |
| 부하 | 3상 RL 부하(값 NR; 모터 아님) |
| 변조 | PWM (방식 NR; 저주파 리플 조건 6f_S ≠ 2f_I, 12f_S ≠ 2f_I 식 (14)) |
| 출력 전력 | 1200 W 및 600 W (50 %) |

### 4. Capacitor 종류, 정격 C, 정격 전압, ESR
- 종류: **알루미늄 전해 커패시터**(모든 조건). 공칭 C = **1100 µF 또는 1000 µF**(Table I), 단위용량상수 H = 33 ms(1100 µF)/30 ms(1000 µF). 정격 전압·정격 ESR·제조사 NR. 초기 측정값(조건 A): 1015 µF / 45 mΩ (제안법 기준 Z_C(measurement)).

### 5. 진단 task: classification / regression
- **Regression**: C 와 ESR(R_S) 을 연속 추정.

### 6. Classification 이면 class 수와 정의
- 해당 없음(분류 아님).

### 7. Regression 이면 추정 대상(C / ESR / SOH)
- **C [µF] + ESR [mΩ] 동시** (6차·12차 고조파 임피던스 2개 연립, 식 (20)–(23)).

### 8. 노화 구현: 실제 aging / parameter emulation / simulation
- **Parameter emulation**: 조건 A C=1100 µF / B 1100 µF + 직렬 150 mΩ / C 1000 µF / D 1000 µF + 직렬 150 mΩ (4.B절). 실제 가속 노화 없음(저자 이전 연구 [16] 인용만).

### 9. Aging sample 별 실제 capacitance
- 공칭: A 1100, B 1100, C 1000, D 1000 µF. 제안법 추정(Table II, L_ac 4.6 mH/L_dc 8.2 mH 케이스 3): A 1015, B 992, C 917, D 919 µF. 케이스별 전체 값은 아래 표.

### 10. Aging sample 별 실제 ESR
- 공칭 ESR NR(초기 추정 45 mΩ). 추정(케이스 3): A 45, B 155, C 37, D 179 mΩ. 모든 케이스 값은 아래 표.

### 11. External resistor Radd 값
- **Radd = 150 mΩ** (조건 B, D).

### 12. C only / ESR only / C+ESR simultaneous
- **C + ESR simultaneous** — 2 C 수준 × 2 ESR 수준의 4 조합(조건 D 가 동시 변화).

### 13. 총 dataset sample 수
- 모델 기반; 측정 조건 = 4 커패시터 조건 × 4 인덕터 조합(Table II) + 출력 전력 2 수준(Table III) = 20 측정점.

### 14. Class 별 sample 수
Not reported (원문에 없음) (분류 아님)

### 15. Train / validation / test split
Not reported (원문에 없음) (학습 없음)

### 16. Operating condition 종류
- 인덕터 조합 4종: 1) L_ac 4.6 mH, L_dc 0 / 2) 4.6, 4.6 / 3) 4.6, 8.2 / 4) 8.2, 4.6 mH.
- 출력 전력 P_O = 1200 W, 600 W (Table III). 연속 도통 조건 I_d ≥ I_C(6ω) 필요(Fig. 8: 약 150 W 이상에서 연속).
- 온도·속도·변조지수 변화 없음.

### 17. 실제 측정 신호
- **커패시터 전압 v_C 만 측정**(DC 블록 필터 → FFT → V_C6, V_C12). 커패시터 전류는 측정하지 않고 V_S, L_ac, L_dc, P_O 로 계산(식 (6)–(16)). P_O 는 인버터 출력 전류 센서(제어용)로 얻는 것으로 가정.

### 18. 기존 inverter sensor 인지 추가 sensor 인지
- **기존 센서만**: 전압 센서(v_C) + 출력 전력용 기존 출력 전류 센서. 전류 센서 추가 없음. 전원 전압 V_S 와 인덕터 값은 파라미터로 알고 있어야 함.

### 19. 직접 측정 신호 vs reconstructed signal
- 직접 측정: v_C (DC 블록 필터 후 리플 ṽ_C).
- 계산(재구성): I_C6, I_C12 = v_Rm/(Z_om + Z_m) (식 (12)(13)), Z_om = j(2 − 3u/2π) mωL_ac, Z_m = jmωL_dc, 겹침각 u = arccos(1 − 2ωL_ac I_d/(√3 V_Sm)), I_d = P_O/V_dc. 임피던스 보정 Ẑ_C = G_comp Z_C, G_comp = Z_C/Z_C(measurement) (식 (18)(19)).

### 20. Sampling frequency
Not reported (원문에 없음) (FFT 는 오실로스코프 파형을 Microsoft Excel 로 오프라인 계산)

### 21. Window length / sample length
Not reported (원문에 없음)

### 22. 전처리 (normalization / filtering / segmentation / phase alignment)
- DC 블록 필터(DC 제거) → 이동평균 필터(차단 1300 Hz) 로 스위칭 리플 제거 → FFT. 정규화·세그먼트 언급 없음. 초기 임피던스 보정 G_comp(LCR 사전 측정 또는 초기 운전값).

### 23. Feature extraction (FFT / PSD / harmonic / STFT / Wavelet)
- FFT 로 360 Hz(6f_S)·720 Hz(12f_S) 성분 V_C6, V_C12 추출 → Z_C(6ω), Z_C(12ω) = V/I.

### 24. 모델 또는 parameter estimation algorithm
- 해석적 연립: Ẑ_C(6ω)² = (1/(6ωC))² + R_S², Ẑ_C(12ω)² = (1/(12ωC))² + R_S² → R_S = sqrt(4/3 Ẑ_C²(12ω) − 1/3 Ẑ_C²(6ω)) (22), C = 1/(2√2 ω) · 1/sqrt(Ẑ_C²(6ω) − Ẑ_C²(12ω)) (23). 전해 커패시터 ESR 의 주파수 의존(6차 vs 12차)은 구분 못 하고 평균값 — 향후 과제.

### 25. AI: network architecture, input size, output, loss, optimizer
- 해당 없음.

### 26. 저자가 직접 주장하는 contribution / novelty
Authors' claimed contributions:
1. AC 라인 인덕터와 DC 인덕터를 **모두** 가진 6-pulse 다이오드 정류기의 리플 전류 해석을 CM 에 도입(선행 [18] 은 DC 인덕터만).
2. 그 고조파 성분으로 **전류 센서 없이 ESR 과 C 를 모두** 감시.
3. 200 V·1.2 kW 실험에서 L_ac, L_dc, 출력 전력을 바꿔도 ESR·C 변화 관측 확인(결론).
4. 수백 W ~ 수백 kW 의 6-pulse 정류기 인버터에 적용 가능하다고 주장(3.D절).

### 27. True Online / Quasi-Online / Offline
- **True Online**: 정상 운전 중 정류기 고유 리플 사용, 주입·정지 없음. 전제: 연속 도통(I_d ≥ I_C(6ω)), 6f_S·12f_S 가 2f_I 와 다를 것, P_O·V_S·인덕터 값 기지.

### 28. 실제 on-board 구현 여부
- **No**: FFT 를 Microsoft Excel 로 오프라인 계산(3.D절). 저자는 Arduino 급 저가 보드에서 수십 ms FFT 로 충분하다고 언급(구현 아님).

### 29. DSP / MCU / FPGA 모델
Not reported (원문에 없음) (인버터 제어기 모델 미기재)

### 30. Control frequency / inference time / execution time / memory
- NR. (Arduino FFT 수십 ms 가능성만 언급; 노화는 1000 h 단위로 진행하므로 충분하다는 논리)

### 31. Classification accuracy 또는 regression error
- 정량 오차 표 없음. Table II·III 의 추정값 vs 공칭: C 1000 µF 조건에서 904–941 µF(−6 ~ −10 %), 1100 µF 에서 992–1055 µF(조건 A 는 보정 기준이라 1015 고정); Radd 150 mΩ 추가 시 ESR 155–215 mΩ(+110 ~ +170 mΩ). 저자: 전류 센서 방식보다 정확도가 다소 낮을 수 있음, 전압 양자화 오차가 원인(오차 전파 이론 [22]).

### 32. Load / speed / temperature / modulation 변화 robustness
- L_ac(4.6→8.2 mH), L_dc(0→8.2 mH), P_O(1200→600 W) 변화에서도 ESR·C 변화 추적(Table II, III). 600 W 에서 B 조건 C 가 1055 µF 로 과대(공칭 1100)·C 조건 ESR 97 mΩ(1200 W 에서 37) 등 **운전점에 따른 편차 존재**(원문 수치). 온도·속도·변조 변화 없음.

### 33. 저자가 인정한 limitation
- 정확도가 전류 센서 기반 방법보다 낮을 수 있음; 커패시터 전압 양자화 오차 → 전압 센싱 분해능(비트 수) 향상 필요(4.C절).
- ESR 의 6차/12차 주파수 의존을 구분 못 함(2.C절, 향후 과제).
- 연속 도통 모드에서만 유효(식 (17)); 저주파 인버터 리플이 6f_S/12f_S 와 겹치면 무효(식 (14)).

### 34. 내가 보는 추가 limitation
- 다이오드 정류기 전단에만 적용(AFE·배터리·PV 입력 2L 인버터 불가) → 내 '인버터 신호' 목표와 정보원이 다름.
- 전원 전압·인덕터 값·출력 전력이 모델 입력 → 파라미터 오차·전원 불평형(후속 2025 MR 에서 다룸)에 민감.
- 초기 보정 G_comp 가 조건 A 를 기준으로 하므로 절대 정확도가 아니라 '변화 추적' 에 가까움.
- 오프라인 Excel FFT, 샘플링·창 길이 미기재 → 실시간 구현 미검증. 모터 대신 RL 부하.

### 35. MATLAB/Simulink 재현에 필요한 신호와 parameter
- 모델: 3상 200 V/60 Hz 전원 + L_ac(4.6–8.2 mH) + 6-pulse 다이오드 + L_dc(0–8.2 mH) + C(1000/1100 µF, R_S) + 2L 인버터(10 kHz, 50 Hz 출력) + RL 부하(1200/600 W). 로그: v_C, (검증) i_C, i_R, 출력 전류·전압(P_O).
- 구현: DC 블록 → 1300 Hz 이동평균 → FFT 360/720 Hz → 식 (6)–(16) 으로 I_C6, I_C12 → 식 (22)(23). 스윕: C 1100/1000, R_add 0/150 mΩ, L_ac, L_dc, P_O; 추가로 전원 불평형.

### 36. 실험 장치 구현에 필요한 sensor 와 hardware
- 센서: 커패시터 전압 센서(고분해능 ADC 권장), 기존 출력 전류 센서(P_O 계산), 전원 전압 정보(V_S 공칭값 사용 가능). 전류 센서 불필요.
- 하드웨어: DC 블록 필터 회로, L_ac/L_dc 인덕터, 직렬 저항 150 mΩ, 가변 RL 부하, FFT 가능한 MCU(Arduino 급 이상).

### Aging Sample 표 (원문 값만)
| Aging Sample | C | C Change | ESR | ESR Change | Operating Condition | Label |
|---|---:|---:|---:|---:|---|---|
| A (1100 µF, Radd 0) | 1100 µF 공칭 / 추정 1015 µF (모든 케이스, 보정 기준) | 기준 | 추정 45 mΩ | 기준 | L_ac/L_dc 4종, P_O 1200/600 W | C+ESR 추정 |
| B (1100 µF + 150 mΩ) | 추정 1019 / 995 / 992 / 993 µF (케이스 1–4); 600 W: 1055 µF | ≈0 (공칭) | 추정 186 / 163 / 155 / 170 mΩ; 600 W: 215 mΩ | +150 mΩ (Radd) | 〃 | ESR 증가 추적 |
| C (1000 µF, Radd 0) | 추정 918 / 927 / 917 / 908 µF; 600 W: 935 µF | −9.1 % (공칭) | 추정 39 / 64 / 37 / 43 mΩ; 600 W: 97 mΩ | 0 (공칭) | 〃 | C 감소 추적 |
| D (1000 µF + 150 mΩ) | 추정 932 / 940 / 919 / 904 µF; 600 W: 941 µF | −9.1 % (공칭) | 추정 199 / 210 / 179 / 171 mΩ; 600 W: 208 mΩ | +150 mΩ (Radd) | 〃 | C↓ + ESR↑ 동시 |
Table II(케이스 1: L_ac 4.6/L_dc 0, 2: 4.6/4.6, 3: 4.6/8.2, 4: 8.2/4.6 mH, P_O 1200 W)·Table III(케이스 3, P_O 600 W) 원문 값. 'C Change' 는 공칭 기준 분석자 계산.

### 원문 수식 요약 (재현용)
- (5) Z_C(ω_k) = V_C(ω_k)/I_C(ω_k) = sqrt((1/(ω_k C))² + R_S²)
- (6) Z_om = j(2 − 3u/2π) mωL_ac ; (7) Z_m = jmωL_dc ; m = 6, 12, … ; (9)–(11) v_Rm = A_Rm cos mθ + B_Rm sin mθ (겹침각 u 포함 계수) ; (12)(13) i_Cm = i_Rm = v_Rm/(Z_om + Z_m)
- (15) u = arccos(1 − 2ωL_ac I_d/(√3 V_Sm)) ; (16) I_d = P_O/V_dc ; (17) 연속 도통: I_d ≥ I_C(6ω)
- (18)(19) Ẑ_C = G_comp Z_C, G_comp = Z_C/Z_C(measurement)
- (22) R_S = sqrt(4/3 Ẑ_C²(12ω) − 1/3 Ẑ_C²(6ω)) ; (23) C = 1/(2√2) · 1/ω · 1/sqrt(Ẑ_C²(6ω) − Ẑ_C²(12ω))

---
(이 파일은 `2level_top5_fulltext_comparison.md` 와 같은 원문 분석에서 생성됨. 이전 Abstract-level 워크시트의 선정 점수·Tier 는 `2level_inverter_dc_link_capacitor_onboard_top10.md` 5절 참조.)
