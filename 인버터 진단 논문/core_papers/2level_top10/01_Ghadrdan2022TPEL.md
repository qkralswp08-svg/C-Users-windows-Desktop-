# 01. Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor
> Tier S · Rank 1 · **Evidence: Full text (PDF 원문 전체 확인, 2026-10-20)** — 이 파일은 2026-10-20 PDF 원문 36항목 분석으로 갱신됨(이전 Abstract-level 내용 대체). 수치는 원문 표·본문에 적힌 값만 기재했고, 없는 항목은 `Not reported (원문에 없음)`.

### 1. 정확한 제목, 저자, 연도, 저널, DOI, 저자 소속
- Title: Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor
- Authors: Moein Ghadrdan (Student Member, IEEE; corresponding), Saeed Peyghami (Member), Hossein Mokhtari (Senior Member), Frede Blaabjerg (Fellow)
- Year / Journal: IEEE Transactions on Power Electronics, vol. 37, no. 8, pp. 9733–9744, Aug. 2022 (received 11 Oct 2021, accepted 19 Feb 2022, published 25 Feb 2022)
- DOI: 10.1109/TPEL.2022.3153842
- 소속: Ghadrdan, Mokhtari — Center of Excellence in Power System Management and Control (CEPSMC), Dept. of Electrical Engineering, Sharif University of Technology, Tehran, Iran / Peyghami, Blaabjerg — AAU Energy, Aalborg University, Denmark. (Ghadrdan 은 2021-12 부터 AAU 방문 박사과정). 지원: REPEPS (Villum Foundation)

### 2. 정확한 inverter topology
- Back-to-back (AC/DC/AC) 컨버터. 실험·시뮬 모두 **전단은 다이오드 브리지 정류기**(Table VI, VIII 'Rectifier type: Diode based'), 후단은 3상 2-Level IGBT 인버터(Fig. 6 회로도: 레그당 스위치 2개) → 3상 부하.
- 즉 '전압형 2-Level 3상 인버터 + 다이오드 정류기 + 계통측 L 필터' 구조. 능동 정류기(AFE) 실험은 아님.

### 3. Power rating, DC-link voltage, switching frequency, load/motor, modulation
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

### 4. Capacitor 종류, 정격 C, 정격 전압, ESR
- 종류: 알루미늄 전해 커패시터(Al-Cap).
- 실험 DC-link 공칭값: **235 µF / 200 mΩ** (Table VIII). 정격 전압 NR.
- 실험 커패시터 뱅크는 '유사한 10 µF 커패시터 여러 개를 병렬' 로 구성(제조사·모델 NR).
- 수명 실측 데이터(2절): 560 µF / 35 V 전해 커패시터 18개, 35 V·리플 1.4 A@100 Hz·105 °C 에서 2500 h, Agilent E4980A 측정 → 2000 h 후 평균 C −4 %, ESR +35 %.

### 5. 진단 task: classification / regression
- **Regression 형(연속 지표)**: 손실각 δ 와 DF = tan δ 를 측정하고 DF/DF₀ > 1.6 (⇔ tan φ / tan φ₀ < 0.6) 을 EUL(End of Useful Life) 판정 기준으로 제안 → 최종 판정은 **이진 임계 판정**(Fig. 6 'Decision').

### 6. Classification 이면 class 수와 정의
- 학습 기반 분류 아님. 임계 판정은 2 상태(정상 / EUL). 기준: ESR ×2 & C −20 % 동시 → DF ×1.6 (식 (5), (12)).

### 7. Regression 이면 추정 대상(C / ESR / SOH)
- DF(= ω·C·ESR, 무차원) 와 커패시터 임피던스 각 φ / 손실각 δ. **C 와 ESR 을 개별로 출력하지 않음**(DF 는 결합 지표).

### 8. 노화 구현: 실제 aging / parameter emulation / simulation
- **Parameter emulation (실험)**: 10 µF 커패시터 병렬 개수로 C 를 5 단계, **직렬 저항 0 / 0.1 / 0.22 / 0.34 Ω** 으로 ESR 을 4 단계 → 20 조합, 각 조합의 C·ESR 를 RLC 미터로 측정(Table IX).
- 시뮬레이션: C −20 %, ESR +100 % 의 수명 말기 조건을 가정해 임피던스 각 변화 계산(Table III, IV, VII).
- 별도로 실제 가속 노화 데이터(18개, 2500 h)는 DF 지표 타당성 검증(2절)에만 사용, 모니터링 실험에는 미사용.

