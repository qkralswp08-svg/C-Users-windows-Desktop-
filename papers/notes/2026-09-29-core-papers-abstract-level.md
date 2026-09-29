# 핵심 논문 노트 (초록 수준) — 2026-09-29 문헌조사

> 근거 수준: **본문 확인 불가** (컨테이너 네트워크 정책). 모든 항목은 검색 색인의 초록/스니펫 기준이며, paper-analyzer 17항목 정독은 PDF 확보 후 `papers/notes/<연도>-<저자>-<제목>.md` 로 개별 작성할 것.
> 표기: (사실) 초록 명시 / (해석) 분석자 해석 / (추론) 회로 이론에서 도출 / (미확인) 본문 필요.

## K4 = M3. Ribeiro, Han et al. (2025) — Online Estimation of DC-link Capacitor Parameters of Three-Level NPC Converters Using Inherent Signals Analysis. IEEE/CAA J. Autom. Sinica 12, DOI 10.1109/JAS.2025.125159
1. 목적(사실): 계통연계 3L-NPC-VSI 의 DC-link 커패시터 C·ESR 을 기존 센서만으로 온라인 추정.
3. 제안(사실): PWM 전략과 토폴로지의 상호작용으로 생기는 고유 상호변조 신호를 비정수 재귀 슬라이딩 DFT 로 추적하고 망각계수 RLS 와 결합한 관측기 구조(oSDFT-RLS)로 시간-주파수 영역에서 C·ESR 추정.
5–9. 수식·Figure·스펙트럼: (미확인). 추론: 상호변조 성분은 NP 전류의 3f1 성분과 스위칭 측대파 조합일 가능성.
10–11. 조건: (미확인).
13. 입력: 기존 센서(사실). 14. 결과: (미확인).
15. 장점(사실): 무주입, 추가 HW 없음. 16. 한계(추론): 성분 크기가 변조·부하 의존 가능.
17. 프로젝트: 최우선 정독. "NPC 자연 스펙트럼으로 커패시터 진단" 의 유일한 저널 선례이므로 프로젝트의 신규성 경계를 정한다.

## K6 = M1. Min, Choi, Blaabjerg (2026) — An Online Condition Monitoring Method for DC-Link Capacitors of Three-Level NPC Inverters Based on Charge-Discharge Profile. IEEE TIE 73(8):12452–12463
1. 목적(사실): 3L-NPC 상·하단 DC-link 커패시터 C 개별 온라인 추정.
3. 제안(사실): 기준전압 오프셋 주입으로 vC1−vC2 를 설정치까지 발산시키고, 그 충방전 프로파일(도달 전하)에서 C 계산; 출력전류 영향 보상 전략.
14. 결과(사실): 평균 오차 <1%, 추가 HW 없음.
16. 한계(해석): 주입형; ESR 추정 여부 미확인.
17. 프로젝트: "상·하단 개별 진단" 비교 기준. 무주입 개별 진단이 차별점.

## K5 = M2. Ribeiro, Alves, de Sousa, Oliveira (2024) — Online condition monitoring for DC-link capacitors of three-level NPC converters using noninvasive signal injection. Comput. Electr. Eng. 119:109577, DOI 10.1016/j.compeleceng.2024.109577
3. 제안(사실): 상호고조파 주파수의 영상분 구형파를 기준전압에 더해 NP 전류 주입; Wavelet 분해로 여러 주파수 성분에서 ESR·C 동시 추정; HW·제어 알고리즘 변경 없음; 주입 크기는 전력품질 한계와 절충.
14. 결과(사실): 오차 <2%, Fourier 접근 대비 우수.
16. 한계(사실): 주입에 따른 전력품질 제약. (미확인) C1/C2 분리 여부.
17. 프로젝트: 주입형 대 무주입 고조파 접근의 대조군; Wavelet 대 FFT 비교 근거.

## K3 = P26. Ghadrdan, Peyghami, Mokhtari, Blaabjerg (2022) — Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor. IEEE TPEL 37(8):9733–9744, DOI 10.1109/TPEL.2022.3153842
3. 제안(사실): 출력(AC) 전류로 커패시터 전류의 스위칭 주파수 성분을 재구성, DC-link 전압과 함께 DF=ω·C·ESR 계산; DF 를 수명 지표로 제안하고 EoL 기준 제시; 스위칭 주파수·ESL·계통 필터의 영향 언급.
15. 장점(사실): 커패시터 전류 센서 불필요. 16. 한계(추론): DF 단독으로 C/ESR 분리 불가.
17. 프로젝트: 스위칭 상태×상전류 재구성 철학의 저널 선례. 재구성 수식은 본문 확인 필요.

