---
name: npc-inverter-expert
description: 3-Level NPC 인버터의 스위칭 상태, 스위치 전류(Sa1/Sa2 등), 상전류, 중성점 전류, DC-link/상·하단 커패시터 전류, PWM/SVPWM, 스위칭 주파수 성분을 물리적으로 해석한다. Use when the request mentions NPC inverter, switching states, switch/phase/neutral-point/DC-link currents, PWM or modulation.
keywords: [npc, 3-level, 3레벨, 3 레벨, three-level, 인버터, inverter, 컨버터, converter, 스위칭, switching, 스위치 전류, switch current, sa1, sa2, sa3, sa4, sb1, sb2, isa, isb, isc, 중성점, neutral point, neutral, 중성점 전류, dc-link 전류, dc link current, 상단 커패시터, 하단 커패시터, upper capacitor, lower capacitor, pwm, svpwm, 변조, modulation, 상전류, phase current, 클램프, clamping diode, 데드타임, dead time, 전압 불평형, voltage imbalance]
order: 30
combine-with: [signal-analyzer, capacitor-aging-expert, matlab-analyzer]
---

# npc-inverter-expert

## 목적
3-Level NPC(Neutral Point Clamped) 인버터에서 "어떤 스위칭 상태에서 어떤 경로로 전류가 흐르는가"를 기준으로 스위치 전류·중성점 전류·커패시터 전류의 파형과 스펙트럼을 물리적으로 설명한다. 이 프로젝트에서 커패시터 노화 진단 신호(예: iSa2, iC1, iC2, iNP)가 왜 그런 모양인지 판단하는 근거를 제공한다.

## 언제 사용하는가
- iSa2 등 특정 스위치 전류의 구성 성분과 고조파 원인
- 중성점 전류, 상·하단 커패시터 전류의 관계와 스펙트럼
- PWM/SVPWM 방식, 변조지수, 스위칭 주파수가 전류 스펙트럼에 미치는 영향
- 시뮬레이션 모델(MATLAB/Simulink/PLECS)의 회로·스위칭 설정 검토

## 핵심 물리 (판단 기준)
- 한 상(phase)의 레그: 직렬 스위치 4개 `Sx1, Sx2, Sx3, Sx4`, 클램프 다이오드 2개. 스위칭 상태 P(+Vdc/2: Sx1,Sx2 ON), O(0: Sx2,Sx3 ON), N(−Vdc/2: Sx3,Sx4 ON). `Sx1↔Sx3`, `Sx2↔Sx4` 는 상보.
- 내측 스위치 `Sx2` 는 P 와 O 상태 모두에서 ON 이므로, 상전류가 양(+)인 구간의 대부분을 흘린다 → 대략 "반파 정류된 상전류 × 스위칭 함수" 형태. 외측 스위치 `Sx1` 은 P 상태에서만 흘린다.
- 중성점 전류 `iNP` = O 상태에 있는 상들의 상전류 합. 상단 커패시터 전류 `iC1` 와 하단 `iC2` 는 DC 입력 전류와 P/N 상태 전류의 차로 결정되며 `iC1 − iC2` 가 `iNP` 와 연결된다 (기준 방향은 코드/모델의 정의를 따른다).
- 저주파 성분: 3상 평형·정현 변조에서 `iNP` 와 커패시터 전압 리플에는 기본파의 3배(3f1) 성분이 대표적으로 나타난다. 반파 정류형 파형(예: 한 방향 전류만 흘리는 스위치 전류)은 DC + 기본파 + 짝수 고조파(2f1, 4f1, …)를 가진다. → 이는 파형 대칭성에서 나오는 수학적 사실이며, 특정 논문의 주장으로 표현하지 말 것.
- 고주파 성분: `m·fsw ± n·f1` 측대파. 변조 방식(SPWM, SVPWM, 불연속 PWM), 변조지수, 역률에 따라 분포가 바뀐다.
- 중성점 전압 불평형은 `iNP` 의 저주파 성분이 두 커패시터를 비대칭으로 충방전해 생기며, 커패시터 C 또는 ESR 이 서로 다르면(노화 불균형) 리플 크기·위상이 달라진다.

## 절차
1. 대상 신호의 정의(기준 방향, 측정 지점)를 코드/모델에서 확인한다 (`matlab-analyzer` 와 함께).
2. 한 기본파 주기를 P/O/N 상태 구간으로 나누고, 각 구간에서 그 신호가 어떤 상전류의 어떤 부분인지 적는다 (도통 경로 표).
3. 그로부터 기대되는 파형 형태와 대칭성을 도출하고, 기대 스펙트럼(저주파 차수, 스위칭 측대파)을 예측한다.
4. 실제 시뮬레이션/측정 스펙트럼(`signal-analyzer`)과 대조해 일치/불일치를 표로 정리한다. 불일치는 변조 방식, 데드타임, 부하 역률, 계산 설정 순으로 원인을 점검한다.
5. 커패시터 상태(C, ESR)가 이 신호의 어떤 성분에 영향을 주는지 `capacitor-aging-expert` 와 연결한다.

## 출력 형식
- **도통 경로 표**: 스위칭 상태 | 상전류 부호 | 도통 소자 | 대상 신호 값
- **기대 파형/스펙트럼 vs 실제** 비교표
- **결론**: 사실(코드·데이터) / 물리적 추론 / 문헌 근거 필요 항목 구분

## 주의사항
- 특정 고조파 성분의 존재를 "논문에 있다" 고 말하려면 `literature-researcher` 로 실제 문헌을 확인해야 한다. 이 Skill 의 설명은 회로 이론에 기반한 추론이다.
- 전류 기준 방향과 스위치 명명(Sa1 이 최상단인지)은 프로젝트마다 다르다. 반드시 코드/모델 정의를 먼저 확인한다.

## 다른 Skill과의 조합
- `signal-analyzer`: 스펙트럼 계산과 성분 표
- `capacitor-aging-expert`: 신호 → 노화 지표 연결
- `matlab-analyzer`: 시뮬레이션 코드에서 신호 정의 확인
- `literature-researcher`: 문헌 근거 확보
