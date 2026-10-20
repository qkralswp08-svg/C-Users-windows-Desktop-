# 2-Level Inverter DC-Link Capacitor On-board/Online Diagnosis — 핵심 5편 원문(Full-text) 정밀 분석

- 작성일: 2026-10-20
- 근거: 사용자가 제공한 PDF 원문 5편을 처음부터 끝까지 확인. **Evidence = Full text (PDF 원문 전체 확인, 2026-10-20)**. 이전 Abstract-level 추정은 모두 원문 값으로 대체했고, 원문에 없는 항목은 `Not reported (원문에 없음)` 로 두었다(추측 금지).
- 대상: ① Ghadrdan 2022 TPEL ② Lipnicki & Lewandowski 2017 PED ③ Hasegawa & Hirose 2024 TIA ④ Örüklü & Ağalar 2025 TIE ⑤ Park & Kwak 2023 JEET
- 갱신 파일: `core_papers/2level_top10/01_Ghadrdan2022TPEL.md`, `03_Lipnicki2017PED.md`, `04_Hasegawa2024TIA.md`, `02_Oruklu2025TIE.md`, `06_ParkKwak2023JEET.md` (36 항목 + Aging Sample 표, 본 문서 2절과 동일)
- 표기: 원문 값은 그대로, 분석자가 계산한 % 변화·역산값은 '(분석자 계산)' 으로 구분. '(해석)' 은 분석자 해석.

---

## 1. 원문 확인으로 바뀐 핵심 사실 (Abstract-level 대비)

| 논문 | 이전(초록 수준) 판단 | 원문 확인 결과 |
|---|---|---|
| Ghadrdan 2022 | 노화 방식·샘플 NR, 재구성 전류로 실험 | **Radd 0/0.1/0.22/0.34 Ω × C 5 단계 = 20 세트 (Table IX)**; 실험은 인버터 입력 전류를 **센서로 직접 측정**(재구성 식 (13)은 제안만); fsw 1 kHz; STM32H743ZI2 는 수집용, FFT 는 PC; 최대 오차 5.6 % |
| Lipnicki 2017 | 실험·노화 NR | **Radd 0/0.02/0.03/0.11/0.42 Ω**, 실험 최대 상대 오차 11 %, 시뮬 ±1 %/25 ms; **영벡터 구간 트리거**로 시간영역 적분(주파수 분석 아님); ABB AC800PEC(PowerPC+Virtex-II) 리그; 정격·샘플링 전부 NR |
| Hasegawa 2024 | C+ESR 변화 '관측' | **C 1100/1000 µF × Radd 0/150 mΩ 4 조건**, 추정값 표(Table II, III) 공개; 360/720 Hz 두 주파수 임피던스 연립(식 (22)(23)); FFT 는 **Excel 오프라인**; 10 kHz 캐리어, 1.2 kW, Vdc 270 V |
| Örüklü 2025 | ML 종류·수치 NR; 3상 추정 | 출력이 **단상 H-bridge**(3상 아님); 특징 2개(I_out,rms, PSD₃₀₀) → **GPR**; 학습 975·테스트 175×3; MPE <1 %, RMSE 7.07 µF; 50 kHz·2500 점(3 주기), 5 kHz 까지 유효; 온라인 구현은 F28379D 제안만 |
| Park & Kwak 2023 | 신호원·센서 NR | **커패시터 전류 i_C 를 측정**(추가 센서); 병렬 조합 25 쌍(122–650 µF, ESR ≈490→103 mΩ, 연동); 변조지수 0.3/0.5/0.8; 오차표 공개(DNN-Input1: C 0.19–1.20 %, ESR 0.049–1.06 %); 샘플링·네트워크 구조·샘플 수 NR; 오프라인 |

---

## 2. 논문별 36 항목 정밀 분석 + Aging Sample 표

## 2.1 Ghadrdan 2022 TPEL — Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor

> Evidence: Full text (PDF 원문 전체 확인, 2026-10-20)


#### 1. 정확한 제목, 저자, 연도, 저널, DOI, 저자 소속
- Title: Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor
- Authors: Moein Ghadrdan (Student Member, IEEE; corresponding), Saeed Peyghami (Member), Hossein Mokhtari (Senior Member), Frede Blaabjerg (Fellow)
- Year / Journal: IEEE Transactions on Power Electronics, vol. 37, no. 8, pp. 9733–9744, Aug. 2022 (received 11 Oct 2021, accepted 19 Feb 2022, published 25 Feb 2022)
- DOI: 10.1109/TPEL.2022.3153842
- 소속: Ghadrdan, Mokhtari — Center of Excellence in Power System Management and Control (CEPSMC), Dept. of Electrical Engineering, Sharif University of Technology, Tehran, Iran / Peyghami, Blaabjerg — AAU Energy, Aalborg University, Denmark. (Ghadrdan 은 2021-12 부터 AAU 방문 박사과정). 지원: REPEPS (Villum Foundation)

#### 2. 정확한 inverter topology
- Back-to-back (AC/DC/AC) 컨버터. 실험·시뮬 모두 **전단은 다이오드 브리지 정류기**(Table VI, VIII 'Rectifier type: Diode based'), 후단은 3상 2-Level IGBT 인버터(Fig. 6 회로도: 레그당 스위치 2개) → 3상 부하.
- 즉 '전압형 2-Level 3상 인버터 + 다이오드 정류기 + 계통측 L 필터' 구조. 능동 정류기(AFE) 실험은 아님.

#### 3. Power rating, DC-link voltage, switching frequency, load/motor, modulation
| 항목 | 시뮬레이션 (Table VI) | 실험 (Table VIII) |
|---|---|---|
| 정격 피상전력 | 4 kVA | 1.2 kVA |
| 입력 선간전압 / 주파수 | 380 V / 50 Hz | 190 V / 50 Hz |
| 공칭 DC-link 전압 | NR | 260 V |
| 계통 L 필터 | 3.6 mH | 3.377 mH |
| 스위칭 주파수 | 1–5 kHz 분석 | 1–5 kHz 스펙트럼 측정 후 **1 kHz 로 고정**하여 본 측정 |
| 부하 | 3상 부하(종류 NR) | 3상 부하(Fig. 8 'Load'; R/모터 여부 NR) |
| 변조 방식 | NR (스위칭 패턴 S_a,S_b,S_c 만 사용) | NR |
| 기본파 | 입력 50 Hz; 출력 주파수 NR | 입력 50 Hz |
- 커패시터 ESL 분석용 데이터시트 커패시터: Cornell Dubilier 500R112M500BC2B, 1.1 mF, 최대 ESR 108.8 mΩ (25 °C, 10 kHz), cutoff 10 kHz (Table II).

#### 4. Capacitor 종류, 정격 C, 정격 전압, ESR
- 종류: 알루미늄 전해 커패시터(Al-Cap).
- 실험 DC-link 공칭값: **235 µF / 200 mΩ** (Table VIII). 정격 전압 NR.
- 실험 커패시터 뱅크는 '유사한 10 µF 커패시터 여러 개를 병렬' 로 구성(제조사·모델 NR).
- 수명 실측 데이터(2절): 560 µF / 35 V 전해 커패시터 18개, 35 V·리플 1.4 A@100 Hz·105 °C 에서 2500 h, Agilent E4980A 측정 → 2000 h 후 평균 C −4 %, ESR +35 %.

#### 5. 진단 task: classification / regression
- **Regression 형(연속 지표)**: 손실각 δ 와 DF = tan δ 를 측정하고 DF/DF₀ > 1.6 (⇔ tan φ / tan φ₀ < 0.6) 을 EUL(End of Useful Life) 판정 기준으로 제안 → 최종 판정은 **이진 임계 판정**(Fig. 6 'Decision').

#### 6. Classification 이면 class 수와 정의
- 학습 기반 분류 아님. 임계 판정은 2 상태(정상 / EUL). 기준: ESR ×2 & C −20 % 동시 → DF ×1.6 (식 (5), (12)).

#### 7. Regression 이면 추정 대상(C / ESR / SOH)
- DF(= ω·C·ESR, 무차원) 와 커패시터 임피던스 각 φ / 손실각 δ. **C 와 ESR 을 개별로 출력하지 않음**(DF 는 결합 지표).

#### 8. 노화 구현: 실제 aging / parameter emulation / simulation
- **Parameter emulation (실험)**: 10 µF 커패시터 병렬 개수로 C 를 5 단계, **직렬 저항 0 / 0.1 / 0.22 / 0.34 Ω** 으로 ESR 을 4 단계 → 20 조합, 각 조합의 C·ESR 를 RLC 미터로 측정(Table IX).
- 시뮬레이션: C −20 %, ESR +100 % 의 수명 말기 조건을 가정해 임피던스 각 변화 계산(Table III, IV, VII).
- 별도로 실제 가속 노화 데이터(18개, 2500 h)는 DF 지표 타당성 검증(2절)에만 사용, 모니터링 실험에는 미사용.

#### 9. Aging sample 별 실제 capacitance
- Table IX 'C_RLCm' (µF): 234.6, 217.8, 201.5, 185.02, 168.68 / 235.3, 217.9, 201.2, 184.75, 168.47 / 234, 216.7, 199.98, 183.65, 167.48 / 234, 216.8, 200.2, 183.84, 167.72 (직렬 저항 그룹별 5개씩; 아래 표).

#### 10. Aging sample 별 실제 ESR
- Table IX 'ESR_RLCm' (Ω, 직렬 저항 포함 RLC 미터 측정값): 0.211, 0.214, 0.221, 0.245, 0.271 (Radd 0) / 0.289, 0.302, 0.318, 0.337, 0.367 (Radd 0.1) / 0.427, 0.441, 0.459, 0.485, 0.514 (Radd 0.22) / 0.517, 0.53, 0.546, 0.569, 0.6 (Radd 0.34).

#### 11. External resistor Radd 값
- **Radd = 0, 0.1, 0.22, 0.34 Ω** (본문 6절). Table IX 의 ESR 은 Radd 를 포함한 총 ESR 측정값.

#### 12. C only / ESR only / C+ESR simultaneous
- **C + ESR simultaneous** — 5 C 단계 × 4 Radd 단계의 전수 조합(20 세트).

#### 13. 총 dataset sample 수
- 모델 기반이라 학습 데이터셋 없음. 측정 세트 20개(각 세트 = 5 s 간격 20회 반복 측정 평균; 1회 = 100 kHz 1000 샘플).

#### 14. Class 별 sample 수
Not reported (원문에 없음) (분류 아님)

#### 15. Train / validation / test split
Not reported (원문에 없음) (학습 없음)

#### 16. Operating condition 종류
- 스위칭 주파수 1/2/3/4/5 kHz 에서 전류 스펙트럼·위상차 측정(Fig. 9) → 본 측정은 1 kHz 단일.
- 부하·변조지수·온도 변화 실험 **없음**(단일 운전점). 라인 필터·ESL 영향은 해석/시뮬(Table III–V, VII).

#### 17. 실제 측정 신호
- DC-link 전압 v_dc (전압 센서) → 1차 능동 HPF(차단 8.8 Hz) 로 DC 제거 → Fourier(대역통과) 로 스위칭 주파수 성분 v_C,sw.
- 인버터 입력 전류 i_inv: 실험에서는 **센서(LEM LA55-P)로 직접 측정**(센서 수를 줄이려고); 제안 방법은 출력 상전류 i_a,i_b,i_c 와 스위칭 패턴으로 계산(식 (13)).
- 추가로 커패시터 전류 i_C 를 측정해 스펙트럼 비교(Fig. 9, 검증용).

#### 18. 기존 inverter sensor 인지 추가 sensor 인지
- 제안 방법 기준: **기존 센서만**(출력 상전류 + DC-link 전압; 상전류는 제어용으로 이미 측정됨 — 본문). 커패시터 직렬 전류 센서 불필요.
- 실험 셋업 기준: 인버터 입력 전류를 별도 전류 센서로 직접 측정 → 실험은 'Partially'.

#### 19. 직접 측정 신호 vs reconstructed signal
- 직접 측정: v_dc, (실험) i_inv, (검증) i_C.
- Reconstructed: i_inv = S_a·i_a + S_b·i_b + S_c·i_c (식 (13); S_x = 상 x 상단 스위치 도통 시 1). 스위칭 주파수 등가회로(Fig. 6)에서 I_C,sw ≈ I_sw (계통 L 필터가 스위칭 고조파를 거의 차단; 식 (14)–(16), 위상차 θ_e 0.14°@1 kHz, 오차 <0.26 %, Table V).

