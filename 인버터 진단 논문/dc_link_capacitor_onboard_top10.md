# Inverter DC-Link Capacitor On-board / Online Condition Monitoring — Top 10 정밀 비교

- 작성일: 2026-10-14
- 핵심 질문: 실제 인버터에 탑재하여, 기존 센서(또는 최소 추가 센서)로, 정상 운전을 유지하면서 DC-link 커패시터의 노화 상태(C, ESR, SoH)를 진단할 수 있는 기술은 무엇인가?
- 수행: Harness Skill `literature-researcher → bibliographic-verifier → capacitor-aging-expert → paper-analyzer → paper-comparator` (+ `npc-inverter-expert`). 탐색은 4개 응용 영역(2L·AFE·UPS·ESS / NPC·T-type·ANPC / PV·계통·풍력 / 모터·산업·EV·철도·항공)으로 병렬 수행, 선정·채점 기준은 단일.
- 파일: `dc_link_capacitor_onboard_top10.md`(이 문서), `dc_link_capacitor_onboard_top10_comparison.csv`(UTF-8 BOM).

---

## 1. Executive Summary

- **근거 수준: 전 논문 `Abstract-level only`.** 이 클라우드 환경은 출판사·DOI·Crossref·arXiv 호스트를 DNS 단계에서 차단해 본문을 한 편도 열지 못했다. 서지는 검색 색인 스니펫·대학 리포지터리·OpenAlex 레코드에 보인 값만 기록했고, 보이지 않은 값은 `(확인 필요)`로 남겼다. 알고리즘·실험 조건은 초록에 있는 범위만 적었다(사용자 요청 20절 준수).
- 후보 저널 논문 58편(DC-link 한정)을 Q1(기존 센서)·Q2(온라인 유형)·Q3(추정 대상)으로 선별하고 100점 기준(A 25 / B 20 / C 15 / D 15 / E 10 / F 10 / G 5)으로 채점해 10편을 선정했다.
- **Tier S(3)**: Ghadrdan 2022 TPEL(출력 전류+스위칭 상태로 커패시터 전류 재구성 → DF, True Online), Ribeiro 2025 IEEE/CAA JAS(3L-NPC 고유 상호변조 성분 → C+ESR, 무주입, 기존 센서), Hasegawa & Hirose 2024 TIA(전류 센서 없이 C+ESR, 정류기 전단 드라이브).
- **Tier A(4)**: Örüklü & Ağalar 2025 TIE(vdc 리플 PSD → GPR, 다중 조건, 불확실성), Sundararajan 2020 TPEL(Goertzel, ESR+C+온도), Zhang 2023 TPEL(T-type 고유 고조파 모델 + 전류 재구성 + RLS), Min/Choi/Blaabjerg 2026 TIE(NPC 상·하단 충방전 프로파일, <1 %, 주입형).
- **Tier B(3)**: Zhao 2023 TPEL(전압 센서만, 대신호 과도 grey-box, 수상), Wechsler 2012 TIA(필름 DC-link True Online, 토크·속도 독립, 기반), Baumann 2024 TPEL(정지 시 방전 + 온도 보상 SoH, 현장 153대).
- 결론: ① 기존 센서만으로 정상 운전 중 **C 와 ESR 을 함께** 추정한 저널 논문은 Ribeiro 2025(NPC)와 Hasegawa & Hirose 2024(정류기 전단)뿐이다. ② 2-Level 일반 인버터에서는 "상전류+스위칭 상태 → 커패시터 전류 재구성"(Ghadrdan 2022, Lipnicki 2017, Zhang 2023)과 "DC-link 전압만"(Zhao 2023, Örüklü 2025) 두 흐름이 True Online 의 주류다. ③ 최근 5년은 C 추정이 ESR 추정보다 많다. ④ 다중 운전조건 검증을 초록에 명시한 논문은 소수(Örüklü, Wechsler, Baumann, Zhang)다.

---

## 2. Search Scope

| 항목 | 내용 |
|---|---|
| 대상 | DC-link / DC-bus / 분할(상·하단) DC-link / NPC 중성점 커패시터, 전해·필름 |
| 제외 | LCL 필터·플라잉·MMC 서브모듈 커패시터(방법 비교용 참고만), 학회 논문(별도 표기), 학위논문·특허, 단순 수명 예측 |
| 응용 | 2L 3상 VSI, AC/DC/AC(AFE+인버터), UPS, ESS, 3L-NPC/T-type/ANPC, PV·계통연계·풍력, 모터·산업 드라이브, EV/HEV·철도 견인, 항공·선박 |
| 기간 | 2022–2026 집중 + 기반 논문(2005–2021) |
| 키워드 | 사용자 4절 목록 × 응용 키워드. 출처: IEEE Xplore, ScienceDirect, Springer, Wiley/IET, MDPI, J-STAGE, KoreaScience, OpenAlex, Semantic Scholar, 대학 리포지터리(AAU VBN, NTU, Kyutech, SeoulTech, Newcastle, NTNU, HIT, CTU) |
| 검색량 | 웹 검색 160회(4×40) + 본 세션 3회; 본문·DOI 페이지 접근 0회(차단) |

---

## 3. Definition of On-board / Online Diagnosis (채점에 쓴 정의)

| 구분 | 정의 | B 점수 |
|---|---|---|
| **True Online** | 정상 운전·부하 공급 중 연속 진단, 주입·시퀀스 없음 | 20 |
| **Quasi-Online** | 정상 운전 중이지만 주입·오프셋·간헐 시퀀스·스위칭 로직 일시 변경이 필요 | 15 |
| **특정 운전조건에서 Online** | 자연 발생 이벤트(부하 과도, MPPT 전이, 회생 모드)가 있어야 추정 | 12 |
| **정지 후 측정** | 셧다운·주차·모터 정지·사전충전 구간 이용 | 5 |
| **Offline** | 분리·정지 계측 | 2 |

Q1 기존 센서: DC-link 전압, 상전류, DC 전류(있는 경우), 스위칭 상태/게이트, 제어기 내부 변수 = 기존. 커패시터 전류 센서, 자기 센서, 비접촉 HF 센서, 평가 회로, 전용 모니터링 보드 = 추가.
Q3: Parameter(C / ESR / C+ESR / |Z| / DF) · Health(SoH, 등급) · Prognostics(RUL).

---

## 4. Candidate Papers (1차 Screening, 저널 58편)

약어: Quasi=Quasi-Online, 특정 조건=특정 운전조건에서 Online, 정지 후=정지 후 측정. 전 항목 Abstract-level only.

