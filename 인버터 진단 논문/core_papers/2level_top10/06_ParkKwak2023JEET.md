# 06. DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs
> Tier A · Rank 6 · **Evidence: Full text (PDF 원문 전체 확인, 2026-10-20)** — 이 파일은 2026-10-20 PDF 원문 36항목 분석으로 갱신됨(이전 Abstract-level 내용 대체). 수치는 원문 표·본문에 적힌 값만 기재했고, 없는 항목은 `Not reported (원문에 없음)`.

### 1. 정확한 제목, 저자, 연도, 저널, DOI, 저자 소속
- Title: DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs
- Authors: Hye-Jin Park, Sangshin Kwak (corresponding, sskwak@cau.ac.kr)
- Year / Journal: Journal of Electrical Engineering & Technology (KIEE/Springer), vol. 18, pp. 1841–1850, 2023 (received 7 Jun 2022, accepted 18 Aug 2022, published online 16 Feb 2023)
- DOI: 10.1007/s42835-023-01424-z
- 소속: School of Electrical and Electronics Engineering, Chung-Ang University, Seoul, Korea. 지원: NRF 2021M1A2A2060313, KIAT P0012453.

### 2. 정확한 inverter topology
- **DC 전원 + 입력(DC-link) 커패시터 C + 3상 2-Level 인버터(IGBT 6개, Fig. 2(a)) + 3상 RL 부하**. 정류단 없음(DC 소스 직결).

### 3. Power rating, DC-link voltage, switching frequency, load/motor, modulation
| 항목 | 값 (3절) |
|---|---|
| 입력(DC-link) 전압 | 100 V |
| 부하 | 3상 RL: R 10 Ω, L 10 mH (모터 아님) |
| 변조지수 | 0.3, 0.5, 0.8 (3 조건) |
| 스위칭 주파수 | 본문 수치 없음; '스위칭 주파수의 2배' 성분 = 10 kHz (Fig. 3) → **f_sw = 5 kHz** (분석자 역산) |
| 기본파 | '기본파 2배' 성분 = 360 Hz → **f₁ = 180 Hz** (분석자 역산) |
| 변조 방식 | NR (PWM) |
| Power rating | NR (100 V, 10 Ω 급 → 수백 W, 분석자 추정) |

### 4. Capacitor 종류, 정격 C, 정격 전압, ESR
- 종류: 전해 커패시터 2종 — SAMXON **EKM226M2GI20RRSHP (22 µF)**, CHANG **RL2G101MM300Z35CE002 (100 µF)**; 정격 전압·정격 ESR NR(형명에서 추정 가능하나 원문 미기재).
- 병렬 조합으로 **25 쌍의 C/ESR**: 데이터시트 기준 122 µF → 650 µF (22 µF 간격), 각 값 LCR 미터로 측정. 측정 예: 106.92 µF / 490.83 mΩ (Test C 타깃, Fig. 7·8).

### 5. 진단 task: classification / regression
- **Regression**: C 와 ESR 연속 추정(지도학습, 정답 = LCR 측정값).

### 6. Classification 이면 class 수와 정의
- 해당 없음.

### 7. Regression 이면 추정 대상(C / ESR / SOH)
- **C [µF] + ESR [mΩ]** (각각 별도 학습·평가).

### 8. 노화 구현: 실제 aging / parameter emulation / simulation
- **Parameter emulation**: 커패시터 병렬 개수 조합으로 25 C/ESR 쌍 생성(병렬 수↓ → C↓·ESR↑, 노화 방향과 동일). 실제 노화 없음.

### 9. Aging sample 별 실제 capacitance
- 데이터시트 기준 **122, 144, 166, …, 650 µF (22 µF 간격, 25 값)**; 실측값은 LCR 로 측정(개별 값 표는 없음; 예시 106.92 µF).

### 10. Aging sample 별 실제 ESR
- Fig. 3 가로축 ESR [mΩ]: **103, 111, 121, 135, 155, 184, 229, 309, 490** (표시된 눈금; 25 쌍 전체 ESR 표는 없음). 예시 490.83 mΩ (Test C).