### 9. Aging sample 별 실제 capacitance
- Table IX 'C_RLCm' (µF): 234.6, 217.8, 201.5, 185.02, 168.68 / 235.3, 217.9, 201.2, 184.75, 168.47 / 234, 216.7, 199.98, 183.65, 167.48 / 234, 216.8, 200.2, 183.84, 167.72 (직렬 저항 그룹별 5개씩; 아래 표).

### 10. Aging sample 별 실제 ESR
- Table IX 'ESR_RLCm' (Ω, 직렬 저항 포함 RLC 미터 측정값): 0.211, 0.214, 0.221, 0.245, 0.271 (Radd 0) / 0.289, 0.302, 0.318, 0.337, 0.367 (Radd 0.1) / 0.427, 0.441, 0.459, 0.485, 0.514 (Radd 0.22) / 0.517, 0.53, 0.546, 0.569, 0.6 (Radd 0.34).

### 11. External resistor Radd 값
- **Radd = 0, 0.1, 0.22, 0.34 Ω** (본문 6절). Table IX 의 ESR 은 Radd 를 포함한 총 ESR 측정값.

### 12. C only / ESR only / C+ESR simultaneous
- **C + ESR simultaneous** — 5 C 단계 × 4 Radd 단계의 전수 조합(20 세트).

### 13. 총 dataset sample 수
- 모델 기반이라 학습 데이터셋 없음. 측정 세트 20개(각 세트 = 5 s 간격 20회 반복 측정 평균; 1회 = 100 kHz 1000 샘플).

### 14. Class 별 sample 수
Not reported (원문에 없음) (분류 아님)

### 15. Train / validation / test split
Not reported (원문에 없음) (학습 없음)

### 16. Operating condition 종류
- 스위칭 주파수 1/2/3/4/5 kHz 에서 전류 스펙트럼·위상차 측정(Fig. 9) → 본 측정은 1 kHz 단일.
- 부하·변조지수·온도 변화 실험 **없음**(단일 운전점). 라인 필터·ESL 영향은 해석/시뮬(Table III–V, VII).

### 17. 실제 측정 신호
- DC-link 전압 v_dc (전압 센서) → 1차 능동 HPF(차단 8.8 Hz) 로 DC 제거 → Fourier(대역통과) 로 스위칭 주파수 성분 v_C,sw.
- 인버터 입력 전류 i_inv: 실험에서는 **센서(LEM LA55-P)로 직접 측정**(센서 수를 줄이려고); 제안 방법은 출력 상전류 i_a,i_b,i_c 와 스위칭 패턴으로 계산(식 (13)).
- 추가로 커패시터 전류 i_C 를 측정해 스펙트럼 비교(Fig. 9, 검증용).

### 18. 기존 inverter sensor 인지 추가 sensor 인지
- 제안 방법 기준: **기존 센서만**(출력 상전류 + DC-link 전압; 상전류는 제어용으로 이미 측정됨 — 본문). 커패시터 직렬 전류 센서 불필요.
- 실험 셋업 기준: 인버터 입력 전류를 별도 전류 센서로 직접 측정 → 실험은 'Partially'.

### 19. 직접 측정 신호 vs reconstructed signal
- 직접 측정: v_dc, (실험) i_inv, (검증) i_C.
- Reconstructed: i_inv = S_a·i_a + S_b·i_b + S_c·i_c (식 (13); S_x = 상 x 상단 스위치 도통 시 1). 스위칭 주파수 등가회로(Fig. 6)에서 I_C,sw ≈ I_sw (계통 L 필터가 스위칭 고조파를 거의 차단; 식 (14)–(16), 위상차 θ_e 0.14°@1 kHz, 오차 <0.26 %, Table V).

### 20. Sampling frequency
- **100 kHz** (실험: 1000 샘플 배열을 100 kHz 로 수집 후 UART 로 PC 전송).

### 21. Window length / sample length
- 1000 샘플 = 10 ms 창(1 kHz 스위칭 10 주기). 5 s 간격 20회 반복 → 평균.

### 22. 전처리 (normalization / filtering / segmentation / phase alignment)
- v_dc: 1차 능동 HPF 8.8 Hz(DC 제거, 스위칭 주파수에서 위상 지연 없음) → 대역통과(FFT).
- i_inv: 대역통과(FFT) 로 스위칭 고조파 추출.
- 핵심 요구: 두 필터가 스위칭 주파수에서 위상 이동이 없거나 동일해야 함(본문 3절). 정규화·세그먼트·위상 정렬 명시 없음(반복 평균만).