| ID | Title | Authors/Year | Journal | DOI/식별 | Application | Q1 기존센서 | Q2 Online | Q3 Target | Method/Result | 비고 |
|---|---|---|---|---|---|---|---|---|---|---|
| C01 | Online capacitance estimation of DC-link electrolytic capacitors for three-phase AC/DC/AC PWM converters using RLS | Lee, Lee, Seok, Choi 2005 | IEE Proc. EPA 152(6):1503–1508 | 10.1049/ip-epa:20050027(이전 스니펫) | AC/DC/AC | Yes(SW만) | Quasi(무부하 주입) | C | 입력 LF 전류 주입+RLS, 오차<0.26 % | 기반 |
| C02 | DC-Link Capacitance Estimation in AC/DC/AC PWM Converters Using Voltage Injection | Abo-Khalil & Lee 2008 | IEEE TIA 44(5):1631–1637 | 10.1109/TIA.2008.2002181(이전 스니펫) | AC/DC/AC | Yes(SW만) | Quasi(전압 주입) | C | 주입+SVR, 오차<0.15 % | 기반 |
| C03 | Condition Monitoring of DC-Link Electrolytic Capacitors in Adjustable-Speed Drives | Lee et al. 2008 | IEEE TIA 44(5):1606–1613 | 10.1109/TIA.2008.2002220 | ASD | Yes | 정지 후(모터 정지) | C+ESR(+온도) | 정지 중 인버터로 고정자 여기; 250 W PMSM 가속 열화 커패시터 | 기반 |
| C04 | Life-Cycle Monitoring and Voltage-Managing Unit for DC-Link Electrolytic Capacitors in PWM Converters | Vogelsberger, Wiesinger, Ertl 2011 | IEEE TPEL 26(2):493–503 | 10.1109/TPEL.2010.2059713 | PWM 컨버터 | No(전용 유닛) | True Online | ESR | 커패시터 장착 모니터링 보드, 온도, 통신 | 추가 HW |
| C05 | Condition Monitoring of DC-Link Capacitors in Aerospace Drives | Wechsler et al. 2012 | IEEE TIA 48(6):1866–1874 | 10.1109/TIA.2012.2222333 | 항공 드라이브 | Yes | True Online | C(+ESR?) | 기존 보호/제어 센서, 무주입, 토크·속도 독립 | Top10 #9 |
| C06 | Fault Diagnosis of DC-Link Capacitors in Three-Phase AC/DC PWM Converters by Online Estimation of ESR | Pu, Nguyen, Lee, Lee, Kim 2013 | IEEE TIE 60(9):4118–4127 | 10.1109/TIE.2012.2218561(이전 스니펫) | AC/DC | Partial(온도 보정) | Quasi(전류 주입) | ESR | 주입+필터+RLS+온도 보정 | 기반 |
| C07 | Deterioration Monitoring of DC-Link Capacitors in AC Machine Drives by Current Injection | Nguyen & Lee 2015 | IEEE TPEL 30(3):1126–1130 | 10.1109/TPEL.2014.2339374 | IM 드라이브 | Partial(DC 전류 n/s) | 특정 조건(회생)+주입 | C | 고정자 AC 주입→리플→RLS, <1 % | 기반 |
| C08 | Estimation of ESR in the DC-Link Capacitors of AC Motor Drive Systems with a Front-End Diode Rectifier | Nguyen, Le, Lee 2015 | J. Power Electron. 15:411–418 | (확인 필요) | IM 드라이브 | Yes(재구성) | 특정 조건(회생)+주입 | ESR | 고정자 전류+스위칭 상태로 ESR 전류 재구성, ≈1.2 % | #20 |
| C09 | Online Monitoring Technique for Aluminum Electrolytic Capacitor in Solar PV-Based DC System | Ahmad, Agarwal, Anand 2016 | IEEE TIE 63(11):7059–7066 | 10.1109/TIE.2016.2582470 | PV boost(입력 커패시터) | Yes(PV V/I) | True Online | ESR | 스위칭 리플 계수, 온도 효과 포함; boost 프로토타입 | DC-link 경계 |
| C10 | Capacitor impedance estimation utilizing dc-link voltage oscillations in single phase inverter | Arya, Ahmad, Agarwal, Anand 2017 | IET Power Electron. 10(9):1046–1053 | 10.1049/iet-pel.2016.0603 | 단상 PV | Yes(PV V/I, 인덕터 I) | True Online | |Z(2f)| | SOGI 2f 추출, 같은 DSP | PV 대표 |
| C11 | DC link condition monitoring method for two-level AC/DC/AC converters | Lipnicki & Lewandowski 2017 | Power Electronics and Drives 2(37)(1):43–56 | 10.5277/PED170107 | 2L AC/DC/AC | Yes(재구성) | True Online | ESR | 상전류+스위칭 함수 DC-link 전류 재구성 | #13 |
| C12 | Online Condition Monitoring for Both IGBT Module and DC-Link Capacitor … Short-Circuit Current | Sun et al. 2017 | IEEE TIE 64(5):3662–3671 | (확인 필요) | 컨버터 | n/s | 특수 모드(추정) | n/s | 단락 전류 기반 | 세부 n/s |
| C13 | Quasi-Online Technique for Health Monitoring of Capacitor in Single-Phase Solar Inverter | Agarwal, Ahmad, Anand 2018 | IEEE TPEL 33(6):5283–5291(이전 스니펫) | 10.1109/TPEL.2017.2736162(이전 스니펫) | 단상 PV | n/s | Quasi(야간 주입) | C+ESR | 홀수 고조파 주입+LMS | PV |
| C14 | Noninvasive Technique for DC-Link Capacitance Estimation in Single-Phase Inverters | Ahmad, Kumar, Arya, Anand 2018 | IEEE TPEL 33(5):3693–3696 | 10.1109/TPEL.2017.2762341 | 단상 계통 | Yes | True Online | C | 2f v/i 비, 최대 2.56 % | #12 |
| C15 | Online Condition Monitoring System for DC-Link Capacitor in Industrial Power Converters | Sundararajan et al. 2018 | IEEE TIA 54(5):4775–4785 | 10.1109/TIA.2018.2845889 | 산업용/상용 드라이브 | Partial | True Online | ESR | fsw 성분 비; 상용 AC 드라이브 구현 | #16 |
| C16 | ESR and capacitance monitoring of a dc-link capacitor used in a three-phase PWM inverter with a front-end diode rectifier | Hasegawa, Nishizawa, Omura 2018 | Microelectron. Reliab. 88–90:433–437 | 10.1016/j.microrel.2018.07.023 | 정류기 전단 드라이브 | Partial(리플 전류 측정) | True Online | C+ESR | 실제 리플 전류·전압 | — |
| C17 | Real-Time Reliability Monitoring of DC-Link Capacitors in Back-to-Back Converters | Abo-Khalil, Alyami, Alhejji, Awan 2019 | Energies 12(12):2369 | 10.3390/en12122369 | B2B | n/s(전류 'sensed or derived') | n/s | C | PSO-SVR | — |
| C18 | A Condition-Monitoring Method of DC-Link Capacitors Used in a High-Power Three-Phase PWM Inverter with an Evaluation Circuit | Hasegawa, Nishizawa, Omura 2019 | IEEJ J. Ind. Appl. 8(3):480–487 | (확인 필요) | 고출력 인버터 | No(평가회로) | (확인 필요) | C+ESR | FFT(리플 전류·전압) | 추가 회로 |
| C19 | Condition Monitoring of DC-Link Electrolytic Capacitors in PWM Power Converters Using OBL Method | Abo-Khalil 그룹 2020 | Sustainability 12(9):3719 | (확인 필요) | B2B | n/s | n/s | C | OBL-PSO SVR | — |
| C20 | Condition Monitoring of DC-Link Capacitors Using Goertzel Algorithm for Failure Precursor Parameter and Temperature Estimation | Sundararajan et al. 2020 | IEEE TPEL 35(6):6386–6396 | 10.1109/TPEL.2019.2951859 | 정류기 전단 인버터 | Partial | True Online | ESR+C+온도 | Goertzel | Top10 #5 |
| C21 | Online Monitoring of Aluminum Electrolytic Capacitors in Photovoltaic Systems by Magnetoresistive Sensors | Miao, Lam, Pong 2020 | IEEE Sensors J. 20(2):767–777 | 10.1109/JSEN.2019.2945943 | PV | No(TMR 센서) | True Online | C+ESR | 자기장 전류 센싱 | 추가 센서 |
| C22 | Online ESR Monitoring of DC-Link Capacitor in VSC Using Damping Characteristic of Switching Ringings | Xiang et al. 2021 | IEEE TPEL 36(7):7429–7441 | 10.1109/TPEL.2020.3042218 | 2L VSC | No(비접촉 HF 센서) | True Online | ESR | 링잉 감쇠, half-power bandwidth | 추가 센서 |
| C23 | Online Estimation Method of DC-Link Capacitors for Reduced DC-Link Capacitance IPMSM Drives | (HIT) 2021 | IEEE TPEL 36(11) (쪽 확인 필요) | (확인 필요) | 감소용량 IPMSM | Yes | True Online | C | n/s, 오차 <1 % | 저자 미확인 |
| C24 | DC-Link Capacitor Diagnosis in a Single-Phase Grid-Connected PV System | Plazas-Rosas et al. 2021 | Energies 14(20):6754 | 10.3390/en14206754 | 단상 PV | n/s | Quasi(EIS 주입 추정) | C+ESR | 임피던스 곡선+피팅, <1 %, 일사 변화 강건 | — |
| C25 | Measurement-Based Identification of DC-Link Capacitance of Single-Phase PE Devices for Grey-Box Modeling | Kaufhold, Meyer, Schegner 2022 | IEEE TPEL 37(4):4545–4552 | 10.1109/TPEL.2021.3127241 | 단상 PV(상용) | n/s | n/s | C | 전압 리플 분석(모델링 목적, CM 아님) | 참고 |
| C26 | Online Condition Monitoring of DC-Link Capacitor for AC/DC/AC PWM Converter | Li, Chen, Cong, Dai, Qiu, Liu 2022 | IEEE TPEL 37(1):865–878 | 10.1109/TPEL.2021.3092429 | AFE+인버터 | Yes | Quasi(주입) | C | 센서 없이 커패시터 전류 계산+슬라이딩 DFT | #11 |
| C27 | Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor | Ghadrdan et al. 2022 | IEEE TPEL 37(8):9733–9744 | 10.1109/TPEL.2022.3153842 | B2B | Yes(재구성) | True Online | DF | 출력 전류 재구성 fsw 성분 | Top10 #1 |
| C28 | On-Line Condition Monitoring System for DC-Link Capacitor of Back-to-Back Converters Using Large-Signal Transients | Ghadrdan et al. 2022 | IEEE JESTPE (권/쪽 확인 필요) | 10.1109/JESTPE.2022.3163012 | B2B | Yes | Quasi(스위칭 로직 변경) | C | 대신호 과도, <1 % | #17 |
| C29 | Online condition monitoring for DC-link capacitors of motor drives under noise interference | Zhu, Zhao, Song, Zhou, Sun 2022 | J. Power Electron. 22(7):1142–1153 | 10.1007/s43236-022-00426-w | 모터 드라이브 | Yes | 특정 조건(회생) | C | RLS+이상치 제거 | — |
| C30 | An Online DC-Link Capacitance Estimation Method for Motor Drive Systems Based on an Intermittent Reverse-Charging Control Strategy | Meng & Zhang 2022/23 | IEEE TPEL (권/쪽 확인 필요) | (확인 필요) | 모터 드라이브 | Yes | Quasi(간헐 역충전) | C | 전압 상승+한 상전류 | #15 |
| C31 | A Capacitance Estimation Method for DC-Link Capacitors Based on Pre-Charging Model and Noise Evaluation | Wu et al. 2022/23 | IEEE TIE (권/쪽 확인 필요) | 10.1109/TIE.2022.3217587 | (철도 추정) | n/s | Quasi(사전충전) | C | 사전충전 모델+잡음 평가 | 서지 충돌 주의 |
| C32 | DC-Link Electrolytic Capacitors Monitoring Techniques Based on Advanced Learning Intelligence Techniques for Three-Phase Inverters | Dang, Park, Kwak, Choi 2022 | Machines 10(12):1174 | (확인 필요) | 3상 인버터 | Yes(소스 전류) | n/s | C/ESR(n/s) | DL 비교 | 세부 n/s |
| C33 | Dissipation Factor as a Degradation Indicator for Electrolytic Capacitors | Ghadrdan et al. 2023 | IEEE JESTPE 11(1):1035–1044 | 10.1109/JESTPE.2022.3183837 | 소자 수준 | — | — | DF | 지표 연구 | 참고 |
| C34 | A Transient-Modeling-Based Grey-Box Method for Online Monitoring of DC-Link Capacitors | Zhao et al. 2023 | IEEE TPEL 38(11):14547–14562 | 10.1109/TPEL.2023.3308115 | AC/DC·DC/DC | Yes(vdc) | 특정 조건(과도) | C+α | TECM, <1 % | Top10 #8 |
| C35 | Wavelet-based estimation method for online condition monitoring of dc-link capacitors of distributed energy resources | Ribeiro et al. 2023 | IJEPES 151 (art 확인 필요) | (확인 필요) | boost+3상 VSC(DER) | n/s | Quasi(상호고조파 주입) | C+ESR | RT-SDWPT, 마이크로그리드 실험 | — |
| C36 | A Comprehensive Method for Online Switch Fault Diagnosis and Capacitor Condition Monitoring of Three-Level T-Type Inverters | Zhang, He, Wang, Chen 2023 | IEEE TPEL 38(8):10183–10195(재확인 필요) | 10.1109/TPEL.2023.3262758(재확인 필요) | 3L T-type | Partial | True/Quasi(고유 또는 주입) | C | 고유 고조파 모델+전류 재구성+RLS | Top10 #6 |
| C37 | Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor in a PWM Inverter With a Six-Pulse Diode Rectifier | Hasegawa, Kubo, Hirose 2023 | IEEJ J. Ind. Appl. 12(3) | (확인 필요) | 정류기 전단 드라이브 | Yes | True Online | C+ESR | 정류기 모델 전류 계산 | — |
| C38 | Noninvasive Online Capacitor Monitoring Method for Three-Level Converter Based on Active Neutral-Point Current Adjustment | Guan & Zhen (2023/24) | IEEE (저널명·권 확인 필요; Xplore 10149200) | (확인 필요) | 3L-NPC | Yes(재구성) | Quasi(NP 전류 능동 조정) | C | 스위칭 상태+상전류로 NP 전류 재구성, 2단 RLS, 시뮬+실험 | 저널 여부 미확인 |
| C39 | A High-Accuracy Capacitor Condition Monitoring Scheme at Low Sample Frequency Based on Improved Current Reconstruction Method | Dai, Zhao, Han, Chen 2024 | IEEE JESTPE 12(2):2281–2291 | 10.1109/JESTPE.2024.3370616 | AC/DC | Yes | 특정 조건(부하 변화) | C | 전류 적분 재구성 | #19 |
| C40 | Online condition monitoring for DC-link capacitors of three-level NPC converters using noninvasive signal injection | Ribeiro, Alves, de Sousa, Oliveira 2024 | Comput. Electr. Eng. 119:109577 | 10.1016/j.compeleceng.2024.109577 | 3L-NPC | Yes | Quasi(영상분 주입) | C+ESR | Wavelet, <2 % | #14 |
| C41 | An Improved Discharge Profile-Based DC-Link Capacitance Estimation for Traction Inverter in Electric Vehicle Applications | Wei et al. 2024 | IEEE TPEL 39(7):8696–8708(이전 스니펫; VBN in press) | 10.1109/TPEL.2024.3383153(이전 스니펫) | EV 견인 | Yes | 정지 후(주차 방전) | C | 방전 프로파일 | — |
| C42 | Discharge-Based Condition Monitoring for Electrolytic DC-Link Capacitors | Baumann et al. 2024 | IEEE TPEL (권/쪽 확인 필요) | 10.1109/TPEL.2024.3442077 | 200 kW 컨버터 | Yes | 정지 후 | C→SoH | 온도 보상, 현장 153대 | Top10 #10 |
| C43 | Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor Based on Analysis of a Six-Pulse Diode Rectifier Having AC and DC Inductors | Hasegawa & Hirose 2024 | IEEE TIA 60(6):9043–9051 | (확인 필요) | 정류기 전단 드라이브 | Yes | True Online | C+ESR | 모델 기반 전류 계산, 200 V 실험 | Top10 #3 |
| C44 | Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters | Örüklü & Ağalar 2025 | IEEE TIE 72(4):4227–4237 | 10.1109/TIE.2024.3454814 | B2B | Yes(vdc) | True Online | C | PSD→GPR, 다중 조건, <2 % | Top10 #4 |
| C45 | A Capacitance Estimation Method for DC-Link Capacitors in Rail Transit Based on Maximum Likelihood and Variable Convergence Factor | Wu et al. 2025 | IEEE TIE 72 (호/쪽 확인 필요) | 10.1109/TIE.2024.3525135 | 철도 견인 | n/s | n/s | C | ML+가변 수렴계수 | 세부 n/s |
| C46 | Online Estimation of DC-link Capacitor Parameters of Three-Level NPC Converters Using Inherent Signals Analysis | Ribeiro et al. 2025 | IEEE/CAA JAS 12(7):1434–1444 | 10.1109/JAS.2025.125159 | 3L-NPC | Yes | True Online | C+ESR | 고유 상호변조 + oSDFT-RLS | Top10 #2 |
| C47 | Condition monitoring of a DC-link capacitor in an inverter with a front-end diode rectifier under imbalanced three-phase supply voltage | Yamasoto & Hasegawa 2025 | Microelectron. Reliab. 173:115873 | (확인 필요) | 정류기 전단 드라이브 | Yes | True Online | C/ESR(n/s) | 불평형 전원 확장 | — |
| C48 | Discharge-Based DC-Bus Voltage Link Capacitor Monitoring with Repetitive RLS for Hybrid-Electric Aircraft | Oliszewski, Pawlak, Dybkowski 2025 | Energies 18(17):4743 | 10.3390/en18174743 | 항공 DC 버스 | n/s | 정지 후(방전) | C | RRLS, <5 % | — |
| C49 | DC-Link Capacitors Online Condition Monitoring Using Repetitive RLS in Hybrid-Electric Aircraft | Oliszewski et al. 2025 | IEEE Access 13 | 10.1109/ACCESS.2025.3591882 | 항공 | n/s | n/s | C | RRLS | 초록 미회수 |
| C50 | Online Monitoring Method for Capacitor Lifetime in Brushless DC Motor Drive Systems with DC-Link Series Switch | (확인 필요) 2025 | World Electric Vehicle J. 16(6):330 | 10.3390/wevj16060330 | BLDC(직렬 스위치) | Partial(토폴로지 요소) | True Online | C→수명 | 3상 전류로 커패시터 전류 재구성 | 토폴로지 특수 |
| C51 | A Simple and Cost-Effective Method for Condition Monitoring of Inverter DC-Link Film Capacitors Based on Capacitance Variation | (확인 필요) 2025 | IEEE OJ-IA(accepted, 확인 필요) | (확인 필요) | 인버터+모터(필름) | Yes | Quasi(제어 방전 시험) | C | 고정자 권선 방전 경로, 500→100 V 적분 | 저널 미확정 |
| C52 | An Online Estimation Method for DC-Link Capacitor in Doubly Salient Electromagnetic Motor Drive System | (확인 필요) 2025 | IEEE (저널명 확인 필요; Xplore 11178083) | (확인 필요) | DSEM 드라이브 | Yes | True Online | C | 정류 중 에너지 환류 전압 변동 | 저널 미확정 |
| C53 | Non-Intrusive Capacitor Monitoring in Photovoltaic Inverters Based on MPPT-Induced Voltage Transients | Muhammed Ramees & Ahmad 2025/26 | IEEE TPEL (Early Access) | (확인 필요) | PV | Yes | 특정 조건(MPPT 전이) | C | 출력 전류→커패시터 전류 추정 | #18 |
| C54 | A Highly Accurate Generative Learning-Based DC-Link Capacitance Estimation Approach for Electrified Railway Traction Systems | Zhao, Qie, Zhang, Iu, Fernando, Xiang 2025/26 | IET Power Electron. | 10.1049/pel2.70151 | 철도 견인 | n/s | n/s | C | VAE+LSTM, 실험 | — |
| C55 | An Online Condition Monitoring Method for DC-Link Capacitors of Three-Level NPC Inverters Based on Charge-Discharge Profile | Min, Choi, Blaabjerg 2026 | IEEE TIE (in press) | (확인 필요) | 3L-NPC | Yes | Quasi(오프셋 주입) | C | 충방전 프로파일, <1 % | Top10 #7 |
| C56 | Capacitance estimation algorithm based on DC-link voltage ripples using hybrid ML techniques in power electronics converters | (확인 필요) 2025 | Results in Engineering (PII S2590123025022881) | (확인 필요) | 일반 | n/s | n/s | C | 하이브리드 ANN-GB-LR, 최대 오차 ~1.1–1.3 % | — |
| C57 | Online Estimation of DC-Link Capacitance for PMSM Drive with Reduced DC-Link Capacitor | Zhou et al. 2021 | IEEE (저널/학회 확인 필요; Xplore 9589375) | (확인 필요) | 감소용량 PMSM | Yes | True Online | C | 계통 입력전력·재구성 입력전류→커패시터 순시전력 | 유형 미확정 |
| C58 | DC-Link Capacitor Parameter Identification of Inverters Based on Digital Twin Method | Liang et al. 2026 | Ship Engineering 48(3):101–109 (중국어) | 10.13788/j.cnki.cbgc.2026.03.11 | 3L-NPC | n/s | n/s | C+ESR | RK4 디지털 트윈+PSO, 시뮬만 | 저품질 근거 |

