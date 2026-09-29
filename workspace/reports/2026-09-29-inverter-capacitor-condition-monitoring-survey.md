# 인버터 커패시터 노화진단·상태진단 기술 동향 조사 (저널 논문 중심)

- 작성일: 2026-09-29
- 수행 방식: Harness Skill 조합 `literature-researcher → paper-analyzer → paper-comparator` + `capacitor-aging-expert` / `npc-inverter-expert`
- 목적: 인버터·전력변환기 내부 커패시터의 노화/상태진단 분야의 현재 기술 수준과 Research Gap 을 파악하고, 향후 새로운 진단 방법(3-Level NPC, 스위치/커패시터 전류 고조파, CNN) 설계의 근거를 마련한다.

---

## 0. 반드시 먼저 읽을 것 — 근거 수준과 검증 한계

이 조사는 클라우드 컨테이너에서 수행되었고, 컨테이너의 네트워크 정책이 학술 사이트(ieeexplore.ieee.org, sciencedirect.com, mdpi.com, link.springer.com, onlinelibrary.wiley.com, doi.org, api.crossref.org, semanticscholar.org, arxiv.org 등)로의 접근을 차단했다. 그 결과:

| 항목 | 상태 |
|---|---|
| 논문 **본문(Methodology, 수식, Figure, 실험 조건)** | **전 논문 확인 불가**. 모든 방법 서술은 검색 색인의 **초록/스니펫 수준**이다 (사용자 요청 19절 기준 "본문 확인 불가" 등급). |
| 서지정보(저널명, 권/호/쪽, DOI) | 검색 결과에 **그대로 표시된 값만** 기록. 표시되지 않은 항목은 `(확인 필요)`. DOI·권·쪽을 추정하거나 만들어내지 않았다. |
| 저널/학회 구분 | IEEE Xplore 결과의 "Journals & Magazine" 라벨, ScienceDirect PII, Springer/Wiley/MDPI/IET/J-STAGE 저널 URL 로 판별. 학회 논문은 본 목록에서 제외하고 부록 B 에만 언급. |
| 검색 폭 | 세션 웹 검색 예산(200회) 소진으로 일부 계획 검색(UPS, 계통연계 고조파 주입, Flying-capacitor 2차 검색, 6f 정류 리플 기반 C 추정, 2020년대 Kalman 계열)이 미실행. 해당 항목은 "미조사"로 표기. |

**따라서 이 보고서의 모든 기술 서술은 "초록 기준" 이며, 본문 근거가 필요한 주장(특정 수식·특정 고조파의 존재·실험 정확도)은 확인된 범위에서만 적고 나머지는 "미확인" 으로 남겼다.** 서지정보는 인용 전에 IEEE Xplore/ScienceDirect 에서 재확인해야 하며, 로컬 PC 에서 `pwsh -File harness\tools\Search-Papers.ps1 -Query "<논문 제목>" -Source all` 로 대부분의 `(확인 필요)` 칸을 채울 수 있다 (부록 C 에 목록).

근거 등급 표기: **L1** = 저널·연도·권/호/쪽·DOI 모두 스니펫에서 확인 / **L2** = 저널명·연도는 출판사 URL 로 확인, 나머지 미확인 / **L3** = 제목만 확인, 저널은 문맥 추정. 방법 설명은 전부 "초록" 수준.

사실 / 해석 / 추론 구분: 본문에서 **(사실)** = 초록·스니펫에 명시된 내용, **(해석)** = 그 결과에 대한 전력전자 관점 해석, **(추론)** = 논문이 말하지 않았지만 회로 이론·수식에서 도출한 판단.

---

## 1. 조사 범위와 기준

| 구분 | 포함 | 제외 |
|---|---|---|
| 문헌 종류 | Peer-reviewed 저널 논문 (IEEE Trans./JESTPE/OJ/Access, IET, Elsevier, Springer, Wiley, MDPI, J-STAGE, KIPE JPE 등) | 학회 논문·프로시딩, 학위논문, 특허, 기술보고서, 프리프린트 (기술 계보 추적용으로 부록 B 에만 별도 언급) |
| 기간 | 2020–2026 우선. 기반 기술은 2005–2019 포함 | — |
| 커패시터 | DC-link(단일/분할 상·하단), 중성점 관련, Flying/Nested, CHB 셀, MMC 서브모듈, AC 측 필터(LCL/출력), 스너버·클램프·공진 | 단순히 회로에 존재만 하는 커패시터 |
| 토폴로지 | 2-Level VSI, 3L-NPC, ANPC, T-type, FC, CHB, MMC, PV·모터·견인/EV·계통연계·항공·풍력 | — |
| 진단 대상 | ESR, C, DF, 임피던스, 온도, SoH/RUL, 노화 등급 | 스위치 고장진단 단독 연구 |

Online 구분: **Online** = 정상 운전 중 기존 신호로 추정 (능동 주입 포함 시 "Online(주입)"), **Quasi-online** = 기동/정지/방전/무부하/야간 등 특정 구간 이용, **Offline** = 분해·정지 후 계측.

---

## 2. 검색 전략

### 2.1 질문 구조화

| 축 | 값 |
|---|---|
| 대상 시스템 | 2L VSI / 3L-NPC·ANPC·T-type / FC / CHB / MMC / PV·드라이브·EV·계통연계 |
| 커패시터 위치·종류 | DC-link(AEC/필름) / 분할 DC-link / SM / 필터(필름) / MLCC |
| 신호 | DC-link 전압·전류, 커패시터 전류(측정/재구성), 상전류, 스위치 전류, 중성점 전류·전압, 스위칭 신호 |
| 방법 | 리플 비 / RLS·Kalman·관측기 / 주입 / 충방전·방전 프로파일 / FFT·Goertzel·SDFT·Wavelet / ML·DL |
| HI | ESR, C, DF, |Z|, 온도, SoH, RUL, 노화 등급 |
| 검증 | 시뮬레이션 / 실험(교체·직렬저항 등 모사 노화 / 가속수명) / 다중 운전조건 |

### 2.2 키워드 그룹과 조합 (실제 실행)

| 그룹 | 예시 키워드 |
|---|---|
| 기본 | inverter capacitor aging/degradation, capacitor condition/health monitoring, capacitor fault diagnosis, lifetime estimation |
| DC-link | DC-link capacitor ESR estimation, DC-link capacitance estimation ripple, film capacitor condition monitoring DC-link, electrolytic capacitor RLS, Kalman ESR, impedance estimation online |
| 멀티레벨 | NPC inverter DC-link capacitor condition monitoring, split DC-link / neutral point current capacitance, T-type capacitor aging, flying capacitor condition monitoring, CHB capacitor monitoring, MMC submodule capacitor capacitance/ESR estimation |
| 신호 | capacitor current spectrum aging, ripple current condition monitoring, capacitor FFT/Goertzel/wavelet, switching frequency ripple ESR, second harmonic capacitance single-phase, discharge time constant, charging profile, signal injection impedance |
| AI | deep learning / CNN / LSTM capacitor condition monitoring, machine learning ESR estimation, physics-informed capacitor degradation, digital twin converter, transfer learning capacitor |
| 센서리스·기타 | sensorless / no additional sensor / existing sensors capacitor monitoring, quasi-online, DSP implementation, LCL filter capacitor monitoring, snubber capacitor degradation, film self-healing metallized polypropylene, MLCC degradation, humidity film capacitor |

출처: 검색 엔진이 반환한 IEEE Xplore, ScienceDirect, Springer, Wiley/IET, MDPI, J-STAGE, KoreaScience, Semantic Scholar, ADS, 대학 리포지터리(Aalborg VBN, EPFL Infoscience, SeoulTech Pure, NTU DR) 색인 항목. 5개 주제(리뷰·파라미터 추정 / 멀티레벨·응용 / 고조파·전류·충방전 / ML·DL·하이브리드 / 센서리스·기타 커패시터·소재)로 병렬 탐색 후 DOI·제목 기준 병합.

### 2.3 Stage 구성

Stage 1 넓은 탐색(약 100편 후보) → Stage 2 분류(5절) → Stage 3 핵심 10편 선정(6절) → Stage 4 심층 분석: **본문 접근 불가로 미수행**, 초록 수준 카드로 대체(6절) → Stage 5 기술 동향·Gap(16–18절).

---

## 3. 저널 논문 목록 (서지)

ID 접두어: **R** 리뷰 / **P** DC-link 파라미터·신호·충방전 기반 / **M** 멀티레벨·응용 특화 / **D** 데이터 기반(ML·DL·하이브리드) / **E** 기타 커패시터·소재 메커니즘. `저자` 는 스니펫에 보인 범위(첫 저자 등)만 기록.

### 3.1 리뷰·개관

| ID | 제목 | 저자 | 연도 | 저널 (권/호/쪽) | DOI | 등급 |
|---|---|---|---|---|---|---|
| R1 | Reliability of Capacitors for DC-Link Applications in Power Electronic Converters—An Overview | H. Wang, F. Blaabjerg | 2014 | IEEE Trans. Ind. Appl. 50(5):3569–3578 | 10.1109/TIA.2014.2308357 | L1 |
| R2 | A Review of the Condition Monitoring of Capacitors in Power Electronic Converters | H. Soliman, H. Wang, F. Blaabjerg | 2016 | IEEE Trans. Ind. Appl. 52(6):4976–4989 | 10.1109/TIA.2016.2591906 | L1 |
| R3 | An Overview of Condition Monitoring Techniques for Capacitors in DC-Link Applications | Z. Zhao, P. Davari, W. Lu, H. Wang, F. Blaabjerg | 2021 | IEEE Trans. Power Electron. 36(4):3692–3716 | 10.1109/TPEL.2020.3023469 | L1 |
| R4 | Advances in Capacitor Health Monitoring Techniques for Power Converters: A Review | M. K. P. Muhammed Ramees, M. W. Ahmad | 2023 | IEEE Access 11:133540–133576 | (확인 필요) | L2 |
| R5 | Review of condition monitoring methods for capacitors used in power converters | L. P. Arokia Nathan et al. (확인 필요) | 2023 | Microelectronics Reliability 145:115003 | 10.1016/j.microrel.2023.115003 | L2 |
| R6 | Review of Health Monitoring Techniques for Capacitors Used in Power Electronics Converters | (확인 필요) | 2020 | Sensors 20(13):3740 | 10.3390/s20133740 | L2 |
| R7 | Condition Monitoring of Submodule Capacitors in Modular Multilevel Converters—A Review | (확인 필요) | 2025 | Journal of Energy Storage (PII S2352152X25026672) | (확인 필요) | L2 |

### 3.2 DC-link 커패시터: 파라미터 추정·리플·주입·충방전 (2-Level 및 일반 컨버터)

