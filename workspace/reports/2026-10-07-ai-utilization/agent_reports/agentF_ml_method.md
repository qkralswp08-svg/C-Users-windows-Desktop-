# Agent F — ML Methodology Review (실험 설계 타당성)

- 대상: `785d26be-_____train80.py` (3491행, 읽기만 함). `b81deba1-_____.py` 는 1907행까지 CRLF 차이 외에 **경로 3곳 + tek0172(2조건 case9 정상) 활성 여부만 다름**(diff로 확인: train80 판에서는 476–488행 주석 처리).
- 표기: **[확인]** 코드에서 직접 확인 / **[계산]** 코드의 파일 목록·상수로 손계산(스크립트 `agentF_calc.py`) / **[추정]** 해석·추론 / **[확인하지 못함]** 코드·데이터로 확인 불가.
- 실제 tek*.txt 데이터와 실행 결과(comparison_summary.xlsx 등)는 보지 못했다. 파일당 window 수, 실제 정확도 값은 모두 **확인하지 못함**.

---

## 0. 데이터 구성 요약 (현재 활성 설정, INTEGRATED_ALL) [확인]

| 구분 | 파일 (정상 / 노화) | (f0 Hz, fsw Hz, V1 V) | 근거 행 |
|---|---|---|---|
| Train fsw축 | 0228 / 0219 | (60, 14000, 100) | 910–939 |
| Train fsw축 | 0127 / 0135 | (60, 2000, 100) | 951–969 |
| Train f0축 | 0227 / 0220 | (90, 8000, 100) | 1052–1081 |
| Train f0축 | 0128 / 0133 | (30, 8000, 100) | 1093–1111 |
| Train V1축 | 0129 / 0132 | (60, 8000, 50) | 1192–1210 |
| Train V1축 | 0226 / 0223 | (60, 8000, 200) | 1215–1233 |
| Train R축 | 0225 / 0224 (R1) | (60, 8000, 100), R값 미기재 | 1295–1323 |
| Train R축 | 0138 / 0137 (R4) | (60, 8000, 100), R값 미기재 | 1337–1355 |
| Train 2조건 outer | 0163 / 0173 | (40, 4000, 100) | 112–138 |
| Train 2조건 outer | 0164 / 0174 | (40, 8000, 135) | 140–166 |
| Train 2조건 outer | 0165 / 0175 | (60, 4000, 135) | 168–194 |
| **Train 합계** | **22 파일 (정상 11 / 노화 11)**, 운전점(f0,fsw,V1) 고유값 10개 | | 2847–2849 |
| 1조건 Unseen | ref 0017/0041 (60,8000,100) · fsw3 0021/0045 (60,5000,100) · f0 0126/0134 (45,8000,100) · V1 0152/0161 (60,8000,125) · R3 0025/0033 (60,8000,100) | | 975–1034, 1158–1176, 1258–1276, 1401–1419 |
| 2조건 Unseen | case1 0153/0150, case7 0170/0180 (45,5000,100) · case2 0234/0237 (50,6000,100) · case3 0154/0151, case8 0171/0181 (45,8000,125) · case4 0146/0159 (50,8000,115) · case5 0143/0157, case9 **노화 0182만** (60,5000,125) · case6 0145/0160 (60,6000,115) | | 282–528 |
| 3조건 Unseen | 0166/0176 (50,6000,110) · 0167/0177 (50,7000,115) · 0168/0178 (45,6000,120) · 0169/0179 (45,5000,125) | | 783–895 |
| **Unseen 합계** | **35 파일 (정상 17 / 노화 18)** = 1조건 10 (5/5), 2조건 17 (8/9), 3조건 8 (4/4) | | [계산] |

- 학습 내부 분할: 각 학습 파일의 window 를 파일별 seed(`SPLIT_SEED + 파일번호`)로 섞어 70/20/10 (2074–2127, 2146–2186). window = 2048점 무중첩(1428–1430), 20.48 ms.
- 모든 학습 운전점은 정상 1파일 + 노화 1파일 쌍으로 구성 [확인]. 2/3조건 R=32 Ω, L=18 mH 기재(294–295 등). **1조건 4축 파일에는 R/L 수치가 없다** [확인: 1546–1574 는 R/L 을 파싱하지 않음].

---

## 1. 모델 비교 공정성

