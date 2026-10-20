# 02. Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters
> Tier S · Rank 2 · **Evidence: Full text (PDF 원문 전체 확인, 2026-10-20)** — 이 파일은 2026-10-20 PDF 원문 36항목 분석으로 갱신됨(이전 Abstract-level 내용 대체). 수치는 원문 표·본문에 적힌 값만 기재했고, 없는 항목은 `Not reported (원문에 없음)`.

### 1. 정확한 제목, 저자, 연도, 저널, DOI, 저자 소속
- Title: Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters
- Authors: Kerim Örüklü (Student Member, IEEE; corresponding), Şener Ağalar (Member, IEEE)
- Year / Journal: IEEE Transactions on Industrial Electronics, vol. 72, no. 4, pp. 4227–4237, Apr. 2025 (received 31 Jan 2024, accepted 2 Sep 2024, published 26 Sep 2024, current version 11 Mar 2025)
- DOI: 10.1109/TIE.2024.3454814
- 소속: Dept. of Electrical and Electronics Engineering, Eskisehir Technical University, Eskisehir 26555, Türkiye (두 저자 동일).

### 2. 정확한 inverter topology
- **AC/DC/AC 컨버터: 3상 입력 다이오드 정류기(6-pulse) + DC-link + 단상(H-bridge, 스위치 4개) 출력 인버터** + LC 출력 필터 + 부하(Fig. 2, 2절 '3상 입력, 단상 출력'). 즉 **3상 2-Level 인버터가 아님** — 단상 출력 2-Level 인버터.

### 3. Power rating, DC-link voltage, switching frequency, load/motor, modulation
| 항목 | 값 (Table I; 실험도 동일, 커패시터만 625 µF) |
|---|---|
| 입력 선간전압 V_in | 50 VAC, f_in 50 Hz |
| 출력 전압 V_out | 30 VAC, f_out 60 Hz |
| 공칭 DC-link 전압 | 70 V |
| 공칭 DC-link C | 500 µF (시뮬) / 625 µF (실험, 공칭) |
| 스위칭 주파수 f_s | 2 kHz |
| 변조 | 개루프 사인파 PWM(SPWM), 기본파 60 Hz |
| 입력 필터 | 3상 L 0.4 mH ; 출력 필터 LC 12.5 mH – 28 µF |
| 부하 | 저항 41/44/50/55/71 Ω (실험), 61.5/75/106.5/150/217.5 Ω (시뮬); RL 은 같은 R 에 6.25 또는 12.5 mH 직렬 → 15 부하 조건 |
| Power rating | 명시 NR (30 V/41 Ω 급 → 수십 W, 분석자 추정) |

### 4. Capacitor 종류, 정격 C, 정격 전압, ESR
- 종류: 알루미늄 전해(AL-Cap). 실험 공칭 **625 µF** (측정 기준값 620.85 µF @120 Hz, 25 °C, Escort ELC-132A LCR). 정격 전압·정격 ESR·제조사 NR. EOL 기준 인용: C −20 % 또는 ESR ×2.

### 5. 진단 task: classification / regression
- **Regression**: C_link [µF] 연속 추정(식 (3) f(F₁′, F₂′) = C_link).

### 6. Classification 이면 class 수와 정의
- 해당 없음. (예지보전 단계에서 'New / Aged–Nearly Aged' 로 나누는 개념도는 있으나 분류 모델 아님.)

### 7. Regression 이면 추정 대상(C / ESR / SOH)
- **C only** (저자: 저주파 성분은 ESR 변화의 영향을 받지 않으므로 ESR 추정 불가, 3.B절).

### 8. 노화 구현: 실제 aging / parameter emulation / simulation
- **Parameter emulation**: 실험은 'adjustable capacitor bank' 로 C 를 500–620 µF 10 µF 간격 13 수준으로 설정(각 값 LCR 측정); 시뮬은 Matlab/Simulink 에서 C 값 변경. 실제 가속 노화 없음. 온도 실험(30–75 °C 오븐)은 새 커패시터의 C(T) 특성 측정용.