학회·프리프린트(보조): Chaiyakhot et al. ICEMS 2022 (RLS ESR·C, DSP ½ hp IM, Xplore 9983087); Meng & Zhang 선행 학회(Xplore 9595337); Lopez-Caiza et al. IPEC-Nagasaki 2026 (NPC branch 별 파라미터, 시뮬); Min & Choi 2025 학회판; UPS 비침습 ESR(Xplore 10082405, 유형 미확인); "Online Capacitance Estimation for the DC Link Capacitor of PWM Inverter"(Xplore 11184531, SVPWM·데드타임 고려, 유형 미확인); H5 PV zero-state(Xplore 7544180); 특허 US 6,381,158(3L NP 조정기 주입); arXiv 2609.00218.

---

## 5. Screening Criteria (100점)

| 기준 | 배점 | 적용 규칙 |
|---|---|---|
| A On-board Applicability | 25 | 기존 센서만+정상 운전 25 / 대부분 기존+최소 추가 20 / 추가 센서지만 탑재 가능 15 / 별도 측정회로 8 / offline 2 |
| B Online Capability | 20 | 3절 표 |
| C Diagnostic Target | 15 | C+ESR 15 / C 또는 ESR(또는 DF·α 등 정량 지표) 13 / SoH·등급 10 / 분류·RUL 7 |
| D Signal Practicality | 15 | 상전류+스위칭 상태(또는 출력 전류)로 커패시터 전류 재구성 15 / 모델 기반 재구성·센서 없는 계산 14 / DC-link 전압(및 기존 전류) 13 / 전류 센서 여부 불명 12 |
| E Experimental Validation | 10 | 실제 인버터+실제/가속 열화 10 / 실제 인버터+모사 노화(또는 노화 방식 n/s) 8 / HIL 5 / 시뮬 2 / 검증 n/s 5 |
| F Operating-Condition Robustness | 10 | 다중 조건 10 / 일부 조건 또는 조건 영향 분석 7 / 단일·n/s 3 |
| G Scientific Quality | 5 | 저널 등급·독창성·영향(수상 등) |

Tier 배정은 총점에 "가장 직접적인 On-board/Online DC-link 진단인가(S)", "설계에 바로 쓰는 방법론인가(A)", "특정 요소(물리 모델·신호처리·AI·prognostics)에 중요한가(B)" 를 더해 결정했다.

---

## 6. Final Top 10

| Rank | Title | First author | Year | Journal | DOI | Score | Evidence |
|---|---|---|---|---|---|---|---|
| 1 | Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor | M. Ghadrdan et al. | 2022 | IEEE Transactions on Power Electronics | 10.1109/TPEL.2022.3153842 | 93 | Abstract-level only |
| 2 | Online Estimation of DC-link Capacitor Parameters of Three-Level NPC Converters Using Inherent Signals Analysis | R. L. A. Ribeiro et al. | 2025 | IEEE/CAA Journal of Automatica Sinica | 10.1109/JAS.2025.125159 | 89 | Abstract-level only |
| 3 | Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor Based on Analysis of a Six-Pulse Diode Rectifier Having AC and DC Inductors | K. Hasegawa et al. | 2024 | IEEE Transactions on Industry Applications | (확인 필요) | 88 | Abstract-level only |
| 4 | Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters | K. Örüklü et al. | 2025 | IEEE Transactions on Industrial Electronics | 10.1109/TIE.2024.3454814 | 93 | Abstract-level only |
| 5 | Condition Monitoring of DC-Link Capacitors Using Goertzel Algorithm for Failure Precursor Parameter and Temperature Estimation | P. Sundararajan et al. | 2020 | IEEE Transactions on Power Electronics | 10.1109/TPEL.2019.2951859 | 87 | Abstract-level only |
| 6 | A Comprehensive Method for Online Switch Fault Diagnosis and Capacitor Condition Monitoring of Three-Level T-Type Inverters | W. Zhang et al. | 2023 | IEEE Transactions on Power Electronics | 10.1109/TPEL.2023.3262758 (이전 조사 스니펫; 재확인 필요) | 83 | Abstract-level only |
| 7 | An Online Condition Monitoring Method for DC-Link Capacitors of Three-Level NPC Inverters Based on Charge-Discharge Profile | K. J. Min et al. | 2026 | IEEE Transactions on Industrial Electronics — Accepted/In press (SeoulTech Pure). 이전에 기록한 vol. 73(8):12452–12463 은 이번 검증에서 확인되지 않음 | (확인 필요) — 10.1109/TIE.2026.3672764 는 어느 검색에서도 확인되지 않음 | 82 | Abstract-level only |
| 8 | A Transient-Modeling-Based Grey-Box Method for Online Monitoring of DC-Link Capacitors | Z. Zhao et al. | 2023 | IEEE Transactions on Power Electronics | 10.1109/TPEL.2023.3308115 | 83 | Abstract-level only |
| 9 | Condition Monitoring of DC-Link Capacitors in Aerospace Drives | K. Wechsler et al. | 2012 | IEEE Transactions on Industry Applications | 10.1109/TIA.2012.2222333 | 89 | Abstract-level only |
| 10 | Discharge-Based Condition Monitoring for Electrolytic DC-Link Capacitors | T. F. Baumann et al. | 2024 | IEEE Transactions on Power Electronics (vol/호/쪽 확인 필요; 이전 조사 스니펫 39:16622–16637) | 10.1109/TPEL.2024.3442077 | 81 | Abstract-level only |

### 6.1 종합 비교표 (이 표만으로 On-board 적용 가능성을 판단)

| Rank | Paper | Year | Topology | Application | Signal | Existing Sensor Only | Online Type | Target | Method | Extra Sensor | Experiment | Main Limitation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ghadrdan2022TPEL | 2022 | 2-Level back-to-back (AC/DC/AC) VSC | 계통연계·드라이브 공용 B2B 컨버터 | 컨버터 출력(AC) 상전류 + 스위칭 상태 → 재구성한 커패시터 전류의 스위칭 주파수 성분; DC-link 전압 리플 | Yes | True Online | Dissipation factor DF = tanδ = ω·C·ESR (C·ESR 결합 지표) + EoL 기준 제안 | 스위칭 주파수 성분(리플) 추출; 커패시터 전류 재구성 | None (초록 기준) | 실험(초록: experimental) — 세부 n/s | DF 로 C/ESR 분리 불가; fsw·ESL·필터 의존 |
| 2 | Ribeiro2025JAS | 2025 | 3-Level NPC VSI (계통연계) | 계통연계 3L-NPC | PWM 전략과 토폴로지의 상호작용이 만드는 고유 상호변조(intermodulation) 성분; 측정량은 off-the-shelf 3L-NPC 의 기존 센서(구체 n/s) | Yes | True Online | C + ESR (열화 추적) | 비정수 재귀 슬라이딩 DFT(rnSDFT)로 상호변조 성분 추적 | None | 실험(laboratory setup, 초록 기준) | 성분 정의·조건 강건성·C1/C2 분리 미확인 |
| 3 | Hasegawa2024TIA | 2024 | 6-pulse 다이오드 정류기(AC+DC 인덕터) + 3상 PWM 인버터 | 산업용 모터 드라이브(정류기 전단) | 3상 전원 전압, 선로/DC 인덕턴스(모델), 인버터 출력 전력, DC-link 전압 — 전류 센서 없음 | Yes | True Online | C + ESR | 정류 리플 성분(6·f_grid 계열) 해석; 모델 기반 전류 재구성 | None | 실험(200 V 실험실 시스템) | 다이오드 정류기 전단 구조 한정 |
| 4 | Oruklu2025TIE | 2025 | 2-Level 3상 AC/DC/AC | B2B 컨버터(일반) | DC-link 전압 리플의 PSD | Yes | True Online | C (health indicator) + 예측 불확실성 | PSD(저샘플링 강조) | None | 시뮬레이션 + 실험실 프로토타입 | C 만; 학습 범위 밖 일반화 미확인 |
| 5 | Sundararajan2020TPEL | 2020 | 정류기 전단 3상 인버터 | 산업용 드라이브(상용 AC 드라이브 구현은 2018 TIA 선행 논문) | DC-link 커패시터 전압·전류의 선택 주파수 성분(전류 측정/재구성 여부 n/s) | Partial | True Online | ESR(열화 지표) + C(열화 지표 겸 온도 민감 파라미터) + 코어/핫스팟 온도 | Goertzel 단일 빈 DFT(전체 FFT 대비 경량), 자기 보정 | n/s (커패시터/DC-link 전류 센서 가능성) | 실험(초록 기준; 선행 2018 TIA: PSpice + 커스텀 인버터 + 상용 AC 드라이브 구현) | 전류 센서 요구 여부 미확인 |
| 6 | Zhang2023TPEL | 2023 | 3-Level T-type 인버터 | 3레벨 인버터(일반) | 출력 전류와 그 변화율, 상전류 잔차, NP 전압 잔차(고장진단); DC-link AC 성분(고유 또는 주입) + 재구성 커패시터/입력 전류(CM) | Partial | True Online | C (초록: capacitance; ESR 언급 없음) | DC-link 고유 고조파 모델; 전류 재구성; 잔차 | (확인 필요) — 'extra hardware' 서브모듈 언급 | 실험(다양한 조건) | 주입/추가 HW 여부·ESR 미확인; T-type |
| 7 | Min2026TIE | 2026 | 3-Level NPC 인버터 | 3L-NPC(일반) | 상·하단 DC-link 커패시터 전압(vC1, vC2); 기준전압 오프셋 주입 | Yes | Quasi-Online | C (상·하단 프로파일 사용; 개별 추정 명시 여부 n/s) | 충방전 프로파일(시간영역) | None | 시뮬레이션 + 실험(초록) | 오프셋 주입 필요; C 만 |
| 8 | Zhao2023TPEL | 2023 | AC/DC 및 DC/DC 컨버터(일반) | 상용 전원장치로 실험; 토폴로지 비의존 주장 | DC-link 전압의 자연 발생 대신호 과도(저샘플링) | Yes | True Online | C + 감쇠계수 α(건전성 지표) | 대신호 과도 파형 피팅 | None | 시뮬(AC/DC, DC/DC) + 실험(상용 전원장치) | 과도 이벤트 의존; ESR 없음 |
| 9 | Wechsler2012TIA | 2012 | 항공용 fault-tolerant 드라이브 인버터 | 항공 전기 드라이브(ELGEAR) | 기존 보호/제어용 전압·전류 센서 신호 | Yes | True Online | C (스니펫: C 감소; ESR 포함 여부 확인 필요) | n/s | None | 수계산 + 시뮬 + 저전압 실험 + 고전압 항공 드라이브 구현 | 상세 미공개(초록); 필름·항공 특화 |
| 10 | Baumann2024TPEL | 2024 | 200 kW 풀스케일 전력 컨버터(CERN; 토폴로지 n/s) | 대형 산업/가속기 전원 | 셧다운 시 DC-link 전압 감쇠(방전 프로파일) | Yes | Quasi-Online | 잔존 C → SoH | 방전 프로파일 피팅 + 온도 보상 | n/s (온도 측정 수단 미기재) | 200 kW 컨버터 실험 + 가속 열화 + 현장 153대 | 정지 필요; ESR 없음 |

Rank 11–20 (근소 탈락; 9절·12절에서 함께 참조)

