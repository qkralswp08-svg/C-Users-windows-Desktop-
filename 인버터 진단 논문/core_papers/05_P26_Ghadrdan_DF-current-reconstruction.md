# [S-5] Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor

- 저자: M. Ghadrdan, S. Peyghami, H. Mokhtari, F. Blaabjerg
- 연도: 2022
- 저널: IEEE Transactions on Power Electronics, vol. 37, no. 8, pp. 9733–9744
- DOI: 10.1109/TPEL.2022.3153842
- 근거 수준: **Abstract-level only** — 본문(수식·Figure·실험)은 확인하지 못했다. 아래 "본문 확인 후 채울 항목" 은 PDF 확보 후 작성할 것.
- 역할: **Methodology donor** / Tier S / 읽기 목록 A
- 진단 대상 커패시터: 2L back-to-back DC-link 전해 커패시터
- 서지 확인 메모: 없음

## 1. 왜 읽어야 하는가
'출력(상) 전류와 스위칭 상태로 커패시터 전류의 스위칭 주파수 성분을 재구성' 해 진단한 저널 논문. 내 연구가 시뮬레이션에서 iSa2, iC1, iC2 를 스위칭 상태로 만드는 것과 같은 철학이며, 실제 장치에서 커패시터 전류 센서 없이 feature 를 얻는 방법의 선례다. Aalborg VBN 에 accepted manuscript 가 있을 가능성.

## 2. 내 연구와 같은 점
커패시터 전류 재구성(상전류×스위칭 상태) · 스위칭 주파수 성분 · 추가 센서 없음 · 온라인 · 실험.

## 3. 내 연구와 다른 점
2L B2B(NPC 아님). HI 가 DF(=ωC·ESR) 하나라 C/ESR 분리 불가. 데이터 기반 아님. 스위칭 주파수·ESL·필터 영향이 정확도에 미침(저자).

## 4. 집중해서 읽을 부분
(1) 재구성 수식(스위칭 함수 정의, 데드타임·ESL 처리). (2) fsw 성분 추출 방법과 DF 계산. (3) EoL 기준 정의. (4) 스위칭 주파수·필터·ESL 영향 분석 — 내 시뮬 설정(fsw, 필터)에 그대로 적용. (5) 실험에서 노화를 어떻게 모사했는가.

## 5. 타 토폴로지 이전 가능성
재구성 틀은 NPC 로 이전 가능(스위칭 함수를 3레벨로 확장).

## 6. AI/ML/CNN 적용 가능성
재구성 전류의 스펙트럼을 CNN 입력으로 쓰는 전처리 단계의 근거.

## 7. 평가 점수 (0 없음·미확인 / 1 부분 / 2 충족)
| 기준 | 점수 |
|---|---|
| 3L-NPC/멀티레벨 관련성 | 0 |
| 노화·열화 직접 진단 | 2 |
| C/ESR/SOH 추정 | 2 |
| 전류/전압 파형 사용 | 2 |
| Harmonic/FFT/STFT/Wavelet | 2 |
| 기존 인버터 센서만 | 2 |
| Online 진단 | 2 |
| AI/ML/CNN/LSTM 적용 가능성 | 1 |
| 타 토폴로지 이전 가능성 | 2 |
| **합계** | **15** / 18 |

## 8. 본문 확인 후 채울 항목 (paper-analyzer 17항목)
1. 연구 목적:
2. 기존 방법의 문제점:
3. 제안 방법:
4. 시스템 구조(토폴로지, 커패시터 종류/정격, 센서 위치):
5. 중요한 수식(번호, 변수 정의):
6. 변수의 물리적 의미(프로젝트 변수 대응: iSa2, iC1/iC2, iNP, vC1/vC2, vNP):
7. Figure 해석:
8. Waveform 해석:
9. Spectrum 해석(어떤 성분, 차수, 조건):
10. 실험 조건(정격, 부하, fsw, 샘플링, 온도, 노화 모사):
11. Simulation 조건:
12. Algorithm 단계:
13. 입력 신호(측정/계산, 센서 수):
14. 출력 결과(오차, 비교 대상):
15. 장점:
16. 한계(저자 인정 / 분석자 판단):
17. 현재 프로젝트 활용(신호·feature·구현·비교 실험·관련연구):

## 9. 사실 / 해석 / 추론 요약 (본문 확인 후)
- 사실:
- 해석:
- 추론:
