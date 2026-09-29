---
name: project-analyzer
description: 캡 노화진단 프로젝트의 폴더/파일 관계, MATLAB↔Python↔데이터 흐름, 주요 함수를 파악하고 요약한다. Use when the user asks about project structure, where something is, how files/data connect, or before any analysis that needs to locate the relevant code first.
keywords: [프로젝트 구조, 폴더 구조, 전체 구조, 파일 관계, 파일 탐색, 어떤 파일, 어디에, 어디서, 데이터 흐름, 흐름 파악, 구조 파악, 프로젝트 파악, 파일 목록, 함수 목록, 입력 데이터 생성, project structure, overview, 코드 흐름]
order: 10
combine-with: [matlab-analyzer, python-analyzer, debugger]
---

# project-analyzer

## 목적
프로젝트 전체를 읽지 않고도 "무엇이 어디에 있고, 어떤 순서로 연결되는지"를 빠르게 파악한다.
다른 Skill 이 작업할 파일을 찾아주는 진입 Skill 이다.

## 언제 사용하는가
- "프로젝트 구조 분석해줘", "CNN 입력 만드는 코드가 어디야" 같은 위치/관계 질문
- 다른 분석 Skill 을 적용하기 전에 대상 파일을 찾아야 할 때
- context/project-context.md 초안을 만들거나 갱신할 때 (`.\harness.ps1 init`)

## 확인해야 할 핵심 정보
- 최상위 폴더 구성: MATLAB / Python / 데이터(CSV, MAT, NPY) / 논문 / 결과(그림, 모델) / 하네스(harness, .claude, context 등은 연구 코드가 아님)
- 진입점(main 스크립트, run 함수, 학습 스크립트)과 호출 관계
- 데이터 파이프라인: 시뮬레이션/측정 → 저장 형식 → 전처리 → CNN 입력 → 모델 → 결과 저장
- 파일 간에 주고받는 변수/파일명 (예: `.mat` 안의 변수명, CSV 컬럼명, npy 배열 shape)
- README, 주석, 결과 폴더의 파일명 규칙

## 절차
1. `Glob` 으로 확장자별 파일 목록을 먼저 본다 (`**/*.m`, `**/*.py`, `**/*.mat`, `**/*.csv`, `**/*.npy`, `**/*.pdf`, `**/*.png`). 하네스 폴더(harness, .claude, context, logs, workspace, papers)는 연구 코드에서 제외한다.
2. 파일 수가 많으면 폴더 단위로 묶어 역할을 추정하고, 진입점 후보(파일명에 main/run/train/test/plot 등)를 먼저 연다.
3. 진입점에서 호출하는 함수/모듈을 따라가며 호출 그래프를 만든다. `Grep` 으로 함수명·변수명·파일명(`load`, `save`, `csvread`, `np.load`, `torch.load` 등)을 추적한다.
4. 데이터 흐름을 "생성 → 저장 → 로드 → 변환 → 사용" 순으로 정리한다. 파일 형식과 변수명, 배열 크기를 적는다.
5. 요청이 특정 기능(예: CNN 입력 생성)에 관한 것이면 그 기능에 관련된 파일만 깊게 읽고 나머지는 한 줄로 요약한다.

## 출력 형식
- **폴더 지도**: 폴더 → 역할 (표 또는 트리)
- **핵심 파일 표**: 파일 | 역할 | 입력 | 출력 | 호출하는/되는 파일
- **데이터 흐름 다이어그램**(텍스트 화살표)
- **다음 단계**: 어떤 파일을 어떤 Skill 로 볼지 제안
- context/project-context.md 갱신이 목적이면, 해당 파일의 TODO 항목을 실제 내용으로 바꾼다 (확실하지 않으면 "(확인 필요)" 표기).

## 주의사항
- 파일 내용을 전부 출력하지 마라. 필요한 함수 시그니처와 핵심 라인만 인용한다.
- 추정한 역할(파일명만 보고 판단)과 확인한 역할(내용을 읽고 판단)을 구분해 표기한다.
- 연구 코드를 수정하지 않는다.

## 다른 Skill과의 조합
- 앞단으로 쓰인다: 대상 파일을 찾은 뒤 `matlab-analyzer`, `python-analyzer`, `debugger` 가 이어받는다.