| # | 항목 | 판정 | 근거(행) | 내용 |
|---|---|---|---|---|
| F1 | 동일 split | **PASS** | 2843–2970, 2963–2966, 3314, 3327 | split/window 를 `prepare_shared_data` 에서 1회 생성, 배열 read-only freeze, SHA256 fingerprint 저장. 모든 모델·조합이 동일 TRAIN/VAL/TEST/Unseen 사용 [확인] |
| F2 | 동일 입력 신호 | **PASS(형식) / WARNING(표현)** | 2411–2430, 2740–2745 | Keras 와 RF 모두 같은 정규화 배열 사용. 단 RF 는 2048점을 그대로 flatten → 시계열 구조 미사용(F10) |
| F3 | 동일 정규화 | **PASS** | 2285–2346, 2973–2984 | 조합마다 TRAIN 만으로 z-score 재적합. ripple 은 전체 scalar mean/std 1쌍(axis=(0,1)) → window 간 진폭 차이 보존. scalar 는 feature별 z-score [확인] |
| F4 | Capacity | **WARNING** | 2394–2408, 2626–2667, 2695–2737, 76–81 | A1 기준 학습 파라미터: CNN ≈ 11.5k, LSTM ≈ 5.5k, MLP ≈ 271k, RF 200 full-depth tree [계산, §7]. MLP/CNN 약 24배, MLP/LSTM 약 50배 차이. 모델별 hyperparameter 탐색이 없어(고정 구조) "모델 계열" 비교가 아니라 "이 특정 설정끼리"의 비교다 |
| F5 | Inductive bias / 대역 | **WARNING** | 2710–2712, 1428 | LSTM 앞 `AveragePooling1D(4)` → 등가 25 kHz, Nyquist 12.5 kHz. AvgPool 이득 14 kHz 0.58(→11 kHz 로 alias), 16 kHz 0.47(→9 kHz), 28 kHz 0.12(→3 kHz) [계산]. fsw=8/14 kHz 계열 리플 고조파가 LSTM 에서는 감쇠·alias 됨 → LSTM 은 CNN/MLP/RF 와 **다른 대역의 정보**를 본다 |
| F6 | 위상 정렬 | **WARNING** | 2466–2471 | window 시작점은 샘플 수 기준, 기본파 위상과 무관. 20.48 ms = 기본파 0.61(30 Hz)–1.84(90 Hz) 주기 [계산]. CNN(GAP)은 shift-invariant, MLP·RF 는 위치 고정 가중치/임계값 → MLP·RF 에 구조적으로 불리 [추정] |
| F7 | 학습 budget | **WARNING** | 1444, 1448, 3005–3015 | EPOCHS=15, ES patience=10 → best val_loss epoch ≤5 일 때만 ES 발동. 대부분 15 epoch 를 끝까지 돈다 [계산]. `restore_best_weights=True` 이지만 **ES 미발동 시 best weight 복원 여부는 Keras 버전에 따라 다르다**(Keras 3 는 학습 종료 시 복원, tf.keras 2.x 일부 버전은 중단될 때만 복원) [추정, 버전 의존 — run_config.json 의 tensorflow_version(3477)으로 확인 필요]. 수렴 속도가 다른 LSTM(512 step 순환)에 15 epoch 이 충분한지 보장 없음 |
| F8 | Seed / 반복 | **FAIL(순위 주장 기준)** | 2679–2684, 2990, 2995, 1442 | `random`/`np`/`tf` seed=42 만 설정. `tf.config.experimental.enable_op_determinism()` 없음 → GPU 비결정성 가능. split seed 와 모델 init seed 가 같은 상수(42)에 묶여 있음. **반복 실행 없음** → 모델 간 차이와 seed 분산을 구분할 수 없음 |
| F9 | Class weighting | **WARNING** | 80, 2994, 3012–3015 | RF 는 `class_weight="balanced"`, Keras `fit` 에는 class_weight 없음. 파일 수는 11/11 로 균형 [확인]이지만 window 수 균형은 파일 길이에 달려 있음 [확인하지 못함 → dataset_info.json sample_counts 로 확인 가능]. 불균형이면 처리 방식이 비대칭 |
| F10 | Validation 사용 비대칭 | **WARNING** | 3005–3015, 2992–3001, 3216–3221 | Keras 는 VALIDATION 을 ES·ReduceLROnPlateau·best-weight 선택에 사용하고, RF 는 VALIDATION 을 전혀 쓰지 않음. 그런데 선정표는 모든 모델을 validation accuracy 로 비교 → Keras 의 validation 점수가 낙관적으로 편향됨(checkpoint selection bias) [추정] |
| F11 | RF 입력 표현 | **WARNING** | 2740–2745, 79 | z-score 된 raw 2048점(+scalar) flatten. `max_features="sqrt"` → split 마다 후보 45개, 특정 scalar 가 후보에 들 확률 ≈2.2% [계산] → **B1–B7 의 scalar 효과가 RF 에서는 거의 희석**됨 [추정]. 위상 비정렬 window 에서 샘플 위치별 임계값만 학습 → 주파수 구조 불가, 진폭 분포만 간접 포착 [추정]. tree 에 z-score 는 불필요(무해) |
| F12 | 조합별 구조 일관성 (MLP) | **WARNING** | 2730–2734 | MLP 는 A1(waveform 단독)일 때 fusion Dense(32)+Dropout 이 없고, A2/B 에서는 추가됨 → A1 vs B 비교에 "입력 추가"와 "층 추가"가 섞임. CNN(2651–2657)·LSTM(2731)은 항상 fusion 층 존재 |
| F13 | 정규화 기법 차이 | 참고 | 2396–2406, 2713–2723 | CNN: L2 1e-4 + BN + Dropout 0.3(fusion). LSTM: L2(kernel/recurrent), BN 없음, Dropout 0.3(fusion). MLP: L2 + BN + Dropout 0.3(각 은닉층). RF: 정규화 없음, 깊이 무제한 |
| F14 | 다중 비교 | **WARNING** | 3216–3227 | 9 조합 × 4 모델 = 36 run 중 validation 최대값 선택 → 선택된 조합의 validation 은 낙관 편향(winner's curse) |
| R | 권고 | **RECOMMENDATION** | — | (1) seed ≥5–10회 반복(init seed 와 split seed 분리, 결정론 옵션) → 평균±표준편차. (2) 모델별 동일 budget 의 소규모 hyperparameter 탐색(그룹 CV 기준) 또는 capacity 를 맞춘 변형(예: MLP 은닉 16/8, CNN 채널 ×2) 추가. (3) EPOCHS 를 충분히(예: 100) 두고 ES 가 실제로 작동하게. (4) Keras 도 동일 class_weight 사용 또는 window 수 균형 확인. (5) RF 는 raw 대신 특징 기반(ripple RMS·p2p·FFT 대역 에너지 fsw, 2fsw, 6f0 등) 버전을 공정한 고전 baseline 으로 추가 — `derived_window_features.csv` 에 ripple_rms_v/p2p 등이 이미 계산됨(2506–2512, 2555–2559). (6) LSTM 은 pool 1/2/4 ablation 으로 대역 손실 영향 분리 |

---

## 2. 평가 프로토콜

| # | 항목 | 판정 | 근거(행) | 내용 |
|---|---|---|---|---|
| E1 | Validation 정의 | **WARNING** | 2074–2127, 2168–2176 | 학습 파일과 **같은 녹화**에서 무작위로 뽑은 20% window. 인접 window(20.48 ms)는 같은 연속 캡처라 강한 상관 → validation 은 "녹화 내부 분리 가능성"만 측정. 일반화 지표가 아니다 [추정] |
| E2 | Internal TEST 정의 | **WARNING** | 2178–2186, 3350–3356 | VALIDATION 과 동일한 성격(같은 파일의 다른 10%)이라 정보가 거의 중복됨. "test" 라는 이름이 일반화 성능으로 오해될 위험 |
| E3 | 선정 로직 | **WARNING** | 3216–3227 | 정렬 키 = validation_accuracy ↓, input_count ↑, combination_id ↑, model ↑ → `drop_duplicates("model")`. validation 이 포화(≈100%)하면 동점 처리 규칙에 따라 **입력 수 최소(A1)·ID 사전순이 자동 선정** → 선정이 실질 정보를 담지 못함 [추정: 실제 값 확인하지 못함]. loss/F1/AUC 로 동점을 깨지 않음 |
| E4 | Unseen 역할 | **PASS(코드) / WARNING(연구 과정)** | 35, 3134–3147, 3214–3227 | 코드상 Unseen 은 ES·선정에 미사용 [확인]. 그러나 **파일 목록에 train↔test 를 바꾼 흔적**이 많다: 주석 처리된 2조건 TEST 목록(530–776)에 현재 outer TRAIN 인 0163/0173·0164/0174·0165/0175 가 test case 로 들어 있었고, 현재 2조건 TEST 인 0145/0160·0146/0159 는 주석 처리된 outer TRAIN 후보(196–279)였다. 또 다른 업로드 판에서는 tek0172 가 활성인데 train80 판에서는 제외됨(476–488). 변경 이유가 기록되지 않음 [확인하지 못함]. Unseen 결과를 보고 구성을 바꿨다면 Unseen 은 더 이상 깨끗한 test 가 아니다 (test-set reuse) |
| E5 | 지표 | **WARNING** | 3038, 3089–3108, 3102–3103 | 요약 지표는 accuracy 와 **weighted** precision/recall/F1. 노화 class 의 recall(놓침)과 정상 class 의 specificity(오경보)가 요약표에 따로 없다(classification_report JSON 에는 class 별 값이 있음). AUROC·calibration 없음(prob_aged 는 저장됨 3126–3127 → 사후 계산 가능) |
| E6 | window-level vs file-level | **FAIL(통계적 주장 기준)** | 3033–3047, 3104 | 모든 대표 지표가 window 단위다. 한 파일의 window 는 label·녹화 조건(커패시터 개체, 온도, probe, 세션)을 공유하므로 독립 표본이 아니다. 유효 표본 수 ≈ **파일 수**: Unseen 35(1조건 10, 2조건 17, 3조건 8), case 당 2(case9 는 1). design effect = 1+(m−1)ρ, 파일 내 예측이 거의 같으면 ρ≈1 [추정] |
| E7 | 통계적 유의성 | **FAIL** | (해당 코드 없음) | 신뢰구간, 반복 seed, paired test(McNemar 등) 없음. 파일 단위 Clopper–Pearson 95% 하한 [계산]: 35/35 전부 정답이어도 **90.0%**, 1조건 10/10 → 69.2%, 2조건 17/17 → 80.5%, 3조건 8/8 → 63.1%, case 하나(2/2) → 15.8%. 33/35 → 94.3% [80.8, 99.3]. 즉 현재 설계로는 "모델 A 가 B 보다 1–3%p 높다"를 입증할 수 없다 |
| E8 | Reference 반복 포함 | **WARNING** | 3049–3077, 975–1004 | reference(0017/0041)는 fsw축 unseen 으로 등록됐지만 축별 요약에서는 **모든 축에 반복 포함**. reference 운전점 (60,8000,100)은 R축 TRAIN 4파일과 scalar 가 동일 → f0/fsw/V1 관점에서 unseen 이 아니다(§3). 그래서 축별 성능이 서로 독립이 아니며, 축의 unseen 효과가 희석된다. `by_axis`(3045)에서도 fsw축 = fsw 5000 Hz + reference 가 섞임 |
| E9 | TOTAL_TEST / case mean | **WARNING** | 3134–3147, 3104–3106 | TOTAL_TEST 는 window 수 가중(파일 길이에 좌우). case_mean 은 case 동일 가중인데 **같은 운전점의 반복 녹화**(case1=case7, case3=case8, case5=case9)가 별개 case 라 해당 운전점이 2배 가중됨. case9 는 노화 파일만 있어서 case accuracy = 노화 recall |
| E10 | case 쌍 매칭 | **WARNING(경미)** | 1218, 1228, 2757–2781 | V1 TRAIN 의 `v_4_normal`(0226)과 `v_3_aged`(0223)는 이름이 달라 `_case_id` 가 다른 case 로 분리 → internal TEST case_mean/min 에서 단일 class case 2개가 생김 |
| E11 | 샘플링 검사 | **WARNING** | 1999–2005 | fs 가 명목값과 2% 넘게 달라도 경고만 출력. fs 가 다른 파일이 있으면 같은 2048점이 다른 시간 길이가 되어, 녹화 세션과 상관된 단서가 될 수 있다 [추정] |
| R | 권고 | **RECOMMENDATION** | — | (1) 대표 지표를 **파일 단위**(window 확률 평균 또는 다수결)로 바꾸고 k/n 와 Clopper–Pearson CI 를 함께 보고. (2) 노화 recall·정상 specificity·balanced accuracy·AUROC 를 요약표에 추가. (3) 모델 비교는 파일 단위 paired test(불일치 파일에 exact McNemar) 또는 case 단위 cluster bootstrap. (4) 선정은 학습 조건 안에서 leave-one-operating-point-out CV 평균(+1-SE rule)으로 하고, 동점은 val loss 로 깬다. (5) Unseen 구성을 최종 고정(lockbox)하고 제외 사유를 기록. (6) reference 는 "운전점은 학습에 있고 녹화만 새것"인 별도 범주로 분리해 보고 |

---

## 3. 일반화 설계 — 내삽/외삽

### 3.1 학습 값 집합 (outer TRAIN 포함) [확인]
- f0 ∈ {30, 40*, 60, 90} Hz · fsw ∈ {2000, 4000*, 8000, 14000} Hz · V1 ∈ {50, 100, 135*, 200} V (*는 outer TRAIN 에서만 나오는 값)
- scalar z-score(파일당 window 수가 같다고 가정한 근사) [계산]: mean ≈ (56.4 Hz, 7273 Hz, 110.9 V), std ≈ (14.9, 2988, 35.2). 학습 z 범위 f0 [−1.76, 2.25], fsw [−1.76, 2.25], V1 [−1.73, 2.53]. **모든 Unseen 의 |z| ≤ 0.76** → 주변(marginal) 외삽은 없다.

### 3.2 1조건 축

| 축 | 축 TRAIN 값 | 다른 축·outer TRAIN 의 값 | Unseen 값 | 축만 볼 때 | outer 포함 시 최근접 학습값 | 판정 |
|---|---|---|---|---|---|---|
| fsw | 2000, 14000 | 8000(f0/V1/R축), 4000(outer) | **5000** (0021/0045) | 내삽 (2000–14000) | 4000 (Δ1000, 25%) | 내삽. outer 4000 Hz 덕분에 간격이 좁아짐 |
| fsw | — | — | **8000** (reference 0017/0041) | — | 8000 그대로 학습에 있음 | **unseen 아님**(값이 학습에 있음) |
| f0 | 30, 90 | 60(다른 축), 40(outer) | **45** (0126/0134) | 내삽 (30–90) | 40 (Δ5 Hz) | 내삽, 간격 좁음 |
| V1 | 50, 200 | 100(다른 축), 135(outer) | **125** (0152/0161) | 내삽 (50–200) | 135 (Δ10 V) | 내삽, 간격 좁음 |
| R | "R1", "R4" (0225/0224, 0138/0137) | 2/3조건은 32 Ω | "R3" (0025/0033) | 수치 없음 | — | **확인하지 못함**. 주석은 "Train R1+R3, Unseen R2"(1282–1284)인데 이름은 R1/R4 TRAIN, R3 unseen → 번호가 R 크기 순서라면 내삽 [추정]. R 은 scalar 에 없어 모델 입장에서는 (60,8000,100)으로 학습 운전점과 같은 scalar |

### 3.3 2조건·3조건 (z 공간, outer 포함 학습 운전점 10개 기준) [계산]

| 그룹 | 운전점 (f0,fsw,V1) | 최근접 학습점 (z 거리) | 학습 convex hull 안? (outer 포함 / 축만) | 비고 |
|---|---|---|---|---|
| 2c case1·7 | (45, 5000, 100) | (40,4000,100) 0.47 | 안 / 안 | outer (40,4000,100)와 중심 (60,8000,100)을 잇는 선분 **위에 정확히** 있음 |
| 2c case2 | (50, 6000, 100) | (40,4000,100) 0.95 | 안 / 안 | 같은 선분 위에 정확히 있음 |
| 2c case3·8 | (45, 8000, 125) | (40,8000,135) 0.44 | 안 / 안 | (40,8000,135)–중심 선분 근처(선분 위라면 V1=126.25) |
| 2c case4 | (50, 8000, 115) | (60,8000,100) 0.79 | 안 / 안 | 같은 선분 근처(117.5) |
| 2c case5·9 | (60, 5000, 125) | (60,4000,135) 0.44 | 안 / 안 | (60,4000,135)–중심 선분 근처(126.25) |
| 2c case6 | (60, 6000, 115) | (60,8000,100) 0.79 | 안 / 안 | 같은 선분 근처(117.5) |
| 3c case1 | (50, 6000, 110) | (40,4000,100) 0.99 | 안 / 안 | |
| 3c case2 | (50, 7000, 115) | (60,8000,100) 0.86 | 안 / 안 | |
| 3c case3 | (45, 6000, 120) | (40,8000,135) 0.86 | 안 / **밖** | outer TRAIN 이 없으면 결합 공간에서 외삽 |
| 3c case4 | (45, 5000, 125) | (40,4000,100) 0.85 | 안 / **밖** | 위와 같음 |
| 1c ref / R3 | (60, 8000, 100) | 자기 자신 (0.00) | — | R축 TRAIN 4파일과 scalar 동일 |

**해석 [추정]**: 2조건 test 점들은 outer TRAIN 점과 중심점을 잇는 대각선 위나 근처에 놓여 있어, outer 3점이 2조건 test 를 감싸도록 설계된 것으로 보인다. 그래서 현재의 "2조건/3조건 unseen"은 **결합 공간 내삽** 시험이다. 논문에서는 "operating-condition shift 일반화"가 아니라 "학습 범위 안의 미학습 조합 내삽"이라고 써야 정확하다. 외삽 능력은 현재 설계로 측정되지 않는다.

### 3.4 INTEGRATED_ALL 교차 오염 점검

| 항목 | 판정 | 근거 |
|---|---|---|
| 파일 경로 중복(train↔unseen, unseen 그룹 간) | **PASS** | `collect_metadata` 중복 검사(1836–1910), `validate_metadata_splits`(2824–2840). 활성 tek 번호도 모두 서로 다름 [계산] |
| reference·R3 unseen 의 scalar = R축 TRAIN scalar | **WARNING** | (60,8000,100) 동일. B1–B7 모델에서는 학습 운전점과 구분되지 않음 |
| 한 축의 unseen 값이 다른 축 TRAIN 에 있음 | **WARNING** | fsw=8000(reference)이 f0/V1/R축과 outer TRAIN 에 있음. f0=60, V1=100 도 마찬가지 |
| outer TRAIN 이 1조건 축의 간격을 좁힘 | **WARNING** | 45 Hz↔40 Hz, 5000↔4000 Hz, 125↔135 V. outer 는 두 조건을 동시에 바꾼 파일인데, 1조건 성능 일부가 이 파일들 덕분일 수 있음 (ENABLE_TWO_CONDITION_OUTER_TRAIN=True, 104행, 모든 실험에 적용) |
| 측정 세션 중첩 [추정: tek 번호 = 저장 순서라고 가정] | **WARNING** | 3조건 정상 0166–0169 은 outer TRAIN 정상 0163–0165 직후, 3조건 노화 0176–0179 은 outer TRAIN 노화 0173–0175 직후. 2조건 case7/8/9(0170/0171, 0180–0182)도 같은 블록. 반대로 1조건 ref/fsw/R unseen(tek0017–0045)은 학습 파일이 하나도 없는 세션 → 1조건 test 에는 "조건 변화"와 "세션 변화"가 섞여 있음 |

---

## 4. 운전조건 scalar 입력(B1–B7)의 방법론적 의미

1. **label 과의 독립성 — PASS(조건부)**: 학습 운전점 11쌍 모두 정상 1 + 노화 1 [확인]. 그래서 scalar 만으로는 학습 label 을 맞힐 수 없다(P=0.5). scalar 를 통한 직접 shortcut 은 구조적으로 막혀 있다. 단 window 수가 파일마다 다르면 약한 불균형이 생긴다 [확인하지 못함].
2. **실제 역할 = 조건부 임계값(interaction)**: ripple 진폭은 전역 z-score 후에도 보존된다(2302–2304, 2036–2037). 노화(C↓·ESR↑)와 운전조건(V1·부하·fsw) 모두 진폭을 바꾸므로, scalar 는 "이 조건에서 진폭이 이 정도면 노화"라는 **조건별 기준선**을 주는 역할을 한다 [추정]. 학습 scalar 점이 10개뿐이라 네트워크가 점별 임계값을 외우는(lookup) 형태가 되기 쉽다. 그러면 미학습 조합에서의 기준선은 Dense(16) 보간의 매끄러움에 좌우된다 [추정].
3. **외삽 문제**: 현재 unseen 은 z 범위 안이고 outer 포함 시 모두 hull 안 → 정규화 후 외삽은 **현재 설계에서는 발생하지 않는다** [계산]. outer TRAIN 을 빼면 3조건 case3·4 는 hull 밖이 된다. 경계값(f0=30/90, fsw=2000/14000, V1=50/200)을 빼는 LOCO 에서야 외삽 문제가 드러난다.
4. **배포 시 의미**: scalar 는 metadata 의 명목 설정값이지 측정값이 아니다(2514–2518). 실제 장비에서는 제어기 지령값을 써야 하고, 설정값과 실제 운전점이 다르면 기준선이 어긋난다. R/L 은 scalar 에 없으므로 부하 변화에는 scalar 가 도움이 되지 않는다(R축 unseen).
5. **RF 에서는 희석**: F11 참조. RF 에서 B1–B7 과 A1 의 차이가 작게 나온다면, scalar 가 쓸모없어서가 아니라 RF 구조 때문일 수 있다 [추정].
6. **검증 권고**: test 때 scalar 를 무작위로 섞어 넣는 *scalar-shuffle test* → 정확도가 떨어지면 scalar 를 실제로 쓰는 것이다. condition-only baseline(§5 추가 실험 B)이 50% 근처인지 확인.

---

## 5. 실험 설계 (이 코드의 파일·조건 기준)

공통: 모든 실험은 **파일 단위 지표**(확률 평균 → 판정, k/n, Clopper–Pearson 95% CI), 노화 recall·정상 specificity·balanced accuracy·AUROC 를 보고하고, seed 를 5회 이상 반복(평균±SD)한다. window-level accuracy 는 보조로만 쓴다.

| Exp | 목적 | 학습 데이터 | 테스트 데이터 | 평가지표 | 기대 결과 [추정] | 의미 |
|---|---|---|---|---|---|---|
| **1** Same-condition random split | 상한(sanity)과 시간 자기상관 누수 크기 측정 | 22 TRAIN 파일의 window 70% (현행) + 변형: **시간 블록 분할**(앞 70% / 1 window gap / 20% / gap / 10%) | 같은 파일의 10% (현행 internal TEST) | window acc, 파일별 acc | random ≈ 100%, blocked 는 같거나 약간 낮음 | 녹화 내부에서 분리 가능하다는 것만 보여 줌. random−blocked 차이가 크면 인접 window 누수 |
| **2** File-level holdout (같은 운전점, 다른 녹화) | 녹화 간 변동만 분리 | 22 TRAIN + 반복 녹화 쌍의 한쪽: case1(0153/0150), case3(0154/0151), case5(0143/0157), ref(0017/0041) | 다른 쪽: case7(0170/0180), case8(0171/0181), case9(0182, 정상 0172 사용 가능 여부 확인), 주석 처리된 0018/0042(존재 여부 확인하지 못함). 역할을 바꿔 2-fold | 파일 acc + CI, 파일별 mean P(aged), 반복 녹화 간 예측 일치도 | Exp1 보다 낮음. 큰 하락은 녹화 고유 단서(세션·offset·온도) 의존 신호 | 조건 변화와 녹화 변화를 분리. 현재 unseen 결과 해석의 기준점 |
| **3** Operating-condition holdout (1조건) | 축별 미학습 값 내삽 능력 | (a) 축 TRAIN 16파일만(ENABLE_TWO_CONDITION_OUTER_TRAIN=False) (b) 22파일(현행) | 1조건 unseen 8파일(fsw 5000, f0 45, V1 125, R3). **reference 는 별도 보고** | 축별 파일 acc + CI, (a)−(b) 차이 | (b) ≥ (a) | outer TRAIN 기여량을 정량화. "1조건 일반화" 주장의 순수 근거는 (a) |
| **4** Leave-one-condition-out | 조건별 일반화 성능의 분포와 외삽 | 전체 57파일(22 TRAIN + 35 unseen)을 운전점(f0,fsw,V1,R/L) 그룹으로 묶음(약 26그룹 [계산 근사]). 그룹 하나씩 빼고 학습(inner val 도 그룹 단위) | 빠진 그룹의 정상/노화 쌍. 추가로 **경계값 fold**: f0=30, f0=90, fsw=2000, fsw=14000, V1=50, V1=200 각각 제외 → 외삽 | fold별 파일 acc, 평균±SD, worst-fold, "학습점까지 z 거리 vs 정확도" 곡선 | 내부 fold 는 높고 경계 fold 는 낮음 | 단일 숫자 대신 분포로 일반화를 주장할 수 있음. 내삽/외삽을 실제로 구분해 측정 |
| **5** Two-condition shift | 결합 변화 일반화 | (a) 22파일(현행) (b) 축 TRAIN 16파일만 (c) 역할 교대: 16 + 2조건 test 쌍으로 학습 → outer 3쌍(0163/0173, 0164/0174, 0165/0175)을 test | 2조건 17파일 (c 는 outer 6파일) | case·파일 acc, 반복 녹화(case1↔7, 3↔8, 5↔9) 일치도 | (a) > (b). (c) 는 경계 쪽이라 더 낮음 | 2조건 성능이 진짜 결합 일반화인지, outer 점 근처 내삽인지 구분 |
| **6** Three-condition shift | 3조건 동시 변화 | (a) 22파일 (b) 16파일(case3·4 가 hull 밖이 됨) (c) 세션 통제: outer TRAIN 을 같은 세션이 아닌 파일로 대체(가능하면) | 3조건 8파일 | 파일 acc, hull 안/밖 층화 | (b) 의 case3·4 하락 [추정] | 3조건 결과가 세션 공유(tek 블록)나 outer 근접성 덕분인지 확인 |
| **7** Noise robustness | 측정 잡음 강건성 | clean 학습(현행) / 잡음 증강 학습 | unseen 35파일 + internal TEST 의 **raw ripple 에** (전처리 전) AWGN SNR 40/30/20/10 dB(window RMS 기준), 1/f 잡음, ADC 양자화(8/10/12 bit 모사). 잡음 seed 5회 | 파일 acc·AUROC vs SNR, 노화 recall 변화 | CNN(GAP)이 MLP/RF 보다 완만하게 저하 | edge ADC·현장 잡음에서의 운용 한계 |
| **8** Sensor gain/offset 오차 | 센서 이득·오프셋·샘플링 오차 민감도 | clean 학습 / gain 증강 학습 | raw ripple 에 gain g ∈ {0.8, 0.9, 0.95, 1.05, 1.1, 1.2}, DC offset(창별 평균 제거 2037 → 영향 0 이어야 함: sanity), 느린 drift, fs ±1–2% 재표본(FS_TOLERANCE_RATIO=0.02), A2 는 상전류 gain 따로 | acc vs g 곡선, 판정이 뒤집히는 g, g>1 오경보 / g<1 놓침 | 진폭이 보존되므로 gain 에 민감할 것. ±10% 에서 뒤집히면 사실상 진폭 임계값 분류기 | 센서 공차 요구사항 도출. 민감하면 ripple/상전류 비 같은 무차원 특징이나 정상 상태 보정이 필요 |
| **9** Different capacitor sample | 노화 진단 vs 개체 식별 | 커패시터 개체 ID 별 그룹 분할. 정상 ≥3, 노화 ≥3 개체(또는 C −10/−20%, ESR ×1.5/×2 단계). leave-one-capacitor-out | 미학습 개체 쌍을 대표 운전점 (60,8000,100), (45,5000,100), (50,6000,110)에서 측정 | 개체별 파일 acc, P(aged) vs LCR 측정 C/ESR 상관 | 개체 고유 단서에 의존했다면 크게 하락 | 코드에 개체 ID 가 없음 → **현재 개체 수 확인하지 못함**. 정상·노화가 각 1개체면 현재 결과는 "두 개체 구별"이라 노화 진단 주장의 필수 실험 |
| **10** Different hardware/inverter | 장치 간 이전성 | 현 장비 전체 | 다른 인버터·DC-link 보드·probe·scope(fs, AC coupling 다름). zero-shot → 정상 데이터만으로 재정규화 → few-shot(정상/노화 각 1파일) | 파일 acc, AUROC, ECE, 필요한 target 데이터 양 | zero-shot 하락, 정상 데이터 재정규화로 일부 회복 | 제품·edge 적용성. 정규화 통계(preprocessor.npz)가 장비마다 다를 때의 영향 |
| **A** Label-permutation test | 누수·파이프라인 오류 검출, 귀무분포 확보 | TRAIN 22파일의 label 을 **파일 단위**로 섞음(같은 운전점 쌍 안에서 무작위 교환 → 조건 균형 유지). RF K≈200, Keras K≈20–30 반복. 보조로 window 단위 permutation | internal VAL/TEST, unseen 35파일 | 실제 unseen 파일 acc 의 p-value = (1+#null≥obs)/(K+1) | 파일 단위 permutation 에서도 internal VAL/TEST 는 높게 남을 것(같은 파일 window 를 외우므로). unseen ≈ 50%. unseen 이 50%보다 확연히 높으면 누수 | internal VAL/TEST 가 노화가 아니라 "파일 식별"을 재는지 직접 보여 줌 |
| **B** Condition-only baseline | scalar shortcut 검출 | 입력 = (f0, fsw, V1) [+R/L 이 있으면] 만. logistic / RF / kNN | VAL/TEST/unseen | 파일 acc | ≈50% (학습 쌍이 균형이므로). 벗어나면 window 수 불균형이나 다른 confound | B1–B7 해석의 전제 확인. **추가 권장**: "진폭 + 조건" baseline (ripple_rms_v, ripple_peak_to_peak_v, ripple_std_v + scalar → logistic, derived_window_features.csv 사용). CNN 과 비슷하면 딥러닝의 이득은 진폭 임계값 이상이 아님 |
| **C** Measurement-order baseline | 세션·drift confound 검출 | 입력 = tek 번호(정수), 또는 세션 블록 ID(00xx / 012x–013x / 014x–018x / 022x–023x). 1-NN / logistic | unseen 35파일 | 파일 acc | 코드 목록만으로 계산한 tek 1-NN 예시 [계산]: 1조건 6/10, 2조건 9/17, **3조건 7/8(+동점 1)**, 전체 22/35 | 전체적으로는 강한 예측자가 아니지만, 3조건 test 는 측정 순서만으로 거의 맞힐 수 있음 → 3조건 성능에서 세션 confound 를 배제하려면 Exp6(c)나 세션 단위 split 이 필요 |

---

## 6. 우선순위 권고 (요약)

1. **파일 단위 지표 + CI + 반복 seed** (E6/E7/F8). 이것 없이는 모델 순위와 조합 순위를 주장할 수 없다.
2. **커패시터 개체 수 확인과 Exp9**. 개체가 class 당 1개라면 모든 결과는 개체 식별일 수 있다.
3. **Exp2 + Exp-A**. internal VAL/TEST 가 일반화를 측정하지 않는다는 점을 정량적으로 보이고, 녹화 간 변동을 분리.
4. **outer TRAIN on/off (Exp3/5/6 의 a vs b)**. 1/2/3조건 "unseen" 성능 중 outer 근접 내삽이 기여한 몫을 분리.
5. **공정성 보정**: RF 특징 기반 버전, LSTM pool ablation, 동일 class weighting, 충분한 epoch, (가능하면) capacity 를 맞춘 변형.
6. Unseen 구성 고정(lockbox)과 변경 이력 기록. reference 는 별도 범주로 보고.

---

## 7. Table 3 용 — CNN / LSTM / MLP / RF 비교 (코드 기준)

파라미터 수는 손계산이다(Conv: k·Cin·Cout+Cout, BN: 4C 중 2C non-trainable, LSTM: 4·(u·(in+u)+u), Dense: in·out+out). TensorFlow 가 없어 `model.summary()` 로 대조하지는 못함. 실행 결과의 `model_summary.txt`(3019–3020)로 검증 가능.

| 항목 | CNN | LSTM | MLP | RF |
|---|---|---|---|---|
| 구조 (행) | Conv1D(16,k7,s1)-BN-LReLU → Conv1D(32,k5,s2)-BN-LReLU → Conv1D(64,k3,s2)-BN-LReLU → GAP → [scalar Dense16] → Dense32-LReLU-Dropout0.3 → Dense2 softmax (2394–2408, 2571–2667) | AvgPool1D(4) → LSTM(32, tanh) → [scalar Dense16] → Dense32-LReLU-Dropout0.3 → Dense2 (2708–2716, 2731–2735) | Flatten(2048) → Dense128-BN-LReLU-Drop0.3 → Dense64-BN-LReLU-Drop0.3 → (A1: 바로 Dense2 / 그 외: concat→Dense32-Drop0.3) → Dense2 (2717–2735) | RandomForest 200 trees, max_depth=None, max_features=sqrt, class_weight=balanced, random_state=42 (76–81, 2993–2995) |
| 파라미터 수 [계산] | A1 **11,522** (BN non-trainable 224) · A2 22,946 · B1 12,066 · B7 12,098 | A1 **5,474** · A2 10,850 · B1 6,018 · B7 6,050 | A1 **271,426** (BN non-trainable 384) · A2 546,786 · B1 273,986 · B7 274,018 | node 수는 학습 window 수에 비례 [확인하지 못함: window 수 미상] |
| 연산량/window [계산] | ≈6.0 M MAC (conv 3층) | ≈2.16 M MAC, 512 step **순차** | ≈0.27 M MAC | tree 200개 × 깊이만큼 비교 (깊이 미상) |
| 입력 형태 | (2048,1) waveform(+상전류 branch) + (k,) scalar | (2048,1) → pool 후 (512,1) | (2048,1) flatten | 2048(·2) + k 차원 벡터 |
| 정규화 | TRAIN-only global z-score(waveform 1쌍, scalar feature별), 창별 DC 제거 (2285–2346, 2037) | 같음 | 같음 | 같음(트리에는 불필요하지만 무해) |
| 학습 설정 | Adam 1e-3, batch 32, EPOCHS 15, ES(val_loss, p=10, restore), RLROP(×0.5, p=4), L2 1e-4, class_weight 없음 (1444–1450, 3003–3015) | 같음 + recurrent L2 | 같음 | validation 미사용, 1회 fit |
| 수용영역/대역 | 수용영역 **15 샘플 = 0.15 ms** [계산] → 국소 filter bank + 전역 평균. 위상 불변, 진폭 민감 [추정] | 등가 fs 25 kHz, 12.5 kHz 이상 감쇠·alias (14 kHz→11 kHz, 이득 0.58) [계산] | 2048점 전체를 보지만 위치 고정 가중치 | 샘플 위치별 임계값 |
| 장점 | 파라미터 적음, 이동 불변(GAP)이라 위상 비정렬 window 에 맞음, 학습된 대역 에너지 특징 [추정] | 파라미터 최소, 순서 정보 | 구현 단순, 연산량 최소 | 튜닝 거의 불필요, 빠른 학습, 특징 중요도 확인 가능 |
| 단점/리스크 | 수용영역이 짧아 기본파(16–33 ms)·저 fsw 주기(0.5 ms)를 직접 보지 못함. 진폭 의존 → gain 오차에 민감 [추정] | 고주파 리플 손실·alias, 512 step BPTT 로 수렴이 느림, 15 epoch 부족 가능성 [추정] | 파라미터/표본 비가 큼 → 과적합, 위상 변화 학습에 데이터 필요, A1 만 구조가 다름(F12) | 주파수 구조를 못 봄, scalar 희석(≈2.2%/split), 깊이 무제한 → 모델 크기 큼 [추정] |
| Edge 적합성 | **높음** [추정]: 약 45 KB(float32)/약 12 KB(int8), TFLite 변환 경로 있음(3162–3171), 6 MMAC/20.48 ms | **중간–낮음**: 파라미터는 작지만 TFLite 변환에 `SELECT_TF_OPS`(Flex) 필요(3165–3167) → MCU 용 TFLite Micro 에서 쓰기 어려움 [추정], 순차 연산이라 지연 | **중간**: 연산은 최소지만 가중치 약 1.06 MB(float32)/약 0.27 MB(int8) → 소형 MCU SRAM/Flash 부담 [추정] | **낮음–중간**: 코드에 TFLite 변환 없음(RF 는 joblib 만, 3154–3156). treelite/m2cgen 같은 별도 변환이 필요하고 [추정] full-depth 200 tree 는 MB 단위가 될 수 있음 [추정] |
| 이 비교에서의 공정성 메모 | 기준 모델. 다른 모델보다 대역·불변성 면에서 유리한 설계 | 대역 손실로 불리 | 위치 의존으로 불리, capacity 는 과다 | raw 입력이라 불리. 특징 기반 RF 를 추가해야 공정 |