### 9. Aging sample 별 실제 capacitance
- 실험 13 수준(LCR @120 Hz): **512.50, 521.50, 530.61, 539.68, 548.73, 557.90, 566.96, 576.10, 584.75, 593.91, 603.12, 612.15, 620.85 µF**. 시뮬 학습: 400–500 µF 10 µF 간격 11 수준; 특징 분석: 300–500 µF 20 µF 간격 11 수준.

### 10. Aging sample 별 실제 ESR
- ESR 값 NR (측정·변경하지 않음).

### 11. External resistor Radd 값
- 해당 없음 (ESR 미변경).

### 12. C only / ESR only / C+ESR simultaneous
- **C only**.

### 13. 총 dataset sample 수
- 실험 학습: **975** (13 C × 15 부하 × 5 반복); 실험 테스트: 175 (7 C × 5 저항 부하 × 5 반복, 다른 날 수집) + testset-1 175 (L 6.25 mH) + testset-2 175 (L 12.5 mH). 시뮬 학습 165 (11 C × 15 부하), 테스트 10.

### 14. Class 별 sample 수
Not reported (원문에 없음) (회귀)

### 15. Train / validation / test split
- 학습 975 / 5-fold cross-validation(26 모델 비교) / 독립 테스트 175 (+175, +175). 명시적 validation 셋 대신 5-fold CV.

### 16. Operating condition 종류
- 부하 15 종(순저항 5 × {R, R+6.25 mH, R+12.5 mH}); 테스트는 순저항 5 종 및 RL 2 종. 샘플링 주파수 50→2 kHz 다운샘플 실험. 온도 30–75 °C(커패시터 특성만). 변조지수·출력 주파수·fsw 변화 없음(개루프 고정).

### 17. 실제 측정 신호
- **DC-link 전압 V_dc** 와 **출력 전류 I_out**(단상) — NI-USB-6221 DAQ 로 수집. 특징: F₁ = I_out,rms, F₂ = PSD₃₀₀(V_dc 리플 PSD 의 300 Hz 성분, 실험) / 시뮬에서는 PSD₃₀₀ 과 I_out,rms.

### 18. 기존 inverter sensor 인지 추가 sensor 인지
- **기존 센서만**(보호·제어용 V_dc, I_out). 커패시터 전류 센서·필터 회로·주입 없음. 온도 보정용 NTC 서미스터는 제안(미구현).

### 19. 직접 측정 신호 vs reconstructed signal
- 모두 직접 측정(재구성 없음). PSD 는 식 (1) P_x(k) = (1/N)|X(k)|² 로 계산.

### 20. Sampling frequency
- **50 kHz** (샘플링 주기 20 µs). 다운샘플 실험: 25, 12.5, 10, 5, 2.5, 2 kHz → 5 kHz(250 점)까지 성능 유지, 2.5 kHz 에서 저하(Fig. 11).

### 21. Window length / sample length
- **2500 점 = 0.05 s = 출력 60 Hz 3 주기** (I_out 3 주기와 대응하는 V_dc). 데이터 행렬 2500×975.

### 22. 전처리 (normalization / filtering / segmentation / phase alignment)
- 필터링 없음(raw 데이터; PSD 가 잡음에 강건하다는 논리). 특징 F₁, F₂ 를 [0, 1] 로 재스케일. 창은 I_out 3 주기 기준으로 고정(랜덤 창 지양). 위상 정렬 언급 없음.

### 23. Feature extraction (FFT / PSD / harmonic / STFT / Wavelet)
- PSD(DFT 기반, 식 (1)) 의 300 Hz 빈(6×50 Hz 입력 정류 리플) + I_out RMS. 후보 특징 V_dc,p2p, PSD₆₀, PSD₁₂₀ 은 PCC(식 (2)) 분석으로 제외(PSD₁₂₀ 은 출력 전류 변동에 민감, V_dc,p2p 는 잡음).