### 11. External resistor Radd 값
- 해당 없음(직렬 저항 미사용; ESR 은 병렬 조합에 의해 결정).

### 12. C only / ESR only / C+ESR simultaneous
- **C + ESR simultaneous** — 다만 병렬 조합이므로 C 와 ESR 이 **독립이 아니라 연동**(1 쌍 = 1 조합).

### 13. 총 dataset sample 수
- 25 C/ESR 쌍 × 3 변조지수 = 75 조건. 조건당 파형/샘플 수 **NR**.

### 14. Class 별 sample 수
Not reported (원문에 없음) (회귀)

### 15. Train / validation / test split
- Test A: 전 범위(122–650 µF) 학습 = 테스트(학습 데이터 재사용). Test B: 전 범위 학습, 내부 미학습 값(386 µF 근방) 테스트. Test C: 범위 상단(386–650 µF) 학습, 하단(122 µF, 범위 밖) 테스트(Fig. 6(a)). Validation 셋 NR. Epoch ≈700 (Fig. 6(b)).

### 16. Operating condition 종류
- 변조지수 0.3 / 0.5 / 0.8 만 변화. 부하·전압·온도·fsw 고정.

### 17. 실제 측정 신호
- **커패시터 전압 v_C 와 커패시터 전류 i_C** (실험 파형, Fig. 2(d)(e)); 부하 상전압·상전류는 참고 파형만.

### 18. 기존 inverter sensor 인지 추가 sensor 인지
- **추가 센서 필요**: 커패시터 전류 i_C 측정(제어용 기존 센서 아님). v_C 는 DC-link 전압 센서와 동일.

### 19. 직접 측정 신호 vs reconstructed signal
- 모두 직접 측정(재구성 없음).

### 20. Sampling frequency
Not reported (원문에 없음) (대역 8–125 kHz 사용 → ≥250 kHz 로 추정되나 원문 미기재)

### 21. Window length / sample length
Not reported (원문에 없음) (FFT 창 길이·주기 수 미기재; Fig. 2 파형 50 ms)

### 22. 전처리 (normalization / filtering / segmentation / phase alignment)
- MATLAB 에서 FFT 후 (a) 특정 성분의 최대값 추출, (b) 대역 분할(0–5 kHz, 8–125 kHz). 정규화·필터·세그먼트·위상 정렬 언급 없음.

### 23. Feature extraction (FFT / PSD / harmonic / STFT / Wavelet)
- FFT. 특정 성분: 360 Hz(2f₁) 와 10 kHz(2f_sw) 의 v_C·i_C 진폭(각 대역의 최대값). 광대역: v_C, i_C 의 0–5 kHz(→ C), 8–125 kHz(→ ESR) 스펙트럼.
- 관찰(3.1절): v_C 저주파 성분은 ESR 과 선형 관계 없음; v_C 중주파 성분은 ESR 증가에 따라 감소(변조지수 클수록 기울기 큼); i_C 저·중주파 성분 모두 ESR 증가 시 감소.

### 24. 모델 또는 parameter estimation algorithm
- DL 4종: DNN, CNN, Simple RNN, LSTM(지도 회귀). 입력 3 종: Input1 = {V_C,360Hz, i_C,360Hz, V_C,10kHz, i_C,10kHz}, Input2 = {V_C,10kHz, i_C,10kHz}, Input3 = {V_C 0–5 kHz, i_C 0–5 kHz (C 용); V_C 8–125 kHz, i_C 8–125 kHz (ESR 용)}. RNN 계열은 Input3 에서 미수행(수렴 불안정).