#### 20. Sampling frequency
- **100 kHz** (실험: 1000 샘플 배열을 100 kHz 로 수집 후 UART 로 PC 전송).

#### 21. Window length / sample length
- 1000 샘플 = 10 ms 창(1 kHz 스위칭 10 주기). 5 s 간격 20회 반복 → 평균.

#### 22. 전처리 (normalization / filtering / segmentation / phase alignment)
- v_dc: 1차 능동 HPF 8.8 Hz(DC 제거, 스위칭 주파수에서 위상 지연 없음) → 대역통과(FFT).
- i_inv: 대역통과(FFT) 로 스위칭 고조파 추출.
- 핵심 요구: 두 필터가 스위칭 주파수에서 위상 이동이 없거나 동일해야 함(본문 3절). 정규화·세그먼트·위상 정렬 명시 없음(반복 평균만).

#### 23. Feature extraction (FFT / PSD / harmonic / STFT / Wavelet)
- FFT(대역통과 필터 역할) 로 v_C,sw, i_sw 추출 → 두 성분의 **시간 지연 t 측정** → φ = 지연각, δ = 90° − φ → DF = tan δ. Fig. 7: 1 kHz 에서 t ≈ 148 µs.

#### 24. 모델 또는 parameter estimation algorithm
- 해석적 임피던스 각 측정법(Section III). 수식: DF = ESR·C·ω (3); φ = π/2 − atan(DF) (4); DF/DF₀ = (ESR/ESR₀)(C/C₀) (5); EUL: DF/DF₀ > 1.6 (12); i_inv 재구성 (13); 스위칭 등가회로 I_C,sw, I_N,sw (14)(15); θ_e = π/2 − atan((L_eq ω_s − 1/(Cω_s))/ESR) (16). 추정기(RLS 등) 없음.

#### 25. AI: network architecture, input size, output, loss, optimizer
- 해당 없음(AI 아님).

#### 26. 저자가 직접 주장하는 contribution / novelty
Authors' claimed contributions (1절 끝):
1. 커패시터 임피던스 각을 **스위칭 주파수에서** 측정해 각 측정 오차가 tan 계산 오차에 미치는 영향을 최소화.
2. DF 를 EUL 지표로 쓸 가능성 조사 + 검출 기준(DF/DF₀ > 1.6) 도입.
3. 스위칭 주파수에서 각을 측정함으로써 직렬 전류 센서 불필요(출력 전류로 커패시터 전류 계산).
결론 요약: 측정 주파수를 높여 DF 정확도 향상 / 출력 전류 기반 온라인 측정으로 추가 센서 제거 / 실험 최대 오차 <6 %.

#### 27. True Online / Quasi-Online / Offline
- **True Online**: 정상 운전 중 스위칭 성분만 사용, 주입·시퀀스 없음. 단, 입력 전압에 스위칭 성분이 있으면 적용 불가(본문).

#### 28. 실제 on-board 구현 여부
- **부분 구현**: MCU(STM32H743ZI2)가 ADC 수집·UART 전송, **FFT·위상·DF 계산은 PC 에서** 수행(본문 6절 '1000 samples … transmitted via UART to the computer'). Fig. 6 의 Processing Stage 는 구조도이며 MCU 내 실행 기록 없음.

#### 29. DSP / MCU / FPGA 모델
- 처리장치 STM32H743ZI2 (Table VIII; ARM Cortex-M7 계열), 전류 센서 LA55-P, 전압 센서(모델 NR), RLC 미터(기준 측정).

#### 30. Control frequency / inference time / execution time / memory
- 제어 주파수 NR / 실행 시간 NR / 메모리 NR. 측정 주기: 5 s 간격 20회.

#### 31. Classification accuracy 또는 regression error
- Table IX: 20 세트의 임피던스 각 상대 오차 1 − tan(δ_m)/tan(δ_RLCm) = −0.056 ~ +0.055 → **최대 5.6 %**, 평균 약 2.6 %(표 값 평균, 분석자 계산). 수명 중 tan δ 는 약 60 % 증가 예상 → 오차는 기대 변화의 1/10 미만.
- 시뮬레이션(ESL+필터 포함, Table VII): 오차 0.32 %(1 kHz) ~ 9.60 %(5 kHz).

#### 32. Load / speed / temperature / modulation 변화 robustness
- fsw: 1→5 kHz 로 가면 ESL 오차 0.13→4.16 %(Table III), 시간 지연 37→3 µs(Table IV) → **fsw 는 커패시터 cutoff 의 1/10 이하 권장**.
- 라인 필터: 오차 <0.26 %(Table V).
- 부하·속도·변조지수·온도 변화 실험 없음. 온도는 향후 과제로 명시.

#### 33. 저자가 인정한 limitation
- DF 는 온도에 의존 → 온도 영향 연구와 온도 측정 기반 보정이 필요(결론).
- DF 수명 변화 범위를 정하는 통계 연구 필요(결론).
- 입력 전압에 스위칭 성분이 있으면 등가회로 무효(3절). 필터 위상 보상 필요(6절).
- ESL 영향 때문에 fsw 를 cutoff 보다 한 자릿수 낮게 선택해야 함(5절).

#### 34. 내가 보는 추가 limitation
- DF 는 C·ESR 결합 지표 → 두 열화 메커니즘 분리 불가(내 목표 'C/ESR' 과 불일치).
- 실험은 i_inv 를 **센서로 직접 측정** — 식 (13) 재구성의 실험 검증(데드타임·샘플링 동기 오차)은 수행되지 않음.
- 단일 운전점(부하·변조지수 고정) → 조건 변화 강건성 미검증.
- 처리는 PC 오프라인(온라인 구현 미시연), 100 kHz 샘플링 요구는 저가 MCU 에 부담.
- 실험 C(235 µF/260 V)·fsw 1 kHz 는 산업 드라이브 대비 낮은 fsw — 2–20 kHz 드라이브에서는 ESL 오차 증가.

#### 35. MATLAB/Simulink 재현에 필요한 신호와 parameter
- 모델: 다이오드 정류기 + L 필터(3.4–3.6 mH) + 전해 C(ESR, ESL 포함) + 2L 인버터 + 3상 부하. 로그 신호: i_a,i_b,i_c, S_a,S_b,S_c, v_dc, i_inv(검증), i_C(검증).
- 파라미터 스윕: C 235→168 µF 5단계, R_add 0/0.1/0.22/0.34 Ω, fsw 1–5 kHz, ESL 유무, 필터 L.
- 처리: HPF 8.8 Hz → FFT 대역통과 fsw 빈 → 위상차 → δ → DF, DF/DF₀ 추적. 재현 시 식 (13) 재구성 전류로 i_inv 를 대체해 재구성 오차를 별도 평가.

#### 36. 실험 장치 구현에 필요한 sensor 와 hardware
- 센서: DC-link 전압 센서(HPF 포함 아날로그 프론트엔드), 출력 상전류 센서 3개(기존 제어용 LEM), 검증용 커패시터 전류 센서 1개(LA55-P 급).
- 제어기: STM32H7 급 MCU 또는 DSP(ADC ≥100 kHz 동시 샘플링 2채널 이상), 스위칭 상태 접근, UART/USB 로깅.
- 가변 커패시터 뱅크(10 µF 단위 병렬) + 직렬 저항(0.1/0.22/0.34 Ω), RLC 미터(기준값).

#### Aging Sample 표 (원문 값만)
| Aging Sample | C | C Change | ESR | ESR Change | Operating Condition | Label |
|---|---:|---:|---:|---:|---|---|
| S1-1 | 234.6 µF | 기준(0 %) | 0.211 Ω | 기준(0 %) | fsw 1 kHz, 단일 부하 | DF/φ 측정 (err 2.6 %) |
| S1-2 | 217.8 µF | −7.2 % | 0.214 Ω | +1.4 % | 〃 | err 0.7 % |
| S1-3 | 201.5 µF | −14.1 % | 0.221 Ω | +4.7 % | 〃 | err 0.4 % |
| S1-4 | 185.02 µF | −21.1 % | 0.245 Ω | +16.1 % | 〃 | err 2.5 % |
| S1-5 | 168.68 µF | −28.1 % | 0.271 Ω | +28.4 % | 〃 | err 5.5 % |
| S2-1 (Radd 0.1 Ω) | 235.3 µF | +0.3 % | 0.289 Ω | +37 % | 〃 | err 0.3 % |
| S2-2 | 217.9 µF | −7.1 % | 0.302 Ω | +43 % | 〃 | err 4.0 % |
| S2-3 | 201.2 µF | −14.2 % | 0.318 Ω | +51 % | 〃 | err 4.0 % |
| S2-4 | 184.75 µF | −21.2 % | 0.337 Ω | +60 % | 〃 | err 2.1 % |
| S2-5 | 168.47 µF | −28.2 % | 0.367 Ω | +74 % | 〃 | err 4.2 % |
| S3-1 (Radd 0.22 Ω) | 234 µF | −0.3 % | 0.427 Ω | +102 % | 〃 | err 5.6 % |
| S3-2 | 216.7 µF | −7.6 % | 0.441 Ω | +109 % | 〃 | err 3.4 % |
| S3-3 | 199.98 µF | −14.8 % | 0.459 Ω | +118 % | 〃 | err 0.5 % |
| S3-4 | 183.65 µF | −21.7 % | 0.485 Ω | +130 % | 〃 | err 2.2 % |
| S3-5 | 167.48 µF | −28.6 % | 0.514 Ω | +144 % | 〃 | err 0.4 % |
| S4-1 (Radd 0.34 Ω) | 234 µF | −0.3 % | 0.517 Ω | +145 % | 〃 | err 4.4 % |
| S4-2 | 216.8 µF | −7.6 % | 0.53 Ω | +151 % | 〃 | err 1.2 % |
| S4-3 | 200.2 µF | −14.7 % | 0.546 Ω | +159 % | 〃 | err 2.9 % |
| S4-4 | 183.84 µF | −21.6 % | 0.569 Ω | +170 % | 〃 | err 1.4 % |
| S4-5 | 167.72 µF | −28.5 % | 0.6 Ω | +184 % | 〃 | err 2.5 % |
C·ESR 값과 err 는 Table IX 원문 값. 'C Change / ESR Change' 는 세트 1(234.6 µF / 0.211 Ω) 대비 분석자 계산(원문에는 % 변화 없음). Label 은 라벨이 아니라 측정 오차(회귀형 지표).

#### 원문 수식 요약 (재현용)
- (3) DF = ESR·C·ω ; (4) φ = π/2 − atan(DF) ; (5) DF/DF₀ = (ESR/ESR₀)·(C/C₀) ; (12) EUL: DF/DF₀ = tan δ / tan δ₀ > 1.6 ⇔ tan φ / tan φ₀ < 0.6
- (13) i_inv = S_a i_a + S_b i_b + S_c i_c
- (14) I_C,sw = (R_eq + jL_eq ω_s) / ((R_eq+ESR) + j(L_eq ω_s − 1/(Cω_s))) · I_sw ; (15) I_N,sw = (ESR − j/(Cω_s)) / (…) · I_sw ; R_eq = 2R_Net, L_eq = 2L_Net
- (16) θ_e = π/2 − atan((L_eq ω_s − 1/(Cω_s)) / ESR) — 인버터 전류와 커패시터 전류 스위칭 성분의 위상차(1 kHz: 0.140° 계산, 1.021° 실측 → 5 kHz 0.023°)

#### 원문 해석 표 (fsw 영향)
| fsw (kHz) | ESL 오차 % (Table III) | Δt µs (Table IV) | 필터 오차 % (Table V) | 시뮬 오차 % (Table VII) |
|---|---|---|---|---|
| 1 | 0.13 | 37.0 | 0.265 | 0.32 |
| 2 | 0.52 | 15.2 | 0.209 | 1.25 |
| 3 | 1.23 | 7.73 | 0.196 | 3.60 |
| 4 | 2.38 | 4.57 | 0.191 | 5.67 |
| 5 | 4.16 | 3.00 | 0.189 | 9.60 |

---
(이 파일은 `2level_top5_fulltext_comparison.md` 와 같은 원문 분석에서 생성됨. 이전 Abstract-level 워크시트의 선정 점수·Tier 는 `2level_inverter_dc_link_capacitor_onboard_top10.md` 5절 참조.)

## 2.2 Lipnicki & Lewandowski 2017 PED — DC Link Condition Monitoring Method for Two-Level AC/DC/AC Converters

> Evidence: Full text (PDF 원문 전체 확인, 2026-10-20)


