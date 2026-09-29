# 캡 노화진단 Research Harness

3-Level NPC 인버터 DC-Link 커패시터 노화진단 연구를 위한 **Claude Code 기반 AI Research Harness** 이다.
PowerShell 로 한 번 실행하면 자연어 요청의 목적을 파악해 필요한 Skill(작업 지침)을 골라 조합하고, 프로젝트 맥락을 유지한 채 Claude 를 실행한다.

```
사용자 요청 → 프로젝트 Context(CLAUDE.md) → Skill 선택/조합(라우터) → 작업 지시서 생성 → Claude 실행 → 결과 정리 → 연구 기록 갱신
```

## 1. 설치 (처음 한 번)

1. **이 폴더의 파일을 `캡 노화진단/` 폴더에 넣는다.** (이 저장소를 그 위치에 clone 하거나 파일을 복사한다. 기존 MATLAB/Python/데이터 파일은 그대로 두면 된다.)
   하네스가 쓰는 항목: `harness.ps1`, `harness.cmd`, `CLAUDE.md`, `.claude/`, `harness/`, `context/`, `papers/`, `workspace/`, `logs/`, `.gitignore`, `README.md`
2. **Claude Code 설치 확인**: PowerShell 에서 `claude --version`. 없으면 `irm https://claude.ai/install.ps1 | iex` 로 설치하고 `claude auth login` 으로 로그인한다.
3. **실행 정책**: `.\harness.ps1` 이 "실행할 수 없습니다" 오류를 내면 다음 중 하나.
   - `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (한 번만)
   - 또는 `.\harness.cmd` 사용 (이 실행에 한해 정책을 우회)
4. **점검**: `.\harness.ps1 -Check` → Claude CLI 경로/버전/로그인, 폴더 구조, Skill 목록이 [OK] 로 나오면 준비 완료.
5. **프로젝트 Context 초안**: `.\harness.ps1 init` → Claude 가 프로젝트를 탐색해 `context/project-context.md` 의 TODO 를 채운다. 이후 직접 다듬는다.

PowerShell 5.1(Windows 기본)과 7 모두 지원한다. 한글 폴더명·공백 경로에서 동작하도록 만들었다.

## 2. 사용법

```powershell
.\harness.ps1                                            # 요청을 물어본 뒤 시작
.\harness.ps1 iSa2 전류에서 어떤 고조파가 큰지 확인해줘        # 따옴표 없이 바로 요청
.\harness.ps1 "NPC inverter DC-Link capacitor 노화진단 관련 논문 찾아줘"
```

실행하면 (1) 선택된 Skill 과 근거를 보여주고, (2) `harness/runs/<시각>-brief.md` 작업 지시서를 만들고, (3) Claude Code 대화형 세션을 열어 그 지시서로 작업을 시작한다. 이후에는 Claude Code 안에서 계속 대화하면 된다 (`/exit` 로 종료).

보조 옵션:

| 명령 | 설명 |
|---|---|
| `.\harness.ps1 <프로필> "요청"` | 프로필로 Skill 고정. 프로필: `init` `project` `matlab` `python` `npc` `paper` `research` `debug` `report` `skill` (harness/config.json 에서 수정) |
| `-Skills matlab,npc "요청"` | Skill 직접 지정 (부분 이름 허용, 쉼표 구분) |
| `-Print "요청"` | 대화형 대신 결과만 출력하고 `workspace/results/` 에 저장 |
| `-DryRun "요청"` | Claude 를 실행하지 않고 Skill 선택과 지시서만 확인 (라우터 키워드 튜닝용) |
| `-List` / `-Check` | Skill·프로필 목록 / 환경 점검 |
| `-Continue` / `-Resume <id>` | 직전 Claude 대화 이어가기 |
| `-NewSkill <이름>` | 새 Skill 템플릿 생성 |
| `-Model sonnet` | 모델 지정 (기본은 Claude 설정값) |
| `-NoLog` | 로그 남기지 않음 |

Claude Code 세션 안에서는 `/literature-researcher` 처럼 Skill 을 직접 호출할 수도 있다.

### 요청 예시와 선택되는 Skill

| 요청 | 선택 |
|---|---|
| 현재 프로젝트 구조 분석해줘 | project-analyzer |
| CNN input current 를 만드는 코드 흐름 확인해줘 | project-analyzer, python-analyzer |
| iSa2 의 FFT 에서 주요 고조파를 확인해줘 | npc-inverter-expert, signal-analyzer |
| NPC inverter DC-Link capacitor 노화진단 관련 논문 찾아줘 | literature-researcher, npc-inverter-expert, capacitor-aging-expert |
| iSa2 에 2n harmonic 이 중요하다는 문헌 근거를 찾아줘 | literature-researcher, npc-inverter-expert, signal-analyzer |
| 찾은 논문 방법과 내 MATLAB 코드를 비교해줘 | literature-researcher, paper-comparator, matlab-analyzer, paper-code-bridge |
| train.py 실행하면 shape mismatch 에러가 나 | python-analyzer, debugger |
| 이번 주 결과 정리해서 보고서로 작성해줘 | report-writer |

## 3. 구조

```
캡 노화진단/
├─ harness.ps1            진입점 (환경 확인 → Skill 로딩 → 라우팅 → 지시서 → Claude 실행 → 로그)
├─ harness.cmd            cmd/더블클릭용 래퍼
├─ CLAUDE.md              Claude 가 자동으로 읽는 프로젝트 지침 (context/project-context.md 를 import)
├─ .claude/
│  ├─ settings.json       권한: 하네스 폴더는 자유롭게 쓰고, 연구 코드 수정은 확인, 파괴적 명령 차단
│  └─ skills/<이름>/SKILL.md   Skill 13개 (Claude Code 네이티브 형식 + 라우터용 keywords/order)
├─ harness/
│  ├─ config.json         프로필, 라우터 설정, Claude 옵션
│  ├─ templates/brief.md  작업 지시서 템플릿 ({{REQUEST}}, {{SKILL_SECTIONS}} 등)
│  ├─ templates/SKILL.template.md
│  ├─ tools/Search-Papers.ps1   논문 메타데이터 검색 (Semantic Scholar/Crossref/OpenAlex/arXiv)
│  └─ runs/               생성된 지시서 (git 제외)
├─ context/
│  ├─ project-context.md  핵심 Context (짧게 유지, 매 세션 자동 로드)
│  ├─ research-log.md     작업 기록 (Claude 가 항목 추가, 최근 N개가 지시서에 포함)
│  └─ glossary.md         용어집 (필요할 때 읽음)
├─ papers/  pdf/ notes/ index.md
├─ workspace/  results/ (일회성 결과)  reports/ (보고서)
├─ logs/  harness-YYYY-MM.md (요청·Skill·결과요약·오류만 기록, git 제외)
└─ (MATLAB / Python / 데이터 / 결과 — 기존 연구 파일, 하네스는 건드리지 않음)
```

### Skill 목록

| Skill | 역할 |
|---|---|
| project-analyzer | 폴더/파일 관계, 데이터 흐름, 주요 함수 파악 |
| literature-researcher | 검색 전략 → 키워드 확장 → 후보 탐색 → 관련성 평가 → 핵심 논문 → 인용 네트워크 → 연구 흐름/Gap → 프로젝트 연결 |
| paper-analyzer | 논문 17항목 심층 분석 (목적, 수식, Figure/Waveform/Spectrum, 조건, 알고리즘, 활용) |
| paper-comparator | 여러 논문 비교표, 연구 흐름, Research Gap, 차별점 |
| npc-inverter-expert | 스위칭 상태, 스위치/중성점/커패시터 전류의 물리적 해석 |
| capacitor-aging-expert | C/ESR 노화, 리플, 충방전, 온도, 진단 지표, online monitoring |
| signal-analyzer | FFT/고조파/스펙트럼 방법론, 분해능·누설·창 함수 |
| matlab-analyzer | MATLAB 코드/변수/수식 추적 |
| python-analyzer | 전처리, CNN 입력, dataset/model/training 추적 |
| paper-code-bridge | 논문 방법 ↔ 현재 코드 대응, 차이와 영향, CNN feature 적용 계획 |
| debugger | 오류/비정상 결과의 원인(데이터 흐름·수식·차원·로직) 추적 |
| report-writer | 결과보고서/연구노트 작성 (workspace/reports) |
| skill-builder | 새 Skill 설계·추가, 키워드 검증 |

## 4. 동작 원리 (왜 이런 구조인가)

- **Skill = 파일 하나**: `.claude/skills/<이름>/SKILL.md` 는 Claude Code 가 그대로 인식하는 형식이다. 같은 파일의 frontmatter(`keywords`, `order`)를 `harness.ps1` 의 라우터가 읽는다. 그래서 Skill 을 추가해도 PowerShell 코드는 손대지 않는다.
- **라우터는 단순 키워드 점수**: 요청 문장에 포함된 키워드 수로 점수를 매기고 상위 N개(기본 4)를 `order` 순(탐색 → 문헌 → 도메인 → 코드/신호 → 디버그 → 보고)으로 조합한다. 완벽할 필요는 없다. 지시서에 전체 Skill 목록도 들어가므로 Claude 가 필요하면 다른 Skill 파일을 스스로 읽는다. 틀리면 `-Skills` 로 직접 지정하거나 키워드를 고친다 (`-DryRun` 으로 확인).
- **Context 는 두 층**: `CLAUDE.md` + `context/project-context.md` 는 짧게 유지해 매번 로드하고, 코드·데이터·논문은 Claude 가 필요할 때 탐색한다. `research-log.md` 의 최근 항목만 지시서에 들어간다.
- **지시서는 파일로 전달**: 긴 프롬프트를 명령줄로 넘기지 않고 `harness/runs/*.md` 로 저장한 뒤 "이 파일을 읽고 시작하라" 는 짧은 첫 메시지만 보낸다. Windows 의 따옴표/길이 문제를 피하고, 무엇이 전달됐는지 나중에 확인할 수 있다. `-Print` 모드에서는 지시서 전체를 표준입력으로 넘긴다.
- **연구 코드 보호**: `.claude/settings.json` 은 `context/ papers/ workspace/ logs/` 쓰기만 자동 허용한다. 연구 코드 수정은 Claude Code 가 확인을 요청하며, `git reset --hard`, `rm -rf` 등은 차단된다.

## 5. 새 Skill 추가

```powershell
.\harness.ps1 -NewSkill cnn-input-analysis     # 템플릿 생성 → .claude/skills/cnn-input-analysis/SKILL.md
```

frontmatter 의 `description`(한 문장, Claude 자동 선택 기준), `keywords`(라우터용, 한글+영문 부분 문자열), `order` 를 채우고 본문(목적/언제/핵심 정보/절차/출력/주의/조합)을 쓴다.
`.\harness.ps1 -DryRun "예문"` 으로 의도한 Skill 이 선택되는지 확인한다. Claude 에게 맡기려면 `.\harness.ps1 skill "…작업을 스킬로 만들어줘"`.

키워드 팁: 조사 앞 어간을 쓴다("고조파", "찾"). "분석", "코드" 처럼 모든 요청에 나오는 단어는 넣지 않는다. 짧은 영문("cap")은 다른 단어에 포함될 수 있으니 피한다.

## 6. 논문 탐색 도구

Claude 가 `literature-researcher` 에서 사용하며 직접 써도 된다 (API 키 불필요).

```powershell
pwsh -File harness\tools\Search-Papers.ps1 -Query "three-level NPC inverter DC-link capacitor condition monitoring" -Source all -Limit 20
pwsh -File harness\tools\Search-Papers.ps1 -Query "neutral point current harmonic NPC" -YearFrom 2015 -WithAbstract
pwsh -File harness\tools\Search-Papers.ps1 -Citations 10.1109/TPEL.xxxx    # 이 논문을 인용한 논문
pwsh -File harness\tools\Search-Papers.ps1 -References 10.1109/TPEL.xxxx   # 이 논문이 인용한 논문
```

(PowerShell 5.1 이면 `pwsh` 대신 `powershell`.) 결과는 메타데이터(제목/초록/DOI/인용수)이며, 세부 주장은 본문 확인 전까지 "미확인" 으로 다룬다. 본문 읽기는 `paper-analyzer` 가 PDF(`papers/pdf/`) 또는 공개 URL 로 수행한다.

## 7. 설정 변경 (harness/config.json)

- `claude.path`: CLI 자동 탐지가 실패할 때 실행 파일 경로 (환경변수 `HARNESS_CLAUDE_PATH` 도 가능)
- `claude.model`, `claude.permissionMode`, `claude.extraArgs`: Claude 실행 옵션
- `router.maxSkills`(기본 4), `router.minScore`, `router.defaultSkills`, `router.recentLogEntries`
- `profiles`: 프로필 이름 → skills 목록 (+ 기본 request)
- `log.enabled`, `log.dir`

## 8. 문제 해결

| 증상 | 조치 |
|---|---|
| "Claude CLI 를 찾지 못했습니다" | `claude --version` 확인 → 설치 또는 `config.json` 의 `claude.path` 지정 |
| 로그인 안 됨 | `claude auth login` 또는 `ANTHROPIC_API_KEY` 환경변수 |
| 한글이 깨짐 | Windows Terminal/PowerShell 7 권장. 스크립트는 UTF-8(BOM) 로 저장되어 있어야 한다 |
| Skill 이 이상하게 선택됨 | `-DryRun` 으로 근거 확인 → SKILL.md 의 keywords 수정 또는 `-Skills` 지정 |
| 오류 메시지에 `harness.ps1:<줄>` 이 표시됨 | 그 줄 번호와 메시지로 문제를 보고 |
| 논문 검색 API 오류 | 네트워크/방화벽 확인. `-Source semanticscholar` 등으로 출처를 바꿔 시도 |

## 9. 향후 확장 (필요할 때만)

- `.claude/agents/<이름>.md` 로 서브에이전트(별도 컨텍스트) 정의 — 긴 문헌 탐색을 독립 실행하고 싶을 때
- 하네스 프로필에 자주 쓰는 조합 추가
- `harness/templates/brief.md` 의 마무리 절차 수정으로 기록 형식 변경