| Rank | Authors/Year | Title | Journal | DOI | Application | Method | Q1 | Q2 | Q3 | Exp | Score |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 11 | Li, Chen, Cong, Dai, Qiu, Liu 2022 | Online Condition Monitoring of DC-Link Capacitor for AC/DC/AC PWM Converter | IEEE TPEL 37(1):865–878 | 10.1109/TPEL.2021.3092429 | AFE+인버터 | DC-link 전압 주입(THD 한도 내) + 센서 없이 커패시터 전류 계산 + 슬라이딩 DFT → C | Yes | Quasi-Online(주입) | C | 실험 | 83 |
| 12 | Ahmad, Kumar, Arya, Anand 2018 | Noninvasive Technique for DC-Link Capacitance Estimation in Single-Phase Inverters | IEEE TPEL 33(5):3693–3696 | 10.1109/TPEL.2017.2762341 | 단상 계통연계 | 제어용 측정값의 2f 성분 v/i 비 → C | Yes | True Online | C | 시뮬+프로토타입(최대 오차 2.56 %, 이전 스니펫) | 86 |
| 13 | Lipnicki & Lewandowski 2017 | DC link condition monitoring method for two-level AC/DC/AC converters | Power Electronics and Drives 2(37)(1):43–56 | 10.5277/PED170107 | 2L AC/DC/AC | 상전류+레그 스위칭 함수로 DC-link 전류 재구성 + DC-link 전압 → ESR | Yes | True Online | ESR | n/s | 83 |
| 14 | Ribeiro, Alves, de Sousa, Oliveira 2024 | Online condition monitoring for DC-link capacitors of three-level NPC converters using noninvasive signal injection | Computers and Electrical Engineering 119:109577 | 10.1016/j.compeleceng.2024.109577 | 3L-NPC | 영상분 구형파 주입 → NP 전류 → Wavelet → ESR+C(<2 %) | Yes | Quasi-Online(주입) | C+ESR | n/s | 79 |
| 15 | Meng & Zhang 2022/2023 | An Online DC-Link Capacitance Estimation Method for Motor Drive Systems Based on an Intermittent Reverse-Charging Control Strategy | IEEE TPEL (권/쪽 확인 필요; Xplore 9907882) | (확인 필요) | 모터 드라이브 | 간헐 역충전 모드: 전압 상승 + 한 상전류(=충전전류) → C | Yes | Quasi-Online(간헐 시퀀스) | C | 시뮬+실험 | 82 |
| 16 | Sundararajan et al. 2018 | Online Condition Monitoring System for DC-Link Capacitor in Industrial Power Converters | IEEE TIA 54(5):4775–4785 | 10.1109/TIA.2018.2845889 | 산업용 컨버터/상용 AC 드라이브 | DC-link 전압·전류 스위칭 주파수 성분 비 → ESR; 상용 드라이브 구현 | Partial(전류 센서 n/s) | True Online | ESR | PSpice+커스텀 인버터+상용 드라이브 | 80 |
| 17 | Ghadrdan et al. 2022 | On-Line Condition Monitoring System for DC-Link Capacitor of Back-to-Back Converters Using Large-Signal Transients | IEEE JESTPE (권/쪽 확인 필요) | 10.1109/JESTPE.2022.3163012 | B2B | 스위칭 로직 일시 변경 → 대신호 과도(vdc + 입력 상전류) → C(<1 %) | Yes | Quasi-Online(시퀀스) | C | 실험(LCR 대조) | 81 |
| 18 | Muhammed Ramees & Ahmad 2025/26 | Non-Intrusive Capacitor Monitoring in Photovoltaic Inverters Based on MPPT-Induced Voltage Transients | IEEE TPEL (Early Access; 권/호 확인 필요; Xplore 11146599) | (확인 필요) | PV 인버터 | MPPT 기준 전압 전이 과도 + 출력 전류로 추정한 커패시터 전류 → C | Yes | 특정 운전조건(과도 이벤트) | C | 시뮬+프로토타입(이전 스니펫) | 80 |
| 19 | Dai, Zhao, Han, Chen 2024 | A High-Accuracy Capacitor Condition Monitoring Scheme at Low Sample Frequency Based on Improved Current Reconstruction Method | IEEE JESTPE 12(2):2281–2291 | 10.1109/JESTPE.2024.3370616 | AC/DC 컨버터 | 부하 변화 과도 + 전류 적분 재구성(저샘플링) → C | Yes | 특정 운전조건(부하 변화) | C | n/s | 76 |
| 20 | Nguyen, Le, Lee 2015 | Estimation of ESR in the DC-Link Capacitors of AC Motor Drive Systems with a Front-End Diode Rectifier | J. Power Electron. 15:411–418 | (확인 필요) | IM 드라이브 | 회생 중 q축 전류 주입; 고정자 전류+스위칭 상태로 ESR 전류 재구성 → RLS → ESR(≈1.2 %) | Yes | 특정 운전조건(회생)+주입 | ESR | 실험 | 79 |

---

## 7. Tier S / A / B

### Tier S — 가장 직접적인 On-board/Online DC-link 진단 (3)
| Rank | Title | First author | Year | Journal | DOI | Score | Evidence |
|---|---|---|---|---|---|---|---|
| 1 | Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor | M. Ghadrdan et al. | 2022 | IEEE Transactions on Power Electronics | 10.1109/TPEL.2022.3153842 | 93 | Abstract-level only |
| 2 | Online Estimation of DC-link Capacitor Parameters of Three-Level NPC Converters Using Inherent Signals Analysis | R. L. A. Ribeiro et al. | 2025 | IEEE/CAA Journal of Automatica Sinica | 10.1109/JAS.2025.125159 | 89 | Abstract-level only |
| 3 | Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor Based on Analysis of a Six-Pulse Diode Rectifier Having AC and DC Inductors | K. Hasegawa et al. | 2024 | IEEE Transactions on Industry Applications | (확인 필요) | 88 | Abstract-level only |

### Tier A — 방법론적으로 중요, 연구 설계에 직접 사용 (4)
| Rank | Title | First author | Year | Journal | DOI | Score | Evidence |
|---|---|---|---|---|---|---|---|
| 4 | Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters | K. Örüklü et al. | 2025 | IEEE Transactions on Industrial Electronics | 10.1109/TIE.2024.3454814 | 93 | Abstract-level only |
| 5 | Condition Monitoring of DC-Link Capacitors Using Goertzel Algorithm for Failure Precursor Parameter and Temperature Estimation | P. Sundararajan et al. | 2020 | IEEE Transactions on Power Electronics | 10.1109/TPEL.2019.2951859 | 87 | Abstract-level only |
| 6 | A Comprehensive Method for Online Switch Fault Diagnosis and Capacitor Condition Monitoring of Three-Level T-Type Inverters | W. Zhang et al. | 2023 | IEEE Transactions on Power Electronics | 10.1109/TPEL.2023.3262758 (이전 조사 스니펫; 재확인 필요) | 83 | Abstract-level only |
| 7 | An Online Condition Monitoring Method for DC-Link Capacitors of Three-Level NPC Inverters Based on Charge-Discharge Profile | K. J. Min et al. | 2026 | IEEE Transactions on Industrial Electronics — Accepted/In press (SeoulTech Pure). 이전에 기록한 vol. 73(8):12452–12463 은 이번 검증에서 확인되지 않음 | (확인 필요) — 10.1109/TIE.2026.3672764 는 어느 검색에서도 확인되지 않음 | 82 | Abstract-level only |

### Tier B — 물리모델 / 기반 / prognostics 요소 (3)
| Rank | Title | First author | Year | Journal | DOI | Score | Evidence |
|---|---|---|---|---|---|---|---|
| 8 | A Transient-Modeling-Based Grey-Box Method for Online Monitoring of DC-Link Capacitors | Z. Zhao et al. | 2023 | IEEE Transactions on Power Electronics | 10.1109/TPEL.2023.3308115 | 83 | Abstract-level only |
| 9 | Condition Monitoring of DC-Link Capacitors in Aerospace Drives | K. Wechsler et al. | 2012 | IEEE Transactions on Industry Applications | 10.1109/TIA.2012.2222333 | 89 | Abstract-level only |
| 10 | Discharge-Based Condition Monitoring for Electrolytic DC-Link Capacitors | T. F. Baumann et al. | 2024 | IEEE Transactions on Power Electronics (vol/호/쪽 확인 필요; 이전 조사 스니펫 39:16622–16637) | 10.1109/TPEL.2024.3442077 | 81 | Abstract-level only |

Tier 결정 메모: Örüklü 2025(93점)는 총점으로는 S 급이나 "AI 벤치마크" 성격이 강해 A 로, Hasegawa & Hirose 2024(88점)는 전류 센서 완전 배제 + C+ESR + True Online 으로 핵심 질문에 가장 직접 답해 S 로 두었다. Wechsler 2012(89점)는 점수는 높으나 초록에 알고리즘·신호가 전혀 없어(상세 불명) 기반 논문으로 B, Zhao 2023(83점)·Baumann 2024(81점)는 물리모델·prognostics 요소 대표로 B.

---

## 8. Detailed Analysis of 10 Papers

## Rank 1 — Tier S — Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor

### Bibliographic Information
- Title: Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor
- Authors: M. Ghadrdan, S. Peyghami, H. Mokhtari, F. Blaabjerg
- Year: 2022
- Journal: IEEE Transactions on Power Electronics, vol. 37, no. 8, pp. 9733–9744
- DOI: 10.1109/TPEL.2022.3153842
- Journal Grade: IEEE TPEL (Q1, 전력전자 최상위)
- 식별/출처: Xplore 9721605; AAU VBN 레코드
- **Evidence: Abstract-level only** — 본문 미열람. 아래 항목 중 n/s 는 초록·스니펫에 없는 내용이며 추측으로 채우지 않았다.

### Inverter / Application
- Topology: 2-Level back-to-back (AC/DC/AC) VSC
- Application: 계통연계·드라이브 공용 B2B 컨버터

### DC-Link Capacitor
- 알루미늄 전해, 단일 DC-link (용량 n/s)

### Research Objective
커패시터 전류 센서 없이 B2B 컨버터의 전해 DC-link 커패시터 열화를 운전 중 추적할 수 있는 지표(DF)와 그 측정법을 제시.

### Health Indicator
- Dissipation factor DF = tanδ = ω·C·ESR (C·ESR 결합 지표) + EoL 기준 제안

### Measurement Signal
- 컨버터 출력(AC) 상전류 + 스위칭 상태 → 재구성한 커패시터 전류의 스위칭 주파수 성분; DC-link 전압 리플

### Existing Inverter Sensor?
- **Yes — 초록 기준 '출력 전류로부터 커패시터 전류의 스위칭 주파수 성분을 재구성'하며 커패시터 전류 센서를 쓰지 않음. 상전류·DC-link 전압은 제어용 기존 센서.**

### Additional Sensor
- None (초록 기준)

### Online Capability
- **True Online — 주입·시퀀스 없이 정상 운전 중 스위칭 주파수 성분을 이용(초록 기준).**

### Diagnostic Principle
스위칭 주파수 대역에서 커패시터 임피던스는 ESR과 1/(ωC)가 함께 기여하므로, 재구성 전류와 전압 리플의 비에서 DF를 얻으면 C 감소와 ESR 증가가 모두 DF 증가로 나타난다(해석). 저자는 DF가 수명 지표로 더 많은 정보를 담는다고 주장(초록).

### Signal Processing / Feature
- 스위칭 주파수 성분(리플) 추출; 커패시터 전류 재구성

### Diagnosis Algorithm
- 상전류×스위칭 함수 → 커패시터 전류 재구성 → fsw 성분 추출 → DF 계산 → EoL 임계 비교 (세부 수식 n/s)

### Operating Conditions
- DC-link 전압·fsw·기본파·부하·변조지수·커패시터 값 모두 n/s. 초록은 스위칭 주파수·ESL·계통 필터가 DF 정확도에 미치는 영향을 분석했다고 언급.

### Aging Implementation
- n/s (실험 검증 언급; 노화 모사 방식 미기재)

### Experimental Validation
- 실험(초록: experimental) — 세부 n/s

### Main Result
- 수치 n/s (초록에 오차 수치 없음)

### Strengths
- 커패시터 전류 센서 불필요(출력 전류 재구성)
- 주입 없음, True Online
- DF 하나로 C·ESR 변화를 모두 반영
- 스위칭 주파수·ESL·필터 영향을 명시적으로 분석

### Limitations
- DF 단독으로는 C와 ESR을 분리할 수 없음(추론)
- 스위칭 주파수·ESL·필터 의존(저자 언급) → 운전점·fsw 변경 시 보정 필요 가능성
- 부하·변조지수 의존성 n/s
- 노이즈 민감도 n/s
- 2-Level 한정; NPC 로의 확장은 스위칭 함수 재정의 필요(추론)

### Score (100)
| A On-board 25/25 | B Online 20/20 | C Target 13/15 | D Signal 15/15 | E Exp 8/10 | F Robust 7/10 | G Quality 5/5 | **Total 93** |
|---|---|---|---|---|---|---|---|

### Why This Paper Matters
‘상전류 + 스위칭 상태 → 커패시터 전류 재구성 → 스위칭 주파수 성분’ 이라는, 내 연구의 신호 생성 철학과 가장 가까운 True-Online 저널 논문. 재구성 식·대역 선택·ESL/필터 영향 분석을 그대로 가져올 수 있다.

---

## Rank 2 — Tier S — Online Estimation of DC-link Capacitor Parameters of Three-Level NPC Converters Using Inherent Signals Analysis

### Bibliographic Information
- Title: Online Estimation of DC-link Capacitor Parameters of Three-Level NPC Converters Using Inherent Signals Analysis
- Authors: R. L. A. Ribeiro, R. P. R. de Souza(Sousa), A. C. Oliveira, A. M. N. Lima, Q.-L. Han
- Year: 2025
- Journal: IEEE/CAA Journal of Automatica Sinica, vol. 12, no. 7, pp. 1434–1444 (July 2025)
- DOI: 10.1109/JAS.2025.125159
- Journal Grade: IEEE/CAA JAS (Q1, 자동화 분야 고IF; 전력전자 전문지는 아님)
- 식별/출처: Xplore 10938042; ieee-jas.com
- **Evidence: Abstract-level only** — 본문 미열람. 아래 항목 중 n/s 는 초록·스니펫에 없는 내용이며 추측으로 채우지 않았다.

### Inverter / Application
- Topology: 3-Level NPC VSI (계통연계)
- Application: 계통연계 3L-NPC

### DC-Link Capacitor
- 분할 DC-link(전해 키워드), 상·하단 개별 추정 여부 n/s

### Research Objective
추가 센서나 주입 없이 3L-NPC 의 DC-link 커패시터 C·ESR 을 운전 중 추정.

### Health Indicator
- C + ESR (열화 추적)

### Measurement Signal
- PWM 전략과 토폴로지의 상호작용이 만드는 고유 상호변조(intermodulation) 성분; 측정량은 off-the-shelf 3L-NPC 의 기존 센서(구체 n/s)

### Existing Inverter Sensor?
- **Yes — 초록: 'no additional sensors beyond those already installed in off-the-shelf 3L-NPC-VSI'.**

### Additional Sensor
- None

### Online Capability
- **True Online — 주입 없이 고유 신호를 쓰며 정상 운전 중 관측기로 추정(초록 기준).**

