# 검증 코드 (원본 연구 코드 비수정)

| 파일 | 역할 |
|---|---|
| `capacitor_ai_validation_toolkit.py` | 원본 학습 코드의 함수(로딩·window·정규화·모델·학습·예측)를 import 해서 **평가 프로토콜만 바꿔** 실행: E1 원본 split 재현, E2 조건쌍 LOCO, E3 조건쌍 라벨 뒤집기, E4 조건만/진폭만/스펙트럼 모양 기준선, E5 잡음, E6 센서 이득, E7 seed 반복. 파일 단위 다수결·Wilson 95% CI·조건쌍 정답률 출력 |
| `synthetic_inverter_data.py` | 도구 자체 점검용 **합성** 데이터 생성기(원본 코드의 활성 파일 목록을 ast 로 읽어 같은 파일명으로 생성). 실측이 아님 |
| `extract_active_metadata.py` | 원본 코드 상단 리터럴에서 활성 파일·운전조건 표를 추출(모듈 import 없음) |

## 실측 데이터에서 실행하는 방법

```bash
# 필요: numpy pandas scikit-learn matplotlib joblib openpyxl (+ CNN/LSTM/MLP 는 tensorflow)
python -I capacitor_ai_validation_toolkit.py \
  --code  "<원본 ...train80.py 경로>" \
  --data-root "<tek*.txt 폴더>" \
  --out  "<결과 폴더>" \
  --models RF CNN --aux-models RFspec RFspec_shape \
  --combination A1 --experiments all --permutations 5 --seeds 5
```

- 출력: `validation_results.csv`(실험×모델×테스트셋 지표), `validation_summary.csv/.md`, `file_inventory.csv`(조건쌍 매칭 확인용).
- `--epochs` 를 주면 원본 `EPOCHS` 를 덮어쓴다(기본은 원본 값 15).
- 원본 파일은 읽기 전용으로 import 하며 `__pycache__` 를 만들지 않는다.
- 해석 우선순위: `file_majority_acc`·`case_pair_correct`(파일/조건쌍 단위) > window 정확도.

## 이 저장소에서 실행한 기록 (합성 데이터)

- 환경: Python 3.13, TensorFlow 2.21 / Keras 3.15, scikit-learn 1.9.1.
- `python -I synthetic_inverter_data.py --code <원본> --out <합성 폴더> --duration 1.0 --seed 1`
- `python -I capacitor_ai_validation_toolkit.py --code <원본> --data-root <합성 폴더> --out <결과> --models RF CNN --aux-models RFspec RFspec_shape --experiments all --permutations 3 --seeds 3`
- 결과: `../data/synthetic_validation_results.csv` — **합성 데이터의 메커니즘 예시이며 연구실 성능이 아니다.**