### 25. AI: network architecture, input size, output, loss, optimizer
| Item | Information |
|---|---|
| Input | Input1: 4 스칼라 / Input2: 2 스칼라 / Input3: 대역 스펙트럼(차원 NR) |
| Input shape | NR (스칼라 4·2; 대역 벡터 길이 NR) |
| Preprocessing | FFT, 최대값 추출 또는 대역 분할 |
| Model | DNN(1 입력층·1 출력층·은닉층 다수), CNN(커널·풀링), Simple RNN, LSTM — 층 수·뉴런 수·커널 크기 NR('시행착오로 최적화') |
| Output | C [µF] 또는 ESR [mΩ] (별도 모델) |
| Loss | NR (training loss 곡선만, 12000→≈0, 700 epoch) |
| Optimizer | NR ; epoch·batch 는 데이터 수에 맞춰 조정(값 NR) |

### 26. 저자가 직접 주장하는 contribution / novelty
Authors' claimed contributions (1절, 결론):
1. 같은 신호 성분의 **입력 형태(특정 성분 vs 광대역)에 따라 4 DL 알고리즘의 성능이 어떻게 달라지는지** 분석 — '알고리즘과 입력 데이터 유형' 조합 제시.
2. 저주파 성분은 C, 중주파 성분은 ESR 과 상관이 크다는 특성을 이용한 입력 설계.
3. 특정 성분 입력에는 DNN, 광대역 입력에는 CNN 이 적합; RNN 계열은 불안정.
4. 토폴로지에 제한되지 않는 추정 알고리즘 개발이 목적(2절).

### 27. True Online / Quasi-Online / Offline
- **Offline**: 실험 파형을 수집해 MATLAB/DL 로 후처리. 온라인 운전 중 추정·구현 언급 없음. (신호 자체는 정상 운전 리플이므로 방법론상 True Online 으로 확장 가능 — 분석자 해석.)

### 28. 실제 on-board 구현 여부
- **No**.

### 29. DSP / MCU / FPGA 모델
Not reported (원문에 없음)

### 30. Control frequency / inference time / execution time / memory
Not reported (원문에 없음) (학습 시간: CNN·RNN 은 길다고만 기술)

### 31. Classification accuracy 또는 regression error
- 평균 오차 % (Table 1 C / Table 2 ESR), Test A / B / C:

| 입력 | 모델 | C: A / B / C | ESR: A / B / C |
|---|---|---|---|
| Input1 | DNN | 0.40 / 0.19 / 1.20 | 0.049 / 0.47 / 1.06 |
| Input1 | CNN | 0.43 / 0.46 / 2.77 | 0.03 / 0.21 / 2.76 |
| Input1 | Simple RNN | 0.26 / 0.42 / 4.73 | 0.24 / 0.20 / 2.84 |
| Input1 | LSTM | 0.54 / 0.31 / 1.67 | 0.20 / 0.88 / 1.73 |
| Input2 | DNN | 3.97 / 4.50 / 7.33 | 0.12 / 0.26 / 1.79 |
| Input2 | CNN | 3.61 / 4.69 / 4.30 | 0.87 / 0.17 / 2.61 |
| Input2 | Simple RNN | 0.71 / 0.22 / 2.29 | 0.25 / 0.59 / 3.85 |
| Input2 | LSTM | 0.54 / 1.14 / 1.24 | 0.20 / 0.21 / 1.94 |
| Input3 | DNN | 1.40 / 2.44 / 5.41 | 1.10 / 1.21 / 2.39 |
| Input3 | CNN | 1.11 / 1.18 / 1.83 | 0.63 / 1.11 / 2.75 |
- 최악 조건(Test C, 범위 밖): C 최저 DNN-Input1 1.20 %, ESR 최저 DNN-Input1 1.06 %; 광대역은 CNN(C 1.83 %).

### 32. Load / speed / temperature / modulation 변화 robustness
- 변조지수 0.3/0.5/0.8 를 학습·테스트에 모두 포함(Fig. 7·8 막대). 부하·속도·온도·fsw 변화 없음. 학습 범위 밖(Test C) 외삽 시 오차 1–7 % 로 증가.

### 33. 저자가 인정한 limitation
- RNN 계열은 수렴 불안정, CNN 은 데이터량 증가로 학습 시간 김(4.3절).
- 향후: 다른 전압·전류 성분, 필터로 유도한 데이터 유형으로 정확도 개선(결론).

