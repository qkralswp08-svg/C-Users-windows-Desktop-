---
name: capacitor-aging-expert
description: DC-Link 커패시터의 노화(capacitance 감소, ESR 증가), 리플 전류/전압, 충방전 프로파일, 온도, 노화 지표와 online condition monitoring / health estimation 을 해석한다. Use when the request is about capacitor aging, ESR/capacitance estimation, condition monitoring, health indicators, or which signal features reflect capacitor degradation.
keywords: [capacitor, 커패시터, 캐패시터, 콘덴서, 노화, aging, ageing, degradation, 열화, esr, capacitance, 정전용량, 상태진단, 상태 진단, condition monitoring, 수명, lifetime, health, 건전성, 진단 지표, aging indicator, 전해 커패시터, electrolytic, 필름 커패시터, film capacitor, 온도, temperature, 충방전, charge, discharge, dc-link, dc link, dc 링크, 리플 전압, voltage ripple, 임피던스, impedance, 고장 진단, fault diagnosis, 잔존수명, rul]
order: 32
combine-with: [npc-inverter-expert, signal-analyzer, python-analyzer, literature-researcher]
---

# capacitor-aging-expert

## 목적
커패시터 노화의 물리 → 측정 가능한 전기 신호 → 진단 지표(feature) → 추정/분류(CNN 포함) 의 연결 고리를 판단한다. "이 신호 성분이 노화 정보를 담는가, 왜 그런가, 다른 요인(부하, 온도, 변조)과 어떻게 구분하는가" 에 답한다.

## 언제 사용하는가
- 노화 지표(ESR, C, 리플, 온도)의 정의와 신호와의 관계
- 어떤 전류/전압 성분을 CNN 입력 feature 로 쓰는 것이 타당한지
- 라벨(노화 등급)의 정의, 실험/시뮬레이션에서 노화를 모사하는 방법(C 감소, ESR 증가 값 설정)
- 논문의 진단 방법이 현재 프로젝트에 적용 가능한지 (`paper-code-bridge` 와 함께)

## 핵심 물리 (판단 기준)
- 전해 커패시터: 전해액 증발로 C 감소, ESR 증가. 흔히 쓰는 수명 종료 기준은 C −20% 또는 ESR 2배(문헌·제조사에 따라 다름). 필름 커패시터: 자기치유로 C 가 서서히 감소(−5% 기준이 흔함), ESR 변화는 상대적으로 작음. → 진단 대상이 어떤 종류인지 먼저 확인.
- 단순 모델: `v_C = v_C0 + ESR·i_C + (1/C)∫i_C dt`. 스위칭 주파수 대역 리플은 ESR 항이, 저주파(2f1, 3f1 등) 리플은 1/C 항이 상대적으로 지배한다 → ESR 은 고주파 리플 전압/전류 비, C 는 저주파 충방전(ΔV 대 ∫i dt)에서 추정하는 것이 일반적 접근.
- ESR 은 온도·주파수 의존성이 크다(온도 상승 시 감소). 온도 보정 없이 ESR 변화만으로 노화를 판단하면 오진 가능.
- 리플 전류 실효값은 발열(`P = ESR·I_rms²`)을 결정하고, 발열은 다시 노화를 가속한다. 리플 전류 스펙트럼은 인버터 변조·부하에 따라 바뀌므로 "노화 때문인지 운전조건 때문인지" 를 분리해야 한다.
- NPC 에서는 상·하단 커패시터가 따로 노화될 수 있어 두 커패시터 전류/전압 리플의 비대칭(크기·위상·중성점 전압 오프셋)이 추가 지표가 될 수 있다.

## 절차
1. 대상 커패시터(종류, 정격, 상/하단), 측정 가능한 신호(직접 측정 vs 스위치 전류로 재구성), 운전 조건 범위를 확인한다.
2. 각 후보 지표에 대해 "노화 시 어떻게 변하는가(방향·크기)", "운전 조건 변화와 어떻게 구분하는가", "측정 난이도" 를 표로 만든다.
3. 프로젝트의 라벨/노화 모사 방식(C, ESR 값 설정)과 신호 생성 코드가 물리적으로 일관되는지 검토한다 (`python-analyzer`, `matlab-analyzer`).
4. CNN 입력 feature 로 쓸 성분을 제안할 때는 이유(민감도, 강건성)와 검증 실험(조건 변화 시 혼동 여부)을 함께 제시한다.
5. 문헌 근거가 필요한 주장(예: 특정 고조파가 ESR 에 민감)은 `literature-researcher` 로 확인하고, 미확인이면 명시한다.

## 출력 형식
- **지표 표**: 지표 | 물리적 근거 | 노화 시 변화 | 교란 요인 | 측정/계산 방법 | 프로젝트 적용성
- **신호→지표→진단 흐름도**(텍스트)
- **권고**: 우선 검토할 feature, 필요한 추가 신호/실험, 위험 요소

## 주의사항
- 수명 종료 기준, 온도 계수 같은 숫자는 문헌·데이터시트에 따라 다르므로 "일반적으로", "출처 확인 필요" 를 붙인다.
- 시뮬레이션에서 노화를 C/ESR 값 변경으로만 모사한 경우, 실제 노화의 주파수 의존성·온도 의존성은 반영되지 않았음을 한계로 적는다.

## 다른 Skill과의 조합
- `npc-inverter-expert`: 커패시터 전류의 발생 원인
- `signal-analyzer`: 지표 계산의 신뢰성
- `python-analyzer`: 라벨/feature 구현 확인
- `literature-researcher` / `paper-code-bridge`: 문헌 방법과 프로젝트 연결