| ID | 제목 | 저자 | 연도 | 저널 (권/호/쪽) | DOI | 등급 |
|---|---|---|---|---|---|---|
| P1 | Online capacitance estimation of DC-link electrolytic capacitors for three-phase AC/DC/AC PWM converters using recursive least squares method | D.-C. Lee, K.-J. Lee, J.-K. Seok, J.-W. Choi | 2005 | IEE Proc. Electr. Power Appl. 152(6):1503–1508 | 10.1049/ip-epa:20050027 | L1 |
| P2 | DC-Link Capacitance Estimation in AC/DC/AC PWM Converters Using Voltage Injection | A. G. Abo-Khalil, D.-C. Lee | 2008 | IEEE Trans. Ind. Appl. 44(5):1631–1637 | 10.1109/TIA.2008.2002181 | L1 |
| P3 | Condition Monitoring of DC-Link Electrolytic Capacitors in Adjustable-Speed Drives | K.-W. Lee et al. (확인 필요) | 2008 | IEEE Trans. Ind. Appl. (권/쪽 확인 필요; Xplore 4629383) | (확인 필요) | L2 |
| P4 | An Online and Noninvasive Technique for the Condition Monitoring of Capacitors in Boost Converters | A. M. R. Amaral, A. J. M. Cardoso (확인 필요) | 2010 | IEEE Trans. Instrum. Meas. (Xplore 5290120) | (확인 필요) | L2 |
| P5 | Life-Cycle Monitoring and Voltage-Managing Unit for DC-Link Electrolytic Capacitors in PWM Converters | M. A. Vogelsberger, T. Wiesinger, H. Ertl | 2011 | IEEE Trans. Power Electron. 26(2):493–503 | 10.1109/TPEL.2010.2059713 | L1 |
| P6 | On-line fault detection of aluminium electrolytic capacitors, in step-down DC–DC converters, using input current and output voltage ripple | A. M. R. Amaral, A. J. M. Cardoso | 2012 | IET Power Electron. 5(3):315–322 | 10.1049/iet-pel.2011.0163 | L1 |
| P7 | Condition Monitoring of DC-Link Capacitors in Aerospace Drives | K. Wechsler, B. C. Mecrow, D. J. Atkinson et al. | 2012 | IEEE Trans. Ind. Appl. 48(6):1866–1874 | (확인 필요) | L2 |
| P8 | Fault Diagnosis of DC-Link Capacitors in Three-Phase AC/DC PWM Converters by Online Estimation of Equivalent Series Resistance | X.-S. Pu, T. H. Nguyen, D.-C. Lee, K.-B. Lee, J.-M. Kim | 2013 | IEEE Trans. Ind. Electron. 60(9):4118–4127 | 10.1109/TIE.2012.2218561 | L1 |
| P9 | Deterioration Monitoring of DC-Link Capacitors in AC Machine Drives by Current Injection | T. H. Nguyen, D.-C. Lee | 2015 | IEEE Trans. Power Electron. 30(3):1126–1130 | 10.1109/TPEL.2014.2339374 | L1 |
| P10 | Online Monitoring Technique for Aluminum Electrolytic Capacitor in Solar PV-Based DC System | M. W. Ahmad, N. Agarwal, S. Anand | 2016 | IEEE Trans. Ind. Electron. 63(11):7059–7066 | (확인 필요) | L2 |
| P11 | Capacitor impedance estimation utilizing dc-link voltage oscillations in single phase inverter | A. Arya, M. W. Ahmad, N. Agarwal, S. Anand | 2017 | IET Power Electron. 10(9):1046–1053 | 10.1049/iet-pel.2016.0603 | L1 |
| P12 | Online Condition Monitoring for Both IGBT Module and DC-Link Capacitor of Power Converter Based on Short-Circuit Current Simultaneously | P. Sun, C. Gong, X. Du et al. | 2017 | IEEE Trans. Ind. Electron. 64(5):3662–3671 | (확인 필요) | L2 |
| P13 | Quasi-Online Technique for Health Monitoring of Capacitor in Single-Phase Solar Inverter | N. Agarwal, M. W. Ahmad, S. Anand | 2018 | IEEE Trans. Power Electron. 33(6):5283–5291 | 10.1109/TPEL.2017.2736162 | L1 |
| P14 | Noninvasive Technique for DC-Link Capacitance Estimation in Single-Phase Inverters | M. W. Ahmad, P. N. Kumar, A. Arya, S. Anand | 2018 | IEEE Trans. Power Electron. 33(5):3693–3696 | 10.1109/TPEL.2017.2762341 | L1 |
| P15 | Online Condition Monitoring System for DC-Link Capacitor in Industrial Power Converters | P. Sundararajan, M. H. M. Sathik, F. Sasongko et al. | 2018 | IEEE Trans. Ind. Appl. 54(5):4775–4785 | 10.1109/TIA.2018.2845889 | L1 |
| P16 | ESR and capacitance monitoring of a dc-link capacitor used in a three-phase PWM inverter with a front-end diode rectifier | K. Hasegawa, S. Nishizawa, I. Omura | 2018 | Microelectronics Reliability 88–90:433–437 | 10.1016/j.microrel.2018.07.023 | L1 |
| P17 | Health Estimation of Individual Capacitors in a Bank With Reduced Sensor Requirements | Y. Gupta, M. W. Ahmad, S. Narale, S. Anand | 2019 | IEEE Trans. Ind. Electron. 66(9):7250–7259 | (확인 필요) | L2 |
| P18 | High-Accuracy Capacitance Monitoring of DC-Link Capacitor in VSI Systems by LC Resonance | H. Li, D. Xiang, X. Han, X. Zhong, X. Yang | 2019 | IEEE Trans. Power Electron. 34(12):12200–12211 (확인 필요) | (확인 필요) | L2 |
| P19 | A VEN Condition Monitoring Method of DC-Link Capacitors for Power Converters | Y. Wu, X. Du | 2019 | IEEE Trans. Ind. Electron. 66(2):1296–1306 | 10.1109/TIE.2018.2835393 | L1 |
| P20 | Condition Monitoring of DC-Link Capacitors Using Goertzel Algorithm for Failure Precursor Parameter and Temperature Estimation | P. Sundararajan, M. H. M. Sathik, F. Sasongko, C. S. Tan, J. Pou, F. Blaabjerg, A. K. Gupta | 2020 | IEEE Trans. Power Electron. 35(6):6386–6396 | 10.1109/TPEL.2019.2951859 | L1 |
| P21 | Online Estimation of ESR for DC-Link Capacitor of Boost PFC Converter Using Wavelet Transform Based Time–Frequency Analysis Method | Lu et al. (확인 필요) | 2020 | IEEE Trans. Power Electron. 35(8):7755–7764 | (확인 필요) | L2 |
| P22 | Online ESR Monitoring of DC-Link Capacitor in VSC Using Damping Characteristic of Switching Ringings | D. Xiang, Y. Zheng, H. Li et al. | 2021 | IEEE Trans. Power Electron. 36(7):7429–7441 | (확인 필요) | L2 |
| P23 | A quasi-online condition monitoring technique for the wind power converter | (확인 필요) | 2021 | Int. J. Electr. Power Energy Syst. (PII S0142061521002118) | (확인 필요) | L2 |
| P24 | DC-Link Capacitor Diagnosis in a Single-Phase Grid-Connected PV System | M. Plazas-Rosas, M. Orozco-Gutierrez, G. Spagnuolo, E. Franco-Mejía, G. Petrone | 2021 | Energies 14(20):6754 | 10.3390/en14206754 | L1 |
| P25 | Online Condition Monitoring of DC-Link Capacitor for AC/DC/AC PWM Converter | T. Li, J. Chen, P. Cong, X. Dai, R. Qiu, Z. Liu | 2022 | IEEE Trans. Power Electron. 37(1):865–878 | (확인 필요) | L2 |
| P26 | Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor | M. Ghadrdan, S. Peyghami, H. Mokhtari, F. Blaabjerg | 2022 | IEEE Trans. Power Electron. 37(8):9733–9744 | 10.1109/TPEL.2022.3153842 | L1 |
| P27 | Online Capacitance Monitoring for DC/DC Boost Converters Based on Low-Sampling-Rate Approach | Z. Zhao, P. Davari, Y. Wang, F. Blaabjerg | 2022 | IEEE J. Emerg. Sel. Topics Power Electron. 10(5):5192–5204 | 10.1109/JESTPE.2021.3108420 | L1 |
| P28 | Online condition monitoring for DC-link capacitors of motor drives under noise interference | Q. Zhu, J. Zhao, Y. Song et al. | 2022 | J. Power Electron. 22:1142–1153 | 10.1007/s43236-022-00426-w | L1 |
| P29 | Online DC-Link Capacitance Monitoring for Digital-Controlled Boost PFC Converters Without Additional Sampling Devices | Z. Zhao, P. Davari, W. Lu, F. Blaabjerg | 2023 | IEEE Trans. Ind. Electron. 70(1):907–920 | 10.1109/TIE.2022.3153825 | L1 |
| P30 | Wavelet-based estimation method for online condition monitoring of dc-link capacitors of distributed energy resources | R. L. A. Ribeiro, A. Sangwongwanich, D. K. Alves, F. Blaabjerg, T. O. A. Rocha | 2023 | Int. J. Electr. Power Energy Syst. 151 (art. 확인 필요) | (확인 필요) | L2 |
| P31 | An Online DC-Link Capacitance Estimation Method for Motor Drive Systems Based on an Intermittent Reverse-Charging Control Strategy | Meng, Zhang | 2023 | IEEE Trans. Power Electron. 38(2):2481–2492 | (확인 필요) | L2 |
| P32 | Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor in a PWM Inverter With a Six-Pulse Diode Rectifier | K. Hasegawa et al. | 2023 | IEEJ J. Ind. Appl. 12(3), art. 22009135 | (확인 필요) | L2 |
| P33 | A Capacitance Estimation Method for DC-Link Capacitors Based on Pre-Charging Model and Noise Evaluation | (확인 필요) | 2023 | IEEE Trans. Ind. Electron. 70:8477–8487 | (확인 필요) | L2 |
| P34 | An Improved Discharge Profile-Based DC-Link Capacitance Estimation for Traction Inverter in Electric Vehicle Applications | X. Wei, Y. Bo, Y. Peng, Y. Sun, K. Wang, H. Wang | 2024 | IEEE Trans. Power Electron. 39(7):8696–8708 | 10.1109/TPEL.2024.3383153 | L1 |
| P35 | Discharge-Based Condition Monitoring for Electrolytic DC-Link Capacitors | J. Baumann, Murillo Garcia, K. Papastergiou, D. Peftitsis | 2024 | IEEE Trans. Power Electron. 39:16622–16637 (호 확인 필요) | (확인 필요) | L2 |
| P36 | A Capacitance Estimation Method for DC-Link Capacitors in Rail Transit Based on Maximum Likelihood and Variable Convergence Factor | (확인 필요) | 2025 | IEEE Trans. Ind. Electron. 72:8623– | (확인 필요) | L2 |
| P37 | Condition monitoring of a DC-link capacitor in an inverter with a front-end diode rectifier under imbalanced three-phase supply voltage | Yamasoto, Hasegawa | 2025 | Microelectronics Reliability 173:115873 | (확인 필요) | L2 |
| P38 | Discharge-Based DC-Bus Voltage Link Capacitor Monitoring with Repetitive Recursive Least Squares Method for Hybrid-Electric Aircraft | Oliszewski, Pawlak, Dybkowski | 2025 | Energies 18(17):4743 | 10.3390/en18174743 | L1 |
| P39 | Non-Intrusive Capacitor Monitoring in Photovoltaic Inverters Based on MPPT-Induced Voltage Transients | M. K. P. Muhammed Ramees, M. W. Ahmad | 2026 | IEEE Trans. Power Electron. 41(3) (쪽 확인 필요) | (확인 필요) | L2 |
| P40 | Real-Time Reliability Monitoring of DC-Link Capacitors in Back-to-Back Converters | (확인 필요) | 2019 | Energies 12(12):2369 | 10.3390/en12122369 | L3(제목만) |
| P41 | An Online Monitoring Scheme of DC-Link Capacitor's ESR and C for a Boost PFC Converter | (확인 필요) | ~2016 | IEEE Trans. Power Electron. (Xplore 7313000) | (확인 필요) | L3 |
| P42 | An Online Estimation Method for DC-Link Capacitor in Doubly Salient Electromagnetic Motor Drive System | (확인 필요) | 2025 | IEEE 저널 (Xplore 11178083; 저널명 확인 필요) | (확인 필요) | L3 |
| P43 | Implementation of Parameter Observer for Capacitors | (확인 필요) | 2023 | Sensors (MDPI) | 10.3390/s23020948 | L2 |
| P44 | DC-DC Buck Converters with Quasi-Online Estimation of Filter Capacitor Equivalent Parameters | (확인 필요) | 2024 | Applied Sciences (MDPI) | 10.3390/app142210756 | L2 |

### 3.3 멀티레벨·응용 특화 (NPC / T-type / FC / CHB / MMC / PV / 견인)

| ID | 제목 | 저자 | 연도 | 저널 (권/호/쪽) | DOI | 등급 |
|---|---|---|---|---|---|---|
| M1 | An Online Condition Monitoring Method for DC-Link Capacitors of Three-Level NPC Inverters Based on Charge-Discharge Profile | K. J. Min, U.-M. Choi, F. Blaabjerg | 2026 | IEEE Trans. Ind. Electron. 73(8):12452–12463 (SeoulTech Pure 기준) | 10.1109/TIE.2026.3672764 (확인 필요) | L2 |
| M2 | Online condition monitoring for DC-link capacitors of three-level NPC converters using noninvasive signal injection | R. L. A. Ribeiro, D. K. Alves, R. P. R. de Sousa, A. C. Oliveira | 2024 | Computers and Electrical Engineering 119:109577 | 10.1016/j.compeleceng.2024.109577 | L1 |
| M3 | Online Estimation of DC-link Capacitor Parameters of Three-Level NPC Converters Using Inherent Signals Analysis | Ribeiro, Han et al. (전체 확인 필요) | 2025 | IEEE/CAA J. Automatica Sinica 12 (호/쪽 확인 필요) | 10.1109/JAS.2025.125159 | L2 |
| M4 | Noninvasive Online Capacitor Monitoring Method for Three-Level Converter Based on Active Neutral-Point Current Adjustment | (확인 필요) | 2024 | IEEE Trans. Ind. Electron. 71(5):4320–4329 (신뢰도 낮음, 확인 필요) | (확인 필요) | L3 |
| M5 | A Comprehensive Method for Online Switch Fault Diagnosis and Capacitor Condition Monitoring of Three-Level T-Type Inverters | W. Zhang, Y. He, X. Wang, J. Chen | 2023 | IEEE Trans. Power Electron. 38(8):10183–10195 | 10.1109/TPEL.2023.3262758 | L1 |
| M6 | Capacitor voltage balancing, capacitance monitoring, and fast fault detection in a nested neutral point clamped (NNPC) converter with the reduced number of sensors | (확인 필요) | 2024 | Computers and Electrical Engineering 118(B):109453 | (확인 필요) | L2 |
| M7 | High-gain adaptive observer for floating voltages estimation and capacitor aging monitoring in multicell converters | B. Nait Slimani et al. | 2025 | Engineering Science and Technology, an International Journal (권/art 확인 필요) | (확인 필요) | L2 |
| M8 | Online Capacitor Condition Monitoring for Cascaded-H-Bridge Type Converters | (확인 필요) | 2024 | IEEE 저널 (Xplore 10598339; 저널명 확인 필요) | (확인 필요) | L3 |
| M9 | An Online DC-Link Capacitor Condition Monitoring Method for CHB-Type SVG | H. Wang, R. Qiu, Y. Chen, M. Ma, F. Li, X. Zhang | 2025 | IEEE Trans. Power Electron. pp. 10385–10390 (권/호 확인 필요) | (확인 필요) | L2 |
| M10 | Capacitor Condition Monitoring Method for Low-Capacitance StatComs: An Online Approach Using the Inherent Second-Harmonic Oscillations | E. R. Ramos, R. Leyva, Q. Liu, G. G. Farivar, J. Pou | 2023 | IEEE Trans. Power Electron. 38(9):10559–10562 | (확인 필요) | L2 |
| M11 | Condition Monitoring for Submodule Capacitors in Modular Multilevel Converters | H. Wang, H. Wang, Z. Wang, Y. Zhang, X. Pei, Y. Kang | 2019 | IEEE Trans. Power Electron. 34(11):10403–10407 | (확인 필요) | L2 |
| M12 | Online Capacitance Estimation of Submodule Capacitors for Modular Multilevel Converter With Nearest Level Modulation | K. Wang, L. Jin, G. Li, Y. Deng, X. He | 2020 | IEEE Trans. Power Electron. 35(7):6678–6681 | (확인 필요) | L2 |
| M13 | Condition Health Monitoring of Modular Multilevel Converter Submodule Capacitors | I. Polanco, D. Dujic | 2022 | IEEE Trans. Power Electron. 37(3):3544–3554 | (확인 필요) | L2 |
| M14 | An Improved Submodule Capacitor Condition Monitoring Method for Modular Multilevel Converters Considering Switching States | Y. Zhou, P. Hu, D. Jiang, K. Zhang et al. | 2024 | J. Mod. Power Syst. Clean Energy 12(6):2071–2080 | (확인 필요) | L2 |
| M15 | Submodule Capacitance Monitoring Approach for the MMC With Asymptotically Converged Error | Q. Xiao, H. Wang, Y. Jin et al. | 2024 | IEEE Trans. Ind. Electron. 71(5):4330–4339 | (확인 필요) | L2 |
| M16 | Reference Submodule Based Capacitor Monitoring Strategy for Modular Multilevel Converters | F. Deng, Q. Wang, D. Liu, Y. Wang, M. Cheng, Z. Chen | 2019 | IEEE Trans. Power Electron. 34(5):4711–4721 | (확인 필요) | L2 |
| M17 | A Reference Submodule Based Capacitor Condition Monitoring Method for Modular Multilevel Converters | Z. Wang, Y. Zhang, H. Wang, F. Blaabjerg | 2020 | IEEE Trans. Power Electron. 35(7):6691–6696 | (확인 필요) | L2 |
| M18 | Failure Prediction of Submodule Capacitors in Modular Multilevel Converter by Monitoring the Intrinsic Capacitor Voltage Fluctuations | D. Ronanki, S. S. Williamson | 2020 | IEEE Trans. Ind. Electron. 67(4):2585–2594 | (확인 필요) | L2 |
| M19 | Submodule Capacitance Monitoring Strategy for Phase-Shifted Carrier PWM-Based Modular Multilevel Converters | C. Liu, F. Deng, Q. Yu, Y. Wang, F. Blaabjerg, X. Cai | 2021 | IEEE Trans. Ind. Electron. 68(9):8753–8767 | (확인 필요) | L2 |
| M20 | Switching Signals Based Condition Monitoring for Submodule Capacitors in Modular Multilevel Converters | Z. Geng, M. Han, G. Zhou | 2021 | IEEE Trans. Circuits Syst. II 68(6):2017–2021 | (확인 필요) | L2 |
| M21 | A Hierarchic Capacitor Condition Monitoring Strategy for High-Voltage Modular Multilevel Converters | (확인 필요) | 2022 | IEEE Trans. Power Del. 37(6):5310–5324 | (확인 필요) | L3 |
| M22 | Online monitoring method for submodule capacitors in modular multilevel converter based on cumulative sum detection of sliding window | W. Lai, J. Zhang, D. Luo et al. | 2024 | J. Power Electron. 24:964–977 | 10.1007/s43236-023-00760-7 | L1 |
| M23 | Capacitance health monitoring in the modular multilevel converter using a method with minimum number of sensors and computational burden | M. Zoraghi-Jedi, S.-M. Barakati et al. | 2024 | Int. J. Circuit Theory Appl. (권/쪽 확인 필요) | 10.1002/cta.4057 | L2 |
| M24 | Local outlier factor based condition monitoring for sub-module capacitors in modular multilevel converters | Y. Jiang, H. Shu, J. Zhang | 2024 | Electric Power Systems Research (권/art 확인 필요) | (확인 필요) | L2 |
| M25 | Online evaluation method for MMC submodule capacitor aging based on CapAgingNet | X. Deng, Y. Deng, L. Qin et al. | 2025 | Global Energy Interconnection 8(3):420–432 | (확인 필요) | L2 |
| M26 | Neural Network-Based Submodule Capacitance Monitoring in Modular Multilevel Converters for Renewable Energy Conversion Systems | M. Asnoun, A. Rahoui, K. Mesbah et al. | 2026 | Electronics 15(7):1486 | 10.3390/electronics15071486 | L1 |
| M27 | Capacitance Estimation of the Submodule Capacitors in Modular Multilevel Converters for HVDC Applications | (확인 필요) | 2016 | J. Power Electron. (KoreaScience JAKO201628740947636; 권/쪽 확인 필요) | (확인 필요) | L2 |
| M28 | Practical Online Condition Monitoring of DC-Link Capacitors in Modular Multilevel Converters: A Comparative Approach | (확인 필요) | 2024 | IEEE Open J. Power Electron. (Xplore 미확인; TechRxiv 프리프린트 "accepted") | 10.1109/OJPEL.2024.3387829 (확인 필요) | L3 |
| M29 | Analysis of dc-link capacitor current in three-level neutral point clamped and cascaded H-bridge inverters | G. I. Orfanoudakis et al. | 2013 | IET Power Electron. | 10.1049/iet-pel.2012.0422 | L2 (CM 아님, NPC 커패시터 전류 해석) |

### 3.4 데이터 기반 (ML·DL·하이브리드·RUL)