### 34. 내가 보는 추가 limitation
- **커패시터 전류 센서 필요** → on-board·기존 센서 조건 불만족.
- 샘플링 주파수·창 길이·샘플 수·네트워크 구조·손실·옵티마이저 전부 미기재 → 재현 불가에 가까움.
- C 와 ESR 이 병렬 조합으로 연동 → 독립 변화(예: C 고정·ESR↑)에 대한 일반화 미검증; 단일 부하·단일 전압.
- 100 V·수백 W 저전압 실험, 모터 아님, 온라인·실시간 없음.
- Test A 는 학습 데이터 재평가라 성능 과대.

### 35. MATLAB/Simulink 재현에 필요한 신호와 parameter
- 모델: DC 100 V + C(ESR) + 2L 인버터(5 kHz, f₁ 180 Hz 또는 내 조건) + RL 10 Ω/10 mH. 로그: v_C(=v_dc), i_C(검증; 내 연구는 재구성 전류로 대체), i_a,i_b,i_c, S_x. 샘플링 ≥250 kHz(8–125 kHz 대역 재현 시) 또는 내 fsw 기준 ≥10×fsw.
- 처리: FFT → 2f₁ 빈·2f_sw 빈 진폭(Input1) / 대역 벡터(Input3) → DNN(스칼라) 또는 1D-CNN(대역) 회귀 C·ESR. 스윕: C 25 수준(병렬 조합 또는 직접 설정) × ESR 독립(Radd 추가) × 변조지수 0.3/0.5/0.8 + 부하.

### 36. 실험 장치 구현에 필요한 sensor 와 hardware
- 센서: DC-link 전압 센서, (논문 재현 시) 커패시터 전류 센서(고대역, ≥125 kHz), 상전류 센서 3개(재구성 대체 시).
- 하드웨어: 고속 DAQ/오실로스코프(≥250 kHz), 커패시터 뱅크(22 µF·100 µF 단위 병렬), LCR 미터, GPU/PC(학습). 온라인 구현 시 DSP 에 FFT 빈 2개 + 소형 DNN.

### Aging Sample 표 (원문 값만)
| Aging Sample | C | C Change | ESR | ESR Change | Operating Condition | Label |
|---|---:|---:|---:|---:|---|---|
| P01 … P25 | 122 → 650 µF, 22 µF 간격 (데이터시트; 실측은 LCR, 개별값 NR) | 650 µF 기준 −81 % … 0 % | ≈490 → ≈103 mΩ (Fig. 3 눈금: 490, 309, 229, 184, 155, 135, 121, 111, 103) | 103 mΩ 기준 +376 % … 0 % | 변조지수 0.3 / 0.5 / 0.8, DC 100 V, RL 10 Ω/10 mH | 회귀 타깃 (C, ESR 각각) |
| Test C 타깃 예 | 106.92 µF (LCR 실측) | 범위 밖(학습 386–650) | 490.83 mΩ | 최대 | 〃 | 외삽 테스트 |

25 쌍의 개별 C/ESR 표는 원문에 없음(간격·범위·눈금만). % 변화는 범위 양끝 기준 분석자 계산. C↓ 와 ESR↑ 가 병렬 개수로 연동됨.

### 원문 입력 정의 (Fig. 5)
- Input 1: V_C,360Hz, i_C,360Hz, V_C,10kHz, i_C,10kHz (저주파 + 중주파 특정 성분)
- Input 2: V_C,10kHz, i_C,10kHz (중주파만)
- Input 3: V_C 0–5 kHz, i_C 0–5 kHz (C 추정) / V_C 8–125 kHz, i_C 8–125 kHz (ESR 추정) — 광대역
- Test A: 학습 = 테스트 / Test B: 학습 범위 내부 미학습 값 / Test C: 학습 범위 밖(하단) 값

---
(이 파일은 `2level_top5_fulltext_comparison.md` 와 같은 원문 분석에서 생성됨. 이전 Abstract-level 워크시트의 선정 점수·Tier 는 `2level_inverter_dc_link_capacitor_onboard_top10.md` 5절 참조.)