#### 1. 정확한 제목, 저자, 연도, 저널, DOI, 저자 소속
- Title: DC Link Condition Monitoring Method for Two-Level AC/DC/AC Converters
- Authors: Piotr Lipnicki, Daniel Lewandowski (연락: piotr.lipnicki@pl.abb.com)
- Year / Journal: Power Electronics and Drives, vol. 2(37), no. 1, pp. 43–56, 2017 (manuscript received 3 Oct 2016, accepted 2 Feb 2017)
- DOI: 10.5277/PED170107
- 소속: ABB Sp. z o.o., Corporate Research Center, Starowiślna 13a, 31-038 Kraków, Poland. 관련 특허 WO2015165574 (A1) [10].

#### 2. 정확한 inverter topology
- **2-Level AC/DC/AC** 컨버터(제목). 시뮬레이션: 15 kV 계통 → 결합 변압기 → **능동 정류 유닛(IGBT) + DC-link + 인버터 유닛** → 부하(견인 컨버터 예시, Fig. 3/5; DC choke 2개 포함). 다이오드 정류기 변형도 2.3절에서 다룸(계통 각도로 다이오드 도통 상태 결정, Table 1).
- 실험: 드라이브 + 유도전동기(IM) 부하 시험 리그(Fig. 7, 8). 정류단 종류(실험) 명시 없음.

#### 3. Power rating, DC-link voltage, switching frequency, load/motor, modulation
- Power rating: NR (시뮬: 15 kV 계통 연결 full-scale 견인 컨버터; 실험 리그 정격 NR)
- DC-link 전압: NR / 스위칭 주파수: NR / 변조: NR (제어는 동기 좌표계 PI; FOC/scalar/DTC 어느 것이든 스위칭 신호만 있으면 됨)
- 부하: 시뮬 — 정격 전류의 30 % 부하; 실험 — 유도전동기(정격 NR).

#### 4. Capacitor 종류, 정격 C, 정격 전압, ESR
- 종류: 전해 커패시터(본문 'electrolytic' 문맥) — 정격 C, 정격 전압, 정격 ESR 모두 NR.
- 실험 기준 ESR(ESR₁, 저항 미추가) 추정값 **0.15 Ω**. 수명 기준: 용량 75 % 이하이면 수명 종료([8] 인용).

#### 5. 진단 task: classification / regression
- **Regression (ESR 연속 추정)** + 임계 판정: C < k_p·C_init 이면 알람·정지 명령(식 (9), k_p 는 사용자 임계).

#### 6. Classification 이면 class 수와 정의
- 학습 분류 아님. 알람은 2 상태(정상 / 임계 초과).

#### 7. Regression 이면 추정 대상(C / ESR / SOH)
- ESR(t) [Ω] (식 (7)) 와 이를 이용한 C(백분율, 식 (8)). 핵심 health indicator 는 **ESR 증가 추세**.

#### 8. 노화 구현: 실제 aging / parameter emulation / simulation
- **Parameter emulation**: 시뮬레이션에서는 ESR 을 시간 의존 식 (11) 로 모델링하고 '정해진 저항값을 커패시터에 직렬 추가' 하는 스텝 변화로 구현; 실험에서도 **DC-link 커패시턴스에 추가 저항을 직렬 연결**(4.2절). 실제 가속 노화 없음.

#### 9. Aging sample 별 실제 capacitance
- C 값 NR (C 는 바꾸지 않음; ESR 만 변화).

#### 10. Aging sample 별 실제 ESR
- Table 2(원문 표 제목 오기 'Table 1'): ESR₁ 추정 0.15 Ω(기준, 추가 0) / ESR₂ ca. 0.18 (기대 0.17) / ESR₃ ca. 0.185 (0.18) / ESR₄ ca. 0.23 (0.26) / ESR₅ ca. 0.52 (0.57).

#### 11. External resistor Radd 값
- **Radd = 0, 0.02, 0.03, 0.11, 0.42 Ω** (Table 2 'Added resistance').

#### 12. C only / ESR only / C+ESR simultaneous
- **ESR only** (C 고정).

#### 13. 총 dataset sample 수
- 모델 기반, 데이터셋 없음. 실험 측정점 5개(ESR₁–ESR₅).

#### 14. Class 별 sample 수
Not reported (원문에 없음) (분류 아님)

#### 15. Train / validation / test split
Not reported (원문에 없음) (학습 없음)

#### 16. Operating condition 종류
- 시뮬: 정격 전류 30 % 단일 부하, ESR 스텝(Fig. 6, ESR 스텝 상승 8단계, 약 0.005→0.18 Ω — 범례 값은 원문 그림에서 정확히 판독되지 않아 수치 인용 보류).
- 실험: 단일 운전점(부하·속도 변화 없음).

#### 17. 실제 측정 신호
- DC-link 전압 U_DC(직접 측정, 전체 DC-link 양단), 3상 입력 전류 I_a, I_b, I_c(정류 유닛 측; '드라이브 앞 보호 릴레이에 이미 있는 측정' 으로 가정), 스위칭 신호 S_aREC…S_cINV(제어기 내부). Full-scale 구성에서는 인버터 측 상전류도 사용(식 (2), (10)).

#### 18. 기존 inverter sensor 인지 추가 sensor 인지
- **기존 센서만** (초록·4.3절: '추가 센서 불필요, 이미 설치된 센서와 내부 신호 사용'). 실험 리그 측정보드는 LEM 전류 센서 사용.

#### 19. 직접 측정 신호 vs reconstructed signal
- 직접 측정: U_DC, I_a, I_b, I_c.
- Reconstructed: I_REC = S_aREC I_aREC + S_bREC I_bREC + S_cREC I_cREC (1); I_INV = Σ S_xINV I_xINV (2); I_DC(t) = S_aREC(t) I_a(t) + … (6, 트리거 시점); full-scale: I_cap = I_REC − I_INV (10). Fig. 1: 측정 vs 재구성 정류 유닛 DC 전류 일치(재구성 신호는 1 주기 지연).

#### 20. Sampling frequency
Not reported (원문에 없음)

#### 21. Window length / sample length
- 인버터 영벡터 구간(S_aINV = S_bINV = S_cINV → S_TRIG = 1)의 T_on(k)~T_off(k) 창에서 적분(식 (5), (7)). 창 길이 = 영벡터 지속시간(수치 NR).

#### 22. 전처리 (normalization / filtering / segmentation / phase alignment)
- 인버터 스위칭과 동기화(트리거)하여 영벡터 구간만 사용 → 필터 없이 dU_DC/dt, dI_DC/dt 로 ESR 계산. 정규화·세그먼트·위상 정렬 별도 언급 없음. 응답시간 25 ms(시뮬).

#### 23. Feature extraction (FFT / PSD / harmonic / STFT / Wavelet)
- 주파수 변환 없음. 시간영역 미분·적분: ESR(t) = ∫_{T_on}^{T_off} ((dU_DC/dt − I_DC/C_init) / (dI_DC/dt)) dt (7); C = (I_DC·ESR − U_DC)² / U_DC² × 100 % (8).

#### 24. 모델 또는 parameter estimation algorithm
- 해석적 시간영역 추정(식 (1)–(10)). 임피던스 근사 Z ≈ ESR (12), u_C,ac = ESR·i_C (13). 추정기(RLS/Kalman) 없음. 다이오드 정류기용 스위칭 상태 테이블(Table 1: θ∈(−60°,60°) S_a=1; (60°,180°) S_b=1; (−180°,−60°) S_c=1).

#### 25. AI: network architecture, input size, output, loss, optimizer
- 해당 없음(AI 아님).

#### 26. 저자가 직접 주장하는 contribution / novelty
Authors' claimed contributions:
1. 추가 센서 없이 **DC-link 전압 측정 + DC-link 전류 재구성** 만으로 온라인 ESR 추정(초록, 2.1절 '기존 방법 [3,4] 보다 적은 측정').
2. 계산량이 작아 큰 연산 능력 불필요; 인버터 스위칭과 동기화해 SW·HW 를 더 단순화(2절, 특허 [10]).
3. 제어 전략(FOC/scalar/DTC)에 독립.
4. 회생 운전·AC 주입(Le et al. [12]) 없이 운전 중 ESR 결정(4.3절).
5. 시뮬(±1 %, 25 ms) + 실험(최대 상대 오차 11 %)으로 검증.

#### 27. True Online / Quasi-Online / Offline
- **True Online**: 컨버터 운전 중(영벡터 구간은 PWM 에 자연 발생) 추정. 주입·시퀀스·정지 없음.

#### 28. 실제 on-board 구현 여부
- **Yes**: ABB AC800PEC 제어기(PowerPC + Virtex-II FPGA)에 Simulink 설계 제어를 배포(Fig. 8 'Design Control Deployed to PEC'); 측정은 MI 보드(LEM). 데이터 수집은 MATLAB/Java SOAP. 알고리즘이 PEC 에서 실행됐는지 PC 후처리인지는 본문이 명시하지 않음 — 'implemented in an easy manner' 로만 기술.

#### 29. DSP / MCU / FPGA 모델
- ABB AC800PEC (PowerPC 프로세서 + Xilinx Virtex-II FPGA), 측정보드 LEM 센서, 게이트 드라이버(광섬유 PWM).

#### 30. Control frequency / inference time / execution time / memory
- 제어 주파수 NR / 실행 시간 NR / 메모리 NR. 시뮬 응답시간 25 ms.

#### 31. Classification accuracy 또는 regression error
- 시뮬: ESR 스텝 추적 오차 약 ±1 %, 응답 25 ms. 실험: 기대값 대비 **최대 상대 오차 11 %**(Table 2: 0.18 vs 0.17, 0.185 vs 0.18, 0.23 vs 0.26, 0.52 vs 0.57).

#### 32. Load / speed / temperature / modulation 변화 robustness
- 부하·속도·온도·변조 변화 실험 없음(단일 조건). 저자는 과전압·과전류·동적 충방전 등 '원치 않는 현상' 이 ESR 결정에 영향을 준다고 기술.

#### 33. 저자가 인정한 limitation
- 노화 과정이 비선형이어서 ESR·잔여수명 정확 결정이 어려움(2절, 4.2절).
- 정확도 평가에 쓴 점이 적음(4.2절).
- 향후: DC-link 전압·전류의 외란으로부터 알고리즘 분리(decoupling) 또는 외란을 추가 지표로 활용(결론).

#### 34. 내가 보는 추가 limitation
- 정격(전압·전력·fsw·C)·샘플링·실행시간이 전혀 없어 재현 조건 불명.
- C_init 을 알고 있어야 ESR 계산 가능(식 (7)) → C 가 함께 변하면 ESR 오차로 전파(C 변화 실험 없음).
- 영벡터 구간 적분은 변조지수가 높을수록 창이 짧아짐(추론) → 고변조·고속 운전에서 정확도 저하 가능.
- 실험 오차 11 % 는 EoL 기준(ESR ×2) 대비 작지만, 초기 열화(+20–30 %) 검출에는 부족할 수 있음.
- 저널 영향력 낮음, 그림 수치 판독성 낮음.

#### 35. MATLAB/Simulink 재현에 필요한 신호와 parameter
- 모델: 3상 전원 + (능동 또는 다이오드) 정류기 + DC choke + C(ESR) + 2L 인버터 + IM/RL 부하. 로그: U_DC, I_a,I_b,I_c(정류 측), 필요 시 인버터 측 상전류, S_xREC, S_xINV, 검증용 I_DC·I_cap.
- 구현: 영벡터 검출(S_aINV=S_bINV=S_cINV) → 트리거 창 → 식 (6) 재구성 → 식 (7) ESR, 식 (8) C. 스윕: R_add 0/0.02/0.03/0.11/0.42 Ω(원문) + 추가로 C 변화·부하 30/60/100 %.
- 다이오드 정류기면 Table 1 각도 기반 S_x 생성(계통 각도 필요).

#### 36. 실험 장치 구현에 필요한 sensor 와 hardware
- 센서: DC-link 전압 센서 1개, 정류 측 3상 전류 센서(LEM; 보호 릴레이 공용 가능), (full-scale) 인버터 측 3상 전류 센서.
- 제어기: 스위칭 신호와 측정을 동기 샘플링할 수 있는 DSP/FPGA(ABB 는 AC800PEC). 직렬 저항 삽입용 저항 세트(0.02–0.42 Ω, 전류 정격 고려).

