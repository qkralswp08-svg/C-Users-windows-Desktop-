---
name: python-analyzer
description: Python 코드(데이터 전처리, CNN 입력 생성, dataset/model/training/inference, feature extraction, 결과 저장)를 분석한다. Use when the request involves Python scripts, CNN/deep-learning code, preprocessing pipelines, datasets, model files, or how the CNN input is built.
keywords: [python, 파이썬, .py, cnn, 딥러닝, deep learning, 신경망, dataset, 데이터셋, 전처리, preprocessing, 학습, training, train, inference, 추론, feature, 특징, pytorch, torch, tensorflow, keras, numpy, pandas, 입력 데이터, cnn input, cnn 입력, 모델 파일, 정확도, accuracy, 라벨, label, 배치, epoch]
order: 44
combine-with: [project-analyzer, signal-analyzer, capacitor-aging-expert, debugger]
---

# python-analyzer

## 목적
Python 쪽 파이프라인 "원시 데이터 → 전처리 → CNN 입력 → 모델 → 학습/추론 → 결과 저장" 을 배열 shape 와 물리량 단위까지 추적해 설명한다.

## 언제 사용하는가
- CNN 입력(전류/스펙트럼/이미지 등)이 어떻게 만들어지는지 확인
- dataset 클래스, DataLoader, 정규화, 라벨(노화 등급/ESR/C 값) 생성 방식 파악
- 모델 구조, 손실함수, 학습 설정, 추론/평가 코드 검토
- MATLAB 이 저장한 파일을 Python 이 올바르게 읽는지 확인

## 확인해야 할 핵심 정보
- 입력 파일 형식과 로더 (`np.load`, `scipy.io.loadmat`, `pd.read_csv`, `h5py`) 와 변수/컬럼명
- 배열 shape 변화: (샘플, 채널, 길이) 등 각 단계의 shape, dtype, 단위
- 전처리: 구간 자르기(window), 정규화(어떤 통계로), 리샘플링, FFT/STFT 변환 여부, 증강
- 라벨 정의: 어떤 물리량(ESR, C, 노화 단계)을 어떻게 이산화/회귀하는지, 클래스 불균형
- train/val/test 분리 기준 (같은 조건·같은 커패시터가 양쪽에 섞이는 데이터 누수 여부)
- 모델: 입력 shape, conv 커널/스트라이드, 출력 차원, 손실, 옵티마이저, epoch, seed
- 저장: 체크포인트, 결과 CSV/그림 경로, 재현성(seed, 버전)

## 절차
1. 진입 스크립트(train/main/run)와 설정(config, argparse, yaml)을 먼저 읽고 하이퍼파라미터를 표로 만든다.
2. 데이터 로딩 함수부터 모델 입력까지 shape 를 단계별로 적는다. 확실하지 않으면 코드의 reshape/transpose 라인을 인용한다.
3. 전처리 수식과 MATLAB 쪽 생성 코드가 일관되는지(샘플링, 스케일, 단위) 대조한다.
4. 라벨/분리 방식에서 데이터 누수, 클래스 불균형, 조건 편향 가능성을 점검한다.
5. 요청이 개선/수정이면 문제 → 원인 → 영향 → 수정안 순으로 제시하고, 수정은 사용자 확인 후 최소 범위로 한다.

## 출력 형식
- **파이프라인 표**: 단계 | 함수/파일:라인 | 입력 shape | 출력 shape | 비고
- **설정 표**: 하이퍼파라미터, 경로, seed
- **위험 요소**: 누수/불균형/단위 불일치 등 (사실 근거 라인 포함)
- **개선 제안**: 우선순위와 예상 효과

## 주의사항
- 노트북(.ipynb)은 셀 단위로 읽고 실행 순서 의존성을 표시한다.
- 라이브러리 동작을 기억에 의존해 단정하지 마라. 버전에 따라 다르면 "버전 확인 필요" 라고 쓴다.
- 대량 dependency 설치, 학습 실행 같은 무거운 작업은 사용자에게 먼저 묻는다.

## 다른 Skill과의 조합
- `project-analyzer` 로 파일을 찾은 뒤 적용
- `signal-analyzer`: CNN 입력이 스펙트럼/고조파 특징일 때 변환의 타당성
- `capacitor-aging-expert`: 라벨(노화 지표)의 물리적 타당성
- `paper-code-bridge`: 논문의 feature/모델과 현재 구현 비교