### Diagnostic Principle
PWM×NPC 토폴로지가 만드는 상호변조 성분의 크기·위상이 DC-link 임피던스(C, ESR)에 종속 → 해당 성분을 추적해 파라미터를 역산(초록 수준; 어떤 성분인지 n/s). (추론) 중성점 전류의 3f1 성분과 스위칭 측대파의 조합일 가능성.

### Signal Processing / Feature
- 비정수 재귀 슬라이딩 DFT(rnSDFT)로 상호변조 성분 추적

### Diagnosis Algorithm
- 관측기 구조: rnSDFT + 망각계수 RLS (oSDFT-RLS) → C, ESR 시간-주파수 추정

### Operating Conditions
- n/s (계통연계 실험실 셋업)

### Aging Implementation
- n/s

### Experimental Validation
- 실험(laboratory setup, 초록 기준)

### Main Result
- 수치 n/s

### Strengths
- NPC 에서 무주입·기존 센서·True Online 을 모두 만족하는 유일한 저널 논문(본 조사 범위)
- C 와 ESR 동시 추정
- 재귀 추정으로 실시간 구현 가능(추론)

### Limitations
- 상호변조 성분의 크기가 변조지수·부하·역률에 의존할 가능성(추론) — 다중 운전조건 검증 n/s
- C1/C2 개별 추정 여부 n/s
- PWM 전략 의존(저자 언급 취지)
- 노이즈 민감도 n/s
- 저널이 전력전자 전문지가 아님

### Score (100)
| A On-board 25/25 | B Online 20/20 | C Target 15/15 | D Signal 13/15 | E Exp 8/10 | F Robust 3/10 | G Quality 5/5 | **Total 89** |
|---|---|---|---|---|---|---|---|

### Why This Paper Matters
내 연구(3L-NPC, 무주입, 내부 신호 고조파)의 신규성 경계를 정하는 경쟁 선행. 어떤 상호변조 성분을 쓰는지와 C1/C2 분리 여부에 따라 내 연구의 차별화 지점이 달라진다.

---

## Rank 3 — Tier S — Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor Based on Analysis of a Six-Pulse Diode Rectifier Having AC and DC Inductors

### Bibliographic Information
- Title: Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor Based on Analysis of a Six-Pulse Diode Rectifier Having AC and DC Inductors
- Authors: K. Hasegawa, Y. Hirose
- Year: 2024
- Journal: IEEE Transactions on Industry Applications, vol. 60, no. 6, pp. 9043–9051 (Nov./Dec. 2024)
- DOI: (확인 필요)
- Journal Grade: IEEE TIA (Q1)
- 식별/출처: Kyutech 리포지토리 record 2001388 (권/호/쪽 일치)
- **Evidence: Abstract-level only** — 본문 미열람. 아래 항목 중 n/s 는 초록·스니펫에 없는 내용이며 추측으로 채우지 않았다.

### Inverter / Application
- Topology: 6-pulse 다이오드 정류기(AC+DC 인덕터) + 3상 PWM 인버터
- Application: 산업용 모터 드라이브(정류기 전단)

### DC-Link Capacitor
- DC-link (종류 n/s; 그룹 선행 논문은 전해)

### Research Objective
전류 센서를 전혀 쓰지 않고 정류기 전단 드라이브의 DC-link 커패시터 ESR·C 를 운전 중 추정.

### Health Indicator
- C + ESR

### Measurement Signal
- 3상 전원 전압, 선로/DC 인덕턴스(모델), 인버터 출력 전력, DC-link 전압 — 전류 센서 없음

### Existing Inverter Sensor?
- **Yes — 초록: 'without current sensors'; 전원 전압·DC-link 전압·출력 전력은 드라이브 제어/보호용으로 보통 존재(해석).**

### Additional Sensor
- None

### Online Capability
- **True Online — 정류 리플(6f) 해석 기반, 주입·시퀀스 없음(초록 기준; 명시적 'online' 표현은 n/s).**

### Diagnostic Principle
6-pulse 정류기의 리플 전류를 전원 전압·인덕턴스·출력 전력에서 해석적으로 계산하면 커패시터 전류를 알 수 있고, DC-link 전압 리플과 결합해 ESR(고주파/리플 성분)과 C(저주파 적분 성분)를 분리(해석; 저자 수식 n/s).

### Signal Processing / Feature
- 정류 리플 성분(6·f_grid 계열) 해석; 모델 기반 전류 재구성

### Diagnosis Algorithm
- 정류기 회로 해석 → 커패시터 전류 계산 → DC-link 전압과 결합 → C, ESR 산출 (세부 n/s)

### Operating Conditions
- 200 V 실험 시스템(초록); fsw·부하·커패시터 값 n/s

### Aging Implementation
- n/s ('ESR·C 변화 관측')

### Experimental Validation
- 실험(200 V 실험실 시스템)

### Main Result
- 수치 n/s

### Strengths
- 전류 센서 완전 배제
- C 와 ESR 동시
- 주입 없음
- 불평형 전원 확장판 존재(Yamasoto & Hasegawa 2025)

### Limitations
- 다이오드 정류기 전단 구조에 한정 — AFE·배터리 입력 인버터(EV)에는 부적합(추론)
- 전원 임피던스·인덕턴스 모델 오차에 민감(추론)
- 부하·전원 불평형 의존(후속 논문이 다룸)
- 다중 운전조건 검증 n/s

### Score (100)
| A On-board 25/25 | B Online 20/20 | C Target 15/15 | D Signal 13/15 | E Exp 8/10 | F Robust 3/10 | G Quality 4/5 | **Total 88** |
|---|---|---|---|---|---|---|---|

### Why This Paper Matters
‘모델로 전류를 만들어 센서를 없애는’ 접근의 최신 저널판. 정류기 전단 드라이브라면 가장 실용적인 On-board 후보이며, 내 시뮬→실험 전환 시 전류 확보 전략의 대안이다.

---

## Rank 4 — Tier A — Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters

### Bibliographic Information
- Title: Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters
- Authors: K. Örüklü, Ş. Ağalar
- Year: 2025
- Journal: IEEE Transactions on Industrial Electronics, vol. 72, no. 4, pp. 4227–4237 (Apr. 2025)
- DOI: 10.1109/TIE.2024.3454814
- Journal Grade: IEEE TIE (Q1)
- 식별/출처: ResearchGate 384386370; arXiv 2609.00218 참고문헌
- **Evidence: Abstract-level only** — 본문 미열람. 아래 항목 중 n/s 는 초록·스니펫에 없는 내용이며 추측으로 채우지 않았다.

### Inverter / Application
- Topology: 2-Level 3상 AC/DC/AC
- Application: B2B 컨버터(일반)

### DC-Link Capacitor
- DC-link (종류 n/s)

### Research Objective
정상 운전 신호만으로 DC-link 커패시턴스를 ML 로 추정하고 예측 불확실성을 함께 제공.

### Health Indicator
- C (health indicator) + 예측 불확실성

### Measurement Signal
- DC-link 전압 리플의 PSD

### Existing Inverter Sensor?
- **Yes — DC-link 전압 센서만 사용(초록 기준); 추가 HW·주입 없음.**

### Additional Sensor
- None

### Online Capability
- **True Online — 정상 운전 중 전압 리플 PSD 를 입력으로 사용(초록 기준).**

### Diagnostic Principle
C 감소 → 리플 전압 스펙트럼(특히 저주파·스위칭 대역)의 크기 변화 → PSD 특징을 GPR 이 C 로 회귀(해석).

### Signal Processing / Feature
- PSD(저샘플링 강조)

### Diagnosis Algorithm
- Gaussian Process Regression (불확실성 정량화)

### Operating Conditions
- 여러 부하 수준과 출력 주파수에서 검증(이전 조사 스니펫); 상세 n/s

### Aging Implementation
- n/s (실험 프로토타입)

### Experimental Validation
- 시뮬레이션 + 실험실 프로토타입

### Main Result
- 평균 예측 오차 < 2 % (이전 조사 스니펫), 'high accuracy'

### Strengths
- DC-link 전압만 사용
- 다중 운전조건 검증
- 불확실성 제공 → 신뢰도 기반 판정 가능
- 저샘플링

### Limitations
- C 만(ESR 없음)
- 전압 리플 PSD 는 부하·변조에 의존 → 학습 범위 밖 조건의 일반화 n/s
- 노화 데이터 출처 n/s(모사 추정)
- GPR 의 추론 비용은 데이터 수에 비례(추론)

### Score (100)
| A On-board 25/25 | B Online 20/20 | C Target 13/15 | D Signal 13/15 | E Exp 8/10 | F Robust 10/10 | G Quality 4/5 | **Total 93** |
|---|---|---|---|---|---|---|---|

### Why This Paper Matters
데이터 기반 On-board 진단에서 ‘다중 조건 실험 + 불확실성’ 을 갖춘 벤치마크. 내 CNN 연구의 평가 프로토콜과 비교 기준선으로 직접 사용.

---

## Rank 5 — Tier A — Condition Monitoring of DC-Link Capacitors Using Goertzel Algorithm for Failure Precursor Parameter and Temperature Estimation

### Bibliographic Information
- Title: Condition Monitoring of DC-Link Capacitors Using Goertzel Algorithm for Failure Precursor Parameter and Temperature Estimation
- Authors: P. Sundararajan, M. H. M. Sathik, F. Sasongko, C. S. Tan, J. Pou, F. Blaabjerg, A. K. Gupta
- Year: 2020
- Journal: IEEE Transactions on Power Electronics, vol. 35, no. 6, pp. 6386–6396 (June 2020)
- DOI: 10.1109/TPEL.2019.2951859
- Journal Grade: IEEE TPEL (Q1)
- 식별/출처: Xplore 8892651; AAU VBN / NTU Pure
- **Evidence: Abstract-level only** — 본문 미열람. 아래 항목 중 n/s 는 초록·스니펫에 없는 내용이며 추측으로 채우지 않았다.

### Inverter / Application
- Topology: 정류기 전단 3상 인버터
- Application: 산업용 드라이브(상용 AC 드라이브 구현은 2018 TIA 선행 논문)

### DC-Link Capacitor
- 알루미늄 전해 DC-link

### Research Objective
적은 계산량으로 ESR·C 를 추정하고, 노화에 따른 온도 추정 오차를 자기 보정.

### Health Indicator
- ESR(열화 지표) + C(열화 지표 겸 온도 민감 파라미터) + 코어/핫스팟 온도

### Measurement Signal
- DC-link 커패시터 전압·전류의 선택 주파수 성분(전류 측정/재구성 여부 n/s)

### Existing Inverter Sensor?
- **Partial — DC-link 전압은 기존 센서; 커패시터 전류 센서 사용 여부가 초록에 없음(선행 2018 TIA 는 DC-link 전압·전류 사용).**

### Additional Sensor
- n/s (커패시터/DC-link 전류 센서 가능성)

### Online Capability
- **True Online — 주입 없음, 운전 중 리플 성분 사용(초록 기준).**

### Diagnostic Principle
스위칭 주파수(또는 정류 6f) 성분에서 |Z|≈ESR, 저주파에서 1/(ωC) 지배 → 두 성분 비로 ESR·C; C 의 온도 의존성을 이용해 온도 추정(초록 취지).

### Signal Processing / Feature
- Goertzel 단일 빈 DFT(전체 FFT 대비 경량), 자기 보정

### Diagnosis Algorithm
- Goertzel 로 선택 빈 추출 → ESR, C 계산 → C-온도 관계로 온도 추정 → 노화 보정

### Operating Conditions
- n/s

### Aging Implementation
- n/s

### Experimental Validation
- 실험(초록 기준; 선행 2018 TIA: PSpice + 커스텀 인버터 + 상용 AC 드라이브 구현)

### Main Result
- 수치 n/s

### Strengths
- 경량 스펙트럼 추출(임베디드 적합)
- ESR·C·온도 동시
- 산업 구현 계보(2018 TIA 상용 드라이브)

### Limitations
- 커패시터 전류 센서 요구 가능성(n/s)
- 선택 빈이 fsw 이면 fsw·변조 의존(추론)
- 다중 운전조건 검증 n/s

### Score (100)
| A On-board 20/25 | B Online 20/20 | C Target 15/15 | D Signal 12/15 | E Exp 8/10 | F Robust 7/10 | G Quality 5/5 | **Total 87** |
|---|---|---|---|---|---|---|---|

### Why This Paper Matters
내 CNN 입력 feature 를 ‘소수 고조파 빈’ 으로 줄여 On-board 구현하려면 가장 직접적인 방법론 공여자. 온도 교란을 C 로 추정해 보정하는 아이디어도 가져올 수 있다.

---

## Rank 6 — Tier A — A Comprehensive Method for Online Switch Fault Diagnosis and Capacitor Condition Monitoring of Three-Level T-Type Inverters

### Bibliographic Information
- Title: A Comprehensive Method for Online Switch Fault Diagnosis and Capacitor Condition Monitoring of Three-Level T-Type Inverters
- Authors: W. Zhang, Y. He, X. Wang, J. Chen
- Year: 2023
- Journal: IEEE Transactions on Power Electronics, vol. 38, no. 8, pp. 10183–10195 (이전 조사 스니펫; 이번 재확인에서는 Xplore 10086646·저자·Aug 2023 만 확인)
- DOI: 10.1109/TPEL.2023.3262758 (이전 조사 스니펫; 재확인 필요)
- Journal Grade: IEEE TPEL (Q1)
- 식별/출처: Xplore 10086646; ResearchGate
- **Evidence: Abstract-level only** — 본문 미열람. 아래 항목 중 n/s 는 초록·스니펫에 없는 내용이며 추측으로 채우지 않았다.

### Inverter / Application
- Topology: 3-Level T-type 인버터
- Application: 3레벨 인버터(일반)