### 23. Feature extraction (FFT / PSD / harmonic / STFT / Wavelet)
- FFT(대역통과 필터 역할) 로 v_C,sw, i_sw 추출 → 두 성분의 **시간 지연 t 측정** → φ = 지연각, δ = 90° − φ → DF = tan δ. Fig. 7: 1 kHz 에서 t ≈ 148 µs.

### 24. 모델 또는 parameter estimation algorithm
- 해석적 임피던스 각 측정법(Section III). 수식: DF = ESR·C·ω (3); φ = π/2 − atan(DF) (4); DF/DF₀ = (ESR/ESR₀)(C/C₀) (5); EUL: DF/DF₀ > 1.6 (12); i_inv 재구성 (13); 스위칭 등가회로 I_C,sw, I_N,sw (14)(15); θ_e = π/2 − atan((L_eq ω_s − 1/(Cω_s))/ESR) (16). 추정기(RLS 등) 없음.

### 25. AI: network architecture, input size, output, loss, optimizer
- 해당 없음(AI 아님).

### 26. 저자가 직접 주장하는 contribution / novelty
Authors' claimed contributions (1절 끝):
1. 커패시터 임피던스 각을 **스위칭 주파수에서** 측정해 각 측정 오차가 tan 계산 오차에 미치는 영향을 최소화.
2. DF 를 EUL 지표로 쓸 가능성 조사 + 검출 기준(DF/DF₀ > 1.6) 도입.
3. 스위칭 주파수에서 각을 측정함으로써 직렬 전류 센서 불필요(출력 전류로 커패시터 전류 계산).
결론 요약: 측정 주파수를 높여 DF 정확도 향상 / 출력 전류 기반 온라인 측정으로 추가 센서 제거 / 실험 최대 오차 <6 %.

### 27. True Online / Quasi-Online / Offline
- **True Online**: 정상 운전 중 스위칭 성분만 사용, 주입·시퀀스 없음. 단, 입력 전압에 스위칭 성분이 있으면 적용 불가(본문).

### 28. 실제 on-board 구현 여부
- **부분 구현**: MCU(STM32H743ZI2)가 ADC 수집·UART 전송, **FFT·위상·DF 계산은 PC 에서** 수행(본문 6절 '1000 samples … transmitted via UART to the computer'). Fig. 6 의 Processing Stage 는 구조도이며 MCU 내 실행 기록 없음.

### 29. DSP / MCU / FPGA 모델
- 처리장치 STM32H743ZI2 (Table VIII; ARM Cortex-M7 계열), 전류 센서 LA55-P, 전압 센서(모델 NR), RLC 미터(기준 측정).

### 30. Control frequency / inference time / execution time / memory
- 제어 주파수 NR / 실행 시간 NR / 메모리 NR. 측정 주기: 5 s 간격 20회.

### 31. Classification accuracy 또는 regression error
- Table IX: 20 세트의 임피던스 각 상대 오차 1 − tan(δ_m)/tan(δ_RLCm) = −0.056 ~ +0.055 → **최대 5.6 %**, 평균 약 2.6 %(표 값 평균, 분석자 계산). 수명 중 tan δ 는 약 60 % 증가 예상 → 오차는 기대 변화의 1/10 미만.
- 시뮬레이션(ESL+필터 포함, Table VII): 오차 0.32 %(1 kHz) ~ 9.60 %(5 kHz).

### 32. Load / speed / temperature / modulation 변화 robustness
- fsw: 1→5 kHz 로 가면 ESL 오차 0.13→4.16 %(Table III), 시간 지연 37→3 µs(Table IV) → **fsw 는 커패시터 cutoff 의 1/10 이하 권장**.
- 라인 필터: 오차 <0.26 %(Table V).
- 부하·속도·변조지수·온도 변화 실험 없음. 온도는 향후 과제로 명시.

### 33. 저자가 인정한 limitation
- DF 는 온도에 의존 → 온도 영향 연구와 온도 측정 기반 보정이 필요(결론).
- DF 수명 변화 범위를 정하는 통계 연구 필요(결론).
- 입력 전압에 스위칭 성분이 있으면 등가회로 무효(3절). 필터 위상 보상 필요(6절).
- ESL 영향 때문에 fsw 를 cutoff 보다 한 자릿수 낮게 선택해야 함(5절).