### 24. 모델 또는 parameter estimation algorithm
- Matlab Regression Learner 26 모델 비교(5-fold CV). 실험 최종 **GPR(Matern 5/2 커널, constant basis)**; 시뮬 최종 medium NN(1 층 25 뉴런 ReLU, 1000 반복). 비교: SVM(fine Gaussian), wide NN(1×100), trilayer NN(3×10), bagged trees(min leaf 30, 8 learners), LR(interactions).

### 25. AI: network architecture, input size, output, loss, optimizer
| Item | Information |
|---|---|
| Input | F₁′ = I_out,rms(정규화), F₂′ = PSD₃₀₀(정규화) — **2차원** |
| Input shape | 2 × 1 (원파형 2500 점 → 특징 2개) |
| Preprocessing | PSD(DFT) + RMS, [0,1] 스케일 |
| Model | GPR Matern 5/2 (실험) / NN 1×25 ReLU (시뮬) |
| Output | C_link [µF] |
| Loss | NR (Regression Learner 기본; 평가 지표 R², RMSE, MAE) |
| Optimizer | NR (기본 hyperparameter) |
| 모델 크기 | Matlab Coder 생성 C 코드 ≈100 kB (학습 데이터 포함) |

### 26. 저자가 직접 주장하는 contribution / novelty
Authors' claimed contributions (1절):
1. **V_dc 리플의 PSD** 를 열화 특징으로 제안 — 측정 잡음에 강건해 추가 아날로그/디지털 필터 불필요; I_out,rms 와 결합하면 다양한 부하에서 C_link 고정밀 추정; 데이터 처리 일반화를 위해 **출력 전류 3 주기** 창 고정; 높은 샘플링 주파수 불필요.
2. 특정 운전 조건에 의존하지 않고, 정지 없이, 커패시터 전류 센서 없이, 기존 신호만으로, 주입 없이(IEEE 519 준수), 제어 알고리즘 수정 없이 동작.

### 27. True Online / Quasi-Online / Offline
- **True Online**(측정 단계): 정상 운전 중 기존 신호만. 단 **추론은 오프라인**(3.I·결론: 'testing phase was conducted offline').

### 28. 실제 on-board 구현 여부
- **No**(논의만): Matlab Coder 로 C 코드 ≈100 kB 생성 가능, LAUNCHXL-F28379D(1 MB flash, 204 kB RAM)에 적합, Goertzel 로 300 Hz PSD 추출, 수 분에 1회 실행 — 향후 과제.

### 29. DSP / MCU / FPGA 모델
- 실험 수집: NI-USB-6221 DAQ + PC(Matlab). 제안 타깃(미구현): TI LAUNCHXL-F28379D (TMS320F28379D).

### 30. Control frequency / inference time / execution time / memory
- 추론 시간·실행 시간 NR; 메모리: 모델 C 코드 ≈100 kB(미검증 추정). 실행 주기 제안: 수 분에 1회.

### 31. Classification accuracy 또는 regression error
- 실험(GPR, Table IV): R² 검증/테스트 0.96/0.96, RMSE 7.18/7.07 µF, MAE 5.57/5.16 µF. testset-1(L 6.25 mH): 평균 0.8574 %, 최소 0.0142 %, 최대 5.048 %, R² 0.97; testset-2(12.5 mH): 평균 0.9048 %, 최소 0.0016 %, 최대 4.966 %, R² 0.96 → **MPE < 1 %**.
- 시뮬(NN, Table II/III): R² 0.99, RMSE 3.45 µF, MAE 2.42 µF; 10 테스트 오차 0.031–0.862 %(학습 범위 밖 380 µF: 2.316 %).
- 비교 모델(실험 테스트 RMSE µF): SVM 7.36, wide NN 7.59, trilayer NN 7.66, ensemble 8.04, LR 9.98.