| ID | 제목 | 저자 | 연도 | 저널 (권/호/쪽) | DOI | 등급 |
|---|---|---|---|---|---|---|
| D1 | DC-Link Electrolytic Capacitors Monitoring Techniques Based on Advanced Learning Intelligence Techniques for Three-Phase Inverters | H. Dang, H. Park, S. Kwak, Choi | 2022 | Machines 10(12):1174 | (확인 필요; MDPI URL 2075-1702/10/12/1174) | L2 |
| D2 | Deep learning-based estimation technique for capacitance and ESR of input capacitors in single-phase DC/AC converters | H.-J. Park, J.-C. Kim, S. Kwak | 2022 | J. Power Electron. 22:513– | 10.1007/s43236-021-00366-x | L2 |
| D3 | Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters | (확인 필요) | 2024/2025 | IEEE Trans. Ind. Electron. 72(4):4227–4237 | (확인 필요) | L2 |
| D4 | Investigation on C and ESR Estimation of DC-Link Capacitor in Maglev Choppers Using Artificial Neural Network | (확인 필요) | 2022 | Energies 15(22):8564 | (확인 필요) | L2 |
| D5 | Capacitance estimation algorithm based on DC-link voltage ripples using hybrid machine learning techniques in power electronics converters | (확인 필요) | 2025 | Results in Engineering (PII S2590123025022881) | (확인 필요) | L2 |
| D6 | DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs | (확인 필요) | 2023 | J. Electr. Eng. Technol. | 10.1007/s42835-023-01424-z | L2 |
| D7 | Fault Diagnosis of Capacitance Aging in DC Link Capacitors of Voltage Source Inverters Using Evidence Reasoning Rule | Liao et al. | 2020 | Math. Probl. Eng. 2020:5724019 | 10.1155/2020/5724019 | L1 |
| D8 | Advanced Fault-Detection Technique for DC-Link Aluminum Electrolytic Capacitors Based on a Random Forest Classifier | (확인 필요) | 2023 | Electronics 12(12):2572 | 10.3390/electronics12122572 | L2 |
| D9 | Parameter Identification of DC-Link Capacitor for Electric Vehicle Based on IGWO-BP Neural Network | Yao et al. | 2021 | IEEJ Trans. Electr. Electron. Eng. | 10.1002/tee.23373 | L2 |
| D10 | A Highly Accurate Generative Learning-Based DC-Link Capacitance Estimation Approach for Electrified Railway Traction Systems | Zhao et al. | 2026 | IET Power Electron. | 10.1049/pel2.70151 | L2 |
| D11 | Intelligent Health Monitoring of Capacitor Using Reduced Experimental Input Data | (확인 필요) | 2022 | J. Electr. Eng. Technol. | 10.1007/s42835-022-01328-4 | L3 |
| D12 | Prediction of Capacitor's Accelerated Aging Based on Advanced Measurements and Deep Neural Network Techniques | H. Liu, T. Claeys, D. Pissoort, G. A. E. Vandenbosch | 2020 | IEEE Trans. Instrum. Meas. 69(11):9019–9027 | (확인 필요) | L2 |
| D13 | Deep neural network-based lifetime diagnosis algorithm with electrical capacitor accelerated life test | (확인 필요) | 2024 | J. Power Sources (PII S0378775324001332) | (확인 필요) | L2 |
| D14 | Capacitor Aging State Evaluation and a Remaining-Useful-Life Prediction Method Based on a CNN-LSTM Network Considering the Impact of Parameter Dispersion | (확인 필요) | 2025 | Electronics 14(22):4452 | 10.3390/electronics14224452 | L2 |
| D15 | Converter Capacitor Temperature Estimation Based on Continued Training LSTM under Variable Load Conditions | (확인 필요) | 2024 | Sensors 24(13):4304 | 10.3390/s24134304 | L2 |
| D16 | Using LSTM neural network to predict remaining useful life of electrolytic capacitors in dynamic operating conditions | A. F. Shahraki, S. Al-Dahidi, A. R. Taleqani, O. P. Yadav | 2023 | Proc. IMechE Part O | 10.1177/1748006X221087503 | L2 |
| D17 | A remaining useful life prediction method of aluminum electrolytic capacitor with adaptive degradation model selection | (확인 필요) | 2024 | Microelectronics Reliability (PII S0026271424001896) | (확인 필요) | L2 |
| D18 | Machine learning-assisted remaining useful lifetime prediction of power electronic converters | (확인 필요) | 2026 | Scientific Reports | 10.1038/s41598-026-56011-9 (확인 필요) | L2 |
| D19 | Digital twin based monitoring and control for DC-DC converters | (확인 필요) | 2023 | Nature Communications 14 | 10.1038/s41467-023-41248-z (확인 필요) | L2 |
| D20 | Controller-Embeddable Probabilistic Real-Time Digital Twins for Power Electronic Converter Diagnostics | Milton, De La O, Ginn, Benigni | 2020 | IEEE Trans. Power Electron. 35(9):9850–9864 | (확인 필요) | L2 |
| D21 | CNN-LSTM-Based Prognostics of Bidirectional Converters for Electric Vehicles' Machine | (확인 필요) | 2021 | Sensors 21(21):7079 | 10.3390/s21217079 | L3 |
| D22 | RUL prediction for AECs of power electronic systems based on machine learning and error compensation | Q. Sun, L. Yang, H. Li, G. Sun | 2023 | J. Intelligent & Fuzzy Systems | 10.3233/JIFS-220866 | L3 |

(M24 LOF, M25 CapAgingNet, M26 ADALINE 도 데이터 기반이며 13–14절에서 함께 다룬다.)

### 3.5 기타 커패시터·소재 메커니즘

| ID | 제목 | 저자 | 연도 | 저널 (권/호/쪽) | DOI | 등급 |
|---|---|---|---|---|---|---|
| E1 | A Capacitance Estimation of Film Capacitors in an LCL-Filter of Grid-Connected PWM Converters | (확인 필요) | 2013 | J. Power Electron. (KoreaScience JAKO201308438431900) | (확인 필요) | L2 |
| E2 | Online Condition Monitoring of Three-Phase Filter Capacitors for Vehicular Auxiliary Converter | Hu et al. | 2026 | IET Power Electron. (art. pel2.70299) | 10.1049/pel2.70299 | L2 |
| E3 | Condition Monitoring of Metallized Polypropylene Film Capacitors in Railway Power Trains | G. M. Buiatti et al. (확인 필요) | 2009 | IEEE Trans. Instrum. Meas. (Xplore 5191038) | (확인 필요) | L2 |
| E4 | Multilayer Ceramic Capacitors: An Overview of Failure Mechanisms, Perspectives, and Challenges | (확인 필요) | 2023 | Electronics 12(6):1297 | 10.3390/electronics12061297 (확인 필요) | L2 |
| E5 | Metallized polymer film capacitors ageing law based on capacitance degradation | M. Makdessi, A. Sari, P. Venet (확인 필요) | 2014 | Microelectronics Reliability | (확인 필요) | L3 |
| E6 | Ageing metallized polypropylene film capacitors laws confronted with the phenomenon of corrosion | (확인 필요) | 2023 | Microelectronics Reliability (PII S0026271423002743) | (확인 필요) | L2 |
| E7 | Lifetime prediction and reliability analysis for aluminum electrolytic capacitors in EV charging module based on mission profiles | (확인 필요) | 2023 | Frontiers in Electronics 4:1226006 | 10.3389/felec.2023.1226006 | L2 |
| E8 | Degradation modeling for reliability estimation of DC film capacitors subject to humidity acceleration | (확인 필요) | 2019 | Microelectronics Reliability (PII S0026271419303695) | (확인 필요) | L2 |
| E9 | An improved lifetime prediction method for metallized film capacitor considering harmonics and degradation process | (확인 필요) | 2020 | Microelectronics Reliability (PII S0026271420304893) | (확인 필요) | L2 |
| E10 | Noninvasive condition monitoring of three-phase four-wire inverter system parameters | (확인 필요) | 2024 | Int. J. Electr. Power Energy Syst. (PII S0142061524005520) | (확인 필요) | L3 |

---

## 4. Topology 별 주요 열화 대상 커패시터와 이용 신호

| Topology | 주요 열화·진단 대상 | 토폴로지 특유의 신호·메커니즘 (사실: 초록 기준) | 근거 | 저널 논문 수(본 조사) |
|---|---|---|---|---|
| 2-Level VSI / AC-DC-AC / 드라이브 | 단일 DC-link 커패시터 (AEC 중심, 견인은 필름) | DC-link 전압·전류 리플(스위칭 주파수, 정류 6f, 단상 2f), 주입 리플, 회생 모드 충전, 정지 시 방전 프로파일, 스위칭 링잉 | P1–P39 | 40+ |
| 3-Level NPC | 상·하단 분할 DC-link (C1, C2) | 변조기에 오프셋/영상분 주입 → 중성점 전류 → vC1−vC2 발산(충방전 프로파일) 또는 NP 전압 리플; PWM×토폴로지 상호작용의 고유 상호변조 성분(무주입) | M1, M2, M3, M4 | 4 (2024–2026) |
| 3-Level T-type | 분할 DC-link | DC-link·AC측 모델의 고유 고조파, 재구성 커패시터 전류, NP 전압 잔차 (스위치 고장진단과 통합) | M5 | 1 |
| ANPC | — | **CM 저널 논문 미발견** (수명 추정 논문만: JEET 2022, 10.1007/s42835-021-00992-2) | — | 0 |
| NNPC (4-level) | 중첩(플라잉) 커패시터 | 출력 센서만으로 커패시터 전압 추정 → C 감시 + 밸런싱 + 고장 검출 | M6 | 1 |
| Flying-Capacitor / 멀티셀 | 플라잉 커패시터 | 부동 전압·ESR·C 를 동시에 추정하는 고이득 적응 관측기 | M7 | 1 (2차 검색 미실행) |
| CHB (SVG/STATCOM/PV) | 각 셀 DC 커패시터 | 셀 DC 전압(제어용 기존 센서) + RLS; 기준 셀 충전 전이 + 전력 균형; 저용량 STATCOM 의 고유 2f 진동 | M8, M9, M10 | 3 |
| MMC | 서브모듈 커패시터 | SM 전압 + 암 전류 + 스위칭 상태/각; 기준 SM 비교; 블리딩 저항 방전; 스위칭 신호 합; 2f 순환전류 주입; ML/DL | M11–M28 | 17+ |
| PV 인버터 | DC-link (AEC) | 단상 2f 리플 ↔ C; 야간 무조사 시 주입; MPPT 기준 전압 전이를 자연 여기로 사용 | P10, P11, P13, P14, P24, P39 | 6 |
| EV 견인 / 철도 / 항공 | DC-link 필름(견인·철도), DC 버스 | 주차·비행 후 방전 프로파일; 최대우도 추정; 반복 RLS | P34, P35, P36, P38, D10 | 5 |
| 모터 드라이브(정류기 전단) | DC-link AEC | 회생 모드 전류 주입 / 간헐 역충전 / 전류센서 없는 정류 리플 재구성 / 정지 시 고정자 여기 | P3, P9, P28, P31, P32, P37 | 6 |
| 계통연계 LCL / 3상 출력 필터 | AC 측 필름 커패시터 | 계통 THD 증가, 기존 전압·전류 센서로 C 추정 | E1, E2 | 2 |
| 스너버·클램프·공진 커패시터 | — | **저널 논문 미발견** (LLC 출력 커패시터 방전 프로파일 학회 논문만) | — | 0 |

(해석) 연구량은 2-Level DC-link ≫ MMC ≫ 나머지 순이며, 3-Level NPC 는 2024년 이후에야 저널 논문이 나타났고 **모두 변조기 주입형**이거나(M1, M2, M4) 고유 상호변조 성분(M3)을 쓴다. 스위치 전류 스펙트럼을 쓰는 논문은 없다(18절).

---

## 5. 논문별 기술 분류표 (Stage 2)

약어: AEC=알루미늄 전해, Film=필름, n/s=초록에 미기재, Exist=기존 센서만, Inj=주입, Q-on=quasi-online. 검증 열은 초록에 명시된 것만.

### 5.1 DC-link 파라미터·신호·충방전 (P)