#### Aging Sample 표 (원문 값만)
| Aging Sample | C | C Change | ESR | ESR Change | Operating Condition | Label |
|---|---:|---:|---:|---:|---|---|
| ESR₁ | Not reported (원문에 없음) (C 고정) | 0 % | 0.15 Ω (추정 기준값; Radd 0) | 기준 | 실험 리그, 단일 운전점 | ESR 추정 (기준) |
| ESR₂ | 〃 | 0 % | 기대 0.17 Ω / 추정 ca. 0.18 Ω (Radd 0.02) | +13 % (기대) | 〃 | 오차 ≈ +6 % |
| ESR₃ | 〃 | 0 % | 기대 0.18 Ω / 추정 ca. 0.185 Ω (Radd 0.03) | +20 % | 〃 | 오차 ≈ +3 % |
| ESR₄ | 〃 | 0 % | 기대 0.26 Ω / 추정 ca. 0.23 Ω (Radd 0.11) | +73 % | 〃 | 오차 ≈ −11 % |
| ESR₅ | 〃 | 0 % | 기대 0.57 Ω / 추정 ca. 0.52 Ω (Radd 0.42) | +280 % | 〃 | 오차 ≈ −9 % |
원문 Table 2 값. 'ESR Change' 와 오차 % 는 기대값(0.15 + Radd) 기준 분석자 계산. C 는 변경하지 않았고 정격도 미기재.

#### 원문 수식 요약 (재현용)
- (1) I_REC = S_aREC I_aREC + S_bREC I_bREC + S_cREC I_cREC ; (2) I_INV = Σ S_xINV I_xINV ; (4) 트리거: S_aINV = S_bINV = S_cINV → S_TRIG = 1
- (6) I_DC(t) = S_aREC(t) I_a(t) + S_bREC(t) I_b(t) + S_cREC(t) I_c(t)
- (7) ESR(t) = ∫_{T_on}^{T_off} [ (dU_DC/dt − I_DC(t)/C_init) / (dI_DC(t)/dt) ] dt
- (8) C = (I_DC ESR − U_DC)² / U_DC² × 100 % ; (9) C < k_p C_init → 알람 ; (10) I_cap = I_REC − I_INV
- (11) 1/ESR(t) = 1/ESR(0) · (1 − k t e^{−4700/(T−273)}) (시뮬용 ESR 성장 모델)

---
(이 파일은 `2level_top5_fulltext_comparison.md` 와 같은 원문 분석에서 생성됨. 이전 Abstract-level 워크시트의 선정 점수·Tier 는 `2level_inverter_dc_link_capacitor_onboard_top10.md` 5절 참조.)

## 2.3 Hasegawa & Hirose 2024 TIA — Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor Based on Analysis of a Six-Pulse Diode Rectifier Having AC and DC Inductors

> Evidence: Full text (PDF 원문 전체 확인, 2026-10-20)


#### 1. 정확한 제목, 저자, 연도, 저널, DOI, 저자 소속
- Title: Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor Based on Analysis of a Six-Pulse Diode Rectifier Having AC and DC Inductors
- Authors: Kazunori Hasegawa (Member, IEEE; corresponding), Yuto Hirose (현 Chugoku Electric Power Co.)
- Year / Journal: IEEE Transactions on Industry Applications, vol. 60, no. 6, pp. 9043–9051, Nov./Dec. 2024 (received 8 Feb 2024, accepted 15 Jul 2024, published 15 Aug 2024; paper 2024-IPCC-0225.R1, ECCE 2023 발표판 [26] 확장)
- DOI: 10.1109/TIA.2024.3443784
- 소속: Dept. of Electrical and Electronic Engineering, Kyushu Institute of Technology, Kitakyushu, Fukuoka 804-8550, Japan. 지원: NEDO JPNP20004.

#### 2. 정확한 inverter topology
- **6-pulse 다이오드 정류기(AC 라인 인덕터 L_ac + DC 인덕터 L_dc) + 3상 2-Level PWM 인버터**(Fig. 1: 레그당 스위치 2개, IGBT) + 3상 RL 부하. 회생 제동 없는 범용 모터 드라이브 구조를 대상으로 함.

#### 3. Power rating, DC-link voltage, switching frequency, load/motor, modulation
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

#### 4. Capacitor 종류, 정격 C, 정격 전압, ESR
- 종류: **알루미늄 전해 커패시터**(모든 조건). 공칭 C = **1100 µF 또는 1000 µF**(Table I), 단위용량상수 H = 33 ms(1100 µF)/30 ms(1000 µF). 정격 전압·정격 ESR·제조사 NR. 초기 측정값(조건 A): 1015 µF / 45 mΩ (제안법 기준 Z_C(measurement)).

#### 5. 진단 task: classification / regression
- **Regression**: C 와 ESR(R_S) 을 연속 추정.

#### 6. Classification 이면 class 수와 정의
- 해당 없음(분류 아님).

#### 7. Regression 이면 추정 대상(C / ESR / SOH)
- **C [µF] + ESR [mΩ] 동시** (6차·12차 고조파 임피던스 2개 연립, 식 (20)–(23)).

#### 8. 노화 구현: 실제 aging / parameter emulation / simulation
- **Parameter emulation**: 조건 A C=1100 µF / B 1100 µF + 직렬 150 mΩ / C 1000 µF / D 1000 µF + 직렬 150 mΩ (4.B절). 실제 가속 노화 없음(저자 이전 연구 [16] 인용만).

#### 9. Aging sample 별 실제 capacitance
- 공칭: A 1100, B 1100, C 1000, D 1000 µF. 제안법 추정(Table II, L_ac 4.6 mH/L_dc 8.2 mH 케이스 3): A 1015, B 992, C 917, D 919 µF. 케이스별 전체 값은 아래 표.

#### 10. Aging sample 별 실제 ESR
- 공칭 ESR NR(초기 추정 45 mΩ). 추정(케이스 3): A 45, B 155, C 37, D 179 mΩ. 모든 케이스 값은 아래 표.

#### 11. External resistor Radd 값
- **Radd = 150 mΩ** (조건 B, D).

#### 12. C only / ESR only / C+ESR simultaneous
- **C + ESR simultaneous** — 2 C 수준 × 2 ESR 수준의 4 조합(조건 D 가 동시 변화).

#### 13. 총 dataset sample 수
- 모델 기반; 측정 조건 = 4 커패시터 조건 × 4 인덕터 조합(Table II) + 출력 전력 2 수준(Table III) = 20 측정점.

#### 14. Class 별 sample 수
Not reported (원문에 없음) (분류 아님)

#### 15. Train / validation / test split
Not reported (원문에 없음) (학습 없음)

#### 16. Operating condition 종류
- 인덕터 조합 4종: 1) L_ac 4.6 mH, L_dc 0 / 2) 4.6, 4.6 / 3) 4.6, 8.2 / 4) 8.2, 4.6 mH.
- 출력 전력 P_O = 1200 W, 600 W (Table III). 연속 도통 조건 I_d ≥ I_C(6ω) 필요(Fig. 8: 약 150 W 이상에서 연속).
- 온도·속도·변조지수 변화 없음.

#### 17. 실제 측정 신호
- **커패시터 전압 v_C 만 측정**(DC 블록 필터 → FFT → V_C6, V_C12). 커패시터 전류는 측정하지 않고 V_S, L_ac, L_dc, P_O 로 계산(식 (6)–(16)). P_O 는 인버터 출력 전류 센서(제어용)로 얻는 것으로 가정.

#### 18. 기존 inverter sensor 인지 추가 sensor 인지
- **기존 센서만**: 전압 센서(v_C) + 출력 전력용 기존 출력 전류 센서. 전류 센서 추가 없음. 전원 전압 V_S 와 인덕터 값은 파라미터로 알고 있어야 함.

#### 19. 직접 측정 신호 vs reconstructed signal
- 직접 측정: v_C (DC 블록 필터 후 리플 ṽ_C).
- 계산(재구성): I_C6, I_C12 = v_Rm/(Z_om + Z_m) (식 (12)(13)), Z_om = j(2 − 3u/2π) mωL_ac, Z_m = jmωL_dc, 겹침각 u = arccos(1 − 2ωL_ac I_d/(√3 V_Sm)), I_d = P_O/V_dc. 임피던스 보정 Ẑ_C = G_comp Z_C, G_comp = Z_C/Z_C(measurement) (식 (18)(19)).

#### 20. Sampling frequency
Not reported (원문에 없음) (FFT 는 오실로스코프 파형을 Microsoft Excel 로 오프라인 계산)

#### 21. Window length / sample length
Not reported (원문에 없음)

#### 22. 전처리 (normalization / filtering / segmentation / phase alignment)
- DC 블록 필터(DC 제거) → 이동평균 필터(차단 1300 Hz) 로 스위칭 리플 제거 → FFT. 정규화·세그먼트 언급 없음. 초기 임피던스 보정 G_comp(LCR 사전 측정 또는 초기 운전값).

#### 23. Feature extraction (FFT / PSD / harmonic / STFT / Wavelet)
- FFT 로 360 Hz(6f_S)·720 Hz(12f_S) 성분 V_C6, V_C12 추출 → Z_C(6ω), Z_C(12ω) = V/I.

#### 24. 모델 또는 parameter estimation algorithm
- 해석적 연립: Ẑ_C(6ω)² = (1/(6ωC))² + R_S², Ẑ_C(12ω)² = (1/(12ωC))² + R_S² → R_S = sqrt(4/3 Ẑ_C²(12ω) − 1/3 Ẑ_C²(6ω)) (22), C = 1/(2√2 ω) · 1/sqrt(Ẑ_C²(6ω) − Ẑ_C²(12ω)) (23). 전해 커패시터 ESR 의 주파수 의존(6차 vs 12차)은 구분 못 하고 평균값 — 향후 과제.

#### 25. AI: network architecture, input size, output, loss, optimizer
- 해당 없음.

#### 26. 저자가 직접 주장하는 contribution / novelty
Authors' claimed contributions:
1. AC 라인 인덕터와 DC 인덕터를 **모두** 가진 6-pulse 다이오드 정류기의 리플 전류 해석을 CM 에 도입(선행 [18] 은 DC 인덕터만).
2. 그 고조파 성분으로 **전류 센서 없이 ESR 과 C 를 모두** 감시.
3. 200 V·1.2 kW 실험에서 L_ac, L_dc, 출력 전력을 바꿔도 ESR·C 변화 관측 확인(결론).
4. 수백 W ~ 수백 kW 의 6-pulse 정류기 인버터에 적용 가능하다고 주장(3.D절).

#### 27. True Online / Quasi-Online / Offline
- **True Online**: 정상 운전 중 정류기 고유 리플 사용, 주입·정지 없음. 전제: 연속 도통(I_d ≥ I_C(6ω)), 6f_S·12f_S 가 2f_I 와 다를 것, P_O·V_S·인덕터 값 기지.

#### 28. 실제 on-board 구현 여부
- **No**: FFT 를 Microsoft Excel 로 오프라인 계산(3.D절). 저자는 Arduino 급 저가 보드에서 수십 ms FFT 로 충분하다고 언급(구현 아님).

#### 29. DSP / MCU / FPGA 모델
Not reported (원문에 없음) (인버터 제어기 모델 미기재)

#### 30. Control frequency / inference time / execution time / memory
- NR. (Arduino FFT 수십 ms 가능성만 언급; 노화는 1000 h 단위로 진행하므로 충분하다는 논리)

#### 31. Classification accuracy 또는 regression error
- 정량 오차 표 없음. Table II·III 의 추정값 vs 공칭: C 1000 µF 조건에서 904–941 µF(−6 ~ −10 %), 1100 µF 에서 992–1055 µF(조건 A 는 보정 기준이라 1015 고정); Radd 150 mΩ 추가 시 ESR 155–215 mΩ(+110 ~ +170 mΩ). 저자: 전류 센서 방식보다 정확도가 다소 낮을 수 있음, 전압 양자화 오차가 원인(오차 전파 이론 [22]).

#### 32. Load / speed / temperature / modulation 변화 robustness
- L_ac(4.6→8.2 mH), L_dc(0→8.2 mH), P_O(1200→600 W) 변화에서도 ESR·C 변화 추적(Table II, III). 600 W 에서 B 조건 C 가 1055 µF 로 과대(공칭 1100)·C 조건 ESR 97 mΩ(1200 W 에서 37) 등 **운전점에 따른 편차 존재**(원문 수치). 온도·속도·변조 변화 없음.