### 32. Load / speed / temperature / modulation 변화 robustness
- 부하: 15 조건 학습 + 미학습 RL 테스트에서 <1 %(강건). 샘플링: 5 kHz 까지 유지. 잡음: V_dc 평균 SNR ≈11 dB(Table V)에서도 동작. 온도: C(T) = 0.4382·T + 609.8 (R² 0.9987) 선형 보정식 제안(C_actual = C_link + a(T − 25 °C)). 속도·변조지수·fsw 변화 없음(개루프 고정). 학습 범위 밖 C 는 오차 증가(시뮬 2.3 %).

### 33. 저자가 인정한 limitation
- 테스트는 오프라인 — 온라인 구현과 온도 효과 통합은 향후 과제(결론).
- PSD 지배 성분 위치가 변조 방식·출력/입력 주파수에 따라 달라져(시뮬 120 Hz vs 실험 60 Hz) 특징 라벨 전에 PSD 분석 필요(3.B절).
- 저주파 성분은 ESR 영향을 받지 않아 ESR 추정 불가(3.B절).
- V_dc 측정이 잡음(SNR ≈11 dB).

### 34. 내가 보는 추가 limitation
- **단상 출력 H-bridge**, 70 V·수십 W 급 저전압 프로토타입 — 3상 2L 드라이브(수백 V, 수 kW)로의 일반화 미검증.
- 특징 PSD₃₀₀ 은 **입력 정류 리플(6f_in)** 이므로 다이오드 전단 구조 의존; AFE/배터리 입력에서는 같은 특징이 없음.
- C 범위 500–620 µF(−19 %)는 EoL 근방만, ESR 미포함, 실제 노화 커패시터 없음.
- 개루프 SPWM 고정 → 폐루프 전류 제어·변조지수 변화 시 PSD 변동 미검증.
- 온도 보정은 커패시터 특성 측정만, CM 루프 통합 실험 없음.

### 35. MATLAB/Simulink 재현에 필요한 신호와 parameter
- 모델: 3상 50 Hz 전원 + L 0.4 mH + 다이오드 정류기 + C(500–625 µF) + (내 경우 3상 2L 인버터로 교체) + LC 필터 + R/RL 부하. 로그: v_dc, i_out(또는 3상 i_a,i_b,i_c) 50 kHz, 0.05 s 창(3 주기).
- 처리: 창 고정 → PSD(식 (1)) → 입력 정류 리플 빈(6f_in)·출력 고조파 빈 선택(PCC 로 검증) + I_rms → [0,1] 정규화 → GPR/NN 회귀. 스윕: C 13 수준(−19 %…0), 부하 15 조건, 5 반복, 테스트는 다른 날/미학습 부하.

### 36. 실험 장치 구현에 필요한 sensor 와 hardware
- 센서: DC-link 전압 센서(절연, 잡음 대책), 출력 전류 센서(기존). DAQ 또는 MCU ADC ≥5 kHz(2 채널), NTC 서미스터(온도 보정 시).
- 하드웨어: 조정 가능한 커패시터 뱅크(10 µF 간격 13 수준), 저항·인덕터 부하 세트, LCR 미터(120 Hz 기준값), (온라인 구현 시) TMS320F28379D 급 DSP + Matlab Coder.