| ID | 토폴로지 | 커패시터 | 입력 신호 | Feature | 방법 | 추정/HI | Online | 추가 센서 | 검증 | ML |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 3상 AC/DC/AC | DC-link AEC | DC측 AC 전압·전류 | 주입 저주파 리플 | 입력측 전류 주입(무부하) + RLS | C (오차<0.26%) | Q-on(무부하) | 없음(SW) | 실험 | × |
| P2 | 3상 AC/DC/AC | DC-link | DC측 AC 전력 성분 | 주입 준선주파 리플 | 전압 주입 + SVR | C | Online(Inj) | n/s | n/s | ○(SVR) |
| P3 | ASD(정류기 전단) | DC-link AEC | DC-link 전압 + 고정자 전류(기존) | 정지 시 스위칭 여기 응답 | 인버터로 고정자에 펄스 인가 | ESR, C | Q-on(정지) | 없음 | 실험 | × |
| P4 | Boost DC-DC | 출력 AEC/MPPF | 컨버터 전압·전류 | CCM/DCM 리플 | 이중 추정 | ESR, C | Online(실시간) | 없음 | n/s | × |
| P5 | PWM 컨버터 | DC-link AEC | (전용 유닛) | n/s | 온라인 ESR 식별 유닛 | ESR | Online | **있음(전용 유닛)** | 실험 | × |
| P6 | Buck | 출력 AEC | 입력 전류 + 출력 전압 리플 | 스위칭 리플 | 리플 비 | ESR (EoL: ESR×2 / C−20%) | Online | n/s | 실험 | × |
| P7 | 항공 드라이브 | DC-link AEC·MPPF | n/s | 기동/정지 시 | n/s | C (두 종류 모두 감소) | Q-on | n/s | n/s | × |
| P8 | 3상 AC/DC | DC-link AEC | DC측 리플 + 주입 전류 | 주입 리플 | 입력 전류 주입 + 필터 + RLS | ESR | Online(Inj) | n/s | n/s | × |
| P9 | 정류기+인버터 IM 드라이브 | DC-link AEC | DC-link 전압·전류 AC 성분 | 회생 모드 고정자 전류 주입 리플 | RLS | C (<1%) | Q-on(회생) | 없음 | 실험 | × |
| P10 | PV boost | 입력 AEC | PV 전압·전류(MPPT 센서) | 스위칭 리플(CCM/DCM) | 리플 계수, **온도 보정** | ESR | Online | 없음 | 실험 | × |
| P11 | 단상 PV | DC-link AEC | PV 전압·전류, 인덕터 전류 | 2f_grid 진동(SOGI) | 2f 임피던스, 같은 DSP | |Z(2f)| | Online | 없음 | n/s | × |
| P12 | 컨버터 | DC-link | 단락 전류 | n/s | IGBT+커패시터 동시 CM | n/s | n/s | n/s | n/s | × |
| P13 | 단상 PV | DC-link AEC | DC-link 전압·전류 | 홀수 고조파 다중 주파수 주입, FFT | |Z(f)| LMS 피팅 | ESR, C | Q-on(야간) | 없음 | 실험 | × |
| P14 | 단상 인버터 | DC-link AEC | 제어용 전압·전류 | 2f_grid 성분 | v/i 비 | C (최대 2.56%) | Online | 없음 | 실험 | × |
| P15 | 산업용 컨버터 | DC-link AEC | 커패시터 전압·전류 | 스위칭 주파수 성분 | 성분 비 | ESR | Online | n/s | 실험 | × |
| P16 | 6펄스 정류기+3상 PWM | DC-link | n/s | 정류(6f)+인버터(fsw) 성분 | n/s | ESR, C | n/s | n/s | n/s | × |
| P17 | 병렬 뱅크 | AEC 개별 | n/s | 열화 모델 계수 | 물리 열화 모델 + **EKF** | ESR, C(개별) | Online | 감소 | n/s | × |
| P18 | VSI | DC-link | 공진 전압·전류 | LC 공진 주파수 | 비운전 시 공진 여기 | C | Q-on | n/s | n/s | × |
| P19 | 3상 AC-DC-AC | DC-link | n/s | 가변 전기망(VEN) 여기 | n/s | n/s | Online | n/s | n/s | × |
| P20 | 정류기 전단 3상 인버터 | DC-link AEC | 커패시터 전압·전류(측정/재구성 미확인) | Goertzel 단일 빈 | Goertzel → ESR, C; C 로 코어 온도 | ESR, C, **온도** | Online | n/s | 실험 | × |
| P21 | Boost PFC | DC-link | n/s | Wavelet 시간-주파수 | 시간-주파수 해석 | ESR | Online | n/s | n/s | × |
| P22 | 2L VSC | DC-link | 스위칭 순간 DC-link 전압 | 고주파 링잉 감쇠 | 감쇠율 → ESR | ESR | Online | n/s | 실험 | × |
| P23 | 풍력 컨버터 | DC-link | 기존 DC-link 전압 | 정지 시 방전(온도 이완) | 방전 프로파일 피팅 | C 등 | Q-on(정지) | n/s | n/s | × |
| P24 | 단상 계통 PV | DC-link AEC | PV/DC-link 센서, boost 듀티 변조 주입 | 임피던스 스펙트럼(EIS형) | 2단계 피팅 | ESR, C (<1%) | Online(Inj) | 없음 | 실험/시뮬 | × |
| P25 | AC/DC/AC PWM | DC-link | 스위칭 함수 + 상전류(재구성, 귀속 확인 필요) | 주입 응답 | 정상 운전 중 주입 | C(실시간) | Online(Inj) | 없음 | n/s | × |
| P26 | Back-to-back 2L | DC-link AEC | **출력(AC) 전류** + DC-link 전압 | 재구성 커패시터 전류의 fsw 성분 | DF = ω·C·ESR | DF (EoL 기준 제안) | Online | 없음(전류 센서 불필요) | 실험 | × |
| P27 | Boost DC-DC | 출력 AEC | 출력 전압 과도 | 충전 프로파일 | 모델 기반, 저샘플링 | C | Online(과도) | n/s | n/s | × |
| P28 | 모터 드라이브(회생) | DC-link | DC-link 전류 적분 + 전압 상승 | 전하 균형 | C=∫i dt/Δv, RLS+이상치 제거 | C | Q-on(회생) | 없음 | 실험 | × |
| P29 | Boost PFC | DC-link AEC | DC-link 전압(기존 샘플링) | 대신호 과도 프로파일 | 해석 모델 | C | Online(과도) | 없음 | n/s | × |
| P30 | DER 인버터 | DC-link | DC-link 전압·전류 + 간헐 비특성 주입 | RT-SDWPT 계수 | Wavelet 패킷 | ESR, C (<2%) | Online(Inj) | 없음 | n/s | × |
| P31 | 모터 드라이브 | DC-link AEC | 역충전 구간 전압·전류 | 역충전 과도 | 간헐 능동 제어 | C | Online(간헐) | 없음 | n/s | × |
| P32 | 6펄스 정류기+DC 인덕터+인버터 | DC-link | 3상 전원 전압 + 인덕터 모델 → 전류 계산 | 정류 리플 | 모델 기반 전류 재구성 | ESR, C | Online | **없음(전류 센서 불필요)** | 실험 | × |
| P33 | (일반) | DC-link | 사전충전 전압 | 사전충전 프로파일 | 개선 RELS + 잡음 평가 | C | Q-on(사전충전) | n/s | n/s | × |
| P34 | EV 견인 2L | DC-link(필름 추정) | 기존 DC-link 전압 | 턴오프 방전 프로파일 | 프로파일 피팅(주차 후) | C | Q-on | 없음 | n/s | × |
| P35 | 일반 컨버터 | DC-link AEC | 정지 시 DC-link 전압 감쇠 | 방전 프로파일 | SoH 모델, **온도 의존성 보상** | 잔존 C / SoH | Q-on(정지) | n/s | 실험 | × |
| P36 | 철도 견인 | DC-link **필름** | n/s | n/s | 최대우도 + Newton–Raphson, 가변 수렴계수 | C | n/s | n/s | n/s | × |
| P37 | 정류기+인버터 | DC-link | 불평형 전원 리플 | 2f_grid 성분(추정) | n/s | ESR/C | Online | 없음 | n/s | × |
| P38 | 항공 DC 버스 | AEC | 비행 후 방전 전압 | 방전 프로파일(소량 데이터) | 반복 RLS | C (<5%) | Q-on | 없음 | 실험 | × |
| P39 | 3상 PV 2L | DC-link | PV 전압 + 출력 전류(→커패시터 전류 추정) | MPPT 전이 시 저주파 성분 | 비침습, 무주입 | C | Online | 없음 | 시뮬+실험 | × |

### 5.2 멀티레벨·응용 (M)

| ID | 토폴로지 | 커패시터 | 입력 신호 | Feature | 방법 | 추정/HI | Online | 추가 센서 | 검증 | ML |
|---|---|---|---|---|---|---|---|---|---|---|
| M1 | 3L-NPC | C1, C2 개별 | vC1, vC2 + 기준전압 오프셋 주입 | 충방전 프로파일(설정 전압차 도달 전하) | 오프셋 주입 + 출력전류 영향 보상 | C (평균 오차 <1%) | Online(Inj) | 없음 | 실험(추정) | × |
| M2 | 3L-NPC | 분할 DC-link | 영상분 구형파(상호고조파) 주입 → NP 전류; DC-link 전압·전류 | 상호고조파 + 고조파의 Wavelet 분해 | 주입 + Wavelet, 여러 주파수에서 동시 추정 | ESR, C (<2%, Fourier 대비 우수) | Online(Inj) | 없음(HW·제어 변경 없음) | n/s | × |
| M3 | 3L-NPC 계통연계 | 분할 DC-link | 기존 센서; PWM×토폴로지 **고유 상호변조 성분** | 비정수 재귀 슬라이딩 DFT 로 추적 | oSDFT-RLS(망각계수) 관측기 구조, 시간-주파수 | C, ESR (열화 추적) | Online(**무주입**) | 없음 | n/s | × |
| M4 | 3L(ac/dc/ac) | 분할 DC-link | 스위칭 상태 + 3상 전류(주입 NP 전류 재구성), NP 전압 | NP 전압 리플 응답 | 능동 NP 전류 조정 + RLS | C | Online(Inj) | 없음 | n/s | × |
| M5 | 3L T-type | 분할 DC-link | 출력 전류·미분, 상전류 잔차, NP 전압 잔차 | 정상/OC 고장 시 고유 DC-link 고조파, 재구성 커패시터 전류 | 모델 잔차 + 주입 프레임워크("extra hardware" 서브모듈 언급) | 커패시터 상태 + 스위치 OC | Online | 가능성 있음 | n/s | × |
| M6 | 4L NNPC | 중첩 커패시터 | 출력 전압·전류 센서만 | 추정 커패시터 전압 | 센서리스 전압 추정 | C | Online | 감소 | n/s | × |
| M7 | FC 멀티셀 | 플라잉 | (관측기 입력 미확인) | ESR·C 파라미터화 하이브리드 모델 | 고이득 적응 관측기 | ESR, C | Online | n/s | n/s | × |
| M8 | CHB | 셀 DC-link | 셀 DC 전압(제어용) | 제어 전략 유도식 | 자기적응 망각계수 RLS | C | Online | 없음 | n/s | × |
| M9 | CHB SVG | 셀 DC-link | 셀 DC 전압, 전류/전력 | 기준 모듈 충전 전이 + 전력 균형 | 기준 모듈 → 전 셀 전파 | C(전 셀) | Online | 없음 | 시뮬+실험 | × |
| M10 | CHB 저용량 STATCOM | 셀 DC | 셀 커패시터 전압·전류 | **고유 2f 진동** | 2f 임피던스 식별 | ESR, C | Online | n/s | n/s | × |
| M11 | MMC | SM | SM 전압(방전 중) | 블리딩 저항 방전 곡선 | RC 방전 시간 | C | Q-on | 없음 | n/s | × |
| M12 | MMC(NLM) | SM | SM 전압, 스위칭 각 | 기본파 전압 변동 vs 각 | 해석식 | C | Online | 없음 | n/s | × |
| M13 | MMC | SM | SM 전압, 암 전류(SM 제어기) | SM 수준 C 변화 | 저가 SM 제어기 탑재 알고리즘 | C 변화 | Online | 없음 | 시뮬+실시간시뮬+실험 | × |
| M14 | MMC | SM | SM 전압, 암 전류, 스위칭 상태 | 제어주기별 V–I 관계 | 주기별 C 계산 | C | Online | 없음 | n/s | × |
| M15 | MMC | SM | SM 전압·전류 | 추정 오차 동역학 | Lyapunov 적응 추정기 | C | Online | 없음 | n/s | × |
| M16 | MMC | SM | 기준 SM·감시 SM 전압 | 전압 관계 | 기준 SM 비교 | C | Online | 없음 | n/s | × |
| M17 | MMC | SM | SM 전압 센서 | 센서 전 범위 활용 | 기준 SM 비교 | C | Online | 없음 | n/s | × |
| M18 | MMC | SM **AEC** | SM 전압 | 고유 저주파 진동 진폭 | 변동 기반 고장 예측 | C/건전성 | Online | 없음 | n/s | × |
| M19 | MMC(PSC-PWM) | SM | SM 전압·전류 기본파, 기준값 | 기본파 성분 | 기준 기반 추정(DSP–FPGA 통신 절감) | C | Online | 없음 | n/s | × |
| M20 | MMC | SM | 스위칭 신호 합 | 실제 vs 공칭 합, 데드타임 보상 | 스위칭 신호 기반 | C | Online | 없음 | **시뮬만** | × |
| M21 | HV MMC | SM | n/s | 계층(암→SM) | n/s | C | Online | n/s | n/s | × |
| M22 | MMC | SM | SM 스위치 on/off 시간 | 슬라이딩 윈도 CUSUM | 변화 검출 | 이상(C) | Online | 없음 | n/s | 통계 |
| M23 | MMC | SM | 그룹당 1개 전압 센서 + 암 전류 | 추정/측정 전압 비 | 센서 감소 추정 | C | Online | 감소 | n/s | × |
| M24 | MMC | SM(ESC+ESR) | 스위칭 함수 + 커패시터 전압(1주기) | 이상치 점수 | **LOF(비지도 ML)** | 이상 커패시터 순위 | Online | 없음 | n/s | ○ |
| M25 | MMC | SM | SM 스위칭 상태 시퀀스(시뮬 데이터셋) | 학습 특징 | **CapAgingNet(DL 분류)** Top-1 95.32% | 노화 등급 | Online | 없음 | **시뮬만** | ○ |
| M26 | MMC | SM | 암 전류, SM 스위칭 상태, 커패시터 전압 | 원시 샘플 | **ADALINE(회로식에 매핑)** | C | Online | 없음 | n/s | ○(물리 내장) |
| M27 | MMC-HVDC | SM | 암 전류+스위칭 상태(→커패시터 전류), SM 전압 | 주입 2f 순환전류 리플 | 주입 + RLS | C | Online(Inj) | 없음 | n/s | × |
| M28 | MMC | SM | 측정 SM 전압 + 추정 전류 | 특정 주파수 성분 | 암 내 전 SM 비교로 **온도 효과 분리** | C | Online | 없음 | n/s | × |

### 5.3 데이터 기반 (D)

| ID | 대상 | 입력 데이터 | Feature | 모델 | 목표/라벨 | 데이터 출처 | 다중 조건 | 물리 내장 | Online |
|---|---|---|---|---|---|---|---|---|---|
| D1 | 3상 인버터 DC-link AEC | 소스 전류 | (확인 필요) | 여러 지능 기법(ANN 등, 확인 필요) | C/ESR | (확인 필요) | (확인 필요) | × | (확인 필요) |
| D2 | 단상 DC/AC 입력 커패시터 | 커패시터 전압·전류 실험 파형 → **FFT** | **2·f1 성분 + fsw 성분** | DNN(MLP) | C, ESR 회귀 | 실험 | (확인 필요) | 주파수 선택에 물리 반영 | 주장(확인 필요) |
| D3 | AC/DC/AC DC-link | 정상 운전 신호(DC-link 전압 리플) | 리플 **PSD** | GPR(불확실성 정량화) | C 회귀 | 실험 프로토타입(오차<2%) | ○(부하·출력주파수) | × | ○(무주입·무HW) |
| D4 | 자기부상 초퍼 DC-link | 5 kHz 전압 리플 | 리플 특징 | ANN | 120 Hz 기준 C, ESR | (확인 필요) | (확인 필요) | × | (확인 필요) |
| D5 | DC-link | DC-link 전압 리플 | 리플 특징 | RF/kNN/ANN/GB/DT/LR, 하이브리드 ANN-GB-LR | C 회귀(평균 오차 0.142% 주장) | (확인 필요) | (확인 필요) | × | SW만 |
| D6 | 3상 DC/AC DC 커패시터 | 주파수 대역 분리 입력 | 대역별 스펙트럼 | DL | C, ESR | (확인 필요) | (확인 필요) | 대역 선택 | (확인 필요) |
| D7 | VSI DC-link | DC-link 전압 데이터 | 전압 특징 | 증거 추론 규칙(ER) | C 노화 고장 등급 | (확인 필요) | (확인 필요) | × | 주장 |
| D8 | DC-link AEC | (확인 필요) | (확인 필요) | Random Forest | 고장/노화 등급 | (확인 필요) | (확인 필요) | × | (확인 필요) |
| D9 | EV DC-link | (확인 필요) | (확인 필요) | IGWO-BP NN | C/ESR 식별 | (확인 필요) | (확인 필요) | × | (확인 필요) |
| D10 | 철도 견인 DC-link | (확인 필요) | (확인 필요) | 생성 학습(VAE+LSTM) | C | (확인 필요) | (확인 필요) | × | (확인 필요) |
| D12 | 가속 노화 단품 | "advanced measurements"(임피던스형 추정) | (확인 필요) | LSTM DNN | C·ESR 편차 예측 | 가속 노화 실험 | (확인 필요) | × | × |
| D13 | 가속수명시험 단품 | V, I, R 시계열 → **이미지** | 이미지 | **CNN 분류** | 수명 상태 등급 | 실제 ALT | (확인 필요) | × | × |
| D14 | 단품 | C 감소/ESR 증가 궤적 | 시계열 | CNN-LSTM | 노화 상태 + RUL | (확인 필요) | 파라미터 산포 고려 | × | × |
| D15 | 컨버터 커패시터 | 여러 주파수 전류 + ESR(T,I) 특성 → 손실 | 손실/전류 | LSTM(계속 학습) | 코어 **온도** | 실험 | ○(가변 부하) | 부분(열모델) | ○ |
| D16 | 단품 AEC | 열화 데이터 + 운전조건 이력 | 열화 시점 검출 | LSTM | RUL | (확인 필요) | ○(동적 조건) | × | × |
| D17 | 단품 AEC | C/ESR 열화 경로 | — | 입자필터(UKF 제안)+모델 선택 | RUL | (확인 필요) | 가변 조건 | ○(열화 모델) | × |
| D18 | 컨버터(AEC+반도체) | 건전성 시계열 | (확인 필요) | DL | 커패시터 건전성 → 컨버터 SoH/RUL | (확인 필요) | (확인 필요) | (확인 필요) | (확인 필요) |
| D19 | DC-DC | 단자 V/I | — | 디지털 트윈(모델+파라미터 식별) | 실시간 C, L, 스위치 | 실험(확인 필요) | (확인 필요) | ○ | ○ |
| D20 | 컨버터 | (확인 필요) | — | gPC 확률 디지털 트윈(FPGA) | 진단 | (확인 필요) | (확인 필요) | ○ | ○ |
| M24 | MMC SM | 스위칭 함수 + 전압 | 이상치 | LOF | 이상 순위 | (확인 필요) | (확인 필요) | × | ○ |
| M25 | MMC SM | 스위칭 상태 시퀀스 | 학습 | CapAgingNet | 노화 등급(95.32%) | **시뮬** | 미확인 | × | ○ |
| M26 | MMC SM | 암 전류, 스위칭 상태, 전압 | 원시 | ADALINE | C | (확인 필요) | 노화/가혹 조건 | **○(회로식 매핑)** | ○ |

(사실) 데이터 기반 논문 중 인버터 **전류 고조파**를 입력으로 쓰는 저널 논문은 D2(커패시터 전압·전류의 2f1·fsw FFT 성분, 단상)와 D1(소스 전류, 세부 미확인), D6(대역 분리 입력)뿐이며, 스위치 전류·상전류·중성점 전류의 스펙트럼을 CNN 에 넣은 저널 논문은 발견되지 않았다.

