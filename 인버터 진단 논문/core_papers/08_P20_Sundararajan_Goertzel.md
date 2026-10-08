# [A-8] Condition Monitoring of DC-Link Capacitors Using Goertzel Algorithm for Failure Precursor Parameter and Temperature Estimation

- 저자: P. Sundararajan, M. H. M. Sathik, F. Sasongko, C. S. Tan, J. Pou, F. Blaabjerg, A. K. Gupta
- 연도: 2020
- 저널: IEEE Transactions on Power Electronics, vol. 35, no. 6, pp. 6386–6396
- DOI: 10.1109/TPEL.2019.2951859
- 근거 수준: **Abstract-level only** — 본문(수식·Figure·실험)은 확인하지 못했다. 아래 "본문 확인 후 채울 항목" 은 PDF 확보 후 작성할 것.
- 역할: **Methodology donor** / Tier A / 읽기 목록 B
- 진단 대상 커패시터: 정류기 전단 3상 인버터 DC-link 전해
- 서지 확인 메모: Aalborg VBN/CORE 에 accepted manuscript 존재 가능.

## 1. 왜 읽어야 하는가
전체 FFT 대신 Goertzel 로 '관심 빈 몇 개만' 뽑아 ESR·C·온도를 추정. 내 연구가 feature 를 소수 고조파로 줄여 임베디드 구현까지 가려면 가장 직접적인 방법론 공여자이며, 온도를 C 로 추정하는 아이디어는 온도 교란 문제의 해법 후보.

## 2. 내 연구와 같은 점
고조파 성분 기반 · ESR+C · 온라인 · 3상 인버터.

## 3. 내 연구와 다른 점
2L(정류기 전단). 커패시터 전류 측정 여부 미확인. 데이터 기반 아님. 온도 추정 포함(내 연구에는 없음).

## 4. 집중해서 읽을 부분
(1) 어떤 주파수 빈을 쓰는가(fsw? 6f 정류 리플?). (2) ESR·C 추정식과 각 빈의 역할. (3) C 의 온도 의존성을 이용한 온도 추정 원리와 한계. (4) 아날로그 필터·FFT 대비 비용 비교. (5) 실험 조건.

## 5. 타 토폴로지 이전 가능성
Goertzel 추출은 모든 토폴로지에 적용 가능.

## 6. AI/ML/CNN 적용 가능성
CNN 입력 feature 추출기(저비용) 후보. 온도 feature 추가 가능.

## 7. 평가 점수 (0 없음·미확인 / 1 부분 / 2 충족)
| 기준 | 점수 |
|---|---|
| 3L-NPC/멀티레벨 관련성 | 0 |
| 노화·열화 직접 진단 | 2 |
| C/ESR/SOH 추정 | 2 |
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
