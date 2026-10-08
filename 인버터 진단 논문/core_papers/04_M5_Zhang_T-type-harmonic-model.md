# [S-4] A Comprehensive Method for Online Switch Fault Diagnosis and Capacitor Condition Monitoring of Three-Level T-Type Inverters

- 저자: W. Zhang, Y. He, X. Wang, J. Chen
- 연도: 2023
- 저널: IEEE Transactions on Power Electronics, vol. 38, no. 8, pp. 10183–10195
- DOI: 10.1109/TPEL.2023.3262758
- 근거 수준: **Abstract-level only** — 본문(수식·Figure·실험)은 확인하지 못했다. 아래 "본문 확인 후 채울 항목" 은 PDF 확보 후 작성할 것.
- 역할: **Physical-model reference / Methodology donor** / Tier S / 읽기 목록 B
- 진단 대상 커패시터: 3L T-type 분할 DC-link
- 서지 확인 메모: 없음

## 1. 왜 읽어야 하는가
3레벨 토폴로지에서 'DC-link 측 고유 고조파 성분' 을 모델로 도출하고 커패시터 전류를 재구성해 진단에 쓴 저널 논문. 내 연구가 필요로 하는 '3레벨 DC-link/NP 고조파의 해석적 모델' 을 가장 가까운 형태로 제공할 가능성이 크다.

## 2. 내 연구와 같은 점
3레벨(분할 DC-link, NP 전압) · 고유 고조파 모델 · 커패시터 전류 재구성 · 출력 전류 사용 · 온라인.

## 3. 내 연구와 다른 점
T-type(NPC 와 스위치 구조·도통 경로가 다름). 스위치 OC 고장진단이 주이고 커패시터 CM 은 서브모듈. 'signal injection'·'extra hardware' 서브모듈이 언급되어 완전 센서리스가 아닐 수 있음. 추정 파라미터(C/ESR) 미확인. 데이터 기반 아님.

## 4. 집중해서 읽을 부분
(1) DC-link 전류/전압 고유 고조파의 유도 과정(스위칭 함수 × 상전류)과 결과 식 — NPC 에 그대로 바꿔 쓸 수 있는지. (2) 커패시터 전류 재구성 식. (3) NP 전압 잔차 정의. (4) 커패시터 CM 서브모듈이 어떤 성분으로 무엇을 추정하는지. (5) 추가 HW 가 무엇인지.

## 5. 타 토폴로지 이전 가능성
T-type → NPC 로 모델 이전 가능성 높음(도통 경로만 수정).

## 6. AI/ML/CNN 적용 가능성
고유 고조파 모델이 주는 '이론 스펙트럼' 을 CNN 의 물리 유도 feature 로 사용 가능.

## 7. 평가 점수 (0 없음·미확인 / 1 부분 / 2 충족)
| 기준 | 점수 |
|---|---|
| 3L-NPC/멀티레벨 관련성 | 2 |
| 노화·열화 직접 진단 | 1 |
| C/ESR/SOH 추정 | 1 |
| 전류/전압 파형 사용 | 2 |
| Harmonic/FFT/STFT/Wavelet | 2 |
| 기존 인버터 센서만 | 1 |
| Online 진단 | 2 |
| AI/ML/CNN/LSTM 적용 가능성 | 1 |
| 타 토폴로지 이전 가능성 | 2 |
| **합계** | **14** / 18 |

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