### Aging Sample 표 (원문 값만)
| Aging Sample | C | C Change | ESR | ESR Change | Operating Condition | Label |
|---|---:|---:|---:|---:|---|---|
| C01 | 512.50 µF | −17.5 % (vs 620.85) | Not reported (원문에 없음) | Not reported (원문에 없음) | 15 부하(R 41/44/50/55/71 Ω × {0, 6.25, 12.5 mH}) × 5 반복 | C 회귀 타깃 |
| C02 | 521.50 µF | −16.0 % | Not reported (원문에 없음) | Not reported (원문에 없음) | 〃 | 〃 |
| C03 | 530.61 µF | −14.5 % | Not reported (원문에 없음) | Not reported (원문에 없음) | 〃 | 〃 |
| C04 | 539.68 µF | −13.1 % | Not reported (원문에 없음) | Not reported (원문에 없음) | 〃 | 〃 |
| C05 | 548.73 µF | −11.6 % | Not reported (원문에 없음) | Not reported (원문에 없음) | 〃 | 〃 |
| C06 | 557.90 µF | −10.1 % | Not reported (원문에 없음) | Not reported (원문에 없음) | 〃 | 〃 |
| C07 | 566.96 µF | −8.7 % | Not reported (원문에 없음) | Not reported (원문에 없음) | 〃 | 〃 |
| C08 | 576.10 µF | −7.2 % | Not reported (원문에 없음) | Not reported (원문에 없음) | 〃 | 〃 |
| C09 | 584.75 µF | −5.8 % | Not reported (원문에 없음) | Not reported (원문에 없음) | 〃 | 〃 |
| C10 | 593.91 µF | −4.3 % | Not reported (원문에 없음) | Not reported (원문에 없음) | 〃 | 〃 |
| C11 | 603.12 µF | −2.9 % | Not reported (원문에 없음) | Not reported (원문에 없음) | 〃 | 〃 |
| C12 | 612.15 µF | −1.4 % | Not reported (원문에 없음) | Not reported (원문에 없음) | 〃 | 〃 |
| C13 (new) | 620.85 µF | 0 % (기준) | Not reported (원문에 없음) | Not reported (원문에 없음) | 〃 | 〃 |
| 시뮬 학습 | 400–500 µF, 10 µF 간격 11 수준 | −20 ~ 0 % (vs 500) | Not reported (원문에 없음) | Not reported (원문에 없음) | 15 부하(R 61.5–217.5 Ω × {0, 6.25, 12.5 mH}) | C 회귀 타깃 |

C 값은 3.A절 원문(LCR 120 Hz). 'C Change' 는 620.85 µF 기준 분석자 계산. 테스트 175 는 7 C 수준 × 5 저항 부하 × 5 반복(어느 7 수준인지는 Fig. 10 축: 512.5–620.85 µF 중 7개).

### 원문 결과표 요약
| 모델 (실험, Table IV) | R² val/test | RMSE val/test [µF] | MAE val/test [µF] |
|---|---|---|---|
| I GPR Matern 5/2 | 0.96 / 0.96 | 7.18 / 7.07 | 5.57 / 5.16 |
| II SVM fine Gaussian | 0.95 / 0.96 | 7.28 / 7.36 | 5.69 / 5.58 |
| III NN wide (1×100 ReLU) | 0.95 / 0.96 | 7.63 / 7.59 | 5.85 / 5.62 |
| IV NN trilayer (3×10 ReLU) | 0.95 / 0.96 | 7.94 / 7.66 | 6.23 / 5.90 |
| V Ensemble bagged trees | 0.94 / 0.95 | 8.14 / 8.04 | 6.53 / 6.15 |
| VI LR interactions | 0.91 / 0.92 | 9.99 / 9.98 | 7.90 / 7.89 |

| SNR (Table V) | 파형 수 | V_dc min/max/mean dB | I_out min/max/mean dB |
|---|---|---|---|
| Training | 975 | 1.22 / 23.53 / 11.45 | 23.81 / 42.61 / 34.49 |
| Testset-1 | 175 | 1.54 / 22.20 / 10.99 | 27.06 / 40.63 / 35.17 |
| Testset-2 | 175 | 1.58 / 23.00 / 11.76 | 23.68 / 41.87 / 35.90 |

---
(이 파일은 `2level_top5_fulltext_comparison.md` 와 같은 원문 분석에서 생성됨. 이전 Abstract-level 워크시트의 선정 점수·Tier 는 `2level_inverter_dc_link_capacitor_onboard_top10.md` 5절 참조.)