### DC-Link Capacitor
- 분할 DC-link (종류 n/s)

### Research Objective
스위치 OC 고장진단과 DC-link 커패시터 CM 을 하나의 온라인 프레임워크로 통합.

### Health Indicator
- C (초록: capacitance; ESR 언급 없음)

### Measurement Signal
- 출력 전류와 그 변화율, 상전류 잔차, NP 전압 잔차(고장진단); DC-link AC 성분(고유 또는 주입) + 재구성 커패시터/입력 전류(CM)

### Existing Inverter Sensor?
- **Partial — 상전류·NP 전압은 기존 센서. 프레임워크 서술에 'signal injection', 'extra hardware' 서브모듈이 언급되어 완전 센서리스 여부 판별 불가(스니펫 문맥 손상).**

### Additional Sensor
- (확인 필요) — 'extra hardware' 서브모듈 언급

### Online Capability
- **True Online(고유 AC 성분 사용 시) / Quasi-Online(주입 AC 성분 사용 시) — 초록이 'inherent or injected AC component' 둘 다 언급.**

### Diagnostic Principle
3L T-type 의 DC-link 측·AC 측 모델에서 정상/고장 시 고유 고조파 성분을 도출; 커패시터 전류(및 입력 전류)를 재구성해 DC-link AC 성분과 함께 RLS 로 C 추정(초록 취지).

### Signal Processing / Feature
- DC-link 고유 고조파 모델; 전류 재구성; 잔차

### Diagnosis Algorithm
- 모델 기반 잔차(고장) + 커패시터 전류 재구성 + RLS(C)

### Operating Conditions
- 'various conditions' 에서 실험(초록); 수치 n/s

### Aging Implementation
- n/s

### Experimental Validation
- 실험(다양한 조건)

### Main Result
- 수치 n/s

### Strengths
- 3레벨 분할 DC-link 의 고유 고조파 모델과 커패시터 전류 재구성을 함께 제시
- 다양한 조건 실험
- 고장진단과 통합

### Limitations
- T-type(NPC 와 도통 경로 상이)
- 주입·추가 HW 요구 여부 불명
- C 만
- 상·하단 개별 추정 n/s

### Score (100)
| A On-board 20/25 | B Online 15/20 | C Target 13/15 | D Signal 15/15 | E Exp 8/10 | F Robust 7/10 | G Quality 5/5 | **Total 83** |
|---|---|---|---|---|---|---|---|

### Why This Paper Matters
내 NPC 연구에 필요한 ‘3레벨 DC-link 고유 고조파의 해석 모델 + 커패시터 전류 재구성 + RLS’ 를 가장 가깝게 제공할 가능성이 큰 논문. 모델을 NPC 도통 경로로 바꿔 쓸 수 있다.

---

## Rank 7 — Tier A — An Online Condition Monitoring Method for DC-Link Capacitors of Three-Level NPC Inverters Based on Charge-Discharge Profile

### Bibliographic Information
- Title: An Online Condition Monitoring Method for DC-Link Capacitors of Three-Level NPC Inverters Based on Charge-Discharge Profile
- Authors: K. J. Min, U.-M. Choi, F. Blaabjerg
- Year: 2026
- Journal: IEEE Transactions on Industrial Electronics — Accepted/In press (SeoulTech Pure). 이전에 기록한 vol. 73(8):12452–12463 은 이번 검증에서 확인되지 않음
- DOI: (확인 필요) — 10.1109/TIE.2026.3672764 는 어느 검색에서도 확인되지 않음
- Journal Grade: IEEE TIE (Q1)
- 식별/출처: pure.seoultech.ac.kr; 학회 선행판(2025, Min & Choi) 존재
- **Evidence: Abstract-level only** — 본문 미열람. 아래 항목 중 n/s 는 초록·스니펫에 없는 내용이며 추측으로 채우지 않았다.

### Inverter / Application
- Topology: 3-Level NPC 인버터
- Application: 3L-NPC(일반)

### DC-Link Capacitor
- 상·하단 분할 DC-link (종류 n/s)

### Research Objective
추가 HW 없이 3L-NPC 상·하단 DC-link 커패시터의 C 를 운전 중 추정.

### Health Indicator
- C (상·하단 프로파일 사용; 개별 추정 명시 여부 n/s)

### Measurement Signal
- 상·하단 DC-link 커패시터 전압(vC1, vC2); 기준전압 오프셋 주입

### Existing Inverter Sensor?
- **Yes — 초록: 'without requiring additional hardware'; vC1, vC2 는 NPC 의 NP 밸런싱용 기존 센서.**

### Additional Sensor
- None

### Online Capability
- **Quasi-Online — 기준전압에 오프셋을 주입해 vC1−vC2 를 능동적으로 발산시키는 진단 시퀀스가 필요(출력전류 왜곡 보상 포함).**

### Diagnostic Principle
Q = C·Δv: 지정 전압차에 도달하는 충방전 프로파일(시간/전하)에서 C 를 산출(초록 취지).

### Signal Processing / Feature
- 충방전 프로파일(시간영역)

### Diagnosis Algorithm
- 오프셋 주입 → vC1−vC2 추적 → 도달 시간/전하 → C; 출력전류 왜곡 보상 전략

### Operating Conditions
- n/s

### Aging Implementation
- n/s

### Experimental Validation
- 시뮬레이션 + 실험(초록)

### Main Result
- 평균 오차 < 1 %

### Strengths
- NPC 상·하단 커패시터를 다루는 유일한 TIE 급 저널 논문(본 조사)
- <1 % 오차
- 추가 HW 없음
- 국내 그룹(본문 확보 용이)

### Limitations
- 주입형(출력 왜곡 보상 필요)
- C 만
- 고조파 아님
- 서지(권/쪽/DOI) 미확정

### Score (100)
| A On-board 25/25 | B Online 15/20 | C Target 13/15 | D Signal 13/15 | E Exp 8/10 | F Robust 3/10 | G Quality 5/5 | **Total 82** |
|---|---|---|---|---|---|---|---|

### Why This Paper Matters
내 연구가 C1/C2 개별 노화를 목표로 한다면 반드시 비교해야 할 경쟁 선행. 주입 없이 같은 결과를 얻는 것이 내 연구의 차별점이 된다.

---

## Rank 8 — Tier B — A Transient-Modeling-Based Grey-Box Method for Online Monitoring of DC-Link Capacitors

### Bibliographic Information
- Title: A Transient-Modeling-Based Grey-Box Method for Online Monitoring of DC-Link Capacitors
- Authors: Z. Zhao, (Hu), P. Davari et al. (전체 저자 확인 필요)
- Year: 2023
- Journal: IEEE Transactions on Power Electronics, vol. 38, no. 11, pp. 14547–14562
- DOI: 10.1109/TPEL.2023.3308115
- Journal Grade: IEEE TPEL (Q1); 2023 TPEL Prize Paper 2위
- 식별/출처: AAU VBN 저자 최종본; AAU 수상 기록
- **Evidence: Abstract-level only** — 본문 미열람. 아래 항목 중 n/s 는 초록·스니펫에 없는 내용이며 추측으로 채우지 않았다.

### Inverter / Application
- Topology: AC/DC 및 DC/DC 컨버터(일반)
- Application: 상용 전원장치로 실험; 토폴로지 비의존 주장

### DC-Link Capacitor
- DC-link (종류 n/s)

### Research Objective
토폴로지·제어 정보에 거의 의존하지 않고 DC-link 전압의 대신호 과도만으로 C 와 건전성 지표를 추정.

### Health Indicator
- C + 감쇠계수 α(건전성 지표)

### Measurement Signal
- DC-link 전압의 자연 발생 대신호 과도(저샘플링)

### Existing Inverter Sensor?
- **Yes — DC-link 전압 센서만(초록 기준).**

### Additional Sensor
- None

### Online Capability
- **True Online(이벤트 구동) — 비침습이나 대신호 과도가 발생할 때만 추정 가능 → 본 채점에서는 '특정 운전조건에서 Online'(12점)으로 보수 분류.**

### Diagnostic Principle
과도 시 DC-link 전압이 병렬 RLC 영상태 응답과 유사 → 감쇠계수·고유주파수에서 C·α 식별(grey-box TECM).

### Signal Processing / Feature
- 대신호 과도 파형 피팅

### Diagnosis Algorithm
- 등가 RLC 과도 모델(TECM) 파라미터 식별

### Operating Conditions
- 다양한 부하 종류(시뮬); 상용 전원장치 실험; fsw 등 n/s

### Aging Implementation
- n/s

### Experimental Validation
- 시뮬(AC/DC, DC/DC) + 실험(상용 전원장치)

### Main Result
- α, C 오차 < 1 %

### Strengths
- 전압 센서만, 저샘플링
- 토폴로지 비의존 주장
- 오차 <1 %, 수상 논문

### Limitations
- 과도 이벤트가 있어야 추정(연속 아님)
- ESR 직접 추정 없음(α 간접)
- 인버터 고조파와 무관 → 내 접근과 보완 관계

### Score (100)
| A On-board 25/25 | B Online 12/20 | C Target 13/15 | D Signal 13/15 | E Exp 8/10 | F Robust 7/10 | G Quality 5/5 | **Total 83** |
|---|---|---|---|---|---|---|---|

### Why This Paper Matters
‘전압 센서 하나로 On-board’ 의 최신 물리 모델 대표. 내 고조파 접근과 보완적으로 결합(과도 시 C, 정상상태 고조파로 ESR)할 수 있고, 저샘플링 구현 논리를 참고.

---

## Rank 9 — Tier B — Condition Monitoring of DC-Link Capacitors in Aerospace Drives

### Bibliographic Information
- Title: Condition Monitoring of DC-Link Capacitors in Aerospace Drives
- Authors: K. Wechsler, B. C. Mecrow, D. J. Atkinson, J. W. Bennett, M. Benarous
- Year: 2012
- Journal: IEEE Transactions on Industry Applications, vol. 48, no. 6, pp. 1866–1874
- DOI: 10.1109/TIA.2012.2222333
- Journal Grade: IEEE TIA (Q1)
- 식별/출처: Xplore 6319385; Newcastle ePrints 190775
- **Evidence: Abstract-level only** — 본문 미열람. 아래 항목 중 n/s 는 초록·스니펫에 없는 내용이며 추측으로 채우지 않았다.

### Inverter / Application
- Topology: 항공용 fault-tolerant 드라이브 인버터
- Application: 항공 전기 드라이브(ELGEAR)

### DC-Link Capacitor
- Metallized polypropylene 필름 DC-link

### Research Objective
보호·제어용 기존 센서만으로, 주입이나 특수 운전 없이 필름 DC-link 커패시터 열화를 운전 중 감시.

### Health Indicator
- C (스니펫: C 감소; ESR 포함 여부 확인 필요)

### Measurement Signal
- 기존 보호/제어용 전압·전류 센서 신호

### Existing Inverter Sensor?
- **Yes — 초록: 기존 보호·제어 센서 사용, 'no injected signals or special operation'.**

### Additional Sensor
- None

### Online Capability
- **True Online — 주입·특수 운전 없음, 운전 중 추정(초록 기준).**

### Diagnostic Principle
n/s (초록 수준). (해석) 필름 커패시터는 ESR 이 작아 C 변화가 주 지표.

### Signal Processing / Feature
- n/s

### Diagnosis Algorithm
- n/s

### Operating Conditions
- 토크·속도 독립 주장(초록); 저전압 실험 + 고전압 항공 드라이브 구현

### Aging Implementation
- n/s ('deterioration' 추적)

### Experimental Validation
- 수계산 + 시뮬 + 저전압 실험 + 고전압 항공 드라이브 구현

### Main Result
- 수치 n/s

### Strengths
- 필름 커패시터 True Online 의 기반 논문
- 토크·속도 독립(운전조건 강건성 명시)
- 실제 항공 드라이브 구현

### Limitations
- 2012 — 알고리즘 상세 n/s
- ESR 여부 미확인
- 항공 특수 구조(fault-tolerant) 의존 가능성(추론)

### Score (100)
| A On-board 25/25 | B Online 20/20 | C Target 13/15 | D Signal 12/15 | E Exp 8/10 | F Robust 7/10 | G Quality 4/5 | **Total 89** |
|---|---|---|---|---|---|---|---|

### Why This Paper Matters
‘기존 센서 + 무주입 + 운전조건 독립’ 을 가장 먼저 명시한 필름 DC-link 논문. 내 연구의 커패시터가 필름이면 지표(C)와 강건성 주장의 근거로 인용.

---

## Rank 10 — Tier B — Discharge-Based Condition Monitoring for Electrolytic DC-Link Capacitors

### Bibliographic Information
- Title: Discharge-Based Condition Monitoring for Electrolytic DC-Link Capacitors
- Authors: T. F. Baumann, R. Murillo Garcia, K. Papastergiou, D. Peftitsis
- Year: 2024
- Journal: IEEE Transactions on Power Electronics (vol/호/쪽 확인 필요; 이전 조사 스니펫 39:16622–16637)
- DOI: 10.1109/TPEL.2024.3442077
- Journal Grade: IEEE TPEL (Q1)
- 식별/출처: Xplore 10633828; NTNU Open; CERN author copy
- **Evidence: Abstract-level only** — 본문 미열람. 아래 항목 중 n/s 는 초록·스니펫에 없는 내용이며 추측으로 채우지 않았다.

### Inverter / Application
- Topology: 200 kW 풀스케일 전력 컨버터(CERN; 토폴로지 n/s)
- Application: 대형 산업/가속기 전원

### DC-Link Capacitor
- 알루미늄 전해 DC-link

### Research Objective
정지 시 DC-link 전압 감쇠로 잔존 C 를 구하고, 온도·사전충전 조건을 보상한 SoH 모델을 현장 데이터로 검증.

