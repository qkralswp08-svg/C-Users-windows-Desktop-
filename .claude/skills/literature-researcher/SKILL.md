---
name: literature-researcher
description: 연구 질문에서 검색 전략을 세우고 키워드를 확장해 IEEE/ScienceDirect/Semantic Scholar/Crossref 등에서 관련 논문을 넓게 찾은 뒤 관련성으로 좁혀 핵심 논문을 선정하고, 인용 네트워크·연구 흐름·Research Gap 을 정리해 현재 프로젝트와 연결한다. Use when the user asks to find, search, or survey papers, literature, prior work, evidence for a claim, or research trends.
keywords: [논문, paper, papers, 문헌, literature, 찾, 검색, search, 탐색, 선행연구, 선행 연구, 관련 연구, related work, 참고문헌, reference, survey, 서베이, review, 리뷰, ieee, scholar, doi, 근거, evidence, 인용, citation, 연구 동향, trend, research gap, 리서치 갭, 갭, 최신 연구, state of the art]
order: 20
combine-with: [paper-analyzer, paper-comparator, paper-code-bridge, capacitor-aging-expert, npc-inverter-expert]
---

# literature-researcher

## 목적
"검색 결과 몇 개 나열" 이 아니라, 연구 질문 → 검색 전략 → 넓은 후보 → 관련성 평가 → 핵심 논문 → 연구 흐름/Gap → 프로젝트 연결 까지의 탐색을 수행한다. 심층 분석은 `paper-analyzer`, 여러 논문 비교는 `paper-comparator` 가 이어받는다.

## 언제 사용하는가
- "…관련 논문 찾아줘", "…라는 근거가 있는 논문 있어?", "이 분야 연구 동향/Gap"
- 새로운 feature/방법을 검토하기 전에 선행연구 확인

## 도구
- 우선 `WebSearch` / `WebFetch` 로 검색하고, 구조화된 메타데이터(DOI, 초록, 인용수)는 하네스 보조 스크립트를 사용한다:
  - `pwsh -File harness/tools/Search-Papers.ps1 -Query "..." -Source all -Limit 20` (PowerShell 5.1 이면 `powershell -File ...`)
  - 인용 네트워크: `-Citations <DOI>` (이 논문을 인용한 논문), `-References <DOI>` (이 논문이 인용한 논문)
  - 출력: 표(markdown) 또는 `-Json`. Semantic Scholar / Crossref / OpenAlex / arXiv 를 질의한다.
- 사용 가능한 출처: IEEE Xplore, ScienceDirect, Springer, Wiley, IET, MDPI, Google Scholar, Semantic Scholar, Crossref, OpenAlex, arXiv. 한 출처에만 의존하지 않는다.