---

## 6. 핵심 논문 비교 (Stage 3 선정 + Stage 4 대체 카드)

선정 기준: (a) 현재 기술 동향을 대표, (b) 3-Level NPC·분할 DC-link·고조파·데이터 기반 등 본 프로젝트 축과 직접 연결, (c) 최근 5년. **본문 접근 불가로 17항목 정독(paper-analyzer)은 수행하지 못했고**, 아래 카드는 초록 수준이다. 각 카드의 "사실" 은 초록에 있는 내용, "해석/추론" 은 본 분석자의 판단이다.

### 6.1 핵심 10편 카드

**K1 = R3. Zhao, Davari, Lu, Wang, Blaabjerg (2021), IEEE TPEL 36(4):3692–3716** — 사실: DC-link 커패시터 CM 기법을 응용 목적·구현 방식·정확도 기준으로 비교 평가한 개관(TPEL 우수논문 언급 페이지 확인). 해석: 2021 시점의 분류 체계(ESR/C/온도, 주입/비주입, online/quasi/offline)가 이후 논문의 공통 언어가 됨. 프로젝트 관련성: 관련연구 절의 기준 리뷰. 근거: 초록. 본문 확인 불가.

**K2 = P20. Sundararajan et al. (2020), IEEE TPEL 35(6):6386–6396, DOI 10.1109/TPEL.2019.2951859** — 사실: 정류기 전단 3상 인버터의 전해 DC-link 커패시터에 대해 Goertzel 알고리즘(단일 빈 DFT)으로 선택 주파수 성분을 추출해 ESR 과 C 를 추정하고, C 를 온도 민감 파라미터로 써서 코어/핫스팟 온도까지 추정. 해석: FFT 전체 대신 관심 주파수 몇 개만 계산하는 것이 임베디드 구현에 유리하다는 접근. 추론: 프로젝트의 CNN 입력 feature 를 전 스펙트럼이 아니라 소수 고조파 빈으로 줄일 때 Goertzel 이 직접 쓰일 수 있다. 미확인: 어떤 빈(fsw 대역인지 6f 정류 리플인지), 커패시터 전류가 측정인지 재구성인지.

**K3 = P26. Ghadrdan, Peyghami, Mokhtari, Blaabjerg (2022), IEEE TPEL 37(8):9733–9744, DOI 10.1109/TPEL.2022.3153842** — 사실: Back-to-back 컨버터에서 **출력(AC) 전류**로부터 커패시터 전류의 스위칭 주파수 성분을 재구성하고 DC-link 전압과 함께 소산계수 DF = tanδ = ω·C·ESR 를 계산, DF 를 수명 지표로 제안하며 EoL 기준을 제시; 스위칭 주파수·ESL·계통 필터가 정확도에 미치는 영향 언급. 해석: "커패시터 전류 센서 없이 상전류+스위칭 상태로 커패시터 전류를 재구성한다" 는 본 프로젝트의 신호 생성 철학(iSa2, iC1/iC2 를 스위칭 상태로 얻음)과 가장 가까운 저널 논문. 미확인: 재구성 수식, 온도·부하 처리.

**K4 = M3. Ribeiro/Han et al. (2025), IEEE/CAA J. Autom. Sinica 12, DOI 10.1109/JAS.2025.125159** — 사실: 계통연계 3L-NPC-VSI 에서 **PWM 전략과 토폴로지의 상호작용으로 생기는 고유 상호변조(intermodulation) 신호**를 주입 없이 이용, 비정수 재귀 슬라이딩 DFT + 망각계수 RLS(oSDFT-RLS) 관측기 구조로 C 와 ESR 을 시간-주파수 영역에서 추정, 기존 센서만 사용. 해석: 본 조사에서 **"NPC 의 자연 발생 스펙트럼 성분으로 커패시터를 진단" 한 유일한 저널 논문**. 추론: 그 상호변조 성분이 중성점 전류의 3f1 성분과 스위칭 측대파의 조합일 가능성이 크나 본문 미확인. 프로젝트 관련성: 최우선 정독 대상. 미확인: 정확한 성분, 검증 조건, C1/C2 개별 여부.

**K5 = M2. Ribeiro, Alves, de Sousa, Oliveira (2024), Comput. Electr. Eng. 119:109577, DOI 10.1016/j.compeleceng.2024.109577** — 사실: 3L-NPC 기준전압에 상호고조파 주파수의 영상분 구형파를 더해 중성점 전류를 주입하고, Wavelet 분해로 여러 주파수 성분에서 ESR 과 C 를 동시 추정(오차 <2%, Fourier 대비 우수), HW·제어 변경 없음. 해석: NP 전류가 C1·C2 를 나누어 흐르는 구조를 진단에 이용한 능동형. 프로젝트 관련성: 주입형 대비 "무주입 고조파" 접근의 차별점 근거. 미확인: C1/C2 분리 여부, 검증 형태.

**K6 = M1. Min, Choi, Blaabjerg (2026), IEEE TIE 73(8):12452–12463** — 사실: 3L-NPC 기준전압에 오프셋을 주입해 vC1−vC2 를 설정치까지 발산시키고, 그 충방전 프로파일에서 **상·하단 커패시터 C 를 개별 추정**(평균 오차 <1%), 출력전류 영향 보상, 추가 HW 없음. 해석: Q = C·Δv 의 시간영역 직접 이용. 프로젝트 관련성: "상·하단 개별 진단" 을 다룬 유일한 저널 논문이므로 비교 기준. 미확인: ESR 추정 여부, 실험 조건.

**K7 = M5. Zhang, He, Wang, Chen (2023), IEEE TPEL 38(8):10183–10195, DOI 10.1109/TPEL.2023.3262758** — 사실: 3L T-type 인버터를 DC-link·AC 측에서 모델링해 정상/OC 고장 시의 고유 DC-link 고조파 성분을 도출, 커패시터 전류를 재구성하며, 스위치 OC 진단(출력전류·미분, 상전류 잔차, NP 전압 잔차)과 커패시터 CM 을 하나의 프레임워크로 통합; "signal injection", "extra hardware" 서브모듈 언급. 해석: 3레벨 분할 DC-link 의 고유 고조파 모델을 진단에 쓴 사례. 추론: NPC 와 T-type 은 NP 전류 형성 원리가 유사하므로 모델링 방식이 이식 가능. 미확인: 커패시터 파라미터가 C 인지 ESR 인지.

**K8 = D2. Park, Kim, Kwak (2022), J. Power Electron. 22:513–, DOI 10.1007/s43236-021-00366-x** — 사실: 단상 DC/AC 컨버터 입력 커패시터의 전압·전류 실험 파형을 FFT 해 **2·f1 과 fsw 의 지배 성분**을 DNN 입력으로 사용, C 와 ESR 을 회귀. 해석: "물리적으로 의미 있는 두 주파수 성분만 골라 신경망에 넣는" 구조로, 프로젝트의 "고조파 feature → CNN" 과 가장 가깝다(단, 단상·커패시터 직접 측정·DNN). 미확인: 정확도, 운전조건 범위, 온라인 여부.

**K9 = D3. IEEE TIE 72(4):4227–4237 (2024/2025, 저자 확인 필요)** — 사실: 3상 AC/DC/AC 컨버터에서 정상 운전 신호(DC-link 전압 리플의 PSD)를 GPR 로 학습해 C 를 추정, 예측 불확실성 제공, 추가 HW·주입 없음, **여러 부하·출력 주파수**에서 실험 프로토타입 평균 오차 <2%. 해석: 데이터 기반 방법 중 다중 운전조건 검증과 불확실성 정량화를 갖춘 드문 사례. 프로젝트 관련성: 운전조건 강건성 검증 설계의 벤치마크. 미확인: 저자, 정확한 입력 대역.

**K10 = M25. Deng et al. (2025), Global Energy Interconnection 8(3):420–432** — 사실: MMC 시뮬레이션 플랫폼으로 노화 상태별 SM 스위칭 상태 시퀀스 데이터셋을 만들고 딥 네트워크 CapAgingNet 으로 노화 등급 분류(Top-1 95.32%, F1 95.49%), 추가 샘플링 채널 없음. 해석: 밸런싱 정렬 알고리즘이 노화 SM 을 더 자주/덜 삽입하는 효과를 학습한 것으로 보임(추론). 한계(사실): 시뮬레이션 데이터만. 프로젝트 관련성: "시뮬 기반 DL 노화 등급 분류" 의 한계(실험 검증 부재)를 그대로 보여주는 대조군.

동향 대표 보조: **P35 Baumann 2024** (정지 시 방전 프로파일 + 온도 의존성 보상 SoH), **P39 Muhammed Ramees & Ahmad 2026** (MPPT 전이를 자연 여기로 쓰는 무주입 C 추정), **M28** (암 내 SM 비교로 온도 효과 분리) — 최근 흐름의 세 방향(quasi-online 과도, 자연 여기, 비교 기준).

### 6.2 핵심 논문 비교표

| 논문 | 연도 | Journal | Topology | Cap 위치 | Cap 종류 | 입력 신호 | Feature | 진단 방법 | 추정 대상 | Online | 실험 검증 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| K1 R3 | 2021 | IEEE TPEL | 전반 | DC-link | AEC·필름 | — | — | 리뷰 | ESR, C, T | — | — |
| K2 P20 | 2020 | IEEE TPEL | 정류기+3상 인버터 | DC-link | AEC | 커패시터 v, i | Goertzel 선택 빈 | 성분 비 | ESR, C, 온도 | ○ | ○(초록) |
| K3 P26 | 2022 | IEEE TPEL | B2B 2L | DC-link | AEC | 출력 전류 + vdc | 재구성 i_C 의 fsw 성분 | DF=ωC·ESR | DF | ○ | ○(초록) |
| K4 M3 | 2025 | IEEE/CAA JAS | 3L-NPC | 분할 DC-link | n/s | 기존 센서 | 고유 상호변조 성분 | oSDFT-RLS 관측기 | C, ESR | ○(무주입) | 미확인 |
| K5 M2 | 2024 | CEE | 3L-NPC | 분할 DC-link | n/s | vdc, idc + 영상분 주입 | Wavelet 계수 | 주입 + Wavelet | ESR, C | ○(주입) | 미확인 |
| K6 M1 | 2026 | IEEE TIE | 3L-NPC | C1, C2 개별 | n/s | vC1, vC2 + 오프셋 주입 | 충방전 프로파일 | Q=CΔv | C(개별) | ○(주입) | ○(추정) |
| K7 M5 | 2023 | IEEE TPEL | 3L T-type | 분할 DC-link | n/s | 출력 전류, NP 전압 | 고유 DC-link 고조파, 재구성 i_C | 모델 잔차 | 커패시터 상태 | ○ | 미확인 |
| K8 D2 | 2022 | JPE | 단상 DC/AC | 입력 커패시터 | n/s | 커패시터 v, i 실험 파형 | FFT: 2f1, fsw 성분 | DNN 회귀 | C, ESR | 미확인 | ○(데이터 실험) |
| K9 D3 | 2024/25 | IEEE TIE | AC/DC/AC 2L | DC-link | n/s | vdc 리플 | PSD | GPR | C | ○ | ○(다중 조건) |
| K10 M25 | 2025 | GEI | MMC | SM | n/s | 스위칭 상태 시퀀스 | 학습 특징 | DL 분류 | 노화 등급 | ○ | ×(시뮬만) |
| **본 프로젝트** | — | — | 3L-NPC | C1, C2 | (확인 필요) | iSa2, iC1, iC2, iNP (스위칭 상태로 생성) | 저차·측대파 고조파 | FFT → CNN | 노화 등급/C·ESR | 목표: 무주입 online | 현재 시뮬 |

### 6.3 항목 체크표 (○ 사용 / × 미사용 / ? 미확인)

| 항목 | K1 | K2 | K3 | K4 | K5 | K6 | K7 | K8 | K9 | K10 | 프로젝트 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DC-link voltage | 리뷰 | ○ | ○ | ? | ○ | ○ | ○ | ○ | ○ | × | (가능) |
| Capacitor current(직접) | 리뷰 | ? | × | × | ? | × | × | ○ | × | × | 시뮬 생성 |
| Capacitor current(재구성) | 리뷰 | ? | ○ | ? | ? | × | ○ | × | × | × | ○ |
| Neutral-point current/전압 | × | × | × | ? | ○(주입) | ○(간접) | ○(NP 전압) | × | × | × | ○ |
| Phase current | 리뷰 | × | ○ | ? | × | × | ○ | × | × | × | ○ |
| Switching(device) current | × | × | × | × | × | × | × | × | × | × | **○** |
| Ripple current | 리뷰 | ○ | ○ | ? | ○ | × | ○ | ○ | × | × | ○ |
| Harmonic component | 리뷰 | ○ | ○ | ○ | ○ | × | ○ | ○ | ○(PSD) | × | ○ |
| FFT / DFT | 리뷰 | Goertzel | ? | SDFT | × | × | ? | FFT | PSD | × | FFT |
| Wavelet | 리뷰 | × | × | × | ○ | × | × | × | × | × | (후보) |
| Charge/discharge profile | 리뷰 | × | × | × | × | ○ | × | × | × | × | (후보) |
| ESR | ○ | ○ | (DF) | ○ | ○ | ? | ? | ○ | × | × | (라벨 후보) |
| Capacitance | ○ | ○ | (DF) | ○ | ○ | ○ | ? | ○ | ○ | (등급) | ○ |
| Temperature | ○ | ○ | ? | ? | ? | ? | ? | ? | ? | ? | 미반영 |
| Machine Learning | 언급 | × | × | × | × | × | × | ○ | ○ | ○ | ○ |
| CNN | × | × | × | × | × | × | × | ×(DNN) | × | ○(DL) | **○** |
| 3-Level NPC | 언급 | × | × | ○ | ○ | ○ | (T-type) | × | × | × | ○ |
| 실험 검증 | — | ○ | ○ | ? | ? | ○ | ? | ○ | ○ | × | **×** |
| 상·하단 개별 진단 | — | × | × | ? | ? | ○ | × | × | × | × | 목표 |

(사실) "Switching(device) current" 행은 10편 모두 ×이며, 검색 전체에서도 해당 저널 논문을 찾지 못했다. (사실) "3-Level NPC × ML/CNN" 조합은 비어 있다. (해석) 프로젝트가 채워야 할 칸은 실험 검증과 온도 반영이다.

### 6.4 기술적으로 중요한 논문의 추가 평가 (초록 기준, 미확인 항목 다수)

| 논문 | 장점 | 한계(저자/분석자) | 센서 요구 | 계산 복잡도 | 실시간 구현 | 부하 변동 | 온도 | 스위칭 조건 |
|---|---|---|---|---|---|---|---|---|
| K2 P20 | 단일 빈 계산으로 경량, ESR·C·온도 동시 | 커패시터 전류 측정 필요 여부 미확인 | vC, iC(측정/재구성 ?) | 낮음(Goertzel) | 명시적 동기(초록) | ? | **온도 추정 포함** | 선택 빈이 fsw 이면 fsw 의존(추론) |
| K3 P26 | 커패시터 전류 센서 불필요, DF 는 C·ESR 정보 모두 포함 | DF 만으로 C/ESR 분리 불가(추론); ESL·필터 영향(저자) | 상전류, vdc(기존) | 중간(재구성+스펙트럼) | ? | ? | ? | **fsw 영향 언급(저자)** |
| K4 M3 | 무주입, 기존 센서, 시간-주파수 추적 | 상호변조 성분의 크기가 변조지수·부하에 의존할 가능성(추론) | 기존 | 중간(SDFT+RLS) | 관측기 구조(재귀) | ? | ? | PWM 전략 의존(저자 언급) |
| K5 M2 | ESR·C 동시, 다중 주파수 | 주입은 전력품질 제약(저자 언급) | 기존 | 중간~높음(Wavelet) | ? | ? | ? | 상호고조파 선택 |
| K6 M1 | C1/C2 개별, <1%, 보상 전략 | 주입형; ESR 미확인 | vC1, vC2 | 낮음 | ? | 출력전류 보상(저자) | ? | ? |
| K7 M5 | 스위치 고장과 통합, 고유 고조파 모델 | 추가 HW 가능성 | 출력 전류, NP 전압 (+?) | 중간 | ? | ? | ? | 고조파 모델이 변조 의존(추론) |
| K8 D2 | 물리 기반 주파수 선택 + DNN | 단상, 커패시터 직접 측정, 데이터 범위 미확인 | vC, iC | 학습 후 낮음 | ? | ? | ? | fsw 성분 사용 |
| K9 D3 | 다중 조건, 불확실성, 저샘플링 | 저자·입력 대역 미확인 | vdc | 학습 후 낮음(GPR 추론 비용은 데이터 수 의존, 추론) | ○(주장) | **○(부하·주파수 변화 검증)** | ? | ? |
| K10 M25 | 추가 채널 없음, 높은 분류 정확도 | **시뮬 데이터만**, 일반화 미검증 | 스위칭 상태 | 학습 후 낮음 | ○(주장) | ? | ? | 정렬 알고리즘 의존(추론) |