### Health Indicator
- 잔존 C → SoH

### Measurement Signal
- 셧다운 시 DC-link 전압 감쇠(방전 프로파일)

### Existing Inverter Sensor?
- **Yes — DC-link 전압 센서(초록 기준); 온도 보상 수단은 n/s.**

### Additional Sensor
- n/s (온도 측정 수단 미기재)

### Online Capability
- **Quasi-Online(정지 후 측정) — 컨버터 셧다운 구간을 이용('low-invasive').**

### Diagnostic Principle
RC 방전 시정수에서 C; 전해 커패시터의 온도 의존성을 모델에 넣어 보상.

### Signal Processing / Feature
- 방전 프로파일 피팅 + 온도 보상

### Diagnosis Algorithm
- 방전 해석 → 잔존 C → SoH 모델

### Operating Conditions
- 다양한 온도·사전충전 조건의 가속 열화 시험; 153 대 현장 데이터

### Aging Implementation
- 실제 가속 열화 시험 + 현장 열화 데이터

### Experimental Validation
- 200 kW 컨버터 실험 + 가속 열화 + 현장 153대

### Main Result
- 수치 n/s

### Strengths
- 실제 열화·현장 데이터 규모가 가장 큼
- 온도 보상 SoH 모델
- 구현 단순

### Limitations
- 정지 구간 필요(True Online 아님)
- ESR 없음
- 고조파 무관

### Score (100)
| A On-board 25/25 | B Online 5/20 | C Target 13/15 | D Signal 13/15 | E Exp 10/10 | F Robust 10/10 | G Quality 5/5 | **Total 81** |
|---|---|---|---|---|---|---|---|

### Why This Paper Matters
진단 결과를 SoH·수명으로 연결하고 온도 교란을 모델로 보상하는 ‘prognostics 요소’ 의 대표. 내 연구의 라벨(노화 등급) 정의와 온도 보정 논리의 참고.

---

## 9. Existing-Sensor-Only Methods (Top 10 중 Q1 = Yes)

| Paper | Existing Signal | Estimated Parameter | Reconstruction Required | Online | Accuracy |
|---|---|---|---|---|---|
| 1 Ghadrdan2022TPEL | 컨버터 출력(AC) 상전류 + 스위칭 상태 → 재구성한 커패시터 전류의 스위칭 주파수 성분; DC-link 전압 리플 | Dissipation factor DF = tanδ = ω·C·ESR (C·ESR 결합 지표) + EoL 기준 제안 | Yes | True Online | 수치 n/s (초록에 오차 수치 없음) |
| 2 Ribeiro2025JAS | PWM 전략과 토폴로지의 상호작용이 만드는 고유 상호변조(intermodulation) 성분; 측정량은 off-the-shelf 3L-NPC 의 기존 센서(구체 n/s) | C + ESR (열화 추적) | n/s | True Online | 수치 n/s |
| 3 Hasegawa2024TIA | 3상 전원 전압, 선로/DC 인덕턴스(모델), 인버터 출력 전력, DC-link 전압 — 전류 센서 없음 | C + ESR | Yes (모델 기반; 상전류×스위칭 상태 방식 아님) | True Online | 수치 n/s |
| 4 Oruklu2025TIE | DC-link 전압 리플의 PSD | C (health indicator) + 예측 불확실성 | No | True Online | 평균 예측 오차 < 2 % (이전 조사 스니펫), 'high accuracy' |
| 7 Min2026TIE | 상·하단 DC-link 커패시터 전압(vC1, vC2); 기준전압 오프셋 주입 | C (상·하단 프로파일 사용; 개별 추정 명시 여부 n/s) | n/s | Quasi-Online | 평균 오차 < 1 % |
| 8 Zhao2023TPEL | DC-link 전압의 자연 발생 대신호 과도(저샘플링) | C + 감쇠계수 α(건전성 지표) | No | True Online(이벤트 구동) | α, C 오차 < 1 % |
| 9 Wechsler2012TIA | 기존 보호/제어용 전압·전류 센서 신호 | C (스니펫: C 감소; ESR 포함 여부 확인 필요) | n/s | True Online | 수치 n/s |
| 10 Baumann2024TPEL | 셧다운 시 DC-link 전압 감쇠(방전 프로파일) | 잔존 C → SoH | No | Quasi-Online(정지 후 측정) | 수치 n/s |

Top 10 밖에서 "상전류 + 스위칭 상태 → 커패시터 전류 재구성" 을 초록에 명시한 저널 논문: Lipnicki & Lewandowski 2017 PED(2L, ESR, True Online), Nguyen/Le/Lee 2015 JPE(드라이브, 회생+주입, ESR 1.2 %), WEVJ 2025 BLDC(3상 전류 재구성 → C), Guan & Zhen(3L NP 전류 재구성, 2단 RLS, 저널 여부 미확인). 출력 전류로 커패시터 전류를 추정하는 PV 논문: Muhammed Ramees & Ahmad 2025/26 TPEL. 모델(정류기 해석)로 전류를 만드는 계열: Hasegawa 2023/2024/2025.

(사실) 이 패턴은 존재하지만 수가 적고, 2023–2025 IEEE Transactions 급에서 2L 인버터에 명시한 것은 Ghadrdan 2022(출력 전류)와 Zhang 2023(T-type)뿐이다. (해석) 따라서 "재구성 전류의 스펙트럼 feature" 는 아직 넓게 열린 영역이다.

---

## 10. True Online Methods (Top 10 중 주입·시퀀스 없음)

| Paper | Topology | Signal | Target | 판단 근거 |
|---|---|---|---|---|
| 1 Ghadrdan2022TPEL | 2-Level back-to-back (AC/DC/AC) VSC | 컨버터 출력(AC) 상전류 + 스위칭 상태 → 재구성한 커패시터 전류의 스위칭 주파수 성분; DC-link 전압 리플 | Dissipation factor DF = tanδ = ω·C·ESR (C·ESR 결합 지표) + EoL 기준 제안 | 주입·시퀀스 없이 정상 운전 중 스위칭 주파수 성분을 이용(초록 기준). |
| 2 Ribeiro2025JAS | 3-Level NPC VSI (계통연계) | PWM 전략과 토폴로지의 상호작용이 만드는 고유 상호변조(intermodulation) 성분; 측정량은 off-the-shelf 3L-NPC 의 기존 센서(구체 n/s) | C + ESR (열화 추적) | 주입 없이 고유 신호를 쓰며 정상 운전 중 관측기로 추정(초록 기준). |
| 3 Hasegawa2024TIA | 6-pulse 다이오드 정류기(AC+DC 인덕터) + 3상 PWM 인버터 | 3상 전원 전압, 선로/DC 인덕턴스(모델), 인버터 출력 전력, DC-link 전압 — 전류 센서 없음 | C + ESR | 정류 리플(6f) 해석 기반, 주입·시퀀스 없음(초록 기준; 명시적 'online' 표현은 n/s). |
| 4 Oruklu2025TIE | 2-Level 3상 AC/DC/AC | DC-link 전압 리플의 PSD | C (health indicator) + 예측 불확실성 | 정상 운전 중 전압 리플 PSD 를 입력으로 사용(초록 기준). |
| 5 Sundararajan2020TPEL | 정류기 전단 3상 인버터 | DC-link 커패시터 전압·전류의 선택 주파수 성분(전류 측정/재구성 여부 n/s) | ESR(열화 지표) + C(열화 지표 겸 온도 민감 파라미터) + 코어/핫스팟 온도 | 주입 없음, 운전 중 리플 성분 사용(초록 기준). |
| 6 Zhang2023TPEL | 3-Level T-type 인버터 | 출력 전류와 그 변화율, 상전류 잔차, NP 전압 잔차(고장진단); DC-link AC 성분(고유 또는 주입) + 재구성 커패시터/입력 전류(CM) | C (초록: capacitance; ESR 언급 없음) | 초록이 'inherent or injected AC component' 둘 다 언급. |
| 8 Zhao2023TPEL | AC/DC 및 DC/DC 컨버터(일반) | DC-link 전압의 자연 발생 대신호 과도(저샘플링) | C + 감쇠계수 α(건전성 지표) | 비침습이나 대신호 과도가 발생할 때만 추정 가능 → 본 채점에서는 '특정 운전조건에서 Online'(12점)으로 보수 분류. |
| 9 Wechsler2012TIA | 항공용 fault-tolerant 드라이브 인버터 | 기존 보호/제어용 전압·전류 센서 신호 | C (스니펫: C 감소; ESR 포함 여부 확인 필요) | 주입·특수 운전 없음, 운전 중 추정(초록 기준). |

구분: Quasi-Online(주입·시퀀스) = Min 2026(오프셋 주입), Zhang 2023(주입 AC 성분 사용 시); 특정 운전조건 = Zhao 2023(대신호 과도); 정지 후 = Baumann 2024. Top 10 밖 True Online 대표: Ahmad 2018 TPEL(단상 2f), Lipnicki 2017, Sundararajan 2018 TIA, Hasegawa 2018/2023/2025, Arya 2017 IET PEL, HIT 2021 TPEL(저자 미확인), DSEM 2025(저널 미확인).

---

## 11. C vs ESR Estimation

### C estimation (가장 많음)
- 신호: DC-link 전압(과도·방전·2f·PSD) ≫ 재구성 전류. 알고리즘: 과도/방전 프로파일 피팅(Zhao 2023, Baumann 2024, Wei 2024, Ghadrdan JESTPE 2022, Meng 2023), RLS(Nguyen 2015, Zhu 2022, Oliszewski 2025), 2f 비(Ahmad 2018), ML(Örüklü 2025, Results in Eng. 2025, Zhao IET 2026).
- 장점: 전압 센서만으로 가능, 온도 의존성이 ESR 보다 작음(해석), 필름 커패시터에도 적용. 단점: 전해 커패시터의 초기 열화는 ESR 이 먼저 변해 C 만으로는 늦게 감지(해석); 과도·방전형은 연속성이 없음.

### ESR estimation
- 신호: 스위칭 주파수(또는 정류 6f) 대역의 커패시터 전류·전압 리플. 알고리즘: 대역 성분 비(Sundararajan 2018/2020, Hasegawa 2018), 재구성 전류 기반(Lipnicki 2017, Nguyen/Le/Lee 2015), 링잉 감쇠(Xiang 2021, 추가 센서), 주입+RLS(Pu 2013).
- 장점: 전해 커패시터 열화에 민감. 단점: 커패시터 전류(측정 또는 재구성) 필요, 온도·주파수 의존(Pu 2013·Sundararajan 2020·Ahmad 2016 이 보정 다룸), 필름 커패시터에는 부적합.

### C + ESR simultaneous
- 확인된 저널: Ribeiro 2025 JAS(NPC, 고유 성분), Hasegawa & Hirose 2024 TIA / Hasegawa 2018·2023(정류기 전단), Sundararajan 2020(Goertzel), Agarwal 2018(야간 주입), Ribeiro 2023 IJEPES·2024 CEE(주입+Wavelet), Plazas-Rosas 2021(EIS), Lee 2008(정지 시), Miao 2020(TMR 센서). (해석) 동시 추정은 "고주파 대역(ESR)과 저주파 대역(C)을 모두 포함한 전류·전압" 이 있어야 하므로, 전류 재구성 또는 다중 주파수 여기가 전제다.
- 지표 결합형: DF(Ghadrdan 2022/2023) — 하나의 지표로 둘을 반영하나 분리 불가.

---

## 12. Application Comparison

| Application | 사용 센서 | 진단 중단/주입 | C/ESR | 가장 실용적(해석) |
|---|---|---|---|---|
| **2-Level 3상 / AC-DC-AC** | vdc, 상전류, 스위칭 상태 | True Online(Ghadrdan 2022, Örüklü 2025, Lipnicki 2017) / 주입(Li 2022) / 시퀀스(Ghadrdan JESTPE 2022) / 과도(Zhao 2023, Dai 2024) | DF·ESR(재구성형), C(전압형) | 재구성 전류 fsw 성분(ESR/DF) + 전압 PSD 또는 과도(C) 의 조합 |
| **3-Level NPC** | vC1, vC2(또는 vdc, vNP), 상전류, 스위칭 상태 | 무주입(Ribeiro 2025) / 주입·오프셋(Ribeiro 2024, Min 2026, Guan & Zhen) | C+ESR(Ribeiro) / C(Min, Guan) | 고유 성분(Ribeiro 2025)이 유일한 True Online; 상·하단 개별은 주입형(Min)만 |
| **T-type** | 상전류, vNP | 고유 또는 주입(Zhang 2023) | C | 고유 고조파 모델 + 재구성 |
| **PV 인버터** | PV V/I, 인덕터 전류, 출력 전류 | True Online 2f(Arya 2017, Ahmad 2018) / MPPT 과도(Ramees 2025) / 야간 주입(Agarwal 2018) / EIS 주입(Plazas 2021) | |Z| 또는 C(2f), C+ESR(주입) | 단상: 2f 비(C); 3상: MPPT 과도(C) 또는 주입(C+ESR) |
| **모터 드라이브(정류기 전단)** | 전원 전압, vdc, 출력 전력(또는 고정자 전류, 스위칭 상태) | True Online(Hasegawa 2023/2024/2025, Sundararajan 2018/2020) / 회생+주입(Nguyen 2015) / 간헐 역충전(Meng 2023) / 정지(Lee 2008) | C+ESR(Hasegawa), ESR(Sundararajan), C(Meng, Zhu) | 전류 센서 없는 정류 리플 해석(Hasegawa) |
| **EV/철도 견인, 항공** | vdc(주차·셧다운 방전), 사전충전 | 정지 후(Wei 2024, Baumann 2024, Oliszewski 2025, Wu 2022) / True Online(Wechsler 2012) | C, SoH | 주차·정지 방전 프로파일(구현 단순, 온도 보상 필요) |
| **UPS / ESS / 풍력** | — | 저널 논문 미발견(UPS 는 학회 1편, 풍력 후보는 열 진단 논문으로 판명) | — | — |