## K7 = M5. Zhang, He, Wang, Chen (2023) — A Comprehensive Method for Online Switch Fault Diagnosis and Capacitor Condition Monitoring of Three-Level T-Type Inverters. IEEE TPEL 38(8):10183–10195, DOI 10.1109/TPEL.2023.3262758
3. 제안(사실): DC-link·AC 측 모델로 정상/OC 고장 시 고유 DC-link 고조파 성분 도출; 커패시터 전류 재구성; 스위치 OC 검출(출력전류·미분)과 위치 판별(상전류 잔차, NP 전압 잔차 합); 프레임워크에 signal injection·extra hardware 서브모듈 언급.
17. 프로젝트: 3레벨 고유 고조파 모델링의 참고. 커패시터 파라미터 종류(C/ESR) 미확인.

## K9 = D3. (저자 확인 필요) — Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters. IEEE TIE 72(4):4227–4237
3. 제안(사실): 정상 운전 신호(DC-link 전압 리플 PSD)로 GPR 학습, C 추정과 예측 불확실성 제공; 추가 HW·주입 없음; 저샘플링.
14. 결과(사실): 여러 부하·출력 주파수에서 실험 프로토타입 평균 오차 <2%.
17. 프로젝트: 다중 운전조건 검증 프로토콜과 불확실성 보고의 벤치마크.

## K8 = D2. Park, Kim, Kwak (2022) — Deep learning-based estimation technique for capacitance and ESR of input capacitors in single-phase DC/AC converters. J. Power Electron. 22:513–, DOI 10.1007/s43236-021-00366-x
3. 제안(사실): 커패시터 전압·전류 실험 파형의 FFT 에서 2·f1 과 fsw 지배 성분을 DNN 입력으로 사용해 C·ESR 회귀.
17. 프로젝트: "물리적으로 선택한 소수 고조파 → NN" 의 선례(단상). 3상 NPC·스위치/NP 전류·CNN 으로의 확장이 차별점. 정확도·조건 범위 미확인.

## K2 = P20. Sundararajan et al. (2020) — Condition Monitoring of DC-Link Capacitors Using Goertzel Algorithm for Failure Precursor Parameter and Temperature Estimation. IEEE TPEL 35(6):6386–6396, DOI 10.1109/TPEL.2019.2951859
3. 제안(사실): Goertzel 단일 빈 DFT 로 선택 주파수 성분 추출 → ESR(열화 지표), C(열화 지표 + 온도 민감 파라미터 → 코어/핫스팟 온도).
17. 프로젝트: CNN 입력 feature 를 소수 빈으로 줄이는 경량 추출기; 온도 지표 확보 방법. 선택 빈·전류 측정 방식 미확인.

## K10 = M25. Deng et al. (2025) — Online evaluation method for MMC submodule capacitor aging based on CapAgingNet. Global Energy Interconnection 8(3):420–432
3. 제안(사실): MMC 시뮬레이션 플랫폼으로 노화 상태별 SM 스위칭 상태 시퀀스 데이터셋 구축, 딥 네트워크로 노화 등급 분류(Top-1 95.32%, F1 95.49%), 추가 샘플링 채널 없음.
16. 한계(사실): 시뮬레이션 데이터만.
17. 프로젝트: 시뮬 기반 DL 분류의 한계(실험 부재)를 보여주는 대조군; 프로젝트 F 단계(실험) 필요성의 근거.

## K1 = R3. Zhao, Davari, Lu, Wang, Blaabjerg (2021) — An Overview of Condition Monitoring Techniques for Capacitors in DC-Link Applications. IEEE TPEL 36(4):3692–3716, DOI 10.1109/TPEL.2020.3023469
(사실) 응용 목적·구현 방식·정확도 기준의 비교 평가 개관. 프로젝트: 관련연구 절 기준 리뷰, 분류 용어 통일.

## 보조: P35 Baumann 2024 (정지 시 방전 프로파일 + 온도 보상 SoH), P39 Muhammed Ramees & Ahmad 2026 (MPPT 전이 자연 여기), M28 (암 내 SM 비교로 온도 분리) — 최근 흐름 대표.

## 프로젝트 To-Do (3개)
1. M3, M1, M2 PDF 확보 → paper-analyzer 정독 → 프로젝트 신규성 경계 확정.
2. MATLAB 민감도 실험(보고서 20.3 A–B): C1/C2/ESR 스윕 대 부하/변조 스윕에서 iSa2·ia·iNP·vNP 고조파 민감도 비교.
3. 인용용 서지 재확인: `harness/tools/Search-Papers.ps1` 로 (확인 필요) 항목 채우기.
