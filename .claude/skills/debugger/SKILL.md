---
name: debugger
description: MATLAB/Python 오류, 경고, NaN/Inf, 차원 불일치, 비정상적인 결과(예상과 다른 파형·스펙트럼·정확도)의 원인을 데이터 흐름·수식·dimension·logic 수준에서 추적하고 최소 수정안을 제시한다. Use when something errors, crashes, produces wrong or suspicious results, or the user asks to fix/debug code.
keywords: [오류, 에러, error, exception, traceback, 버그, bug, 디버그, debug, 디버깅, 고장, 안 돼, 안돼, 안됨, 작동 안, 실행 안, 이상해, 이상한, 비정상, 예상과 다, 값이 다르, 결과가 다르, 결과가 이상, nan, inf, dimension, 차원, 크기 불일치, mismatch, shape, index, 인덱스, 실패, fail, warning, 경고, 수정해, 고쳐, fix, 안 맞]
order: 50
combine-with: [project-analyzer, matlab-analyzer, python-analyzer, signal-analyzer]
---

# debugger

## 목적
오류 메시지를 없애는 데서 멈추지 않고 "왜 그 값/차원/흐름이 되었는가" 를 확인해 근본 원인을 고친다. 결과가 물리적으로 말이 되는지(예: 스펙트럼에 있어야 할 성분이 없음)도 디버깅 대상으로 본다.

## 언제 사용하는가
- 실행 오류/경고, NaN/Inf, dimension/shape 불일치, 인덱스 오류
- 비정상 결과: 파형이 이상, 고조파가 예상과 다름, CNN 정확도가 비정상적으로 높거나 낮음
- MATLAB↔Python 간 데이터 전달이 어긋남

## 절차
1. **재현 정보 수집**: 오류 전문(traceback), 실행한 명령/스크립트, 입력 파일, 최근 변경 사항, 기대 결과 vs 실제 결과. 사용자가 안 줬으면 필요한 것을 구체적으로 묻되, 코드에서 알 수 있는 것은 먼저 직접 확인한다.
2. **위치 특정**: 오류 라인에서 거꾸로 변수 정의를 따라간다 (`Grep`). 각 변수의 기대 shape/단위/범위를 적고 실제와 비교한다.
3. **원인 분류**: 데이터 흐름(잘못된 파일·변수·순서) / 수식(부호, 스케일, 단위) / dimension(행·열, 채널 순서, 1-based vs 0-based, column-major vs row-major) / logic(조건, 반복 범위, off-by-one, 정상상태 구간) / 환경(버전, 경로, 인코딩, 한글 경로).
4. **가설 검증**: 각 가설에 대해 확인 방법(추가 출력, 작은 입력으로 실행, 단위 테스트)을 제시한다. 실행이 가능하면 사용자 확인 후 최소한의 진단 실행만 한다.
5. **수정안**: 근본 원인을 고치는 최소 변경을 제시한다. 원본 동작을 바꾸는 부분은 영향 범위를 명시한다. 수정 후 확인 방법(회귀 체크)을 적는다.
6. 비정상 결과의 경우 물리적 타당성 검토를 `signal-analyzer` / 도메인 Skill 과 함께 수행한다 (계산 문제인지 모델 문제인지 분리).

## 출력 형식
- **증상** → **원인** (근거 파일:라인) → **영향** → **수정안** (diff 수준) → **검증 방법**
- 가설이 여러 개면 확률 순으로 나열하고 각각의 확인 방법

## 주의사항
- 오류 메시지만 보고 수정하지 않는다. 입력 데이터와 차원까지 확인한다.
- 파일 삭제, 덮어쓰기, 대규모 리팩토링, 의존성 대량 설치, git reset 은 하지 않는다. 필요하면 사용자에게 이유와 함께 제안만 한다.
- 수정은 사용자 확인 후 최소 범위로. 수정 전 원본 라인을 답변에 기록해 둔다.

## 다른 Skill과의 조합
- `project-analyzer`: 관련 파일 위치
- `matlab-analyzer` / `python-analyzer`: 언어별 상세 추적
- `signal-analyzer`: 결과의 물리적 타당성