---

## 7. 주요 진단 신호

| 신호 | 사용 논문(대표) | 어떤 정보(사실/해석) | 프로젝트 관련성 |
|---|---|---|---|
| DC-link 전압 리플 (fsw 대역) | P6, P10, P15, P26, D4 | ESR 항이 지배 → ESR (해석: v_ripple,sw ≈ ESR·i_ripple,sw) | vC1, vC2 리플 |
| DC-link 전압 리플 (저주파: 2f_grid, 6f 정류, 주입 서브하모닉) | P11, P14, P16, P32, P37, M10 | 1/(ωC) 항이 지배 → C | NPC 의 3f1 NP 리플과 유사 원리 |
| DC-link 전압 과도/방전/충전 프로파일 | P23, P27, P29, P31, P33–P35, P38, M1, M11 | RC 방전·Q=CΔv → C, 온도 보상 가능(P35) | quasi-online 대안 |
| 커패시터 전류(직접 측정) | P15, P20(?), D2 | ESR·C 추정의 기준 신호이나 센서 추가 부담 | 시뮬에서는 직접 얻음 |
| 커패시터 전류(재구성: 상전류×스위칭 상태) | P26, M4, M5, M27, P25(?) | 센서 없이 fsw 성분 확보 | **iC1/iC2 생성 방식과 동일** |
| 상전류·출력전류 | P26, M5, P39 | 재구성 원천 / 고장 잔차 | ia, ib, ic |
| 중성점 전류·전압 | M1, M2, M4, M5 | 3레벨 특유; 주입 또는 잔차 | iNP, vNP |
| 스위칭 신호·상태 시퀀스 | M20, M22, M25 | MMC 정렬·삽입 통계에 노화 반영 | (해당 없음) |
| 스위치 전류(iSa2 등) | **없음** | — | 프로젝트 고유 |
| PV 전압·MPPT 전이 | P10, P11, P24, P39 | 자연 여기 | — |
| 온도(직접) | D15, P20(추정) | ESR 보정 | 미반영(추가 필요) |

---

## 8. 주요 Health Indicator

| HI | 논문 수(대략) | 커패시터 종류 | 비고(사실/해석) |
|---|---|---|---|
| ESR 증가 | ~25 | AEC 중심 | fsw 리플 비 또는 임피던스; 온도 의존성 강함(P10, P35 보정 언급) |
| Capacitance 감소 | ~50 | AEC, 필름, MMC SM | 가장 많이 추정되는 양; 필름은 C 가 사실상 유일 지표(E5, E6) |
| DF(tanδ) | P26 | AEC | C·ESR 결합 지표 |
| 임피던스 |Z(f)| | P11, P13, P24 | AEC | 다중 주파수 피팅으로 ESR/C 분리 |
| 온도(코어) | P20, D15 | AEC | C 의 온도 민감성 이용 |
| 노화 등급 분류 | D7, D8, D13, D14, M25 | — | 라벨 정의는 논문마다 다름(미확인 다수) |
| SoH / RUL | P35, D14, D16–D18, D22 | AEC | 열화 궤적 기반 |
| 이상 순위(비지도) | M22, M24 | MMC | 기준 없는 상대 비교 |

논문별 "입력 → Feature → 추정 → HI" 사슬(대표):
- P26: 출력 전류+스위칭 상태 → 재구성 i_C 의 fsw 성분 + vdc 리플 → DF=ωC·ESR → DF 임계.
- P20: vC, iC → Goertzel 빈 → ESR, C → ESR(열화), C(열화+온도).
- P14: vdc, idc → 2f_grid 성분 → v/i 비 → C.
- M1: vC1, vC2 + 오프셋 → 설정 전압차 도달 전하 → C1, C2.
- M2: 영상분 주입 → NP 전류 → Wavelet 계수 → ESR, C.
- M3: 고유 상호변조 성분 → SDFT 추적 → RLS → C, ESR.
- D2: vC, iC FFT → 2f1, fsw 성분 → DNN → C, ESR.
- D3: vdc 리플 PSD → GPR → C(+불확실성).
- M25: 스위칭 상태 시퀀스 → DL → 노화 등급.

---

## 9. Parameter estimation 기술

| 계열 | 논문 | 핵심(사실) | 해석·한계 |
|---|---|---|---|
| 리플 비(정상상태) | P6, P10, P15, P14, P11 | fsw 또는 2f 성분의 v/i 비 | 단순·경량; 리플이 작은 필름 커패시터에서 SNR 낮음(추론) |
| RLS 계열 | P1, P8, P9, P28, P38, M8, M27, M3 | 주입 또는 자연 리플 + 재귀 최소제곱 | 잡음·이상치 대책(P28), 망각계수(M3, M8) |
| Kalman/관측기 | P17(EKF), M7(고이득 적응), M15(Lyapunov), P43·P44(파라미터 관측기), P33(RELS), TIE 2026 VBAKF(제목만) | 상태·파라미터 동시 추정 | 2020 년대 DC-link Kalman 저널은 드묾(사실: 확인된 것 P17 뿐) |
| 최대우도/통계 | P36(ML+NR), M22(CUSUM) | 수렴 안정화, 변화 검출 | 필름·철도 응용 |
| 주입/여기 | P1, P2, P8, P9, P13, P18, P19, P24, P25, P30, M1, M2, M4, M27 | 저주파·상호고조파·공진·영상분 | 전력품질·손실 제약; 멀티레벨은 변조기 내 주입으로 HW 없이 가능 |
| 과도/방전 프로파일 | P23, P27, P29, P31, P33, P34, P35, P38, M9, M11 | 기동·정지·주차·회생 구간 | 실용성 높음(EV·항공·풍력); 온도 보상(P35) |
| 자연 여기 | P39(MPPT 전이), M10(2f), M3(상호변조), P22(링잉) | 무주입 | 성분 크기가 운전조건에 의존(추론) |
| 비교/기준 | M16, M17, M28, M9 | 동일 암·동일 컨버터 내 상대 비교로 온도 공통 성분 제거 | NPC 에서 C1 vs C2 비교로 이식 가능(추론) |

---

## 10. Signal processing 기술

| 기법 | 논문 | 목적 | 비고 |
|---|---|---|---|
| 아날로그/디지털 대역통과 + 비 | P6, P10, P15 | fsw 성분 추출 | 온도 민감(P20 초록 언급) |
| FFT | P13, D2 | 다중 주파수 임피던스, DNN 입력 | 전체 스펙트럼 계산 부담 |
| Goertzel(단일 빈 DFT) | P20 | 관심 빈만 계산 | 임베디드 적합 |
| SOGI | P11(2f), (P24?) | 특정 주파수 성분 추출 | 계통 주파수 추종 |
| 슬라이딩 DFT(비정수 재귀) | M3 | 상호변조 성분 실시간 추적 | RLS 와 결합 |
| Wavelet / RT-SDWPT | P21, P30, M2 | 비정상 신호·주입 응답의 시간-주파수 | 계산량 큼(추론) |
| PSD | D3 | ML 입력 | 저샘플링 강조 |
| 링잉 감쇠 해석 | P22 | MHz 대역 | 고대역 센서 필요(추론) |
| 시계열→이미지 | D13 | CNN 입력 | 단품 ALT |
| 시간-주파수 이미지(CWT)→CNN | (capCNN, 저널 미확인) | MMC SM 전압·암 전류 | 부록 B |

(사실) 흐름: 아날로그 필터·FFT(2010년대 초) → 디지털 필터+RLS → Goertzel(2020) → Wavelet/RT-SDWPT(2020–2024) → 비정수 SDFT+RLS 관측기(2025) → PSD/스펙트럼 특징의 ML 입력(2022–2025).

---

## 11. Harmonic 기반 기술 (프로젝트 핵심 관심)

### 11.1 문헌에서 확인된 고조파 이용 방식

| 대역/성분 | 물리적 근거(논문 명시 여부) | 논문 | 추정 |
|---|---|---|---|
| 스위칭 주파수 성분(fsw 및 측대파) | |Z(fsw)| ≈ ESR (P6·P15 초록 취지) | P6, P10, P15, P26, D2, D4 | ESR, DF |
| 2·f_grid(단상 전력 맥동) | 1/(ωC) 지배 (P14 취지) | P11, P14, P24(?), P37, M10 | C, |Z| |
| 6·f_grid 정류 리플 | 정류기 전단 리플 | P16, P20(?), P32 | ESR, C (대역 미확인) |
| 주입 서브하모닉/상호고조파 | 임피던스 피팅 | P1, P8, P13, P30, M2 | ESR, C |
| PWM×토폴로지 고유 상호변조 | (M3 초록: PWM 전략·토폴로지 상호작용) | M3 | C, ESR |
| DC-link 고유 고조파 모델(3L T-type) | (M5 초록) | M5 | 커패시터 상태 |
| MMC 고유 저주파 진동 | (M18 초록) | M18 | 건전성 |

### 11.2 부정적 발견(사실: 검색 범위 내 미발견)

- **스위칭 소자(IGBT/MOSFET) 전류 스펙트럼**을 커패시터 CM feature 로 쓴 저널 논문: 없음. 가장 가까운 것은 P26(출력 전류로 커패시터 fsw 전류 재구성)과 반대 방향의 IET J. Eng. 2018(IGBT 고장 → DC-link 전류 스펙트럼, 10.1049/joe.2018.8612), 그리고 특허(US 11,428,750).
- **중성점 전류의 자연 스펙트럼**을 쓴 저널 논문: 없음. M2(주입 NP 전류), M4(능동 조정), M3(고유 상호변조, 신호 미확인)만 존재.
- **출력 기본파의 짝수 고조파(2f1, 4f1, …)** 를 커패시터 노화 feature 로 쓴 저널 논문: 없음. 짝수 고조파 이용은 단상 2f_grid(전력 맥동)뿐.
- 6f 정류 리플 기반 C 추정, 상전류 측대파 vs DC-link C, 전류 스펙트럼→CNN 검색은 예산 소진으로 **미실행**.

### 11.3 커패시터 열화 ↔ 고조파 변화의 물리 (해석·추론, 문헌 직접 근거 없음)

- (해석) 커패시터 임피던스 |Z(f)| = √(ESR² + (1/ωC)²) 이므로, 같은 리플 전류에 대해 ESR 증가는 fsw 대역 전압 리플을, C 감소는 저주파 전압 리플을 키운다. 이것이 모든 리플 기반 방법의 공통 원리다(P6, P14 취지).
- (추론) 3L-NPC 에서 상·하단 커패시터 전압 리플의 저주파 성분은 중성점 전류의 3f1 성분(평형 3상, 정현 변조 시 대표 성분)이 C1, C2 를 충방전하며 생긴다. C1 ≠ C2 이면 vNP 에 3f1 리플과 오프셋 비대칭이 생기고, 이 vNP 변동이 출력 상전압을 변조해 **출력 전압·상전류에 2f1, 4f1 등 짝수 고조파**가 나타날 수 있다(3f1 리플 × f1 기본파의 측대파). 따라서 스위치 전류 iSa2 의 짝수 고조파 "변화량" 은 커패시터 노화 정보를 간접적으로 담을 수 있다.
- (추론, 주의) 그러나 iSa2 는 P·O 상태에서 상전류를 흘리는 반파 정류형 파형이라 **노화와 무관하게** DC + 기본파 + 짝수 고조파를 갖는다. 노화 정보는 "짝수 고조파의 존재" 가 아니라 "C1/C2·ESR 변화에 따른 진폭·위상의 변화" 이며, 이 변화는 부하·변조지수·역률 변화에 따른 변화보다 작을 수 있다. 문헌(D3, M28)이 다중 운전조건 검증과 비교 기준을 강조하는 이유와 같다.
- (추론) 폐루프 전류 제어는 출력 전류의 저차 고조파를 억제하므로, 상전류·스위치 전류보다 **vC1, vC2, vNP, iNP** 쪽이 노화 민감도가 클 가능성이 있다. MATLAB 에서 C1, C2, ESR 을 스윕하며 각 신호의 2f1/3f1/4f1/측대파 민감도를 비교하는 것이 첫 실험이어야 한다(20절).

---

## 12. Online condition monitoring 평가

### 12.1 Offline / Quasi-online / Online 분류

| 구분 | 논문 | 조건 |
|---|---|---|
| Offline | (본 목록에 CM 목적 offline 논문은 포함하지 않음; 소재 가속시험 E5–E9) | 분해·정지 계측 |
| Quasi-online | P1(무부하), P3(정지), P7(기동/정지), P9·P28(회생), P13(야간), P18(비운전 공진), P23(정지 방전), P33(사전충전), P34(주차), P35(정지), P38(비행 후), M11(블리딩 방전) | 특정 운전 구간 |
| Online(주입) | P2, P8, P24, P25, P30, P31(간헐 역충전), M1, M2, M4, M27 | 전력품질·손실 제약 |
| Online(무주입) | P6, P10, P11, P14, P15, P16, P20, P22, P26, P32, P39, M3, M5, M8–M10, M12–M20, M22–M26, M28, D3 | 기존 센서 |

### 12.2 실제 인버터 적용 관점 체크 (초록 기준)

| 논문 | 운전 중 측정 | 추가 센서 | 기존 제어 신호 활용 | 주입 필요 | 정지 필요 | 실시간 계산 | DSP/MCU/FPGA 언급 |
|---|---|---|---|---|---|---|---|
| P11 | ○ | × | ○(MPPT 센서) | × | × | ○ | **○(같은 DSP)** |
| P14 | ○ | × | ○ | × | × | ○ | ○(같은 디지털 제어기) |
| P20 | ○ | ? | ? | × | × | ○ | 암시(Goertzel) |
| P26 | ○ | × | ○(상전류·스위칭 상태) | × | × | ? | ? |
| P29 | ○(과도) | × | ○ | × | × | ○ | ○(디지털 제어기) |
| P32 | ○ | × | ○ | × | × | ? | ? |
| P34/P35/P38 | ×(정지) | × | ○ | × | ○ | ○ | ? |
| P39 | ○ | × | ○(MPPT) | × | × | ? | ? |
| M1 | ○ | × | ○(변조기) | ○(오프셋) | × | ○ | ? |
| M2 | ○ | × | ○(변조기) | ○(영상분) | × | ? | ? |
| M3 | ○ | × | ○ | × | × | ○(재귀) | ? |
| M13 | ○ | × | ○ | × | × | ○ | **○(SM 제어기, 실시간 시뮬)** |
| M23 | ○ | 감소 | ○ | × | × | ○(저부담) | 암시 |
| D3 | ○ | × | ○ | × | × | ○ | ? |
| M25 | ○ | × | ○ | × | × | ○ | ? |

(해석) 2020 년 이후 저널 논문은 대부분 "추가 센서 없음" 을 기본 요건으로 삼는다. 명시적 임베디드 구현 보고는 소수(P11, P14, P29, M13)이며, 실험 검증이 초록에 명시된 논문도 절반 이하다. (사실) R2 는 학계 방법이 복잡성·비용 때문에 산업 채택이 드물다고 지적했다.

### 12.3 센서리스·최소 센서 기술 (14절 요구)

