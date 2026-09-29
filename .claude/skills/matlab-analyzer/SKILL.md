---
name: matlab-analyzer
description: MATLAB(.m/.mat/Simulink) 코드의 함수 흐름, 변수 관계, 데이터 처리와 신호 계산 과정을 분석한다. Use when the request involves MATLAB scripts/functions, .mat data, Simulink models, or how a signal/variable is computed in MATLAB.
keywords: [matlab, 매트랩, simulink, 시뮬링크, .m 파일, .mat, mat 파일, plecs, 스크립트, m파일, 변수 관계, 함수 흐름, 워크스페이스]
order: 42
combine-with: [signal-analyzer, npc-inverter-expert, project-analyzer, debugger]
---

# matlab-analyzer

## 목적
MATLAB 코드가 "어떤 입력에서 어떤 변수를 어떻게 계산해 무엇을 저장/그리는지"를 정확히 추적한다.
신호처리 방법론 자체는 `signal-analyzer`, 인버터/커패시터의 물리적 의미는 `npc-inverter-expert` / `capacitor-aging-expert` 가 맡고, 이 Skill 은 코드와 변수의 사실관계를 담당한다.

## 언제 사용하는가
- MATLAB 스크립트/함수의 동작 설명, 변수 계산 과정 추적
- `.mat` 파일의 변수 구조 파악 (Claude 는 .mat 을 직접 열 수 없으므로 생성/저장 코드에서 역추적)
- Simulink 모델의 To Workspace / logging 변수 확인 (`.slx` 는 직접 못 읽으므로 관련 스크립트와 변수명으로 파악)
- FFT/고조파 계산 코드가 올바른지 검토

## 확인해야 할 핵심 정보
- 샘플링: `Ts`, `fs`, 시뮬레이션 step, 데이터 길이 `N`, 분석 구간(정상상태 진입 후인지)
- 기본파 `f1`, 스위칭 주파수 `fsw`, 변조지수, DC-link 전압
- 신호 변수명과 물리량 대응 (예: `iSa2` = a상 상단 내측 스위치 전류, `iC1`/`iC2` = 상/하단 커패시터 전류, `iNP` = 중성점 전류)
- 배열 방향(행/열), 단위, 부호 규약(전류 기준 방향)
- FFT 구현: `fft` 길이, 창 함수, 스케일링(`2/N`), 단측/양측, 주파수축 계산(`(0:N-1)*fs/N`), 정수 주기 여부
- 저장/출력: `save`, `writematrix`, `csvwrite`, 그림 저장 → Python 이 읽는 파일과 이름/형식이 맞는지

## 절차
1. 진입 스크립트부터 호출 순서대로 읽는다. 함수는 시그니처(입력/출력)와 핵심 수식 라인만 인용한다.
2. 질문 대상 변수를 정하고, 그 변수가 정의되는 모든 지점을 `Grep` 으로 찾아 "정의 → 변환 → 사용" 사슬을 만든다.
3. 각 변환의 수식을 적고 물리적 의미를 한 줄로 붙인다 (의미 해석은 도메인 Skill 지침 참조).
4. 수치 설정(fs, N, 창, 구간)이 분석 목적에 맞는지 점검한다. 주파수 분해능 `Δf = fs/N`, 스펙트럼 누설, 과도구간 포함 여부를 확인한다.
5. 의심되는 부분은 "코드가 이렇게 되어 있다(사실)" 와 "그래서 이런 영향이 있을 것이다(추론)" 를 분리해 적는다.

## 출력 형식
- **변수 사슬**: `원신호 → 처리 → 결과` 를 파일:라인 과 함께
- **핵심 수식**: 코드 → 수학식 대응
- **설정값 표**: fs, N, f1, fsw, 창, 구간
- **문제/개선 후보**: 있으면 원인과 영향, 수정 방향 (수정은 사용자 확인 후)

## 주의사항
- `.mat`, `.slx`, `.fig` 는 바이너리라 직접 읽을 수 없다. 이를 만든/읽는 코드로 추정하고 "코드 기준 추정" 이라고 밝힌다.
- MATLAB 은 1-based 인덱스, 열 우선(column-major) 임을 dimension 문제 판단에 반영한다.
- 코드 수정 요청이 아니면 수정하지 않는다. 수정하더라도 원본 로직을 바꾸는 부분은 먼저 설명한다.

## 다른 Skill과의 조합
- `signal-analyzer` 와 함께: FFT/고조파 결과의 타당성 검토
- `npc-inverter-expert` / `capacitor-aging-expert` 와 함께: 변수의 물리적 의미와 기대 스펙트럼
- `paper-code-bridge` 와 함께: 논문 수식과 코드 대응
