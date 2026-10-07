# AI 활용 보고서 (2026-10-07)

「전력전자 설비 상태진단 연구에서의 인공지능 활용 현황 및 연구 적용 가능성 분석」 산출물 폴더.

| 파일 | 내용 |
|---|---|
| `07_AI_utilization_report_FINAL.md` | **최종 통합 보고서** (Figure 1–10, Table 1–5, Q1–Q7 답변, 참고문헌) |
| `01_lab_research_analysis.md` | 창업계획서 기반 연구실 연구분야·보유/개발/목표 기술·AI 사용 현황(Table 1) |
| `02_ai_literature_review.md` | 분야별 AI 선행연구 동향(A–O), AI 기법 분류, 연구 공백 G1–G6 |
| `03_paper_comparison_table.md` | 핵심 선행논문 18편 비교(Table 2, 16개 항목) |
| `04_code_audit.md` | 커패시터 노화진단 코드 감사: pipeline, 누수 PASS/WARNING/FAIL, 공정성, 일반화, 물리 타당성, 실행 검증, Exp 1–10 (Table 3, 4) |
| `05_ai_research_opportunities.md` | 후보 연구주제 17개 평가(Table 5), TOP 5, 로드맵 |
| `06_reference_verification.md` | 참고문헌 실재성·등급·근거 URL, 연구실 논문 29편 검증, 보류·제외 목록 |
| `agent_reports/` | 에이전트 A–G 원보고서(1차 근거)와 Red Team(H) 검토 결과 — 반영 기록은 06 §8 |
| `data/` | 운전조건 메타데이터 표, 합성 데이터 검증 결과 |
| `figures/` | 데이터 그림 4종 + 생성 코드 `make_figures.py` |
| `verification_code/` | 원본 코드 비수정 검증 도구, 합성 데이터 생성기, 메타데이터 추출기 |

## 반드시 알아둘 한계
- 선행연구는 **검색 스니펫 수준**(본문 미열람, doi.org 해석 불가). V2·P 등급과 "(초록)" 서술은 제출 전 원문 확인 필요.
- 연구실 **실측 데이터는 제공되지 않아** 실제 정확도는 확인하지 못했다. `data/synthetic_*` 와 Figure 9–10은 **합성 데이터**의 메커니즘 예시다.
- 검증한 `train80.py`는 연구실 주 모델이 아니라 "첨부 CNN"(미제공)에서 PI·PI 보조 손실 등을 뺀 비교 스크립트다. 원 CNN에 같은 검증을 적용해야 한다.
- 원본 연구 코드와 PDF는 이 저장소에 복사하지 않았다(업로드 파일을 읽기만 함, 개인정보 포함 PDF).