#### 33. 저자가 인정한 limitation
- 정확도가 전류 센서 기반 방법보다 낮을 수 있음; 커패시터 전압 양자화 오차 → 전압 센싱 분해능(비트 수) 향상 필요(4.C절).
- ESR 의 6차/12차 주파수 의존을 구분 못 함(2.C절, 향후 과제).
- 연속 도통 모드에서만 유효(식 (17)); 저주파 인버터 리플이 6f_S/12f_S 와 겹치면 무효(식 (14)).

#### 34. 내가 보는 추가 limitation
- 다이오드 정류기 전단에만 적용(AFE·배터리·PV 입력 2L 인버터 불가) → 내 '인버터 신호' 목표와 정보원이 다름.
- 전원 전압·인덕터 값·출력 전력이 모델 입력 → 파라미터 오차·전원 불평형(후속 2025 MR 에서 다룸)에 민감.
- 초기 보정 G_comp 가 조건 A 를 기준으로 하므로 절대 정확도가 아니라 '변화 추적' 에 가까움.
- 오프라인 Excel FFT, 샘플링·창 길이 미기재 → 실시간 구현 미검증. 모터 대신 RL 부하.

#### 35. MATLAB/Simulink 재현에 필요한 신호와 parameter
- 모델: 3상 200 V/60 Hz 전원 + L_ac(4.6–8.2 mH) + 6-pulse 다이오드 + L_dc(0–8.2 mH) + C(1000/1100 µF, R_S) + 2L 인버터(10 kHz, 50 Hz 출력) + RL 부하(1200/600 W). 로그: v_C, (검증) i_C, i_R, 출력 전류·전압(P_O).
- 구현: DC 블록 → 1300 Hz 이동평균 → FFT 360/720 Hz → 식 (6)–(16) 으로 I_C6, I_C12 → 식 (22)(23). 스윕: C 1100/1000, R_add 0/150 mΩ, L_ac, L_dc, P_O; 추가로 전원 불평형.

#### 36. 실험 장치 구현에 필요한 sensor 와 hardware
- 센서: 커패시터 전압 센서(고분해능 ADC 권장), 기존 출력 전류 센서(P_O 계산), 전원 전압 정보(V_S 공칭값 사용 가능). 전류 센서 불필요.
- 하드웨어: DC 블록 필터 회로, L_ac/L_dc 인덕터, 직렬 저항 150 mΩ, 가변 RL 부하, FFT 가능한 MCU(Arduino 급 이상).

#### Aging Sample 표 (원문 값만)
| Aging Sample | C | C Change | ESR | ESR Change | Operating Condition | Label |
|---|---:|---:|---:|---:|---|---|
| A (1100 µF, Radd 0) | 1100 µF 공칭 / 추정 1015 µF (모든 케이스, 보정 기준) | 기준 | 추정 45 mΩ | 기준 | L_ac/L_dc 4종, P_O 1200/600 W | C+ESR 추정 |
| B (1100 µF + 150 mΩ) | 추정 1019 / 995 / 992 / 993 µF (케이스 1–4); 600 W: 1055 µF | ≈0 (공칭) | 추정 186 / 163 / 155 / 170 mΩ; 600 W: 215 mΩ | +150 mΩ (Radd) | 〃 | ESR 증가 추적 |
| C (1000 µF, Radd 0) | 추정 918 / 927 / 917 / 908 µF; 600 W: 935 µF | −9.1 % (공칭) | 추정 39 / 64 / 37 / 43 mΩ; 600 W: 97 mΩ | 0 (공칭) | 〃 | C 감소 추적 |
| D (1000 µF + 150 mΩ) | 추정 932 / 940 / 919 / 904 µF; 600 W: 941 µF | −9.1 % (공칭) | 추정 199 / 210 / 179 / 171 mΩ; 600 W: 208 mΩ | +150 mΩ (Radd) | 〃 | C↓ + ESR↑ 동시 |
Table II(케이스 1: L_ac 4.6/L_dc 0, 2: 4.6/4.6, 3: 4.6/8.2, 4: 8.2/4.6 mH, P_O 1200 W)·Table III(케이스 3, P_O 600 W) 원문 값. 'C Change' 는 공칭 기준 분석자 계산.

#### 원문 수식 요약 (재현용)
- (5) Z_C(ω_k) = V_C(ω_k)/I_C(ω_k) = sqrt((1/(ω_k C))² + R_S²)
- (6) Z_om = j(2 − 3u/2π) mωL_ac ; (7) Z_m = jmωL_dc ; m = 6, 12, … ; (9)–(11) v_Rm = A_Rm cos mθ + B_Rm sin mθ (겹침각 u 포함 계수) ; (12)(13) i_Cm = i_Rm = v_Rm/(Z_om + Z_m)
- (15) u = arccos(1 − 2ωL_ac I_d/(√3 V_Sm)) ; (16) I_d = P_O/V_dc ; (17) 연속 도통: I_d ≥ I_C(6ω)
- (18)(19) Ẑ_C = G_comp Z_C, G_comp = Z_C/Z_C(measurement)
- (22) R_S = sqrt(4/3 Ẑ_C²(12ω) − 1/3 Ẑ_C²(6ω)) ; (23) C = 1/(2√2) · 1/ω · 1/sqrt(Ẑ_C²(6ω) − Ẑ_C²(12ω))

---
(이 파일은 `2level_top5_fulltext_comparison.md` 와 같은 원문 분석에서 생성됨. 이전 Abstract-level 워크시트의 선정 점수·Tier 는 `2level_inverter_dc_link_capacitor_onboard_top10.md` 5절 참조.)

## 2.4 Örüklü & Ağalar 2025 TIE — Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters

> Evidence: Full text (PDF 원문 전체 확인, 2026-10-20)


#### 1. 정확한 제목, 저자, 연도, 저널, DOI, 저자 소속
- Title: Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters
- Authors: Kerim Örüklü (Student Member, IEEE; corresponding), Şener Ağalar (Member, IEEE)
- Year / Journal: IEEE Transactions on Industrial Electronics, vol. 72, no. 4, pp. 4227–4237, Apr. 2025 (received 31 Jan 2024, accepted 2 Sep 2024, published 26 Sep 2024, current version 11 Mar 2025)
- DOI: 10.1109/TIE.2024.3454814
- 소속: Dept. of Electrical and Electronics Engineering, Eskisehir Technical University, Eskisehir 26555, Türkiye (두 저자 동일).

#### 2. 정확한 inverter topology
- **AC/DC/AC 컨버터: 3상 입력 다이오드 정류기(6-pulse) + DC-link + 단상(H-bridge, 스위치 4개) 출력 인버터** + LC 출력 필터 + 부하(Fig. 2, 2절 '3상 입력, 단상 출력'). 즉 **3상 2-Level 인버터가 아님** — 단상 출력 2-Level 인버터.

#### 3. Power rating, DC-link voltage, switching frequency, load/motor, modulation
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

#### 4. Capacitor 종류, 정격 C, 정격 전압, ESR
- 종류: 알루미늄 전해(AL-Cap). 실험 공칭 **625 µF** (측정 기준값 620.85 µF @120 Hz, 25 °C, Escort ELC-132A LCR). 정격 전압·정격 ESR·제조사 NR. EOL 기준 인용: C −20 % 또는 ESR ×2.

#### 5. 진단 task: classification / regression
- **Regression**: C_link [µF] 연속 추정(식 (3) f(F₁′, F₂′) = C_link).

#### 6. Classification 이면 class 수와 정의
- 해당 없음. (예지보전 단계에서 'New / Aged–Nearly Aged' 로 나누는 개념도는 있으나 분류 모델 아님.)

#### 7. Regression 이면 추정 대상(C / ESR / SOH)
- **C only** (저자: 저주파 성분은 ESR 변화의 영향을 받지 않으므로 ESR 추정 불가, 3.B절).

#### 8. 노화 구현: 실제 aging / parameter emulation / simulation
- **Parameter emulation**: 실험은 'adjustable capacitor bank' 로 C 를 500–620 µF 10 µF 간격 13 수준으로 설정(각 값 LCR 측정); 시뮬은 Matlab/Simulink 에서 C 값 변경. 실제 가속 노화 없음. 온도 실험(30–75 °C 오븐)은 새 커패시터의 C(T) 특성 측정용.

#### 9. Aging sample 별 실제 capacitance
- 실험 13 수준(LCR @120 Hz): **512.50, 521.50, 530.61, 539.68, 548.73, 557.90, 566.96, 576.10, 584.75, 593.91, 603.12, 612.15, 620.85 µF**. 시뮬 학습: 400–500 µF 10 µF 간격 11 수준; 특징 분석: 300–500 µF 20 µF 간격 11 수준.

#### 10. Aging sample 별 실제 ESR
- ESR 값 NR (측정·변경하지 않음).

#### 11. External resistor Radd 값
- 해당 없음 (ESR 미변경).

#### 12. C only / ESR only / C+ESR simultaneous
- **C only**.

#### 13. 총 dataset sample 수
- 실험 학습: **975** (13 C × 15 부하 × 5 반복); 실험 테스트: 175 (7 C × 5 저항 부하 × 5 반복, 다른 날 수집) + testset-1 175 (L 6.25 mH) + testset-2 175 (L 12.5 mH). 시뮬 학습 165 (11 C × 15 부하), 테스트 10.

#### 14. Class 별 sample 수
Not reported (원문에 없음) (회귀)

#### 15. Train / validation / test split
- 학습 975 / 5-fold cross-validation(26 모델 비교) / 독립 테스트 175 (+175, +175). 명시적 validation 셋 대신 5-fold CV.

#### 16. Operating condition 종류
- 부하 15 종(순저항 5 × {R, R+6.25 mH, R+12.5 mH}); 테스트는 순저항 5 종 및 RL 2 종. 샘플링 주파수 50→2 kHz 다운샘플 실험. 온도 30–75 °C(커패시터 특성만). 변조지수·출력 주파수·fsw 변화 없음(개루프 고정).

#### 17. 실제 측정 신호
- **DC-link 전압 V_dc** 와 **출력 전류 I_out**(단상) — NI-USB-6221 DAQ 로 수집. 특징: F₁ = I_out,rms, F₂ = PSD₃₀₀(V_dc 리플 PSD 의 300 Hz 성분, 실험) / 시뮬에서는 PSD₃₀₀ 과 I_out,rms.

#### 18. 기존 inverter sensor 인지 추가 sensor 인지
- **기존 센서만**(보호·제어용 V_dc, I_out). 커패시터 전류 센서·필터 회로·주입 없음. 온도 보정용 NTC 서미스터는 제안(미구현).

#### 19. 직접 측정 신호 vs reconstructed signal
- 모두 직접 측정(재구성 없음). PSD 는 식 (1) P_x(k) = (1/N)|X(k)|² 로 계산.

#### 20. Sampling frequency
- **50 kHz** (샘플링 주기 20 µs). 다운샘플 실험: 25, 12.5, 10, 5, 2.5, 2 kHz → 5 kHz(250 점)까지 성능 유지, 2.5 kHz 에서 저하(Fig. 11).

#### 21. Window length / sample length
- **2500 점 = 0.05 s = 출력 60 Hz 3 주기** (I_out 3 주기와 대응하는 V_dc). 데이터 행렬 2500×975.

#### 22. 전처리 (normalization / filtering / segmentation / phase alignment)
- 필터링 없음(raw 데이터; PSD 가 잡음에 강건하다는 논리). 특징 F₁, F₂ 를 [0, 1] 로 재스케일. 창은 I_out 3 주기 기준으로 고정(랜덤 창 지양). 위상 정렬 언급 없음.

#### 23. Feature extraction (FFT / PSD / harmonic / STFT / Wavelet)
- PSD(DFT 기반, 식 (1)) 의 300 Hz 빈(6×50 Hz 입력 정류 리플) + I_out RMS. 후보 특징 V_dc,p2p, PSD₆₀, PSD₁₂₀ 은 PCC(식 (2)) 분석으로 제외(PSD₁₂₀ 은 출력 전류 변동에 민감, V_dc,p2p 는 잡음).

#### 24. 모델 또는 parameter estimation algorithm
- Matlab Regression Learner 26 모델 비교(5-fold CV). 실험 최종 **GPR(Matern 5/2 커널, constant basis)**; 시뮬 최종 medium NN(1 층 25 뉴런 ReLU, 1000 반복). 비교: SVM(fine Gaussian), wide NN(1×100), trilayer NN(3×10), bagged trees(min leaf 30, 8 learners), LR(interactions).

#### 25. AI: network architecture, input size, output, loss, optimizer
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

