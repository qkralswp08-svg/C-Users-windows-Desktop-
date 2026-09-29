---
name: skill-builder
description: 반복되는 작업 패턴을 새 Skill(.claude/skills/<name>/SKILL.md)로 분리하도록 설계·작성하고, 기존 Skill 의 키워드/절차를 개선한다. Use when the user wants to add, create, or refine a harness skill or automate a recurring task pattern.
keywords: [새 스킬, 스킬 추가, 스킬 만들, 스킬 수정, 스킬로, 스킬 설계, new skill, skill 추가, skill 만들, skill 설계, 자동화, 반복 작업, 반복되는, 하네스 확장, harness 확장, 라우터 키워드, 키워드 추가]
order: 70
combine-with: [project-analyzer]
---

# skill-builder

## 목적
하네스가 커져도 단순함을 유지하도록, 새 작업 유형을 "작고 겹치지 않는 Skill" 로 추가한다. PowerShell 코드를 고치지 않고 SKILL.md 파일 하나로 라우터와 Claude 가 동시에 인식하게 한다.

## Skill 파일 규약
- 위치: `.claude/skills/<kebab-case-name>/SKILL.md` (템플릿: `harness/templates/SKILL.template.md`, 생성: `.\harness.ps1 -NewSkill <name>`)
- frontmatter:
  - `name`: 폴더명과 동일
  - `description`: 한 문장. 하는 일 + 언제 쓰는지 (Claude 자동 선택 기준). 영문 "Use when …" 을 포함하면 좋다.
  - `keywords`: 라우터가 요청 문장에서 찾는 부분 문자열 목록 (한글+영문, 소문자 무시). 너무 일반적인 단어("분석", "코드")는 피한다. 한글은 조사 앞 어간 위주(예: "고조파", "찾").
  - `order`: 파이프라인 순서. 10 탐색 · 20 문헌 · 30 도메인 · 40 코드/신호 · 50 디버그 · 60 보고 · 70 메타
  - `combine-with`: 자주 함께 쓰는 Skill (문서용)
- 본문: 목적 / 언제 사용 / 핵심 정보 / 절차 / 출력 형식 / 주의사항 / 조합. 80~120줄 이내.

## 절차
1. 사용자가 반복한 요청 유형을 `logs/` 와 `context/research-log.md` 에서 확인하고, 기존 Skill 로 커버되는지 먼저 판단한다 (기존 Skill 의 키워드/절차 보강으로 충분하면 새로 만들지 않는다).
2. 새 Skill 의 경계를 정한다: 입력(무엇을 받는가), 출력(무엇을 내는가), 다른 Skill 과 겹치지 않는 책임.
3. 템플릿으로 파일을 만들고 절차를 구체적 확인 항목 위주로 쓴다. 도메인 지식은 판단 기준 형태로만 넣는다.
4. 키워드를 실제 요청 예문 3개 이상으로 검증한다: `.\harness.ps1 -DryRun "예문"` 이 의도한 Skill 을 고르는지 확인.
5. 필요하면 `harness/config.json` 의 profiles 에 단축 프로필을 추가한다.
6. `context/project-context.md` 나 README 에 Skill 목록이 있으면 갱신한다.

## 출력 형식
- 새/수정 Skill 파일 내용
- 검증 예문과 DryRun 결과 요약
- 기존 Skill 과의 책임 구분 설명

## 주의사항
- Skill 간 중복 서술을 피한다. 공통 원칙(사실/추론 구분, 코드 보호)은 CLAUDE.md 와 지시서 템플릿에 이미 있다.
- 거대한 프롬프트로 만들지 않는다. 절차와 확인 항목 중심으로 짧게.