### 34. 내가 보는 추가 limitation
- DF 는 C·ESR 결합 지표 → 두 열화 메커니즘 분리 불가(내 목표 'C/ESR' 과 불일치).
- 실험은 i_inv 를 **센서로 직접 측정** — 식 (13) 재구성의 실험 검증(데드타임·샘플링 동기 오차)은 수행되지 않음.
- 단일 운전점(부하·변조지수 고정) → 조건 변화 강건성 미검증.
- 처리는 PC 오프라인(온라인 구현 미시연), 100 kHz 샘플링 요구는 저가 MCU 에 부담.
- 실험 C(235 µF/260 V)·fsw 1 kHz 는 산업 드라이브 대비 낮은 fsw — 2–20 kHz 드라이브에서는 ESL 오차 증가.

### 35. MATLAB/Simulink 재현에 필요한 신호와 parameter
- 모델: 다이오드 정류기 + L 필터(3.4–3.6 mH) + 전해 C(ESR, ESL 포함) + 2L 인버터 + 3상 부하. 로그 신호: i_a,i_b,i_c, S_a,S_b,S_c, v_dc, i_inv(검증), i_C(검증).
- 파라미터 스윕: C 235→168 µF 5단계, R_add 0/0.1/0.22/0.34 Ω, fsw 1–5 kHz, ESL 유무, 필터 L.
- 처리: HPF 8.8 Hz → FFT 대역통과 fsw 빈 → 위상차 → δ → DF, DF/DF₀ 추적. 재현 시 식 (13) 재구성 전류로 i_inv 를 대체해 재구성 오차를 별도 평가.

### 36. 실험 장치 구현에 필요한 sensor 와 hardware
- 센서: DC-link 전압 센서(HPF 포함 아날로그 프론트엔드), 출력 상전류 센서 3개(기존 제어용 LEM), 검증용 커패시터 전류 센서 1개(LA55-P 급).
- 제어기: STM32H7 급 MCU 또는 DSP(ADC ≥100 kHz 동시 샘플링 2채널 이상), 스위칭 상태 접근, UART/USB 로깅.
- 가변 커패시터 뱅크(10 µF 단위 병렬) + 직렬 저항(0.1/0.22/0.34 Ω), RLC 미터(기준값).

### Aging Sample 표 (원문 값만)
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

### 원문 수식 요약 (재현용)
- (3) DF = ESR·C·ω ; (4) φ = π/2 − atan(DF) ; (5) DF/DF₀ = (ESR/ESR₀)·(C/C₀) ; (12) EUL: DF/DF₀ = tan δ / tan δ₀ > 1.6 ⇔ tan φ / tan φ₀ < 0.6
- (13) i_inv = S_a i_a + S_b i_b + S_c i_c
- (14) I_C,sw = (R_eq + jL_eq ω_s) / ((R_eq+ESR) + j(L_eq ω_s − 1/(Cω_s))) · I_sw ; (15) I_N,sw = (ESR − j/(Cω_s)) / (…) · I_sw ; R_eq = 2R_Net, L_eq = 2L_Net
- (16) θ_e = π/2 − atan((L_eq ω_s − 1/(Cω_s)) / ESR) — 인버터 전류와 커패시터 전류 스위칭 성분의 위상차(1 kHz: 0.140° 계산, 1.021° 실측 → 5 kHz 0.023°)

### 원문 해석 표 (fsw 영향)
| fsw (kHz) | ESL 오차 % (Table III) | Δt µs (Table IV) | 필터 오차 % (Table V) | 시뮬 오차 % (Table VII) |
|---|---|---|---|---|
| 1 | 0.13 | 37.0 | 0.265 | 0.32 |
| 2 | 0.52 | 15.2 | 0.209 | 1.25 |
| 3 | 1.23 | 7.73 | 0.196 | 3.60 |
| 4 | 2.38 | 4.57 | 0.191 | 5.67 |
| 5 | 4.16 | 3.00 | 0.189 | 9.60 |

---
(이 파일은 `2level_top5_fulltext_comparison.md` 와 같은 원문 분석에서 생성됨. 이전 Abstract-level 워크시트의 선정 점수·Tier 는 `2level_inverter_dc_link_capacitor_onboard_top10.md` 5절 참조.)
