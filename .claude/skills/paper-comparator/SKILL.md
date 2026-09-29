---
name: paper-comparator
description: 여러 논문을 대상 시스템·입력 신호·분석 방법·진단 대상·online 여부·검증·장단점·프로젝트 관련성 기준으로 비교표를 만들고, 연구 흐름과 Research Gap, 현재 연구의 차별점을 도출한다. Use when the user asks to compare papers/methods, summarize how a field evolved, or identify research gaps and differentiation.
keywords: [비교, compare, comparison, 비교표, 차이, 여러 논문, 논문들, 논문 간, 연구 흐름, research flow, 발전 과정, 발전 흐름, 차별, 차별점, 차별성, novelty, 표로 정리, 표로 만들, 표로 비교, 어떤 논문이 가장, 가장 가까운, 가장 관련]
order: 24
combine-with: [literature-researcher, paper-analyzer, paper-code-bridge]
---

# paper-comparator

## 목적
개별 요약을 나열하지 않고, 같은 기준으로 여러 논문을 정렬해 "무엇이 공통이고, 무엇이 비어 있고, 우리 연구가 어디에 놓이는지" 를 보이게 한다.

## 언제 사용하는가
- "찾은 논문들 비교해줘", "내 연구와 가장 가까운 논문 골라줘", "이 분야 연구 흐름 정리"
- 결과보고서의 관련연구 절을 만들기 전에

## 비교 기준 (표의 열)
| 논문 | 대상 시스템 | 입력 신호 | 분석 방법 | 진단 대상 | Online 여부 | 실험 검증 | 장점 | 한계 | 현재 프로젝트 관련성 |

추가로 중요하게 확인할 항목(각 논문마다 ○/×/미확인):
DC-link voltage · Capacitor current · Neutral point current · Phase current · Switching current · Ripple current · Harmonic component · FFT · Wavelet · Charge/discharge profile · ESR · Capacitance · Temperature · Machine Learning · CNN · 3-Level NPC 사용 · 실험 검증

## 절차
1. 비교 대상 논문 목록과 각 논문의 근거 자료 수준(본문 정독 / 초록만)을 먼저 적는다. 초록만 본 논문은 표에서 "(초록)" 표기.
2. 주 비교표를 채운다. 빈 칸은 "미확인" 으로 남기고 추측으로 채우지 않는다.
3. 항목 체크표(○/×/미확인)를 만든다.
4. 연도순으로 정렬해 연구 흐름을 서술한다 (방법의 변화, 신호의 변화, 검증 수준의 변화). 문헌이 보여주는 것만 쓴다.
5. 체크표에서 "모두 × 이거나 미확인인 열", "특정 조합이 없는 칸" 을 찾아 Research Gap 후보로 제시하고, 각 후보에 근거 논문 번호를 붙인다.
6. 현재 프로젝트(3-Level NPC, 스위치/커패시터 전류 고조파, CNN)를 같은 표의 마지막 행에 넣어 차별점과 부족한 점(예: 실험 검증)을 대조한다.
7. 가장 가까운 논문 1~3편을 고르고 이유를 쓴다. 필요하면 `paper-analyzer` 로 정독을 제안한다.

## 출력 형식
- 주 비교표 + 항목 체크표
- 연구 흐름(연도순 서술 또는 화살표 체인)
- Research Gap 목록 (각각 근거 논문 번호, 확신도)
- 현재 프로젝트의 위치와 차별점 / 보완점
- `papers/index.md` 갱신 (관련성 열)

## 주의사항
- 표의 각 칸은 확인한 범위에서만 채운다. "미확인" 이 많으면 어떤 논문을 정독해야 하는지 제안한다.
- Gap 은 "문헌에 없다" 는 관찰이지 "아무도 안 했다" 는 단정이 아니다. 검색 범위의 한계를 함께 적는다.

## 다른 Skill과의 조합
- `literature-researcher` → (`paper-analyzer`) → 이 Skill → `paper-code-bridge` / `report-writer`
