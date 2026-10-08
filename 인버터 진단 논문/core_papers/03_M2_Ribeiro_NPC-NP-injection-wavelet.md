# [S-3] Online condition monitoring for DC-link capacitors of three-level NPC converters using noninvasive signal injection

- 저자: R. L. A. Ribeiro, D. K. Alves, R. P. R. de Sousa, A. C. Oliveira
- 연도: 2024
- 저널: Computers and Electrical Engineering, vol. 119, art. 109577
- DOI: 10.1016/j.compeleceng.2024.109577
- 근거 수준: **Abstract-level only** — 본문(수식·Figure·실험)은 확인하지 못했다. 아래 "본문 확인 후 채울 항목" 은 PDF 확보 후 작성할 것.
- 역할: **Core competitor / Methodology donor (Wavelet)** / Tier S / 읽기 목록 A
- 진단 대상 커패시터: 3L-NPC 분할 DC-link (중성점 경로)
- 서지 확인 메모: SSRN 4875339 프리프린트 확인 권장.

## 1. 왜 읽어야 하는가
M3 의 전신으로, 중성점 전류 경로를 이용해 ESR 과 C 를 동시에 추정하며 Wavelet 분해를 쓴다. 내 연구의 'NP 경로 고조파' 와 같은 물리를 능동 주입으로 구현한 사례이므로, 무주입 접근의 차별점을 서술할 때 직접 대조 대상이다. SSRN 프리프린트(4875339)가 있어 본문 접근 가능성이 높다.

## 2. 내 연구와 같은 점
3L-NPC · 중성점 전류 이용 · 시간-주파수(스펙트럼) 분해 · ESR+C · HW·제어 변경 없음.

## 3. 내 연구와 다른 점
영상분 구형파(상호고조파)를 기준전압에 더하는 '주입형'. Wavelet(FFT 아님). 데이터 기반 아님. 전력품질 제약을 저자가 언급.

## 4. 집중해서 읽을 부분
(1) NP 전류가 C1/C2 로 나뉘어 흐르는 모델과 각 주파수에서의 임피던스 식. (2) Wavelet 대 Fourier 비교 결과(<2% 주장)의 조건. (3) 주입 크기 결정 기준(전력품질). (4) C1/C2 분리 가능 여부. (5) 어떤 주파수에서 ESR 이, 어떤 주파수에서 C 가 잘 보이는지 — 내 feature 대역 선정에 직접 참고.

## 5. 타 토폴로지 이전 가능성
영상분 주입은 T-type·ANPC 에 이전 가능. 2L 에는 중성점이 없어 불가.

## 6. AI/ML/CNN 적용 가능성
Wavelet 계수를 CNN 입력(시간-주파수 이미지)으로 쓰는 변형이 가능.

## 7. 평가 점수 (0 없음·미확인 / 1 부분 / 2 충족)
| 기준 | 점수 |
|---|---|
| 3L-NPC/멀티레벨 관련성 | 2 |
| 노화·열화 직접 진단 | 2 |
| C/ESR/SOH 추정 | 2 |
| 전류/전압 파형 사용 | 2 |
| Harmonic/FFT/STFT/Wavelet | 2 |
| 기존 인버터 센서만 | 2 |
| Online 진단 | 2 |
| AI/ML/CNN/LSTM 적용 가능성 | 1 |
| 타 토폴로지 이전 가능성 | 1 |
| **합계** | **16** / 18 |

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