#### 26. 저자가 직접 주장하는 contribution / novelty
Authors' claimed contributions (1절):
1. **V_dc 리플의 PSD** 를 열화 특징으로 제안 — 측정 잡음에 강건해 추가 아날로그/디지털 필터 불필요; I_out,rms 와 결합하면 다양한 부하에서 C_link 고정밀 추정; 데이터 처리 일반화를 위해 **출력 전류 3 주기** 창 고정; 높은 샘플링 주파수 불필요.
2. 특정 운전 조건에 의존하지 않고, 정지 없이, 커패시터 전류 센서 없이, 기존 신호만으로, 주입 없이(IEEE 519 준수), 제어 알고리즘 수정 없이 동작.

#### 27. True Online / Quasi-Online / Offline
- **True Online**(측정 단계): 정상 운전 중 기존 신호만. 단 **추론은 오프라인**(3.I·결론: 'testing phase was conducted offline').

#### 28. 실제 on-board 구현 여부
- **No**(논의만): Matlab Coder 로 C 코드 ≈100 kB 생성 가능, LAUNCHXL-F28379D(1 MB flash, 204 kB RAM)에 적합, Goertzel 로 300 Hz PSD 추출, 수 분에 1회 실행 — 향후 과제.

#### 29. DSP / MCU / FPGA 모델
- 실험 수집: NI-USB-6221 DAQ + PC(Matlab). 제안 타깃(미구현): TI LAUNCHXL-F28379D (TMS320F28379D).

#### 30. Control frequency / inference time / execution time / memory
- 추론 시간·실행 시간 NR; 메모리: 모델 C 코드 ≈100 kB(미검증 추정). 실행 주기 제안: 수 분에 1회.

#### 31. Classification accuracy 또는 regression error
- 실험(GPR, Table IV): R² 검증/테스트 0.96/0.96, RMSE 7.18/7.07 µF, MAE 5.57/5.16 µF. testset-1(L 6.25 mH): 평균 0.8574 %, 최소 0.0142 %, 최대 5.048 %, R² 0.97; testset-2(12.5 mH): 평균 0.9048 %, 최소 0.0016 %, 최대 4.966 %, R² 0.96 → **MPE < 1 %**.
- 시뮬(NN, Table II/III): R² 0.99, RMSE 3.45 µF, MAE 2.42 µF; 10 테스트 오차 0.031–0.862 %(학습 범위 밖 380 µF: 2.316 %).
- 비교 모델(실험 테스트 RMSE µF): SVM 7.36, wide NN 7.59, trilayer NN 7.66, ensemble 8.04, LR 9.98.

#### 32. Load / speed / temperature / modulation 변화 robustness
- 부하: 15 조건 학습 + 미학습 RL 테스트에서 <1 %(강건). 샘플링: 5 kHz 까지 유지. 잡음: V_dc 평균 SNR ≈11 dB(Table V)에서도 동작. 온도: C(T) = 0.4382·T + 609.8 (R² 0.9987) 선형 보정식 제안(C_actual = C_link + a(T − 25 °C)). 속도·변조지수·fsw 변화 없음(개루프 고정). 학습 범위 밖 C 는 오차 증가(시뮬 2.3 %).

#### 33. 저자가 인정한 limitation
- 테스트는 오프라인 — 온라인 구현과 온도 효과 통합은 향후 과제(결론).
- PSD 지배 성분 위치가 변조 방식·출력/입력 주파수에 따라 달라져(시뮬 120 Hz vs 실험 60 Hz) 특징 라벨 전에 PSD 분석 필요(3.B절).
- 저주파 성분은 ESR 영향을 받지 않아 ESR 추정 불가(3.B절).
- V_dc 측정이 잡음(SNR ≈11 dB).

#### 34. 내가 보는 추가 limitation
- **단상 출력 H-bridge**, 70 V·수십 W 급 저전압 프로토타입 — 3상 2L 드라이브(수백 V, 수 kW)로의 일반화 미검증.
- 특징 PSD₃₀₀ 은 **입력 정류 리플(6f_in)** 이므로 다이오드 전단 구조 의존; AFE/배터리 입력에서는 같은 특징이 없음.
- C 범위 500–620 µF(−19 %)는 EoL 근방만, ESR 미포함, 실제 노화 커패시터 없음.
- 개루프 SPWM 고정 → 폐루프 전류 제어·변조지수 변화 시 PSD 변동 미검증.
- 온도 보정은 커패시터 특성 측정만, CM 루프 통합 실험 없음.

#### 35. MATLAB/Simulink 재현에 필요한 신호와 parameter
- 모델: 3상 50 Hz 전원 + L 0.4 mH + 다이오드 정류기 + C(500–625 µF) + (내 경우 3상 2L 인버터로 교체) + LC 필터 + R/RL 부하. 로그: v_dc, i_out(또는 3상 i_a,i_b,i_c) 50 kHz, 0.05 s 창(3 주기).
- 처리: 창 고정 → PSD(식 (1)) → 입력 정류 리플 빈(6f_in)·출력 고조파 빈 선택(PCC 로 검증) + I_rms → [0,1] 정규화 → GPR/NN 회귀. 스윕: C 13 수준(−19 %…0), 부하 15 조건, 5 반복, 테스트는 다른 날/미학습 부하.

#### 36. 실험 장치 구현에 필요한 sensor 와 hardware
- 센서: DC-link 전압 센서(절연, 잡음 대책), 출력 전류 센서(기존). DAQ 또는 MCU ADC ≥5 kHz(2 채널), NTC 서미스터(온도 보정 시).
- 하드웨어: 조정 가능한 커패시터 뱅크(10 µF 간격 13 수준), 저항·인덕터 부하 세트, LCR 미터(120 Hz 기준값), (온라인 구현 시) TMS320F28379D 급 DSP + Matlab Coder.

#### Aging Sample 표 (원문 값만)
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

#### 원문 결과표 요약
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

## 2.5 Park & Kwak 2023 JEET — DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs

> Evidence: Full text (PDF 원문 전체 확인, 2026-10-20)


#### 1. 정확한 제목, 저자, 연도, 저널, DOI, 저자 소속
- Title: DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs
- Authors: Hye-Jin Park, Sangshin Kwak (corresponding, sskwak@cau.ac.kr)
- Year / Journal: Journal of Electrical Engineering & Technology (KIEE/Springer), vol. 18, pp. 1841–1850, 2023 (received 7 Jun 2022, accepted 18 Aug 2022, published online 16 Feb 2023)
- DOI: 10.1007/s42835-023-01424-z
- 소속: School of Electrical and Electronics Engineering, Chung-Ang University, Seoul, Korea. 지원: NRF 2021M1A2A2060313, KIAT P0012453.

#### 2. 정확한 inverter topology
- **DC 전원 + 입력(DC-link) 커패시터 C + 3상 2-Level 인버터(IGBT 6개, Fig. 2(a)) + 3상 RL 부하**. 정류단 없음(DC 소스 직결).

#### 3. Power rating, DC-link voltage, switching frequency, load/motor, modulation
| 항목 | 값 (3절) |
|---|---|
| 입력(DC-link) 전압 | 100 V |
| 부하 | 3상 RL: R 10 Ω, L 10 mH (모터 아님) |
| 변조지수 | 0.3, 0.5, 0.8 (3 조건) |
| 스위칭 주파수 | 본문 수치 없음; '스위칭 주파수의 2배' 성분 = 10 kHz (Fig. 3) → **f_sw = 5 kHz** (분석자 역산) |
| 기본파 | '기본파 2배' 성분 = 360 Hz → **f₁ = 180 Hz** (분석자 역산) |
| 변조 방식 | NR (PWM) |
| Power rating | NR (100 V, 10 Ω 급 → 수백 W, 분석자 추정) |

#### 4. Capacitor 종류, 정격 C, 정격 전압, ESR
- 종류: 전해 커패시터 2종 — SAMXON **EKM226M2GI20RRSHP (22 µF)**, CHANG **RL2G101MM300Z35CE002 (100 µF)**; 정격 전압·정격 ESR NR(형명에서 추정 가능하나 원문 미기재).
- 병렬 조합으로 **25 쌍의 C/ESR**: 데이터시트 기준 122 µF → 650 µF (22 µF 간격), 각 값 LCR 미터로 측정. 측정 예: 106.92 µF / 490.83 mΩ (Test C 타깃, Fig. 7·8).

#### 5. 진단 task: classification / regression
- **Regression**: C 와 ESR 연속 추정(지도학습, 정답 = LCR 측정값).

#### 6. Classification 이면 class 수와 정의
- 해당 없음.

#### 7. Regression 이면 추정 대상(C / ESR / SOH)
- **C [µF] + ESR [mΩ]** (각각 별도 학습·평가).

#### 8. 노화 구현: 실제 aging / parameter emulation / simulation
- **Parameter emulation**: 커패시터 병렬 개수 조합으로 25 C/ESR 쌍 생성(병렬 수↓ → C↓·ESR↑, 노화 방향과 동일). 실제 노화 없음.

#### 9. Aging sample 별 실제 capacitance
- 데이터시트 기준 **122, 144, 166, …, 650 µF (22 µF 간격, 25 값)**; 실측값은 LCR 로 측정(개별 값 표는 없음; 예시 106.92 µF).

#### 10. Aging sample 별 실제 ESR
- Fig. 3 가로축 ESR [mΩ]: **103, 111, 121, 135, 155, 184, 229, 309, 490** (표시된 눈금; 25 쌍 전체 ESR 표는 없음). 예시 490.83 mΩ (Test C).

#### 11. External resistor Radd 값
- 해당 없음(직렬 저항 미사용; ESR 은 병렬 조합에 의해 결정).

#### 12. C only / ESR only / C+ESR simultaneous
- **C + ESR simultaneous** — 다만 병렬 조합이므로 C 와 ESR 이 **독립이 아니라 연동**(1 쌍 = 1 조합).

#### 13. 총 dataset sample 수
- 25 C/ESR 쌍 × 3 변조지수 = 75 조건. 조건당 파형/샘플 수 **NR**.

#### 14. Class 별 sample 수
Not reported (원문에 없음) (회귀)

#### 15. Train / validation / test split
- Test A: 전 범위(122–650 µF) 학습 = 테스트(학습 데이터 재사용). Test B: 전 범위 학습, 내부 미학습 값(386 µF 근방) 테스트. Test C: 범위 상단(386–650 µF) 학습, 하단(122 µF, 범위 밖) 테스트(Fig. 6(a)). Validation 셋 NR. Epoch ≈700 (Fig. 6(b)).

#### 16. Operating condition 종류
- 변조지수 0.3 / 0.5 / 0.8 만 변화. 부하·전압·온도·fsw 고정.

#### 17. 실제 측정 신호
- **커패시터 전압 v_C 와 커패시터 전류 i_C** (실험 파형, Fig. 2(d)(e)); 부하 상전압·상전류는 참고 파형만.

#### 18. 기존 inverter sensor 인지 추가 sensor 인지
- **추가 센서 필요**: 커패시터 전류 i_C 측정(제어용 기존 센서 아님). v_C 는 DC-link 전압 센서와 동일.

#### 19. 직접 측정 신호 vs reconstructed signal
- 모두 직접 측정(재구성 없음).

#### 20. Sampling frequency
Not reported (원문에 없음) (대역 8–125 kHz 사용 → ≥250 kHz 로 추정되나 원문 미기재)

#### 21. Window length / sample length
Not reported (원문에 없음) (FFT 창 길이·주기 수 미기재; Fig. 2 파형 50 ms)

#### 22. 전처리 (normalization / filtering / segmentation / phase alignment)
- MATLAB 에서 FFT 후 (a) 특정 성분의 최대값 추출, (b) 대역 분할(0–5 kHz, 8–125 kHz). 정규화·필터·세그먼트·위상 정렬 언급 없음.

#### 23. Feature extraction (FFT / PSD / harmonic / STFT / Wavelet)
- FFT. 특정 성분: 360 Hz(2f₁) 와 10 kHz(2f_sw) 의 v_C·i_C 진폭(각 대역의 최대값). 광대역: v_C, i_C 의 0–5 kHz(→ C), 8–125 kHz(→ ESR) 스펙트럼.
- 관찰(3.1절): v_C 저주파 성분은 ESR 과 선형 관계 없음; v_C 중주파 성분은 ESR 증가에 따라 감소(변조지수 클수록 기울기 큼); i_C 저·중주파 성분 모두 ESR 증가 시 감소.