| 이용 신호만 | 논문 | 방식 |
|---|---|---|
| DC 전압 센서만 | P29, P33, P34, P35, P38, D3, D5, D7 | 과도/방전 프로파일, 리플 PSD |
| DC 전압 + 상전류(제어용) | P14, P26, P39, M4, M5 | 커패시터 전류 재구성·2f 비·잔차 |
| DC 전압 + 전원 전압·모델 | P32, P37 | 정류 리플 전류 계산 |
| 변조기 내부 신호(주입) | M1, M2, M4 | 오프셋/영상분/NP 전류 |
| 스위칭 신호·상태만 | M20, M22, M25 | MMC |
| 그룹 센서(감소) | M6, M23, P17 | 추정 전압 |
| 자연 여기 | P39, M10, M3, P22 | MPPT 전이, 2f, 상호변조, 링잉 |

(해석) 본 프로젝트의 "스위칭 상태 × 상전류로 스위치·커패시터 전류를 만든다" 는 접근은 P26·M4·M5·M27 의 재구성 철학과 같은 계열이며, 추가 센서 없이 가능한 방향이다. 단, 시뮬레이션에서 직접 얻는 iSa2 를 실제 장치에서 얻으려면 상전류 센서 + 게이트 신호 동기 샘플링이 필요하다(추론).

---

## 13. Machine Learning (고전 ML)

| 구조 | 논문 | 입력 | 라벨/목표 | 데이터 | 다중 조건 | 비고 |
|---|---|---|---|---|---|---|
| 리플 특징 → 회귀 | D3(GPR), D4(ANN), D5(RF/kNN/ANN/GB/DT/LR), D9(IGWO-BP), P2(SVR, 2008) | vdc 리플(PSD/진폭), 주입 리플 | C(·ESR) | 실험(D3), 미확인(D4, D5, D9) | D3 ○ | D3 만 불확실성·다중조건 명시 |
| 특징 → 분류 | D7(증거추론), D8(RF) | vdc 특징 | 노화/고장 등급 | 미확인 | 미확인 | 라벨 정의 미확인 |
| 비지도 이상 검출 | M24(LOF) | MMC 스위칭 함수+전압 | 이상 순위 | 미확인 | — | 기준 불필요 |
| 통계 변화 검출 | M22(CUSUM) | 스위치 on/off 시간 | 이상 | 미확인 | — | — |
| 생성 모델 | D10(VAE+LSTM) | 미확인 | C | 미확인 | — | 철도 견인 |

(사실) 고전 ML 저널 논문의 입력은 거의 전부 **DC-link 전압 리플**이며, 전류 고조파 입력은 D1(소스 전류, 세부 미확인)과 D6(대역 분리) 정도다. (사실) 노화 데이터는 대부분 커패시터 교체·직렬저항 추가 등 **모사 노화**로 추정되나 초록에서 확인된 것은 D3(실험 프로토타입)뿐이다. (사실) 3L-NPC/T-type 대상 ML 저널 논문은 없다.

---

## 14. Deep Learning / CNN

| 구조 | 논문 | 입력 표현 | 목표 | 데이터 | 물리 결합 |
|---|---|---|---|---|---|
| FFT 성분(2f1, fsw) → DNN | D2 | 커패시터 v, i 의 두 주파수 성분 | C, ESR 회귀 | 실험 파형 | 주파수 선택 |
| 대역 분리 입력 → DL | D6 | 주파수 대역별 신호 | C, ESR | 미확인 | 대역 선택 |
| 시계열→이미지 → CNN | D13 | ALT 단품 V, I, R 이미지 | 수명 등급 | 실제 ALT(컨버터 아님) | × |
| ESR/C 궤적 → CNN-LSTM | D14 | 열화 시계열 | 노화 상태 + RUL | 미확인 | 산포 고려 |
| 스위칭 상태 시퀀스 → DL | M25 | MMC SM 삽입 패턴 | 노화 등급 | **시뮬** | × |
| 회로식 매핑 NN | M26(ADALINE) | 암 전류, 스위칭 상태, 전압 | C | 미확인 | **○(가중치=회로 파라미터)** |
| LSTM(온도) | D15 | 다주파 전류+ESR(T,I) | 온도 | 실험 | 부분 |
| LSTM RUL | D12, D16 | 열화 측정/이력 | RUL | ALT | × |
| 디지털 트윈 | D19, D20 | 단자 V/I | 실시간 파라미터 | 실험(확인 필요) | ○ |
| PINN | (슈퍼커패시터만; DC-link 없음) | — | — | — | — |

**CNN 입력 데이터 정리(사실)**: 확인된 저널 CNN 입력은 (a) ALT 시계열을 변환한 이미지(D13), (b) ESR/C 열화 시계열(D14), (c) MMC 스위칭 상태 시퀀스(M25, 시뮬). 저널 여부 미확인이나 관련성 높은 것: capCNN(IEEE DataPort/Aalborg, MMC SM 전압·암 전류의 CWT 이미지 → CNN → C·ESR 회귀). **인버터 스위치/상/DC-link 전류의 스펙트럼 또는 스펙트로그램을 CNN 입력으로 쓴 저널 논문은 없다.** Transformer·오토인코더·전이학습을 커패시터 CM 에 쓴 저널 논문도 발견되지 않았다.

---

## 15. Topology 별 기술 차이

| Topology | 커패시터 스트레스 특성(해석) | 진단 방법의 차이(사실) | 남은 문제(해석) |
|---|---|---|---|
| 2-Level VSI | 단일 DC-link 에 fsw 리플 + 부하 의존 저주파(단상 2f, 정류 6f) | 리플 비·RLS·주입·방전 프로파일이 성숙; ML 은 vdc 리플 중심 | 온도·부하 분리, 필름 커패시터의 작은 리플 |
| NPC / T-type | 분할 커패시터에 **3f1 NP 전류**가 흐르고 C1≠C2 이면 NP 전압 불평형 | 변조기 주입(오프셋·영상분·NP 조정)으로 C1/C2 개별 추정(M1, M2, M4); 고유 상호변조(M3); 고유 고조파 모델+잔차(M5) | **무주입·개별 진단·ML 결합 없음**; 문헌 4–5편에 불과 |
| Flying-Capacitor | 플라잉 커패시터 전압 자체가 밸런싱 대상; 스위칭 주기 단위 충방전 | 적응 관측기(M7); NNPC 센서리스 전압 추정(M6) | IEEE Trans. 급 CM 논문 미발견(미조사 부분 있음) |
| CHB | 셀별 DC 커패시터에 2f 리플(단상 셀) | 셀 전압 RLS(M8), 기준 셀 전이+전력 균형(M9), 고유 2f 임피던스(M10) | ESR 추정·온도 분리 |
| MMC | 다수 SM 커패시터, 정렬·밸런싱 알고리즘이 삽입 빈도 조절 | 기준 SM 비교, 스위칭 상태 이용, 방전, Lyapunov 추정, ML/DL 등 방법 다양 | 실험 검증 비율 낮음(초록 기준), 온도 분리(M28) |
| PV / 드라이브 / 견인 | 응용 고유 구간(야간, MPPT 전이, 회생, 주차) | quasi-online·자연 여기 | 구간 발생 빈도 의존 |

(해석) 진단 방법은 "그 토폴로지에서 커패시터를 추가 HW 없이 여기(excite)할 수 있는 고유 경로" 를 찾는 방향으로 분화한다: 2L 은 리플·과도, NPC 는 NP 경로, CHB 는 셀 전력 균형, MMC 는 SM 삽입 패턴.

---

## 16. 최근 5년 기술 발전 흐름 (문헌 기반 재구성)

문헌이 보여주는 순서(연도·대표 논문). 사전에 가정한 흐름이 아니라 확인된 논문으로 구성했다.

1. **기반(2005–2013)**: 주입 + 디지털 필터 + RLS 로 C/ESR (P1, P2, P8); 리플 비 (P6); 전용 HW 유닛 (P5); 정지 시 여기 (P3); 항공·철도 필름 C 감소 감시 (P7, E3).
2. **기존 대표(2015–2019)**: 회생 모드 주입 (P9), PV 2f 임피던스·비침습 C (P11, P14), 야간 quasi-online 다중 주파수 임피던스 (P13), fsw 성분 ESR 시스템 (P15), EKF 뱅크 개별 추정 (P17), LC 공진 (P18), MMC 기준 SM·방전 (M16, M11).
3. **최근(2020–2023)**: Goertzel + 온도 추정 (P20), 링잉 감쇠 ESR (P22), DF 지표 + 출력전류 재구성 (P26), 과도 프로파일·저샘플링·추가 샘플링 없음 (P27, P29), Wavelet/RT-SDWPT (P21, P30), 간헐 역충전 (P31), 전류센서 없는 정류 리플 (P32), T-type 통합 진단 (M5), MMC Lyapunov·PSC-PWM·스위칭 신호 (M15, M19, M20), ML 회귀 시작 (D2, D4, D7).
4. **현재 emerging(2024–2026)**: **NPC 전용**(M2 주입 Wavelet → M3 무주입 상호변조 → M1 개별 충방전; M4), 주차·정지·비행 후 방전 프로파일 + 온도 보상 (P34, P35, P38), MPPT 전이 자연 여기 (P39), 최대우도 필름 C (P36), GPR 불확실성·다중조건 (D3), 하이브리드 ML (D5), MMC DL·물리 매핑 NN (M25, M26), 비교 기준으로 온도 분리 (M28), 리뷰의 데이터 기반 지향 (R4, R5).

(사실 기반 요약 흐름) `주입+RLS` → `자연 리플 비(ESR)/2f(C)` → `quasi-online 과도·방전(기존 센서)` → `커패시터 전류 재구성(센서리스)` → `경량 스펙트럼 추출(Goertzel/SDFT/Wavelet)` → `토폴로지 고유 경로(NP·SM·셀)` → `데이터 기반(리플 PSD/FFT 성분 → NN)` → `물리 내장 NN·디지털 트윈·비교 기준(온도 분리)`. 사용자가 예시한 흐름과 대체로 일치하나, "Sensorless" 는 별도 단계라기보다 2018 년 이후 모든 단계의 기본 요건이 되었고, "Hybrid Physics+AI" 는 DC-link 에서는 아직 MMC 의 ADALINE(M26)·디지털 트윈(D19, D20) 수준에 머문다.

---

## 17. 현재 기술적 한계 (문헌 근거)

| 한계 | 근거 |
|---|---|
| ESR 의 온도 의존성으로 인한 오진 | P10·P35 가 온도 보정을 별도 다룸; P20 은 C 로 온도를 추정; M28 은 비교로 분리 |
| 리플 크기·스펙트럼이 부하·변조·역률에 의존 | D3 만 다중 조건 검증 명시; P26 이 fsw·ESL·필터 영향 언급 |
| 커패시터 전류 센서 부담 | P26, P32, M4 등이 재구성으로 회피 → 재구성 정확도가 새 한계(추론) |
| 필름 커패시터의 작은 ESR·리플 | 필름 대상 논문은 C 만 추정(P36, E3, E1, E2) |
| 주입형의 전력품질·손실 제약 | M2 초록 명시 |
| 실험 검증·장기 노화 데이터 부족 | 초록에 실험 명시 비율 낮음; M20·M25 시뮬만; ML 논문 데이터 출처 대부분 미확인 |
| 산업 채택 | R2: 복잡성·비용으로 채택 드묾 |
| NPC 등 비-2L 토폴로지 문헌 희소 | 4절 표 |
| 검증 깊이(본 조사 자체) | 본문 미확인 → 정확도·조건 비교 불가 |

---

## 18. Research Gap (문헌 근거 + 확신도)

| # | Gap | 근거 | 확신도 |
|---|---|---|---|
| G1 | **3L-NPC 커패시터 CM 에 ML/DL 을 결합한 저널 논문 없음** | M1–M4 모두 모델 기반; D 계열에 NPC 없음 | 높음(검색 범위 내) |
| G2 | **스위칭 소자 전류(iSa2 등) 스펙트럼을 커패시터 노화 feature 로 쓴 논문 없음** | 11.2 부정적 발견 | 높음 |
| G3 | **중성점 전류의 자연 스펙트럼(무주입) 이용 없음**; NPC 는 주입형 3편 + 상호변조 1편(성분 미확인) | M1–M4 | 중간(M3 본문 확인 필요) |
| G4 | 출력 기본파 짝수 고조파(2f1, 4f1) 와 노화의 관계 연구 없음 | 11.2 | 중간(관련 검색 일부 미실행) |
| G5 | 상·하단 커패시터 **개별** 진단은 M1 한 편(주입형); 무주입 개별 진단 없음 | M1 | 높음 |
| G6 | 전류 고조파 스펙트럼/스펙트로그램 → CNN 저널 논문 없음 (CNN 은 단품 ALT 이미지·열화 시계열·MMC 스위칭 상태에 한정) | 14절 | 높음 |
| G7 | 데이터 기반 방법의 다중 운전조건·온도 강건성 검증 부족 | D3 외 대부분 미확인 | 중간(초록 한계) |
| G8 | 실험(가속 노화) 데이터 기반 DL 부족; 시뮬 데이터 의존 | M25, M20; ML 데이터 출처 미확인 | 중간 |
| G9 | 필름 DC-link(견인·NPC 산업용)에서 ESR 외 지표·고조파 기반 C 추정 부족 | P36, E 계열 | 중간 |
| G10 | Physics-informed / 하이브리드가 DC-link 에서 부재 (MMC ADALINE, DC-DC 디지털 트윈만) | M26, D19, D20 | 높음 |
| G11 | ANPC·Flying-capacitor·스너버·클램프·공진 커패시터 CM 저널 부재 | 4절 | 중간(FC 2차 검색 미실행) |
| G12 | Transformer·오토인코더·전이학습 부재 | 14절 | 중간 |

검색 한계: 예산 소진으로 미실행 검색(11.2, 4절)과 본문 미확인 때문에 "없다" 는 "본 조사 범위에서 발견되지 않았다" 로 읽어야 한다.

---

## 19. 향후 유망 기술 (문헌 흐름에서 도출)

1. **무주입·기존 센서·토폴로지 고유 경로**: NPC 의 NP 경로(3f1 리플, 상호변조)를 주입 없이 쓰는 방향(M3 의 확장). 근거: 주입형(M1, M2)의 전력품질 제약과 산업 채택 문제(R2).
2. **재구성 전류의 경량 스펙트럼 특징 + 데이터 기반 회귀**: P26(재구성)+P20(Goertzel)+D2/D3(FFT·PSD→NN) 의 결합. 근거: 세 요소가 각각 저널에서 검증됐으나 결합 사례 없음(G2, G6).
3. **운전조건·온도 분리 설계**: 비교 기준(M28: 동일 컨버터 내 상대 비교 → NPC 의 C1 vs C2), 다중 조건 학습(D3), 온도 보정(P35). 근거: 17절 한계 1–2.
4. **물리 내장 학습**: 회로식에 매핑된 NN(M26), 디지털 트윈(D19, D20) 을 DC-link/NPC 로 확장(G10).
5. **quasi-online 과도 이용의 산업 적용**: 주차·정지 방전(P34, P35, P38)은 구현 난이도가 낮아 실용 가치가 높다(프로젝트와는 보완 관계).
6. **필름 커패시터용 C 중심 지표**: 산업용 NPC 가 필름이면 ESR 기반 fsw 리플보다 저주파(3f1) C 지표가 유효(추론; E5, E6, P36).

---

## 20. 새로운 연구주제 후보와 본 프로젝트 연결

### 20.1 연구 설계 사슬

`3L-NPC 내부 전류/전압(iSa2, iC1/iC2, iNP, vC1/vC2, vNP; 스위칭 상태×상전류로 재구성)` → `신호처리(정수 주기 FFT 또는 Goertzel/SDFT 로 2f1·3f1·4f1 및 m·fsw±n·f1 빈 추출)` → `노화 민감 feature(C1/C2·ESR 변화에 따른 진폭·위상 변화, C1 vs C2 상대 비교 feature)` → `CNN/ML(다중 운전조건 증강, 물리 특징 병렬 입력)` → `C1/C2 개별 노화 등급 또는 C·ESR 회귀`.

### 20.2 차별화 가능 지점 (Gap 대응)

