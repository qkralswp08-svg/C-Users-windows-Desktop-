---
name: report-writer
description: 분석·실험·문헌 탐색 결과를 연구보고서/결과보고서/연구노트 형식(목적, 방법, 결과, 고찰, 관련연구, 다음 단계)으로 정리해 workspace/reports 에 저장한다. Use when the user asks to write up, summarize, document, or produce a report of research results or progress.
keywords: [보고서, report, 결과보고, 결과 보고, 연구보고, 연구 보고, 결과 정리, 정리해서, 문서로, 문서 작성, 연구노트, 연구 노트, 주간, 발표 자료, 요약본, 작성해줘, 정리해줘, 마크다운 문서, 결론 정리]
order: 60
combine-with: [paper-comparator, capacitor-aging-expert, signal-analyzer]
---

# report-writer

## 목적
흩어진 결과(코드 분석, 스펙트럼, CNN 결과, 논문 비교)를 읽는 사람이 재현·판단할 수 있는 문서로 만든다. 새로 분석하기보다 이미 확인된 사실을 정확히 조직하는 것이 우선이다.

## 언제 사용하는가
- 결과보고서, 중간보고, 연구노트, 관련연구 절 작성
- `context/research-log.md` 의 여러 항목을 하나의 정리 문서로 묶을 때

## 절차
1. 자료 수집: `context/research-log.md`, `workspace/results/`, `papers/index.md`, `papers/notes/`, 결과 그림/CSV 경로를 훑어 이번 보고 범위의 근거를 모은다. 부족한 부분은 사용자에게 묻거나 "미확인" 으로 표시한다.
2. 독자와 목적 확인(지도교수 보고 / 내부 정리 / 논문 초안). 분량과 형식(markdown 기본; docx 등은 요청 시).
3. 구성: 제목 / 요약(3~5줄) / 1. 배경·목적 / 2. 시스템·데이터(토폴로지, 신호, 조건) / 3. 방법(신호처리, feature, CNN) / 4. 결과(표·그림 참조) / 5. 고찰(물리적 해석, 한계) / 6. 관련연구(비교표 요약) / 7. 다음 단계 / 부록(파일·변수 목록, 재현 명령).
4. 모든 수치에는 출처(파일, 실행 조건, 날짜)를 붙인다. 문헌 인용은 `papers/index.md` 의 서지정보를 사용한다.
5. 사실 / 해석 / 추론 을 문장 수준에서 구분한다 (예: "측정 결과 …이다" vs "…로 해석된다" vs "…로 추정된다").
6. `workspace/reports/<날짜>-<제목>.md` 로 저장하고 요약을 사용자에게 보여준다.

## 출력 형식
- markdown 보고서 파일 + 콘솔 요약
- 표는 markdown 표, 그림은 상대 경로로 링크
- 미확인/추가 필요 항목은 문서 끝에 체크리스트로

## 주의사항
- 보고서에 없는 결과를 만들어내지 않는다. 확인하지 못한 값은 빈칸과 "확인 필요" 로 남긴다.
- 논문 인용은 실제 서지정보가 확인된 것만 쓴다.
- 기존 보고서를 덮어쓰지 않고 새 파일로 저장한다.

## 다른 Skill과의 조합
- `paper-comparator`: 관련연구 절
- `signal-analyzer` / 도메인 Skill: 고찰의 물리적 해석 검토