#### 24. 모델 또는 parameter estimation algorithm
- DL 4종: DNN, CNN, Simple RNN, LSTM(지도 회귀). 입력 3 종: Input1 = {V_C,360Hz, i_C,360Hz, V_C,10kHz, i_C,10kHz}, Input2 = {V_C,10kHz, i_C,10kHz}, Input3 = {V_C 0–5 kHz, i_C 0–5 kHz (C 용); V_C 8–125 kHz, i_C 8–125 kHz (ESR 용)}. RNN 계열은 Input3 에서 미수행(수렴 불안정).

#### 25. AI: network architecture, input size, output, loss, optimizer
| Item | Information |
|---|---|
| Input | Input1: 4 스칼라 / Input2: 2 스칼라 / Input3: 대역 스펙트럼(차원 NR) |
| Input shape | NR (스칼라 4·2; 대역 벡터 길이 NR) |
| Preprocessing | FFT, 최대값 추출 또는 대역 분할 |
| Model | DNN(1 입력층·1 출력층·은닉층 다수), CNN(커널·풀링), Simple RNN, LSTM — 층 수·뉴런 수·커널 크기 NR('시행착오로 최적화') |
| Output | C [µF] 또는 ESR [mΩ] (별도 모델) |
| Loss | NR (training loss 곡선만, 12000→≈0, 700 epoch) |
| Optimizer | NR ; epoch·batch 는 데이터 수에 맞춰 조정(값 NR) |

#### 26. 저자가 직접 주장하는 contribution / novelty
Authors' claimed contributions (1절, 결론):
1. 같은 신호 성분의 **입력 형태(특정 성분 vs 광대역)에 따라 4 DL 알고리즘의 성능이 어떻게 달라지는지** 분석 — '알고리즘과 입력 데이터 유형' 조합 제시.
2. 저주파 성분은 C, 중주파 성분은 ESR 과 상관이 크다는 특성을 이용한 입력 설계.
3. 특정 성분 입력에는 DNN, 광대역 입력에는 CNN 이 적합; RNN 계열은 불안정.
4. 토폴로지에 제한되지 않는 추정 알고리즘 개발이 목적(2절).

#### 27. True Online / Quasi-Online / Offline
- **Offline**: 실험 파형을 수집해 MATLAB/DL 로 후처리. 온라인 운전 중 추정·구현 언급 없음. (신호 자체는 정상 운전 리플이므로 방법론상 True Online 으로 확장 가능 — 분석자 해석.)

#### 28. 실제 on-board 구현 여부
- **No**.

#### 29. DSP / MCU / FPGA 모델
Not reported (원문에 없음)

#### 30. Control frequency / inference time / execution time / memory
Not reported (원문에 없음) (학습 시간: CNN·RNN 은 길다고만 기술)

#### 31. Classification accuracy 또는 regression error
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

#### 32. Load / speed / temperature / modulation 변화 robustness
- 변조지수 0.3/0.5/0.8 를 학습·테스트에 모두 포함(Fig. 7·8 막대). 부하·속도·온도·fsw 변화 없음. 학습 범위 밖(Test C) 외삽 시 오차 1–7 % 로 증가.

#### 33. 저자가 인정한 limitation
- RNN 계열은 수렴 불안정, CNN 은 데이터량 증가로 학습 시간 김(4.3절).
- 향후: 다른 전압·전류 성분, 필터로 유도한 데이터 유형으로 정확도 개선(결론).

#### 34. 내가 보는 추가 limitation
- **커패시터 전류 센서 필요** → on-board·기존 센서 조건 불만족.
- 샘플링 주파수·창 길이·샘플 수·네트워크 구조·손실·옵티마이저 전부 미기재 → 재현 불가에 가까움.
- C 와 ESR 이 병렬 조합으로 연동 → 독립 변화(예: C 고정·ESR↑)에 대한 일반화 미검증; 단일 부하·단일 전압.
- 100 V·수백 W 저전압 실험, 모터 아님, 온라인·실시간 없음.
- Test A 는 학습 데이터 재평가라 성능 과대.

#### 35. MATLAB/Simulink 재현에 필요한 신호와 parameter
- 모델: DC 100 V + C(ESR) + 2L 인버터(5 kHz, f₁ 180 Hz 또는 내 조건) + RL 10 Ω/10 mH. 로그: v_C(=v_dc), i_C(검증; 내 연구는 재구성 전류로 대체), i_a,i_b,i_c, S_x. 샘플링 ≥250 kHz(8–125 kHz 대역 재현 시) 또는 내 fsw 기준 ≥10×fsw.
- 처리: FFT → 2f₁ 빈·2f_sw 빈 진폭(Input1) / 대역 벡터(Input3) → DNN(스칼라) 또는 1D-CNN(대역) 회귀 C·ESR. 스윕: C 25 수준(병렬 조합 또는 직접 설정) × ESR 독립(Radd 추가) × 변조지수 0.3/0.5/0.8 + 부하.

#### 36. 실험 장치 구현에 필요한 sensor 와 hardware
- 센서: DC-link 전압 센서, (논문 재현 시) 커패시터 전류 센서(고대역, ≥125 kHz), 상전류 센서 3개(재구성 대체 시).
- 하드웨어: 고속 DAQ/오실로스코프(≥250 kHz), 커패시터 뱅크(22 µF·100 µF 단위 병렬), LCR 미터, GPU/PC(학습). 온라인 구현 시 DSP 에 FFT 빈 2개 + 소형 DNN.

#### Aging Sample 표 (원문 값만)
| Aging Sample | C | C Change | ESR | ESR Change | Operating Condition | Label |
|---|---:|---:|---:|---:|---|---|
| P01 … P25 | 122 → 650 µF, 22 µF 간격 (데이터시트; 실측은 LCR, 개별값 NR) | 650 µF 기준 −81 % … 0 % | ≈490 → ≈103 mΩ (Fig. 3 눈금: 490, 309, 229, 184, 155, 135, 121, 111, 103) | 103 mΩ 기준 +376 % … 0 % | 변조지수 0.3 / 0.5 / 0.8, DC 100 V, RL 10 Ω/10 mH | 회귀 타깃 (C, ESR 각각) |
| Test C 타깃 예 | 106.92 µF (LCR 실측) | 범위 밖(학습 386–650) | 490.83 mΩ | 최대 | 〃 | 외삽 테스트 |
25 쌍의 개별 C/ESR 표는 원문에 없음(간격·범위·눈금만). % 변화는 범위 양끝 기준 분석자 계산. C↓ 와 ESR↑ 가 병렬 개수로 연동됨.

#### 원문 입력 정의 (Fig. 5)
- Input 1: V_C,360Hz, i_C,360Hz, V_C,10kHz, i_C,10kHz (저주파 + 중주파 특정 성분)
- Input 2: V_C,10kHz, i_C,10kHz (중주파만)
- Input 3: V_C 0–5 kHz, i_C 0–5 kHz (C 추정) / V_C 8–125 kHz, i_C 8–125 kHz (ESR 추정) — 광대역
- Test A: 학습 = 테스트 / Test B: 학습 범위 내부 미학습 값 / Test C: 학습 범위 밖(하단) 값

---
(이 파일은 `2level_top5_fulltext_comparison.md` 와 같은 원문 분석에서 생성됨. 이전 Abstract-level 워크시트의 선정 점수·Tier 는 `2level_inverter_dc_link_capacitor_onboard_top10.md` 5절 참조.)


---

## 3. 5편 전체 비교표

| Paper | Signal | Reconstructed Signal | Target | Classification/Regression | Aging Method | Extra Sensor | True Online | On-board HW | Performance |
|---|---|---|---|---|---|---|---|---|---|
| Ghadrdan 2022 TPEL | v_dc(HPF) + 출력 상전류·스위칭 패턴(실험은 i_inv 직접 측정) @100 kHz | Yes — i_inv = Σ S_x i_x (식 13); 실험 검증은 센서 측정 | DF = ω·C·ESR (결합), EUL 판정 | Regression 지표 + 이진 임계 | Emulation: 10 µF 병렬 5단계 × Radd 0/0.1/0.22/0.34 Ω (20 세트, RLC 측정) | No (제안); 실험은 i_inv 센서 | True Online | STM32H743ZI2 수집 → PC 처리(오프라인) | DF 각 오차 최대 5.6 % (<6 %) |
| Lipnicki & Lewandowski 2017 PED | U_DC + 정류측 3상 전류 + 스위칭 신호(영벡터 트리거) | Yes — I_DC = Σ S_xREC I_x (식 6), I_cap = I_REC − I_INV | ESR [Ω] (+C % 식 8, 임계 알람) | Regression (ESR) + 임계 | Emulation: 직렬 Radd 0/0.02/0.03/0.11/0.42 Ω (C 고정) | No | True Online (영벡터 구간) | ABB AC800PEC (PowerPC + Virtex-II FPGA) 리그; 알고리즘 실행 위치 미명시 | 시뮬 ±1 %/25 ms; 실험 최대 상대 오차 11 % |
| Hasegawa & Hirose 2024 TIA | v_C 만 (DC 블록 + 1300 Hz MA + FFT 360/720 Hz); P_O 는 기존 출력 전류 | Yes — i_C6, i_C12 를 V_S, L_ac, L_dc, P_O 의 정류기 모델로 계산 | C [µF] + ESR [mΩ] | Regression (C+ESR) | Emulation: C 1100/1000 µF × Radd 0/150 mΩ (4 조건) | No (전류 센서 0) | True Online (연속 도통 조건) | 오프라인 Excel FFT; MCU 구현 없음 | % 오차 표 없음; C 1000 µF → 904–941 µF, ESR +150 mΩ → +110~+170 mΩ 추적 |
| Örüklü & Ağalar 2025 TIE | V_dc + I_out(단상) @50 kHz, 3 주기(2500 점) → PSD₃₀₀ + I_out,rms | No | C_link [µF] | Regression (C) | Emulation: 조정 커패시터 뱅크 13 수준 500–620 µF (LCR 측정), ESR 미변경 | No | True Online 측정 / 추론 오프라인 | NI-USB-6221 + PC; F28379D 는 제안만 | GPR R² 0.96, RMSE 7.07 µF, MAE 5.16 µF; MPE 0.86–0.90 %, max ≈5 % |
| Park & Kwak 2023 JEET | v_C + **i_C(추가 센서)** FFT: 360 Hz·10 kHz 빈 또는 0–5 kHz / 8–125 kHz 대역 | No | C [µF] + ESR [mΩ] | Regression (C+ESR) | Emulation: 22/100 µF 전해 병렬 조합 25 쌍 (122–650 µF, ESR ≈490→103 mΩ, 연동) | Yes (i_C) | Offline (후처리) | 없음 (MATLAB/DL) | 평균 오차 C 0.19–1.20 % (DNN Input1), ESR 0.049–1.06 %; 범위 밖 최대 7.33 % |

### 3.1 실험 환경 비교
| Paper | Topology | Power / Vdc | fsw / f₁ / 변조 | Capacitor | Load / Operating points | Sampling / Window |
|---|---|---|---|---|---|---|
| Ghadrdan 2022 | 다이오드 정류기 + 2L 3상 인버터(B2B) | 1.2 kVA / 190 V·50 Hz 입력 / Vdc 260 V | 1 kHz (1–5 kHz 분석) | 235 µF / 200 mΩ 전해 | 3상 부하(종류 NR), 단일 운전점 | 100 kHz, 1000 점 ×20 평균 |
| Lipnicki 2017 | 2L AC/DC/AC (능동 정류 + 인버터; 다이오드 변형 포함) | NR (시뮬 15 kV 계통 견인; 실험 IM 리그) | NR | NR (ESR₁ 0.15 Ω 추정) | 시뮬 30 % 부하; 실험 IM 단일 | NR (영벡터 동기 창) |
| Hasegawa 2024 | 6-pulse 다이오드(L_ac+L_dc) + 2L 3상 PWM 인버터 | 1.2 kW / 200 V·60 Hz / Vdc 270 V | 10 kHz 캐리어, 출력 50 Hz | 1100 / 1000 µF 전해 (+150 mΩ) | RL 부하 1200/600 W; L_ac, L_dc 4 조합 | NR (Excel FFT) |
| Örüklü 2025 | 다이오드 정류기 + 단상 H-bridge 인버터 + LC 필터 | 50 VAC 입력 / 30 VAC 출력 / Vdc 70 V | 2 kHz, 출력 60 Hz, 개루프 SPWM | 625 µF 전해 (500–620 µF 뱅크) | R 41–71 Ω × {0, 6.25, 12.5 mH} = 15 조건 | 50 kHz, 2500 점(3 주기), 5 kHz 까지 유효 |
| Park & Kwak 2023 | DC 100 V + 2L 3상 인버터 + RL | NR / Vdc 100 V | 5 kHz(역산), f₁ 180 Hz(역산) | 22 µF·100 µF 전해 병렬 25 쌍 (122–650 µF) | 변조지수 0.3/0.5/0.8; RL 10 Ω/10 mH 고정 | NR |