---

## 13. Limitations (문헌 공통 + 본 조사)

1. 운전조건 의존: 리플·고조파·과도 크기는 부하·변조지수·fsw·역률에 따라 변한다. 초록에 다중 조건 검증을 명시한 논문은 Örüklü 2025, Wechsler 2012, Baumann 2024, Zhang 2023, Plazas-Rosas 2021 정도다.
2. 온도: ESR 은 온도에 크게 의존. 보정을 다룬 것은 Pu 2013, Ahmad 2016, Sundararajan 2020(온도 추정), Baumann 2024(모델 보상)뿐.
3. 커패시터 전류: 센서 없이 얻으려면 재구성(스위칭 상태×상전류) 또는 모델(정류 리플) 필요 → 데드타임·ESL·샘플링 동기화가 새 오차원(Ghadrdan 2022 가 fsw·ESL·필터 영향 언급).
4. 필름 커패시터: ESR 작아 리플 전압 신호가 작음 → C 중심(Wechsler 2012, Wei 2024, RG 397930319).
5. 주입형의 전력품질·손실 제약(Li 2022 THD 한도, Ribeiro 2024 전력품질 trade-off).
6. 검증 깊이: 실제 노화 커패시터·현장 데이터는 Baumann 2024, Lee 2008 정도이며, 대부분 모사 노화 또는 방식 n/s.
7. 본 조사 자체: 본문 미열람으로 수식·실험 조건·정확도 비교가 불가; 서지 일부(확인 필요).

---

## 14. Research Gap (문헌 근거)

| # | Gap | 근거 |
|---|---|---|
| G1 | 2L/NPC 에서 "상전류+스위칭 상태 재구성 전류의 스펙트럼 feature" 로 C 와 ESR 을 분리 추정한 True-Online 저널 논문 부족 | Ghadrdan 2022 는 DF(결합), Lipnicki 2017 은 ESR 만, Zhang 2023 은 C 만 |
| G2 | NPC 에서 무주입 + 상·하단 개별 + C·ESR 동시를 모두 만족하는 논문 없음 | Ribeiro 2025(개별 n/s), Min 2026(주입, C) |
| G3 | 다중 운전조건·온도 강건성을 동시에 보고한 True-Online 논문 희소 | 13절 1–2 |
| G4 | 기존 센서 True-Online 데이터 기반 방법은 vdc PSD(Örüklü) 중심; 전류 재구성 스펙트럼 입력 ML 없음 | 9절 |
| G5 | UPS·ESS·풍력 DC-link 전용 저널 논문 부재(본 검색) | 12절 |
| G6 | 실제 노화·현장 데이터 검증 부족 | 13절 6 |

---

## 15. Q1~Q10 Answers

**Q1 가장 실용적인 방법:** 두 축이 실용적이다. (a) DC-link 전압 센서만 쓰는 방법 — 정상 운전 중 리플 PSD(Örüklü 2025) 또는 자연 과도(Zhao 2023), 정지 시 방전(Baumann 2024, Wei 2024). (b) 상전류+스위칭 상태(또는 정류기 모델)로 커패시터 전류를 재구성해 스위칭 대역 ESR/DF 를 얻는 방법(Ghadrdan 2022, Hasegawa & Hirose 2024). 구현 단순성은 (a), 전해 커패시터 조기 감지(ESR)는 (b)가 유리(해석).

**Q2 추가 센서 없이 가능한 방법:** 9절 표. 전압만: Zhao 2023, Örüklü 2025, Baumann 2024, Wei 2024, Ahmad 2018(+제어 전류). 전압+상전류/스위칭 상태: Ghadrdan 2022, Zhang 2023, Lipnicki 2017, Min 2026, Guan & Zhen. 전원 전압+모델: Hasegawa 2023/2024/2025. 고유 성분: Ribeiro 2025.

**Q3 True Online / Quasi-Online 대표:** True Online — Ghadrdan 2022(2L DF), Ribeiro 2025(NPC), Hasegawa & Hirose 2024(드라이브), Örüklü 2025(ML), Wechsler 2012(필름). Quasi-Online — Min 2026(오프셋 주입), Li 2022(주입), Ribeiro 2024(영상분 주입), Meng 2023(간헐 역충전), Ghadrdan JESTPE 2022(스위칭 로직 변경). 이벤트형 — Zhao 2023, Dai 2024, Ramees 2025. 정지형 — Baumann 2024, Wei 2024, Lee 2008.

**Q4 C vs ESR:** 2022–2026 저널 후보 중 C 추정이 ESR 추정보다 약 3배 많다(11절). ESR 은 전해 커패시터·재구성 전류가 있는 경우에 한정된다.

**Q5 2-Level 최신:** 재구성형은 Ghadrdan 2022(DF, True Online); 전압형은 Zhao 2023(과도 grey-box, <1 %, 수상)과 Örüklü 2025(PSD GPR, 다중 조건); 주입형은 Li 2022(THD 한도 내, 슬라이딩 DFT).

**Q6 3-Level NPC 최신:** Ribeiro 2025 JAS(무주입 고유 상호변조, C+ESR, 기존 센서)가 가장 발전된 형태이며, 상·하단 개별 C 는 Min 2026(주입, <1 %), NP 전류 재구성은 Guan & Zhen(저널 미확인). 4편 모두 2024–2026.

**Q7 PV 대표:** 단상은 Ahmad 2018 TPEL(2f, 제어 센서만, True Online)과 Arya 2017 IET PEL(2f 임피던스, 같은 DSP); 3상·무주입 최신은 Muhammed Ramees & Ahmad 2025/26 TPEL(MPPT 과도 + 출력 전류로 커패시터 전류 추정); C+ESR 은 야간 주입(Agarwal 2018) 또는 EIS 주입(Plazas-Rosas 2021).

**Q8 모터 드라이브 대표:** 정류기 전단은 Hasegawa & Hirose 2024 TIA(전류 센서 없이 C+ESR)와 Sundararajan 2018/2020(ESR, 상용 드라이브 구현); 능동형은 Meng & Zhang 2023(간헐 역충전)과 Nguyen & Lee 2015(회생+주입); 정지형은 Lee 2008.

**Q9 운전조건에 가장 강한 방법:** 초록 근거로는 Wechsler 2012(토크·속도 독립 명시), Örüklü 2025(부하·주파수 다중 조건 <2 %), Baumann 2024(온도·사전충전 조건), Zhang 2023(다양한 조건 실험). (해석) 정지·과도형은 운전점과 무관하다는 구조적 장점이 있고, 리플형은 조건 보정이 필수다.

**Q10 향후 가치가 높은 구조:** `상전류 + 스위칭 상태(기존 센서) → 커패시터(또는 NP) 전류 재구성 → 스위칭 대역(ESR)과 저주파 대역(C)의 소수 고조파 빈(Goertzel/SDFT) → 운전조건 정규화(변조지수·부하) + 온도 보정 → C·ESR 동시 추정(모델 기반 또는 조건 증강 ML)`. NPC 에서는 상·하단 전류를 따로 재구성해 개별 진단까지 확장하는 것이 G1–G3 를 동시에 메운다. 보완으로 정지 시 방전(Baumann)을 교차 검증용으로 둔다.

---

## 16. Reading Priority

1위 **Ghadrdan2022TPEL** — 왜: 상전류+스위칭 상태 재구성과 True Online 스위칭 리플 지표의 저널 선례 / 집중: 재구성 수식, fsw 성분 추출, DF·EoL 정의, fsw/ESL/필터 영향 절
2위 **Ribeiro2025JAS** — 왜: NPC 무주입·기존 센서·True Online 의 유일한 저널 선례(경쟁 선행) / 집중: 상호변조 성분의 주파수식과 측정 신호, C/ESR 종속식, 검증 조건, C1/C2 분리 여부
3위 **Hasegawa2024TIA** — 왜: 전류 센서 없이 C+ESR 을 True Online 으로 얻는 최신 드라이브 논문 / 집중: 리플 전류 해석식, ESR/C 분리 대역, 모델 파라미터 민감도, 200 V 실험 조건
4위 **Oruklu2025TIE** — 왜: 기존 센서 + 다중 조건 검증 + 불확실성을 갖춘 AI 기반 On-board 벤치마크 / 집중: PSD 설정, 학습/검증 조건 분할, 오차 분포, 노화 모사 방식
5위 **Sundararajan2020TPEL** — 왜: 경량 고조파 추출(Goertzel)과 온도 보정을 갖춘 ESR+C 방법 / 집중: 선택 빈(주파수), ESR/C 식, 온도 추정·자기보정, 전류 측정 방식
6위 **Zhang2023TPEL** — 왜: 3레벨 고유 고조파 모델과 커패시터 전류 재구성의 저널 선례 / 집중: DC-link 고조파 유도식, 재구성식, RLS 입력, 주입/추가 HW 필요 여부
7위 **Min2026TIE** — 왜: NPC 상·하단 커패시터 C 를 <1 % 로 추정한 경쟁 선행(주입형) / 집중: 오프셋 크기·보상, C 산출식, C1/C2 개별 여부, 실험 조건
8위 **Zhao2023TPEL** — 왜: 전압 센서만으로 C·건전성 지표를 얻는 수상급 물리 모델 / 집중: TECM 식, 과도 검출 조건, 저샘플링 설계, 부하 종류별 결과
9위 **Wechsler2012TIA** — 왜: 필름 DC-link 를 기존 센서로 True Online 감시한 기반 논문(토크·속도 독립) / 집중: 추정 원리, C 지표 정의, 토크·속도 독립 근거, 항공 드라이브 구현
10위 **Baumann2024TPEL** — 왜: 실제 열화·현장 데이터와 온도 보상 SoH 모델을 갖춘 prognostics 대표 / 집중: 온도 보상식, SoH 정의, 현장 데이터 분석, 방전 측정 요건

### 지금 당장 먼저 읽을 3편
- 1위 Ghadrdan2022TPEL: Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor (2022) — 상전류+스위칭 상태 재구성과 True Online 스위칭 리플 지표의 저널 선례
- 2위 Ribeiro2025JAS: Online Estimation of DC-link Capacitor Parameters of Three-Level NPC Converters Using Inherent Signals Analysis (2025) — NPC 무주입·기존 센서·True Online 의 유일한 저널 선례(경쟁 선행)
- 3위 Hasegawa2024TIA: Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor Based on Analysis of a Six-Pulse Diode Rectifier Having AC and DC Inductors (2024) — 전류 센서 없이 C+ESR 을 True Online 으로 얻는 최신 드라이브 논문

### 그 다음 읽을 4편
- 4위 Oruklu2025TIE: Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters (2025) — 기존 센서 + 다중 조건 검증 + 불확실성을 갖춘 AI 기반 On-board 벤치마크
- 5위 Sundararajan2020TPEL: Condition Monitoring of DC-Link Capacitors Using Goertzel Algorithm for Failure Precursor Parameter and Temperature Estimation (2020) — 경량 고조파 추출(Goertzel)과 온도 보정을 갖춘 ESR+C 방법
- 6위 Zhang2023TPEL: A Comprehensive Method for Online Switch Fault Diagnosis and Capacitor Condition Monitoring of Three-Level T-Type Inverters (2023) — 3레벨 고유 고조파 모델과 커패시터 전류 재구성의 저널 선례
- 7위 Min2026TIE: An Online Condition Monitoring Method for DC-Link Capacitors of Three-Level NPC Inverters Based on Charge-Discharge Profile (2026) — NPC 상·하단 커패시터 C 를 <1 % 로 추정한 경쟁 선행(주입형)

### 필요할 때 참고할 3편
- 8위 Zhao2023TPEL: A Transient-Modeling-Based Grey-Box Method for Online Monitoring of DC-Link Capacitors (2023) — 전압 센서만으로 C·건전성 지표를 얻는 수상급 물리 모델
- 9위 Wechsler2012TIA: Condition Monitoring of DC-Link Capacitors in Aerospace Drives (2012) — 필름 DC-link 를 기존 센서로 True Online 감시한 기반 논문(토크·속도 독립)
- 10위 Baumann2024TPEL: Discharge-Based Condition Monitoring for Electrolytic DC-Link Capacitors (2024) — 실제 열화·현장 데이터와 온도 보상 SoH 모델을 갖춘 prognostics 대표

---

## 부록 A. 서지 검증 대기 목록
- (확인 필요) DOI: Hasegawa & Hirose 2024 TIA, Min 2026 TIE(in press; 이전 기록 10.1109/TIE.2026.3672764 미확인), Zhang 2023 TPEL(이전 스니펫 10.1109/TPEL.2023.3262758 재확인), Meng & Zhang TPEL, Wu 2022 TIE 권/쪽(AAU 레코드의 70(1):907–920 은 다른 논문이므로 사용 금지), Baumann 2024 권/호/쪽, Ribeiro 2023 IJEPES 저자·권, Muhammed Ramees 2025/26 권/호, Nguyen/Le/Lee 2015 JPE 호.
- 저널/학회 미확정: Guan & Zhen(Xplore 10149200), DSEM(Xplore 11178083), RG 397930319(OJ-IA accepted), HIT 2021 TPEL 저자.
- 로컬 PC 에서: `pwsh -File harness\tools\Search-Papers.ps1 -Query "<제목>" -Source all` 로 Crossref type(journal-article/proceedings-article)·권·쪽·DOI 확인 후 본 표 갱신.

## 부록 B. 사실 / 해석 / 추론 구분
- 사실: 각 논문 항목 중 초록·스니펫 인용 부분(기본). 해석: "(해석)" 표기. 추론: "(추론)" 표기. 수치는 초록에 있는 것만 기재.
