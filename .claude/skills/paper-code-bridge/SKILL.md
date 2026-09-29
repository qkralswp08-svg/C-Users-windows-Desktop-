---
name: paper-code-bridge
description: 논문의 수식·시스템 구조·알고리즘을 현재 프로젝트의 MATLAB/Python 코드와 대응시켜 같은 부분과 다른 부분, 그 차이가 결과에 미치는 영향, 그리고 CNN 입력 feature 로의 적용 가능성을 분석한다. Use when the user asks whether a paper's method matches or can be applied to the current code, or how to implement a paper's feature/signal in this project.
keywords: [내 코드, 현재 코드, 우리 코드, 내 matlab, 내 python, 내 연구, 코드와 비교, 코드를 비교, 코드와 같은지, 코드에 반영, 구현 가능, 구현할 수, 적용 가능, 적용할 수, 적용해, 논문 방법, 논문의 방법, 논문과 코드, 논문 기반, 현재 구현, cnn 입력으로, feature로, 특징으로, 재현, reproduce, 같은지 확인, 동일한지]
order: 46
combine-with: [paper-analyzer, matlab-analyzer, python-analyzer, capacitor-aging-expert, npc-inverter-expert]
---

# paper-code-bridge

## 목적
"논문에서는 이렇게 했고, 우리 코드는 이렇게 되어 있다" 를 변수·수식·조건 수준에서 1:1 로 맞춰 보고, 차이가 진단 결과(스펙트럼, feature, CNN 성능)에 어떤 영향을 줄지 설명한다. 수정은 제안까지만 하고 사용자 확인 후 진행한다.

## 언제 사용하는가
- "이 논문의 capacitor current 계산이 내 MATLAB 코드와 같은지 확인"
- "논문 방법을 CNN 입력 feature 로 쓸 수 있을지"
- "찾은 논문 방법과 내 코드 비교"

## 절차
1. **논문 측 정리**: `paper-analyzer` 결과(또는 직접 읽어) 시스템 구조, 핵심 수식(번호), 입력 신호 정의, 처리 단계, 조건(fs, fsw, 정격, 노화 모사)을 표로 만든다.
2. **코드 측 탐색**: `project-analyzer` / `matlab-analyzer` / `python-analyzer` 로 대응되는 변수·함수·수식을 찾는다. 파일:라인 을 기록한다.
3. **대응표**: 논문 기호 ↔ 코드 변수 ↔ 물리량 ↔ 단위 ↔ 정의 위치. 대응이 없는 항목은 "코드에 없음 / 논문에 없음".
4. **차이 분석**: 각 차이를 "정의 차이(부호·기준점) / 조건 차이(fs, 변조, 부하) / 처리 차이(창, 정규화, 구간) / 모델 차이(C·ESR 모사 방식)" 로 분류하고, 결과에 미칠 영향을 정성적으로(가능하면 크기 추정) 설명한다.
5. **적용 가능성**: 논문 feature 를 현재 파이프라인에 넣으려면 (a) 추가로 측정/저장할 신호, (b) MATLAB 에서 구현할 부분, (c) Python 전처리에서 구현할 부분, (d) CNN 입력 shape 변화, (e) 비교 실험 설계(기존 feature vs 새 feature, 조건 변화 시 강건성) 를 적는다.
6. **수정 제안**: 필요한 코드 변경을 최소 단위로 제안한다 (어느 파일의 어느 부분을, 왜, 어떻게). 실제 수정은 사용자 확인 후, 원본 로직을 보존하는 방식(새 함수/옵션 추가)을 우선한다.

## 출력 형식
- **대응표** (논문 ↔ 코드)
- **같은 점 / 다른 점 / 영향** 표
- **적용 계획**: 신호 → 구현 위치 → CNN 입력 → 실험 설계
- **수정 제안** (사용자 확인 필요 표시)
- 사실(코드·논문에서 확인) / 해석 / 추론 구분

## 주의사항
- 논문 수식을 코드에 옮길 때 단위·스케일(피크/RMS, 정규화)·부호 규약을 반드시 맞춘다.
- 논문 조건과 프로젝트 조건이 다르면 "그대로 적용 불가" 인지 "조정 후 적용 가능" 인지 구분한다.
- 연구 코드를 직접 수정하기 전에 문제·원인·영향·수정 방향을 먼저 보고한다.

## 다른 Skill과의 조합
- `paper-analyzer` (논문 측) + `matlab-analyzer`/`python-analyzer` (코드 측) 를 잇는 다리
- `capacitor-aging-expert` / `npc-inverter-expert`: 차이의 물리적 영향 판단