## 절차 (Stage)
1. **질문 구조화**: 대상 시스템(3-Level NPC / 일반 VSI), 진단 대상(DC-link 커패시터 C/ESR), 사용 신호(커패시터 전류, 중성점 전류, 스위치 전류, 전압 리플), 방법(FFT/고조파, 충방전, ML/CNN), 검증(시뮬레이션/실험) 으로 나눈다. 사용자가 구체적 주장(예: "iSa2 주요 고조파가 2n 계열")을 물으면 그 주장을 그대로 검증 대상으로 적는다.
2. **키워드 확장**: 각 축별 동의어를 만든다. 예: three-level NPC inverter / NPC converter / neutral-point-clamped; DC-link capacitor / electrolytic capacitor / film capacitor; condition monitoring / health monitoring / aging / degradation / ESR estimation / capacitance estimation; capacitor current / ripple current / neutral point current / switching device current spectrum / even harmonic; FFT / harmonic analysis / spectral / wavelet; CNN / deep learning / machine learning. 구체적 질문일수록 좁은 조합(예: "NPC switch current harmonic", "neutral point current spectrum even harmonic")을 추가한다.
3. **Stage 1 – 넓게 (10~20편)**: 여러 키워드 조합 × 여러 출처로 후보를 모은다. 각 후보에 제목/저자/연도/학술지·학회/DOI/URL 을 기록한다. 중복(DOI 기준) 제거.
4. **Stage 2 – 분류**: 제목+초록으로 "대상 시스템 / 입력 신호 / 방법 / 진단 대상 / online 여부 / 검증 / ML 사용" 을 표로 채운다. 초록에 없는 항목은 "미확인".
5. **Stage 3 – 관련성 평가**: 아래 기준으로 매우 높음 / 높음 / 보통 / 참고용 을 매긴다. 기준: 실제 3-Level NPC 사용, DC-link 커패시터 직접 다룸, capacitor current 사용, neutral current 사용, harmonic/FFT 사용, ESR 추정, capacitance 추정, online 방식, 실험 검증, ML/CNN 사용, 현재 코드에 참고 가능. 3~5편을 핵심 논문으로 고른다.
6. **Stage 4 – 인용 네트워크**: 핵심 논문의 References(과거)와 Cited-by(후속)를 확인해 놓친 논문과 연구 계보를 보강한다.
7. **Stage 5 – 연구 흐름과 Gap**: 문헌이 실제로 보여주는 발전 흐름(예: ESR 기반 → C 기반 → 전압 리플 → 전류 리플 → 충방전 프로파일 → 신호처리 → ML → CNN)을 정리하되, 실제 문헌이 다르면 문헌을 따른다. Gap 은 "표에서 비어 있는 칸" 처럼 문헌 근거로만 제시한다 (예: capacitor current 를 쓰지만 harmonic 을 직접 쓰지 않음, simulation 만 있음, ESR 만 추정, offline 중심, 특정 topology 부족, FFT 특징과 CNN 입력을 연결한 연구 부족).
8. **프로젝트 연결**: 논문 → 물리적 원리 → 신호 → 특징 추출 → MATLAB/Python 구현 → CNN/노화진단 → 현재 프로젝트 의 사슬로 "무엇을 추가 측정/구현/비교할 수 있는지" 를 적는다. 심층 분석이 필요하면 `paper-analyzer` 로 넘긴다.
9. 결과를 `papers/index.md` 의 표에 추가한다 (기존 항목은 DOI 로 중복 확인). 필요하면 상세 노트를 `papers/notes/<연도>-<제1저자>-<짧은제목>.md` 로 저장한다.

## 출력 형식
- **검색 전략**: 질문 구조 + 키워드 조합 표 + 사용 출처
- **후보 논문 표**(Stage 1~3): 번호 | 제목 | 저자 | 연도 | 출처 | DOI/URL | 대상 시스템 | 입력 신호 | 방법 | 진단 대상 | Online | 검증 | ML | 관련성 | 근거
- **핵심 논문 3~5편**: 각 논문의 연구 목적·제안 방법·프로젝트 관련성 (초록/본문 확인 범위 명시)
- **연구 흐름** 과 **Research Gap** (각 항목에 근거 논문 번호)
- **프로젝트 연결 제안**과 **다음 단계**(어떤 논문을 `paper-analyzer` 로 정독할지)

## 주의사항 (매우 중요)
- **제목/초록만으로 세부 내용을 단정하지 않는다.** 특정 고조파 존재, 특정 수식, 특정 알고리즘, 실험 결과 같은 주장은 본문·수식·그림을 확인한 경우에만 "확인됨" 으로 쓰고, 그렇지 않으면 "초록 기준 / 본문 미확인" 으로 표기한다.
- **사실 / 해석 / 추론 구분**: (a) 논문에서 직접 확인된 내용, (b) 논문 결과에 대한 물리적 해석, (c) 논문이 말하지 않았지만 스위칭 상태·수식에서 도출한 추론. 근거를 못 찾으면 "직접적인 문헌 근거를 확인하지 못함" 이라고 명확히 쓴다.
- 존재하지 않는 논문·DOI 를 만들어내지 않는다. DOI 는 검색 결과에서 복사한 것만 쓰고, 확인 못 한 서지정보는 "(확인 필요)" 로 남긴다.
- 페이월로 본문을 못 읽으면 그 사실을 적고 초록/공개 버전(arXiv, 저자 페이지) 여부를 확인한다.
- Research Gap 을 문헌 근거 없이 만들어내지 않는다.

## 다른 Skill과의 조합
- → `paper-analyzer`: 핵심 논문 정독
- → `paper-comparator`: 여러 논문 비교표·연구 흐름
- → `paper-code-bridge`: 논문 방법과 현재 코드 비교
- `npc-inverter-expert` / `capacitor-aging-expert`: 관련성 판단 기준 보강