| 후보 주제 | 대응 Gap | 차별점 | 논문화 가능성(해석) |
|---|---|---|---|
| T1. 무주입 NP 경로 고조파(3f1 vNP/iNP, 2f1·4f1 출력 측대파)로 C1/C2 개별 진단 | G3, G4, G5 | M1·M2 는 주입형, M3 는 개별 진단 미확인 | 높음(단, M3 본문 대비 필요) |
| T2. 스위치 전류(iSa2/iSa1) 스펙트럼의 노화 민감도 규명 + 상전류 대비 우위/열위 정량화 | G2 | 문헌 부재; "왜 스위치 전류인가" 를 물리로 정당화해야 함 | 중간(민감도가 작으면 부정적 결과) |
| T3. 재구성 전류 고조파 벡터 → CNN, 부하·변조·온도 증강 데이터로 강건성 검증 | G1, G6, G7 | D2(단상 DNN)·D3(vdc PSD GPR)·M25(시뮬 DL) 대비 3L-NPC + 전류 고조파 + 조건 강건성 | 높음 |
| T4. C1 vs C2 상대 스펙트럼 feature 로 온도·부하 공통 성분 제거 (M28 의 NPC 판) | G7, G5 | 비교 기준 개념을 NPC 에 최초 적용 | 높음 |
| T5. 물리 유도 feature(|Z(f)| 모델) + CNN 하이브리드 | G10 | DC-link PINN/하이브리드 부재 | 중간~높음 |
| T6. 필름 DC-link NPC 에서 저주파 C 지표 | G9 | 필름 특화 | 중간(커패시터 종류 확인 필요) |

### 20.3 구현 계획 (MATLAB 선검증 → Python/CNN 확장)

| 단계 | 내용 | 산출 |
|---|---|---|
| A. MATLAB 민감도 실험 | C1, C2 ∈ {100, 90, 80%}, ESR ∈ {×1, ×1.5, ×2} 격자(개별·동시), 부하 {25, 50, 100%}, 변조지수 {0.6, 0.8, 0.95}, 역률 {1, 0.8} 스윕. 각 신호(iSa2, iSa1, ia, iC1, iC2, iNP, vC1, vC2, vNP)의 2f1·3f1·4f1·6f1 및 fsw±f1, fsw±2f1, 2fsw±f1 진폭·위상 계산(정수 주기, Hann 비교). | 민감도 표: ∂(고조파)/∂C, ∂/∂ESR 대 ∂/∂부하 비율 → "노화 민감·조건 강건" feature 순위 |
| B. 물리 검증 | 추론 11.3 검증: vNP 3f1 진폭 ∝ 1/C 관계, ia/iSa2 의 2f1·4f1 이 vNP 리플에서 유래하는지(개루프 vs 폐루프 비교) | 수식 대 시뮬 대조표(관련연구 절의 "물리 근거") |
| C. 온도 모사 | ESR(T) 곡선을 데이터시트로 넣어 온도 변화가 fsw 성분에 주는 영향을 노화 효과와 대조 | 혼동 행렬 사전 예측 |
| D. Python 데이터셋 | A–C 격자를 npy 로 저장(신호별 고조파 벡터 + 원파형 조각), 라벨 = (C1, C2, ESR1, ESR2) 회귀 및 등급 | 조건 증강 데이터 |
| E. CNN/ML | (i) 고조파 벡터 1D-CNN/MLP, (ii) 원파형 1D-CNN, (iii) C1 vs C2 상대 feature; 학습 조건 외 부하·변조로 테스트(D3 방식) | 강건성 곡선 |
| F. 실험 | 소형 3L-NPC 에 커패시터 교체(C −10/−20%) 및 직렬 저항(ESR ×2) 모사 → 상전류·게이트 신호 동기 샘플링으로 iSa2 재구성 | G8 대응(시뮬→실험) |

필요 데이터·실험: 커패시터 데이터시트(종류·C·ESR(f,T)), 실제 인버터 정격(fsw, f1, 변조 방식), 게이트 신호 동기 샘플링 가능한 계측. 구현 난이도: A–E 는 현재 코드 기반으로 가능(추론), F 는 장비 필요.

### 20.4 위험 요소 (해석)
- 스위치 전류 스펙트럼의 노화 민감도가 부하·변조 민감도보다 작으면 T2 는 부정적 결과가 된다 → A 단계에서 조기 판정.
- 시뮬 노화 모사(C·ESR 상수 변경)는 실제 노화의 주파수·온도 의존성을 담지 않는다(capacitor-aging-expert 주의사항) → C 단계와 F 단계로 보완.
- M3 의 본문이 이미 "NP 경로 자연 성분 + 시간-주파수 추정" 을 다뤘다면 T1 의 신규성은 "개별 진단 + 데이터 기반 + 조건 강건성" 으로 좁혀야 한다.

### 20.5 관련연구 절 작성용 핵심 인용(재확인 후 사용)
R1, R2, R3(리뷰) / P20, P26(경량 스펙트럼·재구성) / M1, M2, M3, M4, M5(3레벨) / D2, D3, M25(데이터 기반) / P35, P39(최근 흐름) / M29(NPC 커패시터 전류 해석, 2013).

---

## 부록 A. 14개 질문에 대한 답 (근거: 3–18절, 초록 수준)

**A1. 가장 많이 사용되는 방법은?** DC-link 전압(·전류) 리플에서 ESR/C 를 추정하는 **리플 기반 파라미터 추정**(fsw 성분 → ESR, 저주파 성분 → C)과 **RLS 계열 추정기**이며, 2020 년 이후에는 기존 센서만 쓰는 **과도/방전 프로파일(quasi-online)** 과 **커패시터 전류 재구성** 이 급증했다 (P 계열 44편 중 리플/RLS 약 20, 과도/방전 약 10). MMC 는 SM 전압+스위칭 상태 기반이 표준이다.

**A2. 가장 중요한 HI 는?** 전해 커패시터는 **ESR**(초기 민감)과 **C**, 필름은 **C** 가 사실상 유일 지표다(E5, E6, P36). 최근 저널은 C 추정 논문이 ESR 보다 많다(온도 의존성이 작고 방전 프로파일·NP 경로로 얻기 쉬움: 해석). DF(P26)와 온도(P20, D15)가 보조 지표로 등장했다.

**A3. 가장 많이 쓰는 신호는?** **DC-link(커패시터) 전압** 이 압도적이고, 다음이 상전류·스위칭 상태로 **재구성한 커패시터 전류**, 그다음이 직접 측정 커패시터 전류다. 3레벨은 NP 전압/전류, MMC 는 SM 전압·암 전류·스위칭 신호.

**A4. 최근 5년 새 접근법은?** (i) 주차·정지·비행 후 방전 프로파일 + 온도 보상(P34, P35, P38), (ii) MPPT 전이·고유 2f·상호변조·링잉 같은 **자연 여기**(P39, M10, M3, P22), (iii) 3L-NPC 변조기 주입으로 C1/C2 개별 추정(M1, M2, M4), (iv) Goertzel/SDFT/Wavelet 경량 시간-주파수 추출(P20, P30, M3), (v) 리플 PSD/FFT 성분 → GPR/DNN(D2, D3), (vi) MMC 스위칭 상태 DL·회로 매핑 NN(M25, M26), (vii) 비교 기준으로 온도 분리(M28).

**A5. Online 진단 수준은?** 저널 논문 대부분이 "정상 운전 중·추가 센서 없음" 을 주장하나, 초록에서 실험 검증이 확인된 것은 절반 이하이고 임베디드 구현을 명시한 것은 소수(P11, P14, P29, M13)다. 산업 채택은 여전히 드물다(R2). 실용 수준이 가장 높은 것은 방전 프로파일형(quasi-online)이다(해석).

**A6. 추가 센서 없이 가능한 방법은?** DC 전압만(P29, P33–P35, P38, D3, D5), DC 전압+상전류(P14, P26, P39, M4, M5), 전원 전압+모델(P32, P37), 변조기 내부 주입(M1, M2, M4), 스위칭 신호만(M20, M22, M25), 자연 여기(P39, M10, M3, P22). 12.3 표.

**A7. Signal processing 발전은?** 아날로그 필터·FFT → 디지털 필터+RLS → Goertzel 단일 빈 → Wavelet/RT-SDWPT → 비정수 재귀 SDFT+RLS 관측기 → PSD/스펙트럼 특징의 ML 입력(10절). 방향은 "전체 스펙트럼 대신 물리적으로 의미 있는 소수 성분을 실시간으로 추적" 하는 쪽이다.

**A8. Harmonic 기반 연구 수준은?** fsw 성분(ESR), 단상 2f(C), 정류 6f, 주입 상호고조파, MMC/STATCOM 고유 2f, 3L 고유 고조파 모델(M5), NPC 고유 상호변조(M3)까지 확인됐다. **스위치 전류 스펙트럼, 자연 NP 전류 스펙트럼, 출력 기본파 짝수 고조파를 노화 feature 로 쓴 저널 논문은 없다.** 열화↔고조파 물리는 |Z(f)| 관계로 설명되며, NPC 의 3f1 NP 리플과 출력 짝수 고조파의 연결은 문헌에서 직접 확인하지 못했다(11.3 추론).

**A9. ML/DL 실제 활용도는?** 저널 기준 22편 내외로 전체의 약 1/5. 대부분 vdc 리플 특징 → 회귀/분류이며, 다중 조건 검증(D3)·실험 데이터 확인(D2, D3, D13)·물리 결합(M26)이 있는 논문은 소수다. NPC/T-type 대상은 없다.

**A10. CNN 입력은?** ALT 시계열→이미지(D13), ESR/C 궤적(D14), MMC 스위칭 상태 시퀀스(M25, 시뮬); 저널 미확인이나 CWT 이미지(capCNN, MMC). 인버터 전류 스펙트럼/스펙트로그램 입력은 없다.

**A11. Topology 별 차이는?** 15절 표. 2L 은 리플·과도, NPC/T-type 은 NP 경로(주입형 우세), FC 는 관측기, CHB 는 셀 전력 균형·2f, MMC 는 SM 삽입 패턴·기준 SM 비교.

**A12. 가장 중요한 한계는?** 온도·부하·변조 조건과 노화 효과의 분리(17절), 커패시터 전류 재구성 정확도, 필름 커패시터의 작은 신호, 실험·장기 데이터 부족, 산업 채택.

**A13. Research Gap 은?** 18절 G1–G12. 프로젝트와 직접 맞닿는 것은 G1(NPC×ML 부재), G2(스위치 전류 스펙트럼 부재), G3/G5(무주입·개별 진단), G6(전류 고조파→CNN 부재), G7(조건 강건성).

**A14. 향후 연구 가치가 높은 방법은?** 19절: 무주입 토폴로지 고유 경로 + 재구성 전류의 경량 스펙트럼 특징 + 조건·온도 분리(비교 기준) + 물리 내장 데이터 기반. 프로젝트 후보 T1, T3, T4 가 이에 해당한다.

---

## 부록 B. 학회·프리프린트·특허 (본 목록 제외, 계보 추적용)

- Lee et al., "Condition Monitoring of DC Link Electrolytic Capacitors in Adjustable Speed Drives," IEEE IAS 2007 (Xplore 4347792) — P3 의 학회판.
- Abo-Khalil & Lee, "DC-Capacitance Estimation of DC-Link Capacitors using AC Voltage Injection…" (Xplore 4025512) — P2 의 학회판.
- Soliman et al., "Capacitance Estimation Algorithm based on DC-Link Voltage Harmonics Using ANN in Three-Phase Motor Drive Systems" (~2017, 학회, 확인 필요); "Condition monitoring for DC-link capacitors based on ANN algorithm" (Xplore 7266382); IPEMC-ECCE Asia 2016 (10.1109/IPEMC.2016.7512885) — DC-link 전압 고조파를 ANN 입력으로 쓴 초기 계보.
- "Capacitance and ESR Estimation of DC-link Capacitors in AC Machine Drives Based on Hybrid CNN-Attention Model," 2024 학회 (Xplore 10567930) — CNN 계열.
- "Real-Time Estimation of ESR and Capacitance in the DC-Link Capacitors of AC Machine Drives," 2022 학회 (Xplore 9983087).
- "DC-link Capacitance Estimation based on Discharge Profile of Inverter for EV Application," 2023 학회 (Xplore 10213625) — P34 의 전신.
- MMC: ECCE 2014 (Xplore 6953683, Kalman/리플), IET PEMD 2016 (10.1049/cp.2016.0369), Xplore 8754625(정렬 내 추정), IFEEC 2019 (Xplore 9015031, 적응 관측기), ECCE 2021(고주파 과도 Wavelet ESR), ICPET 2022 (Xplore 9918452, Cotes+Kalman), Xplore 10142579(디지털 트윈), 9699854/8974877(MPPF 필름 SM).
- capCNN 데이터셋(IEEE DataPort/Aalborg): MMC SM 전압·암 전류 CWT 이미지 → CNN → C·ESR (저널 논문 여부 확인 필요).
- arXiv 2404.13399 (MMC 데이터 기반 C+ESR), 2609.00218 (불확실성 인식 파라미터 추정), 2608.30915 (미분 가능 물리 시뮬레이션) — 프리프린트.
- 특허: US 6,381,158 (3레벨 인버터 NP 조정기에 신호 주입해 DC-link C 감시 — NP 경로 아이디어의 최초 형태), US 11,428,750 (전류 센서로 커패시터·IGBT 열화 동시 감시), US 11,714,114 / 12,216,147 (EMI 기반 비침습 진단).
- 저널이나 CM 아님: Orfanoudakis et al., IET PEL 2013 (M29, NPC/CHB DC-link 커패시터 전류 해석) — 프로젝트의 커패시터 전류 스펙트럼 이론 근거로 정독 권장.

---

## 부록 C. 검증 대기 목록과 절차

C.1 **환경 조치**: 세션 클라우드 환경 설정(제목 표시줄의 환경 메뉴 → Edit → Network access)에서 접근 수준을 넓히거나 ieeexplore.ieee.org, sciencedirect.com, api.crossref.org, api.semanticscholar.org, api.openalex.org, mdpi.com, link.springer.com, onlinelibrary.wiley.com, doi.org, arxiv.org 를 허용하면 다음 조사에서 본문·서지 검증이 가능하다. 또는 로컬 PC 에서 아래를 실행한다.

C.2 **서지 채우기(로컬)**:
```
pwsh -File harness\tools\Search-Papers.ps1 -Query "Online Estimation of DC-link Capacitor Parameters of Three-Level NPC Converters Using Inherent Signals Analysis" -Source all
pwsh -File harness\tools\Search-Papers.ps1 -Citations 10.1016/j.compeleceng.2024.109577
pwsh -File harness\tools\Search-Papers.ps1 -References 10.1109/TPEL.2020.3023469
```
우선 확인 대상(DOI/권/쪽 미확인): R4, P3, P4, P7, P10, P12, P17, P18, P21, P22, P23, P25, P30, P31, P32, P33, P35, P36, P37, P39, M1, M3(저자), M4, M5(OK), M6–M28 중 IEEE 항목, D1, D3, D4, D5, D6, D12, D13, E1–E10.

C.3 **정독 우선순위(paper-analyzer 17항목)**: 1) M3, 2) M1, 3) M2, 4) P26, 5) M5, 6) D3, 7) D2, 8) P20, 9) M28, 10) R3. PDF 를 `papers/pdf/` 에 넣고 `.\harness.ps1 "papers/pdf/<파일> 논문 분석해줘"` 로 실행.

C.4 **미실행 검색(예산 소진)**: 6f 정류 리플 C 추정; 상전류 측대파 vs DC-link C; 전류 스펙트럼→CNN; UPS; 계통연계 고조파 주입; Flying-capacitor 2차; 2020 년대 Kalman 계열; Lahyani/Harada 기반 ESR 논문; Buiatti 2009 서지.

---

## 부록 D. 출처
검색 결과에 나타난 URL(출판사·색인·리포지터리)로, 본문에서 열지 못했다: ieeexplore.ieee.org (문서번호는 각 표 참조), sciencedirect.com (PII 참조), link.springer.com, onlinelibrary.wiley.com / ietresearch.onlinelibrary.wiley.com, digital-library.theiet.org, mdpi.com, jstage.jst.go.jp, koreascience.or.kr, semanticscholar.org, ui.adsabs.harvard.edu, vbn.aau.dk, infoscience.epfl.ch, pure.seoultech.ac.kr, dr.ntu.edu.sg, researchgate.net, techrxiv.org, ssrn.com, arxiv.org, papastergiou.web.cern.ch, gei-journal.com, ieee-dataport.org, patents(uspto). 개별 URL 목록은 `papers/notes/2026-09-29-survey-sources.md` 참조.