### 3.2 Aging 데이터·데이터셋 비교
| Paper | Aging sample 구성 | 범위 | Split | C/ESR 변화 |
|---|---|---|---|---|
| Ghadrdan 2022 | C 5 × Radd 4 = 20 세트 (RLC 측정) | C 234.6→167.7 µF (−28 %), ESR 0.211→0.600 Ω (+184 %) | 해당 없음(모델) | C+ESR 동시 (전수 조합) |
| Lipnicki 2017 | Radd 5 수준 | ESR 0.15→0.57 Ω (기대), C 고정 | 해당 없음 | ESR only |
| Hasegawa 2024 | C 2 × Radd 2 = 4 조건 × 운전 5 | C 1100/1000 µF, Radd 150 mΩ | 해당 없음 | C+ESR 동시 (4 조합) |
| Örüklü 2025 | C 13 수준 × 15 부하 × 5 반복 = 975 (학습) | C 512.5→620.85 µF (−17.5 %), ESR 미변경 | 학습 975 / 5-fold CV / 테스트 175+175+175 | C only |
| Park & Kwak 2023 | C/ESR 25 쌍 × 3 변조지수 (샘플 수 NR) | C 122→650 µF, ESR ≈490→103 mΩ (연동) | Test A/B/C (범위 내/내부 미학습/범위 밖) | C+ESR (연동, 독립 아님) |

### 3.3 원문 비교에서 드러난 공통점·차이 (사실 → 해석)
- (사실) 5편 모두 **파라미터 모사**(커패시터 병렬 조합 또는 직렬 저항)이며 실제 노화 커패시터로 검증한 논문은 없다. Ghadrdan 은 가속 노화 18개 데이터를 지표 타당성(DF 증가)에만 썼다.
- (사실) ESR 모사는 전부 **직렬 저항 Radd**(0.02–0.42 Ω, 0.1–0.34 Ω, 150 mΩ); C 모사는 **병렬 개수**(10 µF, 22/100 µF 단위) 또는 조정 뱅크(10 µF 간격).
- (사실) 기존 센서만 쓴 것은 Ghadrdan(제안), Lipnicki, Hasegawa, Örüklü; Park & Kwak 는 i_C 센서 필요. 재구성(계산) 전류는 Ghadrdan(식 13, 실험 미검증)·Lipnicki(영벡터 창)·Hasegawa(정류기 모델).
- (사실) 온라인 **구현**은 Lipnicki(ABB PEC 리그, 실행 위치 불명)뿐이고, Ghadrdan(PC FFT)·Hasegawa(Excel)·Örüklü(PC Matlab, DSP 제안)·Park(후처리)는 오프라인 처리.
- (사실) 다중 운전조건: Örüklü(부하 15 + 미학습 부하, 샘플링, 잡음, 온도 특성), Hasegawa(L_ac/L_dc/P_O), Park(변조지수 3). Ghadrdan·Lipnicki 는 단일 운전점.
- (사실) C+ESR 동시 추정은 Hasegawa(해석적 2 주파수 연립), Park & Kwak(DL, 센서 추가). Örüklü 는 저주파 PSD 라 ESR 불가를 명시, Ghadrdan 은 DF 결합.
- (해석) **3상 2L 인버터 + DC 소스/AFE** 에서는 Örüklü·Hasegawa 가 쓰는 6f_in 정류 리플이 없고, DC-link 전압·커패시터 전류 리플은 **fsw 및 측대파가 지배**한다. 따라서 ESR 은 fsw 대역에서, C 는 fsw 대역의 1/(ωC) 항(ESR 과 비슷한 크기일 때만) 또는 저주파(6f₁, 과도)에서 얻어야 하며, Hasegawa 식 두 주파수 연립을 fsw·2fsw(또는 측대파)에 적용하는 것이 자연스럽다.
- (해석) Park & Kwak Fig. 3(d): v_C 의 2f_sw 성분이 ESR 증가에 따라 단조 증가 → **vdc 만으로도 ESR 정보가 fsw 대역에 존재**한다는 실험 근거. Örüklü 의 'ESR 불가' 는 저주파 PSD 한정.

---

## 4. 내 연구 방향 후보 A / B / C 비교 (5편 원문 근거)

| 기준 | A. 상전류+스위칭 상태 → 커패시터 전류 재구성 → C/ESR 회귀 | B. vdc 리플 FFT/PSD → ML 회귀 | C. 전류/전압 파형 → 시간-주파수 처리 → 경량 DL 분류/회귀 |
|---|---|---|---|
| Novelty 가능성 | **높음**: 재구성 전류를 쓴 Ghadrdan 은 DF 결합 지표(실험은 센서 측정), Lipnicki 는 영벡터 창 ESR 만 → '재구성 전류 스펙트럼(fsw·측대파·저주파 빈) → C·ESR 동시 회귀 + 운전점 정규화' 는 5편 어디에도 없음 | **낮음~중간**: Örüklü(TIE 2025)가 vdc PSD + I_rms → GPR 로 MPE <1 % 달성. 차별화는 3상 2L·DC/AFE 입력(6f_in 없음)·ESR 포함(fsw 대역)·폐루프 변조 변화 정도 | **중간~높음**: Park & Kwak 는 FFT 스칼라/대역 → DNN/CNN 비교까지; STFT/CWT 이미지·경량 모델·MCU 추론은 5편(및 저널 조사) 모두 없음. 단 신호처리 자체의 새로움은 제한적 |
| 필요한 센서 | 상전류 3 + vdc + 스위칭 상태(모두 기존). 검증용 i_C 센서 1(실험실) | vdc 1 (+출력 전류 rms, 기존) | 원파형 기준 vdc + 상전류(기존); Park 방식 그대로면 i_C 추가 |
| 구현 난이도 | **중~상**: PWM 동기 샘플링(Lipnicki 트리거), 데드타임·센서 대역(fsw 성분을 상전류 센서가 봐야 함), ESL(Ghadrdan: fsw ≤ cutoff/10), 필터 위상 보상(Ghadrdan) | **하**: Goertzel 빈 2–3개 + rms, 50 kHz→5 kHz 로도 동작(Örüklü) | **상**: 데이터량·모델 크기·MCU 추론·양자화; 학습 시간(Park: CNN 느림, RNN 불안정) |
| Dataset 구축 난이도 | **중**: Ghadrdan 식 C×Radd 격자(20 세트) + 운전점(부하·변조지수·fsw) 추가; 라벨은 RLC/LCR 측정 | **하~중**: Örüklü 식 C 뱅크 13 수준 × 부하 15 × 반복 5(975); ESR 추가하려면 Radd 격자 | **상**: 운전점 × 노화 × 반복의 파형 전체 저장(2500 점 이상/샘플), 일반화 위해 미학습 운전점 테스트 필수 |
| 실시간 on-board 가능성 | **높음**: 재구성은 곱·합, 빈 추출은 Goertzel; Lipnicki '큰 연산 불필요'. 제약: 샘플링 ≥10×fsw (Ghadrdan 100 kHz@1 kHz) | **매우 높음**: Örüklü 모델 C 코드 ≈100 kB, F28379D 적합, 수 분 1회 | **중**: 경량 1D-CNN 이면 가능하나 5편 중 시연 0; 2D 이미지 입력은 MCU 부담 |
| 기존 연구와 겹치는 정도 | **중**: Ghadrdan(fsw 성분, 출력 전류 계산), Lipnicki(재구성), Nguyen/Le/Lee 2015(고정자 전류 재구성). 대상(C+ESR 분리)·feature(스펙트럼 벡터)·검증(다중 운전점)이 다름 | **높음**: Örüklü 2025 + Soliman ANN 계열 + Al-Wesabi 2025. 3상·ESR 확장 없이는 증분 연구 | **중**: Park & Kwak(FFT→DL 비교), Dang/Machines(DWT+통계), EMI-CWT-SVM(학회). 경량·on-board 축은 비어 있음 |

### 4.1 추천 방향 (1~2개)

**1순위: A 를 주축으로 B 의 vdc fsw 빈을 결합한 하이브리드 (A+B)**
- 구성: 기존 센서(i_a,i_b,i_c, S_a,S_b,S_c, v_dc) → i_C,rec = i_inv − i_dc,in(DC 소스/AFE 측 전류는 Lipnicki 식 (10) 또는 소스 모델) → Goertzel 로 fsw, 2fsw(측대파 포함) 와 6f₁ 빈의 i_C·v_dc 진폭·위상 → 각 빈에서 Z_C = V/I → Hasegawa 식 2 주파수 연립(식 (22)(23)을 fsw·2fsw 에 적용)으로 **C, ESR 해석 초기 추정** → 운전점 변수(변조지수, I_rms, f₁, fsw, 온도)와 함께 GPR/소형 DNN 으로 잔차 보정·회귀(Örüklü 모델 선택 절차 차용).
- 왜 유망한가(근거): ① 재구성 전류의 실험 검증 자체가 Ghadrdan 에서 비어 있음(실험은 센서 측정) → 첫 기여. ② C+ESR 분리를 '인버터 스위칭 신호' 로 한 저널 논문이 없음(Hasegawa 는 정류 리플, Park 은 센서 추가). ③ Park Fig. 3(d) 가 vdc fsw 대역의 ESR 민감도를 실험으로 보여주므로 B 의 저비용 경로가 A 의 ESR 추정을 교차 검증한다. ④ Goertzel 빈 + GPR(≈100 kB) 은 Örüklü 가 DSP 적합성을 이미 계산 → on-board 시연까지 가면 조사 전체의 공백(G1, G7)을 메운다.
- 리스크와 대책: 상전류 센서의 fsw 대역 응답·샘플링 동기(Lipnicki 영벡터 트리거 또는 PWM 중앙 샘플링), ESL(fsw 를 cutoff 의 1/10 이하로, Ghadrdan Table III), 데드타임 보정(Park et al. 2025 Xplore 11184531 참고), 온도(Örüklü 선형 보정식 C(T), Ghadrdan 이 미해결로 남긴 DF 온도 의존).
- 데이터셋: Ghadrdan 식 C 5 × Radd 4 격자(원문 값 그대로 차용 가능: Radd 0/0.1/0.22/0.34 Ω) × 운전점(부하 3 × 변조지수 3 × fsw 2) × 반복 5 → 약 1800 샘플; 테스트는 미학습 운전점·다른 날(Örüklü 프로토콜).

**2순위: C 를 A 의 후속 단계로 — Goertzel 빈 벡터(또는 STFT 패치) → 경량 1D-CNN/DNN 회귀·등급 분류 + MCU 추론 시간 보고**
- 근거: Park & Kwak 결론(특정 빈엔 DNN, 광대역엔 CNN) 과 Örüklü(특징 2개로 충분)를 종합하면, 원파형 전체가 아니라 **수십 개 빈 벡터**가 경량·일반화에 유리하다. 5편 모두 on-board DL 추론이 없으므로 'TMS320F28379D 급에서 추론 시간·메모리 보고' 자체가 기여가 된다.
- 조건: A 에서 만든 같은 데이터셋을 쓰고, 분류 라벨은 EoL 기준(C −20 %, ESR ×2; 5편 공통 인용)으로 정상/초기/EoL 3 등급 + 회귀 병행.

**비추천: B 단독** — Örüklü 2025 와 구조가 같아 3상·ESR·폐루프 확장 없이는 신규성이 낮고, DC 소스/AFE 2L 인버터에서는 PSD₃₀₀(6f_in) 같은 저주파 지배 성분이 존재하지 않아 C 추정 경로가 약해진다(해석; Hasegawa 2.B절·Örüklü 3.B절 근거).

---

## 5. 다음 단계
1. `core_papers/2level_top10/` 의 5개 파일 35·36 항목대로 MATLAB/Simulink 모델 구성(다이오드 정류기 유무 두 버전) → 재구성 전류 vs 측정 i_C 스펙트럼 비교(Ghadrdan Fig. 9 재현).
2. Ghadrdan Table IX 격자(C 5 × Radd 4) + Örüklü 운전점 프로토콜로 데이터셋 설계서 작성.
3. 나머지 Top 10(Sundararajan 2018, Machines 2022, Zhao 2023, Al-Wesabi 2025, Liao 2020) PDF 확보 시 같은 36 항목으로 갱신.
