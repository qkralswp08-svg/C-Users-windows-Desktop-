---
name: bibliographic-verifier
description: 논문 서지(제목·저자·연도·저널·권/호/쪽·DOI)와 저널/학회 구분을 검색 결과→Crossref→출판사 페이지→본문 순으로 교차검증하고, 확인되지 않은 항목을 "(확인 필요)"·"Abstract-level only" 로 표기한다. Use when a paper list must be verified before citing, when journal vs conference status is unclear, or when DOIs/volumes/pages need to be confirmed.
keywords: [서지, 서지 확인, 서지정보, bibliographic, 검증, verify, verification, doi 확인, doi 검증, 저널 여부, journal or conference, 학회 논문인지, 권호, 페이지 확인, crossref, 출판사 확인, 인용 전 확인, citation check, 확인 필요]
order: 21
combine-with: [literature-researcher, paper-analyzer, paper-comparator]
---

# bibliographic-verifier

## 목적
문헌조사 결과를 인용 가능한 수준으로 만든다. "검색 엔진이 보여준 것" 과 "출판사가 확인해 준 것" 을 구분하고, 추측으로 채운 서지를 남기지 않는다.

## 언제 사용하는가
- literature-researcher 가 만든 후보 목록을 최종 선정·보고서에 쓰기 전
- 저널 논문인지 학회 논문인지 불분명할 때
- DOI·권·호·쪽·저자 목록이 비어 있거나 서로 다른 출처가 충돌할 때

## 검증 단계 (가능한 순서대로, 막히면 그 단계에서 멈추고 등급 기록)
1. **검색 결과(스니펫)**: 제목·연도·저널명이 보이는지. IEEE Xplore 제목의 "IEEE Journals & Magazine" = 저널, "IEEE Conference Publication" = 학회. ScienceDirect PII, Springer/Wiley/MDPI/IET/J-STAGE URL 패턴으로 저널 식별.
2. **Crossref / Semantic Scholar / OpenAlex**: `harness/tools/Search-Papers.ps1 -Query "<제목>" -Source all` 로 DOI·권·호·쪽·저자·type(journal-article / proceedings-article) 확인. Crossref `type` 이 가장 신뢰할 만한 저널/학회 구분이다.
3. **출판사 랜딩 페이지**: DOI 링크를 열어 제목·저자·권/호/쪽이 2단계와 일치하는지, Early Access 인지(권/쪽 미정) 확인.
4. **본문(PDF/OA)**: 열 수 있으면 초록 외 방법·실험 조건을 확인하고 등급을 "본문" 으로 올린다.

## 등급 표기 (모든 논문에 필수)
- **L1**: 저널·연도·권/호/쪽·DOI 모두 확인 / **L2**: 저널명·연도만 출판사 URL 로 확인 / **L3**: 제목만 확인(저널 추정)
- 내용 근거: **본문** / **Abstract-level only**
- 채우지 못한 칸은 `(확인 필요)`. DOI·권·쪽·저자를 추정해 채우지 않는다. URL 패턴에서 유도한 DOI 는 "(URL 유도)" 라고 표시.

## 자주 생기는 오류와 대처
- 학회 논문의 저널 확장판이 따로 있는 경우(예: APEC → TIA): 두 항목을 분리하고 저널판을 인용.
- Early Access: 연도는 온라인 게재 연도, 권/호/쪽은 "(Early Access, 확인 필요)".
- 검색 요약문이 여러 논문의 내용을 섞어 보여주는 경우: 특정 문장을 특정 논문에 귀속시키지 말고 "귀속 확인 필요".
- 같은 제목이 여러 출판사에 보이면 프리프린트(SSRN/TechRxiv/arXiv)와 저널판을 구분.

## 출력 형식
| # | 제목 | 저자 | 연도 | 저널/학회 (권/호/쪽) | DOI | 유형(journal/conference/preprint) | 등급 | 확인 출처(URL) | 미확인 항목 |

## 주의사항
- 네트워크가 막혀 2–4 단계를 못 하면 그 사실을 보고서 맨 앞에 쓰고, 모든 항목을 "Abstract-level only" 로 둔다.
- 검증은 서지에 한정한다. 방법·결과의 해석은 paper-analyzer / paper-comparator 가 맡는다.
