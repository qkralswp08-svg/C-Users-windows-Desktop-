# 2-Level Inverter DC-Link Capacitor Aging Diagnosis — On-board / Online Top 10 정밀 분석

- 작성일: 2026-10-20
- 목표: 2-Level 3상 인버터에서 측정 가능한(가능하면 기존) 신호로 DC-link 커패시터 노화(C 감소·ESR 증가)를 On-board/Online 으로 진단하는 시스템 설계를 위한 핵심 문헌 10편 정밀 비교.
- 수행: Harness Skill `literature-researcher → bibliographic-verifier → capacitor-aging-expert → paper-analyzer → paper-comparator`. 탐색은 4개 병렬 스카우트(ML/DL 분류·회귀 / 해석적 True-Online / 드라이브·EV·PV 응용 / 상세 수치 채굴)로 수행(웹 검색 160회).
- 파일: `2level_inverter_dc_link_capacitor_onboard_top10.md`(이 문서), `2level_inverter_dc_link_capacitor_onboard_top10.csv`(UTF-8 BOM), `core_papers/2level_top10/01_…10_….md`(논문별 분석).

---

## 1. Executive Summary

- **근거 수준: 전 논문 `Abstract-level only`.** 이 클라우드 환경은 출판사·DOI·Crossref·arXiv·대학 리포지터리 호스트를 DNS/프록시 단계에서 차단해 Top 10 의 본문을 한 편도 열지 못했다(사용자 요청 34절 규칙에 따라 명시). 따라서 사용자가 가장 중요하게 본 **샘플별 C/ESR 값, Radd 값, 클래스별 C/ESR, 데이터셋 크기·분할, DSP/MCU 부품, 샘플링 주파수, 추론 시간**은 10편 중 어느 것도 스니펫에 노출되지 않았고(예외: Liao 2020 의 7500 µF 초기값과 90/80 % 구간, Al-Wesabi 2025 의 오차 수치), 모두 `Not reported / Full text verification required` 로 남겼다. 추측으로 채운 수치는 없다.
- 저널 후보 51편 + 학회·미확정 15편 + Reference only(NPC/T-type/MMC) 5편을 검토해, 사용자 7절의 10개 기준(각 10점, 100점 만점)으로 채점하고 10편을 선정했다.
- **Tier S(3)**: Ghadrdan 2022 TPEL(출력 상전류 → 커패시터 전류 스위칭 성분 재구성 → DF, True Online, 실험), Örüklü & Ağalar 2025 TIE(vdc 리플 PSD → ML 회귀 C, 추가 회로 없음, 실험), Lipnicki & Lewandowski 2017 PED(제목부터 2-Level AC/DC/AC, 추가 센서 없이 DC-link 전류 재구성 → ESR, ABB).
- **Tier A(4)**: Hasegawa & Hirose 2024 TIA(전류 센서 없이 C+ESR, 200 V 실험), Sundararajan 2018 TIA(fsw 성분 ESR, 상용 AC 드라이브 구현 = On-board 실증), Park & Kwak 2023 JEET(3상 DC-link C+ESR 를 FFT 대역 입력 → DNN/CNN/RNN/LSTM 회귀), Machines 2022(전원 전류 + FFT/DWT + 통계 지표 → 학습 기반 AEC 파라미터 추정).
- **Tier B(3)**: Zhao 2023 TPEL(전압 과도 grey-box, <1 %, 수상), Al-Wesabi 2025 Results in Eng.(ML 회귀 6종 + 하이브리드 0.142 %), Liao 2020 MPE(노화 등급 정의 90–100/80–90/<80 %, ER rule).
- 핵심 결론: ① 2-Level 계열에서 True Online + 기존 센서 조합은 "상전류(출력/전원 전류) 기반 재구성·feature"(Ghadrdan, Lipnicki, Machines 2022) 와 "vdc 리플/과도 단독"(Örüklü, Zhao, Al-Wesabi, Liao) 두 흐름이다. ② C+ESR 동시 추정은 Hasegawa(정류 리플 모델)와 Park & Kwak(DL) 뿐이며, 둘 다 '인버터 스위칭 신호' 를 쓰지 않는다. ③ 분류 연구는 소수이고 클래스 정의를 저널 본문 수준에서 확인할 수 있었던 것은 Liao 2020(3 구간)뿐이다. ④ On-board 구현을 초록에서 확인한 것은 Sundararajan 2018(상용 드라이브)과 Hasegawa 계열(후속 소형 MCU) 뿐이며, AI 모델의 DSP/MCU 추론 시연은 저널 Top 10 에 없다.
- 가장 큰 공백(31절): "2-Level 3상 인버터 + 기존 센서(상전류·스위칭 상태·vdc) + 재구성 전류 스펙트럼 feature + C·ESR 동시(회귀) 또는 등급(분류) + 다중 운전조건 + DSP/MCU 실시간 추론" 을 한 논문에서 모두 만족한 저널 논문은 없다.

---

## 2. Search Methodology

| 항목 | 내용 |
|---|---|
| 범위 | 최우선: 2L 3상 VSI, 모터 드라이브, 계통연계, PV, 견인/EV, AFE+인버터. 보조: 단상, 정류기-인버터 드라이브, 일반 VSI/DC-link 컨버터. 제외(Reference only): 3L-NPC, MMC, Flying Capacitor |
| 대상 | DC-link 커패시터 C, ESR, C+ESR, |Z|, DF, SoH, 노화 등급, RUL |
| 기간 | 2022–2026 집중 + 기반 논문(2005–2021) |
| 키워드 | 사용자 6절 27개 조합 × (two-level / three-phase / motor drive / PV / traction / AFE) × (classification / regression / CNN / ESR / capacitance / reconstruction / existing sensor) |
| 출처 | IEEE Xplore, ScienceDirect, Springer, Wiley/IET, MDPI, Hindawi, J-STAGE, KoreaScience, OpenAlex, Semantic Scholar, ResearchGate, 대학 리포지터리(AAU VBN, NTU, Kyutech, CAU ScholarWorks, HIT, Cardiff ORCA, Nottingham, CityU, Sharif) — 모두 검색 색인 스니펫 수준 |
| 검색량 | 웹 검색 160회(4 스카우트 × 40) + 본 세션 보조 검색; 본문·DOI 페이지 접근 0회(차단) |
| 서지 검증 | bibliographic-verifier 규칙: 스니펫에 보인 값만 기록, DOI 는 표시된 것만(MDPI 패턴 추정은 '(패턴)' 표기), 저널/학회 구분은 Xplore 유형·출판사 URL 기준, 미확인은 `(확인 필요)` |
| 수치 규칙 | 노화 샘플·클래스 C/ESR·데이터셋·HW·성능 수치는 초록/스니펫 문구 그대로만; 없는 항목은 `Not reported / Full text verification required` |

단계: 후보 탐색 → 서지 검증 → 2-Level 관련성 screening → On-board/Online screening → Top 10 선정 → (본문 정독: 차단으로 미수행, 초록 수준 분석으로 대체) → aging sample 추출 → 신호/전처리 → 알고리즘 → HW/on-board → 성능 → gap → 보고서.

---

## 3. Candidate Papers

### 3.1 Rank 11–25 (근소 탈락, 저널)
| Rank | Authors/Year | Title | Journal | DOI/ID | Topology | Target | Online | 탈락 사유 |
|---|---|---|---|---|---|---|---|---|
| 11 | Dai, Zhao, Han, Sun, Chen 2024 | A High-Accuracy Capacitor Condition Monitoring Scheme at Low Sample Frequency Based on Improved Current Reconstruction Method | IEEE JESTPE 12(2):2281–2291 | 10.1109/JESTPE.2024.3370616 | AC/DC 컨버터(프로토타입) | C | 이벤트형(부하 변화 과도) | 과도 의존·AC/DC 정류단 중심; 재구성(선형 피팅 전류 적분) 아이디어는 참고 |
| 12 | Nguyen, Le, Lee 2015 | Estimation of ESR in the DC-Link Capacitors of AC Motor Drive Systems with a Front-End Diode Rectifier | J. Power Electron. 15(2):411–418 | (확인 필요) koreascience JAKO201509364589514 | 다이오드 정류기 + IM 드라이브 | ESR (≈1.2 %) | Quasi(회생 모드 + q축 주입) | 고정자 전류+스위칭 상태로 커패시터 전류 재구성 — 재구성 선례이나 주입·회생 조건 필요 |
| 13 | Qie, Zhang, Xiang, Zhao, Jiang, Iu, Fernando 2025 | Generative Physics Informed Machine Learning Method for DC-Link Capacitance Estimation | IEEE TIE 72(5):5461–5471 | (DOI 미표시) | 차량 사전충전 DC-link | C | 이벤트형(pre-charging) | 사전충전 구간 전용; diffusion 증강 + PILSTM 은 소표본 AI 참고 |
| 14 | Amaral, Laadjal, Cardoso 2023 | Advanced Fault-Detection Technique for DC-Link Aluminum Electrolytic Capacitors Based on a Random Forest Classifier | Electronics 12(12):2572 | 10.3390/electronics12122572 | DC-link AEC(토폴로지 NR), Matlab/Simulink | ESR 임계 분류(클래스 수 NR) | 주장 Online(시뮬) | 시뮬레이션 전용·클래스 정의 NR; STLSP+RF 분류 구조는 참고 |
| 15 | (저자 미확인; HIT) 2021 | Online Estimation Method of DC-Link Capacitors for Reduced DC-Link Capacitance IPMSM Drives | IEEE TPEL 36(11):12196–12201 (letter) | (확인 필요) Xplore 9429983 | 저용량 필름 DC-link IPMSM 드라이브 | C (<1 %) | True Online | 저자 미확인(학회판 Zhou, Wang, … Xu); 필름·저용량 특수 구조 |
| 16 | Yamasoto & Hasegawa 2025 | (제목 확인 필요) DC-link 커패시터 ESR/C — 불평형 전원 6-pulse 정류기 + 인버터 | Microelectronics Reliability 173:115873 | 10.1016/j.microrel.2025.115873 | 정류기 + 인버터 200 V 1.5 kW | C + ESR | True Online | Rank 4 의 후속(불평형 ≈5 %, 소형 MCU) — 동일 계열이라 별도 선정 안 함 |
| 17 | Zhu, Zhao, Song, Zhou, Sun 2022 | Online condition monitoring for DC-link capacitors of motor drives under noise interference | J. Power Electron. 22(7):1142–1153 | 10.1007/s43236-022-00426-w | 모터 드라이브 | C | 이벤트형(회생 모드) | 회생 구간 전용; 데드타임·펄스 드롭 영향·이상치 제거는 재구성 오차 분석에 참고 |
| 18 | Meng & Zhang 2022/23 | An Online DC-Link Capacitance Estimation Method for Motor Drive Systems Based on an Intermittent Reverse-Charging Control Strategy | IEEE TPEL (권/쪽 확인 필요) | (확인 필요) Xplore 9907882 | 모터 드라이브 | C | Quasi(간헐 역충전) | 능동 제어 시퀀스 필요; 세부 수치 전부 NR |
| 19 | Wei et al. 2024 | An Improved Discharge Profile-Based DC-Link Capacitance Estimation for Traction Inverter in Electric Vehicle Applications | IEEE TPEL 39(7):8696–8708 | (확인 필요) Xplore 10487784 | EV 견인 인버터(축소+실규모) | C (<1 %) | 정지 후(주차 방전) | 운전 중 불가(저자 명시) |
| 20 | Abo-Khalil, Alyami, Alhejji, Awan 2019 | Real-Time Reliability Monitoring of DC-Link Capacitors in Back-to-Back Converters | Energies 12(12):2369 | 10.3390/en12122369 | 3상 B2B | C (PSO-SVR) | Online(주장) | 커패시터 전류 '측정 또는 유도' — 센서 조건 불명; 수치 NR |
| 21 | Ghadrdan, Abdi, Peyghami, Mokhtari, Blaabjerg 2023 | (제목 확인 필요) 대신호 과도 기반 DC-link 커패시터 CM | IEEE JESTPE 11(1):1132–1142 | 10.1109/JESTPE.2022.3163012 | B2B 컨버터 | C (<1 % vs LCR) | Quasi(스위칭 로직 일시 변경) | 진단용 스위칭 변경 필요 |
| 22 | Xiang et al. 2021 | Online ESR Monitoring of DC-Link Capacitor in Voltage-Source-Converter Using Damping Characteristic of Switching Ringings | IEEE TPEL 36(7):7429–7441 | 10.1109/TPEL.2020.3042218 | VSC | ESR (mΩ급) | True Online | 비접촉 고주파 센서 추가 → 기존 센서 조건 위배 |
| 23 | Baumann, Murillo Garcia, Papastergiou, Peftitsis 2024 | Discharge-based condition monitoring for electrolytic DC-link capacitors | IEEE TPEL (권/쪽 확인 필요) | 10.1109/TPEL.2024.3442077 | 200 kW 컨버터(CERN), 현장 153대 | C/SoH(온도 보상) | 정지 후(셧다운 방전) | 2L 드라이브 특화 아님; 현장 데이터·온도 보상은 prognostics 참고 |
| 24 | Park, Kim, Kwak 2022 | Deep learning-based estimation technique for capacitance and ESR of input capacitors in single-phase DC/AC converters | J. Power Electron. 22:513–521 | 10.1007/s43236-021-00366-x | 단상 DC/AC | C + ESR (DNN) | True Online(추정) | 단상(보조 범위); Rank 6 의 선행 |
| 25 | Sundararajan et al. 2020 | Condition Monitoring of DC-Link Capacitors Using Goertzel Algorithm for Failure Precursor Parameter and Temperature Estimation | IEEE TPEL 35(6):6386–6396 | 10.1109/TPEL.2019.2951859 | 정류기 급전 3상 인버터(검증: T-type 3L 프로토타입) | ESR + C + 온도 | True Online | Rank 5 의 후속; 검증 토폴로지가 3L |

### 3.2 그 외 검토한 저널 후보
| Authors/Year | Title/내용 | Journal | DOI/ID | Topology | Target | Online | Screening 메모 |
|---|---|---|---|---|---|---|---|
| Electronics 2025 (저자 NR) | 재구성 커패시터 전류로 C·ESR 식별 | Electronics 14(23):4671 | (확인 필요) | NR | C ≤3 %, ESR ≤2 % | NR | 토폴로지·저자 미확인 → 보류 |
| (저자 NR) 2023 | Wavelet-based estimation … dc-link capacitors of distributed energy resources | IJEPES 2023, PII S0142061523001989 | (확인 필요) | 3상 PV 부스트 + VSC | ESR + C | Quasi(간헐 비특성 주파수 주입) | 주입형 |
| Processes 2025 (저자 NR) | ESR 추정 보상(전기추진선 드라이브) | Processes 13(2):291 | 10.3390/pr13020291 | 선박 추진 드라이브 | ESR (BPF + 변조지수·PWM LUT 보상) | True Online(추정) | 운전점 보상 아이디어 참고; 세부 NR |
| Zhao, Qie, Zhang, Iu, Fernando, Xiang 2026 | A Highly Accurate Generative Learning-Based DC-Link Capacitance Estimation Approach for Electrified Railway Traction Systems | IET Power Electron. | 10.1049/pel2.70151 | 철도 견인 | C (VAE + LSTM) | NR | 운전 영역 불명; 소표본 증강 참고 |
| Wu et al. 2022 | A Capacitance Estimation Method for DC-Link Capacitors Based on Pre-Charging Model and Noise Evaluation | IEEE TIE | 10.1109/TIE.2022.3217587 | 사전충전 회로(철도/EV) | C | 이벤트형(pre-charge) | 사전충전 전용 |
| Wu et al. 2025 | (철도) maximum likelihood + variable convergence factor 기반 C 추정 | IEEE TIE | 10.1109/TIE.2024.3525135 | 철도 견인 | C | NR | ML = maximum likelihood(기계학습 아님) |
| Qian, Gong, Xiao, Lin, Li 2025 | (BLDC 드라이브 DC-link C → 수명) | World Electr. Veh. J. 16(6):330 | 10.3390/wevj16060330 | BLDC 드라이브 | C | 이벤트형(직렬 스위치 구간) | 직렬 스위치 회로 추가 → 추가 하드웨어 |
| Energies 2022 (저자 NR) | Investigation on C and ESR Estimation of DC-Link Capacitor in Maglev Choppers Using ANN | Energies 15(22):8564 | (패턴) 10.3390/en15228564 | 자기부상 초퍼(DC-DC) | C + ESR (ANN; ESR <1 %, C 과적합) | NR | DC-DC → 범위 밖 |
| Abo-Khalil et al. 2020 | (B2B PWM 컨버터 전해 커패시터 온라인 고장 검출, OPSO-SVR) | Sustainability 12(9):3719 | (패턴) 10.3390/su12093719 | B2B PWM | C | Online(주장) | 제목·수치 NR |
| Rezaei et al. 2022 | Adaptation of a Real-Time Deep Learning Approach With an Analog Fault Detection Technique for Reliability Forecasting of Capacitor Banks Used in Mobile Vehicles | IEEE Access 10:132271–132287 | 10.1109/ACCESS.2022.3228916 | EV 커패시터 뱅크 | RUL/신뢰도 | NR | 신뢰도 예측 중심 → 범위 밖 |
| Rojas-Dueñas et al. 2021 | CNN-LSTM-Based Prognostics of Bidirectional Converters for Electric Vehicles' Machine | Sensors 21(21):7079 | (패턴) 10.3390/s21217079 | 양방향 DC-DC | C, ESR 예측 → RUL | NR | DC-DC·prognostics → 범위 밖 |
| Lee, Kim, Yoon, Lee, Yoo 2008 | Condition Monitoring of DC-Link Electrolytic Capacitors in Adjustable-Speed Drives | IEEE TIA 44(5):1606–1613 | 10.1109/TIA.2008.2002220 | ASD, 250 W PMSM | ESR + C (가속 열화 커패시터) | 정지 시(모터 정지) | 기반 논문; 정지 조건 |
| Nguyen & Lee 2015 | (회생 모드 고정자 주입 RLS C 추정) | IEEE TPEL 30(3):1126–1130 (letter) | 10.1109/TPEL.2014.2339374 | IM 드라이브 | C (<1 %) | Quasi(회생 + 주입) | 주입형 |
| Abo-Khalil & Lee 2008 | (DC-link 전압 주입 + SVR C 추정) | IEEE TIA 44(5):1631–1637 | (확인 필요) | PWM 컨버터 | C (<0.15 %) | Quasi(전압 주입) | 주입형 기반 |
| Pu, Nguyen, Lee, Lee, Kim 2013 | (입력측 AC 전류 주입 + RLS + 온도 센싱 ESR) | IEEE TIE 60(9):4118–4127 | (확인 필요) | PWM 컨버터 | ESR (온도 보정) | Quasi(주입) | 온도 보정 회로 추가 |
| Abo-Khalil 2012 | (전류 주입 + BPF + SVR C 추정) | IET Power Electron. 5(1):53–58 | (확인 필요) | PWM 컨버터 | C (<0.146 %) | Quasi(주입) | 주입형 |
| Wechsler, Mecrow, Atkinson, Bennett, Benarous 2012 | Condition Monitoring of DC-Link Capacitors in Aerospace Drives | IEEE TIA 48(6):1866–1874 | 10.1109/TIA.2012.2222333 | 항공 드라이브(필름) | C(필름) | True Online | 필름·항공 특수; 알고리즘 NR |
| Soliman, Wang, Gadalla, Blaabjerg 2015 | Artificial Neural Network Algorithm for Condition Monitoring of DC-link Capacitors Based on Capacitance Estimation | J. Renew. Energy Sustain. Dev. 1(2):294–299 | (확인 필요) | B2B | C (ANN, DSP 개념증명) | True Online | 2019 이전 배경; DSP 구현 언급 |
| Ahmad, Kumar, Arya, Anand 2018 | Non-invasive Technique for DC-link Capacitance Estimation in Single Phase Inverters | IEEE TPEL 33(5):3693–3696 | (확인 필요) | 단상 | C | True Online | 단상(보조) |
| Arya, Ahmad, Agarwal, Anand 2017 | Capacitor impedance estimation utilizing dc-link voltage oscillations in single phase inverter | IET Power Electron. 10(9):1046–1053 | 10.1049/iet-pel.2016.0603 | 단상 PV | /Z/ (2f) | True Online | 단상(보조) |
| Agarwal, Ahmad, Anand 2018 | Quasi-Online Technique for Health Monitoring of Capacitor in Single Phase Solar Inverter | IEEE TPEL 33(6):5283–5291 | (확인 필요) | 단상 PV | C + ESR | Quasi(주입) | 단상·주입 |
| Plazas-Rosas et al. 2021 | (단상 PV EIS 기반 ESR·C) | Energies 14(20):6754 | 10.3390/en14206754 | 단상 PV | C + ESR (<1 %) | Quasi(EIS 주입) | 단상·주입 |
| Hasegawa, Kubo, Hirose 2023 | Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor in a PWM Inverter with a Six-Pulse Diode Rectifier | IEEJ J. Ind. Appl. 12(3) | (확인 필요) | 정류기(DC 인덕터) + 인버터 | C + ESR | True Online | Rank 4 의 선행 |
| Hasegawa, Nishizawa, Omura 2018 | ESR and capacitance monitoring of a dc-link capacitor used in a three-phase PWM inverter with a front-end diode rectifier | Microelectron. Reliab. 88–90:433–437 | (확인 필요) PII S0026271418305651 | 정류기 + 인버터 | C + ESR | True Online | 기반(평가 회로 사용 가능성) |
| Zhao, Davari, Lu, Wang, Blaabjerg 2021 | An Overview of Condition Monitoring Techniques for Capacitors in DC-Link Applications | IEEE TPEL 36(4):3692–3716 | 10.1109/TPEL.2020.3023469 | 리뷰 | — | — | 리뷰(참고문헌 확장용) |
| Li, Chen, Cong, Dai, Qiu, Liu 2022 | Online Condition Monitoring of DC-Link Capacitor for AC/DC/AC PWM Converter | IEEE TPEL 37(1):865–878 | 10.1109/TPEL.2021.3092429 (이전 조사 스니펫; 이번 재검색에서 미검출 — 서지 재확인 필요) | 2L AC/DC/AC PWM 컨버터 | C/ESR (주입, THD 한도) | Quasi(주입) | 주입형; 서지 재확인 전 보류 |

### 3.3 학회·학위논문·venue 미확정(보조)
| Authors/Year | Title | Venue/ID | 핵심 사실(스니펫) |
|---|---|---|---|
| Seferian, Bazzi, Hajj 2020 | Condition Monitoring of DC-link Capacitors in Grid-tied Solar Inverters Using Data-Driven Techniques | IEEE ECCE 2020, Xplore 9235764 | 단상 PV 시뮬; 3 클래스(healthy / half-degraded / fully degraded); 99 %; 저가 MCU 테스트; 클래스별 C NR |
| (저자 NR) 2024 | Capacitance and ESR Estimation of DC-link Capacitors in AC Machine Drives Based on Hybrid CNN-Attention Model | IPEMC 2024, Xplore 10567930 | 정류기 전단 3상 PWM 인버터; 커패시터 전압만으로 C+ESR; 오차 <1 %; 부하·속도·전압 변화 |
| Nakirimoto, Andrade, Flesch 2023 | Capacitance Estimation Algorithm … Using ANN in Front-End Diode Rectifier Three-Phase Motor Drive Systems | SBAI-SBSE 2023 | ANN, 시간영역 파라미터, 커패시터 지그로 학습·노화 샘플로 평가, 오차 <2.4 %(여러 운전조건), 소프트웨어만 |
| Rajendran, Jena, Diaz, Kirthika Devi 2022 | Machine learning based condition monitoring of a DC-link capacitor in a Back-to-Back converter | IEEE ICA-ACCA 2022, Xplore 10006052 | vdc wavelet 특징; KNN/SVM/NB; SVM 최선; 클래스 수 NR |
| Chaiyakhot et al. 2022 | Real-Time Estimation of ESR and Capacitance in the DC-Link Capacitors of AC Machine Drives | ICEMS 2022, Xplore 9983087 | ½ hp IM, SVPWM, RLS, vdc + 출력 전류, DSP(부품 NR), 운전 중 |
| Dang et al. 2023 | Metalized Polymer-Film Capacitors Health Estimation for Three-Phase DC to AC Converters with Artificial Intelligences | ICBIR 2023 | 필름, DWT 특징(커패시터 전류), 99.85 % |
| Raqib et al. 2021 | Comparison of Frequency Transform Methods for Condition Monitoring of a DC-Link Capacitor | IET conf., DOI 10.1049/icp.2021.1169 | FFT/STFT/CWT 임피던스; CWT 최선; Siemens G120C + 가속 노화 커패시터(학위논문 eprints 69277) |
| Soliman et al. 2017 | ANN-based DC-link capacitance estimation in three-phase front-end diode bridge AC/DC/AC converter | IFEEC/ECCE Asia 2017 | 단상 출력 전류 + vdc 리플; 학습 데이터 종류·양 영향 분석 |
| (저자·venue NR) | Condition Monitoring of DC-Link Capacitors Using Time–Frequency Analysis and Machine Learning Classification of Conducted EMI | Xplore 9694516 (저널/학회 미확인) | DC 버스 전도 EMI(15–43 MHz) CWT 이미지 → SVM; 5 단계; 최대 100 %; 추가 EMI 측정 필요 |
| (서지 NR) | Goertzel ESR/C + logistic regression (normal / failure) | RG 337071972 | 서지 미확인 |
| (서지 NR) | HTM 기반 DC-link 커패시터 노화 조기 검출 | listing only | 시뮬; DF·C·ESR 열화 모델; 정확도 >95 %, 오경보 <4 % |
| Sahani, Sundararajan, Siddique, Panda 2024 | Machine Learning-Based Condition Monitoring of DC-Link Capacitors in Drive Inverters Using Case Temperature | 2024 conf., Xplore 10667455 | 케이스 온도 기반 ML |
| AAU (저자 NR) 2024 | Parameter Estimation of Power Electronic Converters With Physics Informed Machine Learning | IPEMC 2024 | 3상 인버터 DC-link C + AC 인덕턴스; 추가 HW 없음; 소표본 |
| (저자 NR) 2021 | Online Condition Monitoring of DC-Link Capacitor for AC/DC/AC PWM Converter | Xplore 9465734 | 중성점 전류 주입 + 스위칭 상태·3상 전류 재구성(2L AC/DC/AC) |
| Park, Hwang, Jeon, Lim, Lee 2025 | Online Capacitance Estimation for the DC Link Capacitor of PWM Inverter | Xplore 11184531 (venue 미확인; IEEE Access 2025 DOI 10.1109/ACCESS.2025.3615584 와 동일 여부 미확인) | SVPWM, 데드타임·샘플링 시간 포함 커패시터 전류식, 온라인+오프라인, EV 견인 |

### 3.4 Reference only — 3-Level NPC / T-type / MMC (핵심 목록 제외)
| Authors/Year | Title | Journal | DOI | 방법론적 의의 |
|---|---|---|---|---|
| Ribeiro, de Sousa, Oliveira, Lima, Han 2025 | Online Estimation of DC-link Capacitor Parameters of Three-Level NPC Converters Using Inherent Signals Analysis | IEEE/CAA J. Autom. Sinica 12(7):1434–1444 | 10.1109/JAS.2025.125159 | 3L-NPC; 고유 상호변조 성분 + rnSDFT + FF-RLS; C+ESR; 기존 센서; True Online — 무주입 고유 성분 추정의 방법론 선례 |
| Min, Choi, Blaabjerg 2026 | An Online Condition Monitoring Method for DC-Link Capacitors of Three-Level NPC Inverters Based on Charge-Discharge Profile | IEEE TIE (in press; 권/쪽/DOI 미확인) | (확인 필요) | 3L-NPC; 오프셋 주입 충방전 프로파일; 상·하단 C 개별; <1 % |
| Ribeiro, Alves, de Sousa, Oliveira 2024 | Online condition monitoring for DC-link capacitors of three-level NPC converters using noninvasive signal injection | Comput. Electr. Eng. 119:109577 | 10.1016/j.compeleceng.2024.109577 | 3L-NPC; 영상분 구형파 주입 + Wavelet; ESR·C; <2 % |
| Zhang, He, Wang, Chen 2023 | A Comprehensive Method for Online Switch Fault Diagnosis and Capacitor Condition Monitoring of Three-Level T-Type Inverters | IEEE TPEL 38(8):10183–10195 | 10.1109/TPEL.2023.3262758 (재확인 필요) | T-type 3L; 고유 DC-link 고조파 모델 + 커패시터 전류 재구성 + RLS |
| Deng et al. 2025 | Online evaluation method for MMC submodule capacitor aging based on CapAgingNet | Global Energy Interconnection 8(3):420–432 | (확인 필요) | MMC; 스위칭 상태 시퀀스 → DL 노화 등급 분류(Top-1 95.32 %); 시뮬 전용 |

탐색에서 확인되지 않은 것(negative findings): Li et al. 2022 TPEL 37(1):865–878(이번 재검색 미검출), DSEM 드라이브(Xplore 11178083), Muhammed Ramees & Ahmad(Xplore 11146599), IEEE TTE 2022–2026 DC-link CM 저널 논문(0건), 서보 특화 논문(0건), transfer learning / spectrogram→2D-CNN / 경량 NN on MCU 저널 논문(0건).

---

## 4. Screening Criteria

사용자 7절의 10개 기준을 각 10점으로 채점(총 100). Tier 는 총점에 "2-Level 3상 + 기존 센서 + True Online 의 직접성(S)", "설계에 바로 쓰는 방법론(A)", "특정 요소(물리 모델·AI 벤치마크·라벨 정의)(B)" 를 더해 결정.

| 기준 | 내용 | 10점 | 5점 | 0–2점 |
|---|---|---|---|---|
| c1 | 2-Level 3상 inverter 인가 | 2L 3상 명시 | 레벨 미명시(2L 추정)·정류기 전단 | 토폴로지 NR·DC-DC |
| c2 | DC-link capacitor aging 을 직접 대상 | DC-link 노화 직접 | 간접(수명·신뢰도) | 다른 대상 |
| c3 | 실제 inverter 실험 | 실제 인버터·실제/가속 노화 | 실험은 있으나 노화 방식 NR | 시뮬 전용 |
| c4 | On-board / True Online 가능 | True Online | Quasi/이벤트형 | 정지·오프라인 |
| c5 | 기존 inverter sensor 활용 | 기존 센서만 명시 | Partially/NR | 추가 센서 필요 |
| c6 | C/ESR 추정 또는 aging state 분류 | C+ESR | C 또는 ESR | 결합 지표·등급 |
| c7 | 구체적 aging dataset/sample 존재 | 샘플 표 공개 | 구간만 | NR |
| c8 | 사용 신호·signal processing 명확 | 신호·전처리 명확 | 일부 | NR |
| c9 | 정량 성능 제시 | 수치 제시 | 정성 | NR |
| c10 | 재현 가능성 | Easy | Moderate | Difficult |

---

## 5. Final Top 10

| Rank | Title | First author | Year | Journal | DOI | Score | Relevance | Evidence |
|---|---|---|---|---|---|---|---|---|
| 1 | Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor | M. Ghadrdan | 2022 | IEEE Transactions on Power Electronics | 10.1109/TPEL.2022.3153842 | 73 | Very High | Abstract-level only |
| 2 | Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters | Kerim Örüklü | 2025 (온라인 2024; 출처에 따라 2024/2025 표기 상이) | IEEE Transactions on Industrial Electronics | 10.1109/TIE.2024.3454814 (검색 결과에 DOI 문자열이 직접 표시되지 않음 — 확인 필요) | 77 | Very High | Abstract-level only |
| 3 | DC Link Condition Monitoring Method for Two-Level AC/DC/AC Converters | P. Lipnicki | 2017 | Power Electronics and Drives | 10.5277/PED170107 | 72 | Very High | Abstract-level only |
| 4 | Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor Based on Analysis of a Six-Pulse Diode Rectifier Having AC and DC Inductors | K. Hasegawa | 2024 | IEEE Transactions on Industry Applications | (확인 필요) — Kyutech 교원 목록·리포지터리에서 권/호/쪽만 확인, IEEE 페이지 미열람 | 76 | High | Abstract-level only |
| 5 | Online Condition Monitoring System for DC-Link Capacitor in Industrial Power Converters | P. Sundararajan et al. (전체 저자 목록 확인 필요; NTU/Rolls-Royce@NTU 그룹) | 2018 | IEEE Transactions on Industry Applications | 10.1109/TIA.2018.2845889 | 71 | High | Abstract-level only |
| 6 | DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs | Hye-Jin Park | 2023 | Journal of Electrical Engineering & Technology | 10.1007/s42835-023-01424-z | 66 | Very High | Abstract-level only |
| 7 | DC-Link Electrolytic Capacitors Monitoring Techniques Based on Advanced Learning Intelligence Techniques for Three-Phase Inverters | (확인 필요) 한 탐색 보고는 'Dang | 2022 | Machines | 10.3390/machines10121174 (MDPI 관례 패턴 — 직접 확인 안 됨) | 70 | High | Abstract-level only |
| 8 | A Transient-Modeling-Based Grey-Box Method for Online Monitoring of DC-Link Capacitors (제목 표기 VBN 레코드 기준 — 하이픈 등 정확 표기 확인 필요) | (S.) Zhao | 2023 | IEEE Transactions on Power Electronics | 10.1109/TPEL.2023.3308115 | 73 | Medium | Abstract-level only |
| 9 | Capacitance estimation algorithm based on DC-link voltage ripples using hybrid machine learning techniques in power electronics converters | Ibrahim AL-Wesabi | 2025 | Results in Engineering | (확인 필요) PII S2590123025022881 | 70 | Medium | Abstract-level only |
| 10 | Fault Diagnosis of Capacitance Aging in DC Link Capacitors of Voltage Source Inverters Using Evidence Reasoning Rule | Linhao Liao | 2020 | Mathematical Problems in Engineering | 10.1155/2020/5724019 | 62 | Medium | Abstract-level only |

### 5.1 최종 Top 10 비교표 (요청 항목 [27])

| Rank | Paper | Year | Topology | Task | Classes/Output | Aging Method | C Values | ESR Values | Signal | Preprocessing | Method | Online | On-board HW | Performance | Relevance |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ghadrdan 2022 TPEL | 2022 | Back-to-back (AC/DC/AC) 전압형 컨버터 | Regression-type indicator (DF) | DF (무차원) | NR | Not reported / Full text verification required | Not reported / Full text verification required | 컨버터 출력(AC) 상전류 → 커패시터 전류의 스위칭 주파수 성분 재구성; DC-link 전압(리플) | 스위칭 주파수 성분 추출 | Analytical: 재구성 전류·전압 리플의 fsw 성분으로 DF 계산 → EoL 임계 비교 | True Online | Not reported / Full text verification required | 수치 NR ('acceptable accuracy' 만 초록에 있음) | Very High |
| 2 | Örüklü & Ağalar 2025 TIE | 2025 (온라인 2024; 출처에 따라 2024/2025 표기 상이) | AC/DC/AC 컨버터(정류단 + 인버터) 실험실 프로토타입 | Regression (C) | C (µF 또는 % — 단위 NR) | NR | Not reported / Full text verification required | Not reported / Full text verification required | DC-link 전압 리플 (PSD 입력) | PSD | ML 기반 회귀 — 알고리즘명 초록 미표시 | True Online | Not reported / Full text verification required | 'high accuracy' (수치 NR). '<2 % 평균 예측 오차' 는 후속 논문 귀속 가능성 → 미채택. | Very High |
| 3 | Lipnicki & Lewandowski 2017 PED | 2017 | 2-Level AC/DC/AC 컨버터(제목에 명시) | Regression (ESR) | ESR (Ω 또는 상대값 — NR) | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | DC-link 전압 측정 + DC-link 전류 재구성(초록) | Not reported / Full text verification required  | Analytical: vdc + 재구성 DC-link 전류 → ESR 추정(세부 추정기 NR) | True Online | Not reported / Full text verification required | Not reported / Full text verification required | Very High |
| 4 | Hasegawa & Hirose 2024 TIA | 2024 | 6-pulse 다이오드 정류기(AC 라인 인덕터 + DC 인덕터) + 3상 PWM 인버터 — 정류기-인버터 드라이브(보조 범위; 인버터부는 3상 PWM 인버터 = 2L 로 추정) | Regression (C+ESR) | C, ESR (단위 NR) | NR | Not reported / Full text verification required | Not reported / Full text verification required | 3상 AC 전원 전압, AC 라인 인덕터·DC 인덕터 값(파라미터), 인버터 출력 전력 → 커패시터 전류 계산; DC-link | 정류 리플 | Analytical: 6-pulse 정류기 리플 전류 모델 → 커패시터 전류 계산 → 리플 전압과의 관계로 ESR·C 산출 | True Online | MCU: Leafony 소형 MCU (학회판/후속 논문; 본 논문 귀속 NR) | Not reported / Full text verification required (초록은 '변화를 관측' 으로만 기술) | High |
| 5 | Sundararajan 2018 TIA | 2018 | 전단 정류기 급전 3상 인버터(front-end rectifier-fed inverter) | Regression (ESR) | ESR (Ω — NR) | NR | Not reported / Full text verification required | Not reported / Full text verification required | DC-link 전압과 DC-link 전류의 스위칭 주파수 성분(초록) | 대역통과 필터로 스위칭 주파수 성분 추출 | Analytical: fsw 대역 /ΔV/ΔI/ 기반 ESR 추정; 한계 fsw 이하에서 대안 해법(초록) | True Online | Yes | 'estimation error is very low' (수치 NR) | High |
| 6 | Park & Kwak 2023 JEET | 2023 | 3상 DC/AC 컨버터(입력 커패시터 = DC-link) | Regression (C+ESR) | C, ESR (단위 NR) | NR | Not reported / Full text verification required | Not reported / Full text verification required | 주파수 성분(저주파 대역 → C, 중주파 대역 → ESR; 초록) | FFT 로 주파수 성분/대역 추출 | Deep learning: DNN, CNN, Simple RNN, LSTM 4종 비교 | True Online | Not reported / Full text verification required | 정성(모델 간 우열)만 초록에 있음; MAE/RMSE NR | Very High |
| 7 | Machines 2022 (3상 AEC) | 2022 | 3상 인버터(2L 추정; 레벨 수 미명시) | Regression (C+ESR 추정; 분류 여부 NR) | C, ESR (단위 NR) | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | 전원(source) 전류(핵심 입력; 초록) | FFT + 저역/고역 통과 필터 | 'advanced learning intelligence techniques' (모델명 NR — ANN 계열 추정, 확인 필요 | True Online | Not reported / Full text verification required | '99.9 % accuracy' (정의·대상 NR) | High |
| 8 | Zhao 2023 TPEL (grey-box) | 2023 | 일반 DC-link(토폴로지 비의존) | Regression (C via damping factor α) | α, C | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | DC-link 전압 과도(대신호 과도) — '극히 낮은 샘플링 주파수' 로 충분(초록) | 과도 구간 분리·피팅 | Grey-box: 과도 등가회로 모델(TECM) + 파라미터 피팅 | Quasi-Online | Not reported / Full text verification required | α·C 오차 <1 % (실험, 초록) | Medium |
| 9 | Al-Wesabi 2025 Results in Eng. | 2025 | 전력전자 컨버터 일반(풍력 터빈 컨버터 맥락 언급) | Regression (C) | C (µF) | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | DC-link 전압 리플; '컨버터의 접근 가능한 입·출력 단자 데이터' 만 사용(초록) | Not reported / Full text verification required | ML 회귀 비교: RF, KNN, ANN, GB, DT, LR (+BR) → 하이브리드 ANN-GB-LR 제안 | True Online | Not reported / Full text verification required | 평균 C 오차 0.142 % (하이브리드); 비교 DT 0.624 / GB 0.586 / BR 0.182 / KNN 0.322 | Medium |
| 10 | Liao 2020 MPE (ER rule) | 2020 | 전압형 인버터(VSI) 시뮬레이션 | Classification (3 ranges: normal / incipient fault / failed) — 노화 등급 판정 | 3 ranges: Normal / Incipient fault / Failed (no longer incipient) | Simulation | 초기값(7500 µF)의 90–100 % (µF 수치 NR); 초기값의 80–90 % (µF 수치 NR); 초기값의 <80 % (µF 수치 NR) | Not reported / Full text verification required; Not reported / Full text verification required; Not reported / Full text verification required | DC-link 전압 특징(진단 증거) | Not reported / Full text verification required | Evidence Reasoning(ER) rule 융합(증거 가중치 조정 가능) vs BP 신경망 비교 | Quasi-Online | No | BP-NN 대비 우수(수치 NR) | Medium |

Tier 메모: Hasegawa & Hirose 2024(76점)는 총점 2위이나 정류기-인버터(보조 범위)라 A, Lipnicki 2017(72점)은 실험·성능이 미확인이라 점수는 낮지만 '2-Level AC/DC/AC + 재구성 + 기존 센서' 가 제목·초록에서 확정되어 S 로 두었다. Liao 2020 은 시뮬 전용이지만 클래스 정의를 제공하는 유일한 후보라 B 에 포함했다.

---

## 6. Tier S / A / B

### Tier S — 반드시 먼저 읽을 3편
| Rank | Title | First author | Year | Journal | DOI | Score | Relevance | Evidence |
|---|---|---|---|---|---|---|---|---|
| 1 | Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor | M. Ghadrdan | 2022 | IEEE Transactions on Power Electronics | 10.1109/TPEL.2022.3153842 | 73 | Very High | Abstract-level only |
| 2 | Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters | Kerim Örüklü | 2025 (온라인 2024; 출처에 따라 2024/2025 표기 상이) | IEEE Transactions on Industrial Electronics | 10.1109/TIE.2024.3454814 (검색 결과에 DOI 문자열이 직접 표시되지 않음 — 확인 필요) | 77 | Very High | Abstract-level only |
| 3 | DC Link Condition Monitoring Method for Two-Level AC/DC/AC Converters | P. Lipnicki | 2017 | Power Electronics and Drives | 10.5277/PED170107 | 72 | Very High | Abstract-level only |

### Tier A — 그 다음 읽을 4편
| Rank | Title | First author | Year | Journal | DOI | Score | Relevance | Evidence |
|---|---|---|---|---|---|---|---|---|
| 4 | Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor Based on Analysis of a Six-Pulse Diode Rectifier Having AC and DC Inductors | K. Hasegawa | 2024 | IEEE Transactions on Industry Applications | (확인 필요) — Kyutech 교원 목록·리포지터리에서 권/호/쪽만 확인, IEEE 페이지 미열람 | 76 | High | Abstract-level only |
| 5 | Online Condition Monitoring System for DC-Link Capacitor in Industrial Power Converters | P. Sundararajan et al. (전체 저자 목록 확인 필요; NTU/Rolls-Royce@NTU 그룹) | 2018 | IEEE Transactions on Industry Applications | 10.1109/TIA.2018.2845889 | 71 | High | Abstract-level only |
| 6 | DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs | Hye-Jin Park | 2023 | Journal of Electrical Engineering & Technology | 10.1007/s42835-023-01424-z | 66 | Very High | Abstract-level only |
| 7 | DC-Link Electrolytic Capacitors Monitoring Techniques Based on Advanced Learning Intelligence Techniques for Three-Phase Inverters | (확인 필요) 한 탐색 보고는 'Dang | 2022 | Machines | 10.3390/machines10121174 (MDPI 관례 패턴 — 직접 확인 안 됨) | 70 | High | Abstract-level only |

### Tier B — 참고할 3편
| Rank | Title | First author | Year | Journal | DOI | Score | Relevance | Evidence |
|---|---|---|---|---|---|---|---|---|
| 8 | A Transient-Modeling-Based Grey-Box Method for Online Monitoring of DC-Link Capacitors (제목 표기 VBN 레코드 기준 — 하이픈 등 정확 표기 확인 필요) | (S.) Zhao | 2023 | IEEE Transactions on Power Electronics | 10.1109/TPEL.2023.3308115 | 73 | Medium | Abstract-level only |
| 9 | Capacitance estimation algorithm based on DC-link voltage ripples using hybrid machine learning techniques in power electronics converters | Ibrahim AL-Wesabi | 2025 | Results in Engineering | (확인 필요) PII S2590123025022881 | 70 | Medium | Abstract-level only |
| 10 | Fault Diagnosis of Capacitance Aging in DC Link Capacitors of Voltage Source Inverters Using Evidence Reasoning Rule | Linhao Liao | 2020 | Mathematical Problems in Engineering | 10.1155/2020/5724019 | 62 | Medium | Abstract-level only |

---

## 7. Detailed Analysis of Top 10

각 논문은 사용자 8절 항목 [1]–[26] 순서로 정리했다. 개별 파일은 `core_papers/2level_top10/` 에 같은 내용으로 저장했다.

## Rank 1 — Tier S — Ghadrdan 2022 TPEL

> **Evidence: Abstract-level only** — 본문 미열람. `Not reported / Full text verification required` 는 초록·스니펫에 없는 항목이며 추측으로 채우지 않았다.

### [1] 기본 논문 정보
- Title: Condition Monitoring of DC-Link Electrolytic Capacitor in Back-to-Back Converters Based on Dissipation Factor
- Authors: M. Ghadrdan, S. Peyghami, H. Mokhtari, F. Blaabjerg
- Year: 2022
- Journal: IEEE Transactions on Power Electronics, vol. 37, no. 8, pp. 9733–9744 (Aug. 2022)
- DOI: 10.1109/TPEL.2022.3153842
- Publication Type: Journal
- 식별/출처: IEEE Xplore 9721605; AAU VBN; Sharif repository; RG 358881451
- 저자 소속: Sharif University of Technology (Ghadrdan, Mokhtari) + Aalborg University (Peyghami, Blaabjerg) — 리포지터리 호스팅 기준(소속 줄 미확인). First author Ghadrdan(이후 KIT). Corresponding NR.

### [2] Converter / Inverter Topology
- Topology: Back-to-back (AC/DC/AC) 전압형 컨버터. 초록은 'back-to-back converters' 로만 기술 — 2-Level 여부는 명시되지 않음(일반 B2B VSC = 2-Level 로 추정, 확인 필요).
- Power rating: Not reported / Full text verification required / DC-link voltage: Not reported / Full text verification required / AC output voltage: Not reported / Full text verification required
- Switching frequency: 수치 NR (스위칭 주파수가 DF 정확도에 미치는 영향은 분석했다고 초록에 명시) / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: Not reported / Full text verification required

### [3] Classification vs Regression
- Task: **Regression-type indicator (DF)**
- 분류 아님. 연속 지표 DF = tanδ = ω·C·ESR 를 추정하고 EoL 기준과 비교(초록). C 와 ESR 을 개별로 출력하지는 않음(초록 기준).
- Output 단위: DF (무차원)

해당 없음(회귀/연속 지표) 또는 클래스 정의 NR.

### [4] 커패시터 기본 정보
| 항목 | 값 |
|---|---|
| Technology | Aluminum electrolytic (제목에 명시) |
| Manufacturer | Not reported / Full text verification required |
| Model | Not reported / Full text verification required |
| Rated C | Not reported / Full text verification required |
| Rated V | Not reported / Full text verification required |
| Rated ESR | Not reported / Full text verification required |
| Temperature rating | Not reported / Full text verification required |

### [5] 노화 모사 방식
- NR — 실험 검증은 언급되나 노화 구현 방식(가속/모사/시뮬) 미기재. 2차 출처(인용 리뷰): 'ESR 이 초기값의 2배가 되면 고장으로 간주하며 그 경우에도 계산 오차가 허용 범위' (귀속 주의).

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| — | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required |

논문에 나온 값이 스니펫·초록에 없어 표를 채우지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): Not reported / Full text verification required

### [7] C / ESR 변화 여부
- **Not reported / Full text verification required (DF 지표 특성상 C·ESR 모두 반영되나 실험에서 무엇을 바꿨는지는 미확인)**

### [8] Dataset 구성
- 해당 없음(모델 기반). 운전점 종류 NR.

### [9] 사용 신호
- 신호: 컨버터 출력(AC) 상전류 → 커패시터 전류의 스위칭 주파수 성분 재구성; DC-link 전압(리플). 초록: 'it is possible to estimate the switching component of the capacitor current by measuring the output currents of the converter'.
- Sampling frequency: Not reported / Full text verification required

### [10] 센서 구성
- Existing inverter sensor only?: **Yes (초록 기준: 출력 전류 측정만으로 커패시터 전류 스위칭 성분 추정; 커패시터 전류 센서 불필요)**
- 추가 센서: None (초록 기준)
- Derived / reconstructed: Yes — 출력 상전류(+스위칭 상태, 추론) → 커패시터 전류 스위칭 주파수 성분. 재구성 식 자체는 본문 확인 필요.

### [11] 전처리 및 Feature Extraction
- 전처리: 스위칭 주파수 성분 추출(방법: 필터/FFT 여부 NR)
- Feature: fsw 대역 커패시터 전류·전압 성분 → DF 계산

### [12] 진단 기법
- Analytical: 재구성 전류·전압 리플의 fsw 성분으로 DF 계산 → EoL 임계 비교. 스위칭 주파수·ESL(capacitor series inductor)·계통 필터의 영향 분석(초록). RLS/Kalman 등 추정기 사용 여부 NR.
- Hyperparameter: 해당 없음

### [13] AI 모델 입력·출력
AI 모델 아님(분석적/모델 기반 방법).

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- DF 를 전해 커패시터 수명 지표로 제안하고 EoL 기준 제시(초록)
- 출력 전류 측정만으로 커패시터 전류 스위칭 성분 추정 → 커패시터 전류 센서 불필요(초록)
- fsw·ESL·계통 필터가 DF 측정 정확도에 미치는 영향 분석(초록)
- 실험으로 수용 가능한 정확도 검증(초록)

My interpretation:
새로운 점은 '측정 지표를 C 또는 ESR 이 아닌 DF 로 바꾼 것' 과 '출력 전류로 커패시터 전류를 재구성한 것' 의 결합이다. DF 는 C·ESR 를 분리하지 못하므로 내 연구에서는 재구성 전류 철학만 가져오고 지표는 분리형으로 바꾸는 것이 자연스럽다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **True Online** — 초록상 주입·시퀀스 없이 정상 운전 중 스위칭 성분을 이용(사실). 상세 운전조건 제약은 본문 확인 필요.
- On-board implementation: Not reported / Full text verification required (DSP/FPGA 구현 언급 없음; 실험 결과는 있음)

### [16] On-board Hardware Environment
| 항목 | 값 |
|---|---|
| DSP | Not reported / Full text verification required |
| MCU | Not reported / Full text verification required |
| FPGA | Not reported / Full text verification required |
| Sampling ADC | Not reported / Full text verification required |
| Memory | Not reported / Full text verification required |
| Sampling frequency | Not reported / Full text verification required |
| Control frequency | Not reported / Full text verification required |
| Execution time | Not reported / Full text verification required |
| Inference time / model size | 해당 없음 |

### [17] Real-time 가능성
- **Real-time feasible** — fsw 성분 추출과 DF 계산은 Goertzel/대역필터 수준의 연산이므로 제어기 탑재가 가능하다고 판단(해석). 구현 시연은 초록에 없음.

### [18] 실험 환경
| Parameter | Value |
|---|---|
| DC-Link Voltage | Not reported / Full text verification required |
| Output Voltage | Not reported / Full text verification required |
| Power | Not reported / Full text verification required |
| Load | Not reported / Full text verification required |
| Motor | 해당 없음(B2B 컨버터) |
| Motor speed | Not reported / Full text verification required |
| Torque | Not reported / Full text verification required |
| Switching Frequency | Not reported / Full text verification required |
| Fundamental Frequency | Not reported / Full text verification required |
| Modulation | Not reported / Full text verification required |
| Capacitor | Not reported / Full text verification required |
| Sampling Frequency | Not reported / Full text verification required |

### [19] Operating Condition 다양성
- NR. 초록은 fsw·ESL·필터 '요인' 영향 분석을 언급하나 부하·변조지수 변화 실험 여부는 미확인.

### [20] 최종 성능
- 종합: 수치 NR ('acceptable accuracy' 만 초록에 있음)
- C error: 해당 없음(DF 지표) / ESR error: 해당 없음(DF 지표) / Classification metrics: 해당 없음

### [21] Noise / Robustness
- fsw·ESL·계통 필터 영향 분석(초록). 측정 노이즈·온도·부하 변화 검증 여부 NR.

### [22] 장점
- 커패시터 전류 센서 없이 출력 전류로 재구성 → 센서 비용 0 추가
- 주입 없음 → 전력품질·제어 영향 없음
- DF 하나로 C 감소·ESR 증가를 모두 반영
- fsw·ESL·필터 의존성을 저자가 직접 분석 → 설계 시 보정 근거

### [23] 한계
Authors' stated limitation:
- (초록 기준) fsw·ESL·계통 필터가 DF 정확도에 영향 — 영향 분석이 필요함을 저자가 인정

Additional limitation identified (분석자):
- DF 로는 C 와 ESR 을 분리할 수 없음 → 열화 메커니즘 구분 불가
- 노화 샘플 값·실험 정격·오차 수치가 초록에 없어 성능 비교 불가(본문 필요)
- 재구성이 스위칭 상태·데드타임·샘플링 동기화에 의존(추론) — 구현 오차원
- 운전조건(부하·변조지수) 다양성 검증 여부 미확인

### [24] 내 연구 목표와의 관련성
- **Very High** — 2L(추정) 3상 컨버터, 기존 센서, True Online, 커패시터 전류 재구성 — 내 목표 파이프라인의 신호 생성 단계와 가장 가깝다. 단 AI·분류 요소는 없음.

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | B2B VSC (2L 추정) | 2-Level 3-Phase |
| Capacitor | DC-link 전해 | DC-Link |
| Signal | 출력 상전류 + vdc (기존 센서) | Existing inverter signal preferred |
| Aging Target | DF (C·ESR 결합) | C / ESR |
| Diagnosis | 연속 지표(회귀형) | Classification or Regression |
| Online | Yes (True Online) | Yes |
| On-board | 구현 NR | Yes |
| Extra Sensor | No | Preferably No |
| AI | No | Candidate |
| Real-time | 시연 NR | Required |

### [26] 재현 가능성
- **Moderate** — 재구성 수식과 fsw 성분 추출은 MATLAB/Simulink 로 구현 가능하나, 본문의 ESL·필터 보정식과 EoL 기준을 확인해야 결과를 비교할 수 있다.
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: ia, ib, ic, 스위칭 함수(Sa,Sb,Sc), vdc, (검증용) iC. 변화 파라미터: C(−0 ~ −20 %), ESR(×1 ~ ×2) 독립·동시 스윕, fsw 2–3 단계, 부하·변조지수. 데이터셋: 각 조합에서 정상상태 수 주기 파형 → fsw 성분·DF.

### 선정 점수 (10 기준 × 10점)
| c1 8 | c2 10 | c3 8 | c4 10 | c5 10 | c6 7 | c7 3 | c8 8 | c9 3 | c10 6 | **Total 73** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: '출력 상전류 → 커패시터 전류 스위칭 성분 재구성 → fsw 대역 지표' 의 IEEE TPEL 선례. 내 신호 생성 단계의 근거 논문.
- 집중할 Figure/Table/Equation: 재구성 수식(출력 전류→커패시터 전류), DF 정의·EoL 기준, fsw/ESL/필터 영향 절과 해당 Figure, 실험 셋업 표
- 동반·후속 논문: 후속: Ghadrdan et al., 'Dissipation Factor as a Degradation Indicator for Electrolytic Capacitors', IEEE JESTPE 11(1):1035–1044, 2023 (VBN); 과도 기반: Ghadrdan, Abdi, Peyghami, Mokhtari, Blaabjerg, IEEE JESTPE 11(1):1132–1142, 2023, DOI 10.1109/JESTPE.2022.3163012 (스위칭 로직 일시 변경, C <1 % vs LCR).

---

## Rank 2 — Tier S — Örüklü & Ağalar 2025 TIE

> **Evidence: Abstract-level only** — 본문 미열람. `Not reported / Full text verification required` 는 초록·스니펫에 없는 항목이며 추측으로 채우지 않았다.

### [1] 기본 논문 정보
- Title: Machine Learning-Based Condition Monitoring for DC-Link Capacitors in AC/DC/AC Converters
- Authors: Kerim Örüklü, Şener Ağalar
- Year: 2025 (온라인 2024; 출처에 따라 2024/2025 표기 상이)
- Journal: IEEE Transactions on Industrial Electronics, vol. 72, no. 4, pp. 4227–4237 (Apr. 2025)
- DOI: 10.1109/TIE.2024.3454814 (검색 결과에 DOI 문자열이 직접 표시되지 않음 — 확인 필요)
- Publication Type: Journal
- 식별/출처: IEEE Xplore 10695772; Semantic Scholar 5b474908…; RG 384386370
- 저자 소속: NR (스니펫에 소속 없음; 저자명으로 보아 튀르키예 기관 추정 — 확인 필요). First author Örüklü.

### [2] Converter / Inverter Topology
- Topology: AC/DC/AC 컨버터(정류단 + 인버터) 실험실 프로토타입. 인버터 레벨 수 미명시(일반 AC/DC/AC = 2-Level 로 추정, 확인 필요).
- Power rating: Not reported / Full text verification required / DC-link voltage: Not reported / Full text verification required / AC output voltage: Not reported / Full text verification required
- Switching frequency: Not reported / Full text verification required / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: 실험실 프로토타입 부하 NR

### [3] Classification vs Regression
- Task: **Regression (C)**
- C 를 health indicator 로 선택(초록). 연속 추정(회귀형). 분류 아님.
- Output 단위: C (µF 또는 % — 단위 NR)

해당 없음(회귀/연속 지표) 또는 클래스 정의 NR.

### [4] 커패시터 기본 정보
| 항목 | 값 |
|---|---|
| Technology | Not reported / Full text verification required (DC-link capacitor 로만 기술) |
| Manufacturer | Not reported / Full text verification required |
| Model | Not reported / Full text verification required |
| Rated C | Not reported / Full text verification required |
| Rated V | Not reported / Full text verification required |
| Rated ESR | Not reported / Full text verification required |
| Temperature rating | Not reported / Full text verification required |

### [5] 노화 모사 방식
- NR. 스니펫 의역: 시뮬레이션 + 실험실 프로토타입에서 '제어된 커패시턴스 변경' — 커패시터 교체/병렬 조합 여부 미확인.

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| — | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required |

논문에 나온 값이 스니펫·초록에 없어 표를 채우지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): Not reported / Full text verification required

### [7] C / ESR 변화 여부
- **C only (초록이 C 만 지표로 선언; ESR 변경 여부 NR)**

### [8] Dataset 구성
- NR (샘플 수·분할·운전점 종류 모두 미확인). 초록: 여러 조건에서 검증했다는 취지의 문구는 2026 TPEL 후속(GPR) 초록에 있음 — 본 논문 귀속 주의.

### [9] 사용 신호
- 신호: DC-link 전압 리플 (PSD 입력). 초록: '높은 샘플링 주파수를 요구하지 않음'.
- Sampling frequency: 수치 NR ('does not require a high sampling frequency')

### [10] 센서 구성
- Existing inverter sensor only?: **Yes (초록: 'No additional circuitry is required, as it solely relies on the available signals')**
- 추가 센서: None
- Derived / reconstructed: No (vdc 직접 사용)

### [11] 전처리 및 Feature Extraction
- 전처리: PSD(power spectral density) 계산 — 창·길이·정규화 NR
- Feature: vdc 리플 PSD (주파수 빈 선택·차원 NR)

### [12] 진단 기법
- ML 기반 회귀 — 알고리즘명 초록 미표시. 주의: 'Gaussian Process Regression-Based Condition Monitoring of DC-Link Capacitors in Three-Phase AC/DC/AC Converters' 는 같은 저자군의 2026 IEEE TPEL 후속 논문 제목으로 보이며(arXiv 2609.00218 인용 목록), '평균 예측 오차 <2 %, 저샘플링에서도 유효, 불확실성 제공' 문구는 그 후속 초록일 가능성이 큼 → 본 TIE 논문의 모델·수치로 단정하지 않음.
- Hyperparameter: Not reported / Full text verification required

### [13] AI 모델 입력·출력
| Item | Information |
|---|---|
| Input | DC-link 전압 리플 |
| Input shape | Not reported / Full text verification required |
| Preprocessing | PSD |
| Feature dimension | Not reported / Full text verification required |
| Model | ML 회귀 (명칭 NR; GPR 은 후속 논문) |
| Output | C (health indicator) |
| Loss | Not reported / Full text verification required |
| Optimizer | Not reported / Full text verification required |

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- C 를 health indicator 로, vdc 리플 PSD 를 진단 도구로 제안(초록)
- 추가 회로 없이 가용 신호만 사용(초록)
- 유사 연구와 달리 높은 샘플링 주파수 불필요(초록)
- 시뮬레이션 + 실험실 프로토타입 검증, 높은 정확도(초록)

My interpretation:
'vdc 리플의 PSD → ML 회귀' 는 신호 하나·센서 추가 없음이라는 구현 단순성이 핵심이다. 내 연구와의 차이는 입력 신호(상전류 재구성 전류 vs vdc)와 대상(C+ESR vs C)이며, 이 논문은 데이터 기반 벤치마크(비교군)로 가장 적합하다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **True Online** — 정상 운전 중 vdc 리플만 사용, 주입·회로 없음(초록).
- On-board implementation: Not reported / Full text verification required (실험 검증은 있으나 DSP/MCU 추론 구현 여부 미기재)

### [16] On-board Hardware Environment
| 항목 | 값 |
|---|---|
| DSP | Not reported / Full text verification required |
| MCU | Not reported / Full text verification required |
| FPGA | Not reported / Full text verification required |
| Sampling ADC | Not reported / Full text verification required |
| Memory | Not reported / Full text verification required |
| Sampling frequency | 저샘플링 강조(수치 NR) |
| Control frequency | Not reported / Full text verification required |
| Execution time | Not reported / Full text verification required |
| Inference time / model size | Not reported / Full text verification required |

### [17] Real-time 가능성
- **Real-time feasible** — 저샘플링 PSD + 경량 회귀는 제어기 탑재가 가능하나, 모델 크기·추론 시간이 미기재라 '시연' 으로 볼 수 없음(해석).

### [18] 실험 환경
| Parameter | Value |
|---|---|
| DC-Link Voltage | Not reported / Full text verification required |
| Output Voltage | Not reported / Full text verification required |
| Power | Not reported / Full text verification required |
| Load | Not reported / Full text verification required |
| Motor | Not reported / Full text verification required |
| Motor speed | Not reported / Full text verification required |
| Torque | Not reported / Full text verification required |
| Switching Frequency | Not reported / Full text verification required |
| Fundamental Frequency | Not reported / Full text verification required |
| Modulation | Not reported / Full text verification required |
| Capacitor | Not reported / Full text verification required |
| Sampling Frequency | Not reported / Full text verification required |

### [19] Operating Condition 다양성
- NR for this paper. 후속(2026 TPEL GPR) 초록에 '여러 부하·출력 주파수' 검증 문구 — 본 논문 귀속 미확인.

### [20] 최종 성능
- 종합: 'high accuracy' (수치 NR). '<2 % 평균 예측 오차' 는 후속 논문 귀속 가능성 → 미채택.
- C error: Not reported / Full text verification required / ESR error: 해당 없음(C only) / Classification metrics: 해당 없음

### [21] Noise / Robustness
- 저샘플링 강건성 주장(초록). 노이즈·온도·미학습 운전조건 검증 NR.

### [22] 장점
- 센서·회로 추가 없음(vdc 만)
- 저샘플링 → 저가 MCU 적합(해석)
- 실험실 프로토타입 검증(초록)
- IEEE TIE 급 최신(2024–25) ML 접근

### [23] 한계
Authors' stated limitation:
- Not reported / Full text verification required

Additional limitation identified (분석자):
- C only — ESR(전해 커패시터 초기 열화 지표) 미추정
- vdc 리플은 부하·변조지수·전원 조건에 따라 변하므로 조건 정규화 없이는 일반화 위험(해석)
- 알고리즘·데이터셋·수치가 초록에 없어 재현 설계 불가(본문 필수)
- 노화 모사 방식 NR

### [24] 내 연구 목표와의 관련성
- **Very High** — 2L(추정) 3상 AC/DC/AC + 기존 센서 + True Online + ML 회귀 — 내 목표 파이프라인과 구조가 같다. 입력 신호·대상만 다름.

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | AC/DC/AC (2L 추정) | 2-Level 3-Phase |
| Capacitor | DC-link | DC-Link |
| Signal | vdc 리플 (기존 센서) | Existing inverter signal preferred |
| Aging Target | C | C / ESR |
| Diagnosis | Regression | Classification or Regression |
| Online | Yes (True Online) | Yes |
| On-board | NR | Yes |
| Extra Sensor | No | Preferably No |
| AI | Yes (ML 회귀) | Candidate |
| Real-time | 시연 NR | Required |

### [26] 재현 가능성
- **Moderate** — vdc 리플 PSD → 회귀는 MATLAB/Python 으로 바로 구성 가능. 단 저자의 PSD 설정·모델·노화 샘플을 본문에서 확인해야 동일 조건 비교가 된다.
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: vdc(리플 포함, 저·고 샘플링 2종), 부하·변조지수·f1 로그. 변화 파라미터: C 5–7 단계(−0…−30 %), 가능하면 ESR 도 교차. 데이터셋: 운전점×C 조합별 PSD 벡터 → 회귀(train/test 를 운전점 기준으로 분리해 일반화 검증).

### 선정 점수 (10 기준 × 10점)
| c1 9 | c2 10 | c3 8 | c4 10 | c5 10 | c6 8 | c7 4 | c8 7 | c9 4 | c10 7 | **Total 77** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: 기존 센서(vdc)만으로 True Online ML 회귀를 IEEE TIE 에 실은 최신 논문. 내 AI 파이프라인의 직접 비교군.
- 집중할 Figure/Table/Equation: PSD 입력 정의(주파수 범위·분해능), 사용 ML 모델과 hyperparameter, 노화 샘플 표, 실험 셋업 표, 오차 표/그림, 저샘플링 실험 절
- 동반·후속 논문: 후속(귀속 확인 필요): 'Gaussian Process Regression-Based Condition Monitoring of DC-Link Capacitors in Three-Phase AC/DC/AC Converters', IEEE TPEL 2026 (arXiv 2609.00218 인용 목록) — 평균 예측 오차 <2 %, 불확실성 제공.

---

## Rank 3 — Tier S — Lipnicki & Lewandowski 2017 PED

> **Evidence: Abstract-level only** — 본문 미열람. `Not reported / Full text verification required` 는 초록·스니펫에 없는 항목이며 추측으로 채우지 않았다.

### [1] 기본 논문 정보
- Title: DC Link Condition Monitoring Method for Two-Level AC/DC/AC Converters
- Authors: P. Lipnicki, D. Lewandowski
- Year: 2017
- Journal: Power Electronics and Drives (Sciendo / Wrocław Univ. of Science and Technology), vol. 2(37), no. 1, pp. 43–56 (online 27 Oct 2017)
- DOI: 10.5277/PED170107
- Publication Type: Journal (국내·중소 저널급; IEEE/IET 아님)
- 식별/출처: ped.pwr.edu.pl 68776; sciendo.com/article/10.5277/ped170107; RG 334696403; 공개 PDF yadda.icm.edu.pl (PED_1_2017_Lipnicki.pdf) — 본 환경에서 열지 못함
- 저자 소속: ABB Corporate Research Center, Kraków (스니펫 기준)

### [2] Converter / Inverter Topology
- Topology: 2-Level AC/DC/AC 컨버터(제목에 명시). 정격 NR.
- Power rating: Not reported / Full text verification required / DC-link voltage: Not reported / Full text verification required / AC output voltage: Not reported / Full text verification required
- Switching frequency: Not reported / Full text verification required / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: Not reported / Full text verification required

### [3] Classification vs Regression
- Task: **Regression (ESR)**
- ESR 온라인 추정; ESR 증가 추세를 고장 지표로 사용(인용 논문 문구).
- Output 단위: ESR (Ω 또는 상대값 — NR)

해당 없음(회귀/연속 지표) 또는 클래스 정의 NR.

### [4] 커패시터 기본 정보
| 항목 | 값 |
|---|---|
| Technology | Not reported / Full text verification required |
| Manufacturer | Not reported / Full text verification required |
| Model | Not reported / Full text verification required |
| Rated C | Not reported / Full text verification required |
| Rated V | Not reported / Full text verification required |
| Rated ESR | Not reported / Full text verification required |
| Temperature rating | Not reported / Full text verification required |

### [5] 노화 모사 방식
- Not reported / Full text verification required (실험 여부·노화 모사 방식 모두 미확인)

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| — | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required |

논문에 나온 값이 스니펫·초록에 없어 표를 채우지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): Not reported / Full text verification required

### [7] C / ESR 변화 여부
- **ESR only (추정 대상 기준; 실험에서 C 변경 여부 NR)**

### [8] Dataset 구성
- 해당 없음(모델 기반)

### [9] 사용 신호
- 신호: DC-link 전압 측정 + DC-link 전류 재구성(초록). 이전 조사 스니펫: 상전류 + 각 레그 스위칭 함수로 DC-link 전류 재구성 — 본문 확인 필요.
- Sampling frequency: Not reported / Full text verification required

### [10] 센서 구성
- Existing inverter sensor only?: **Yes (초록: 'does not require any additional sensors')**
- 추가 센서: None
- Derived / reconstructed: Yes — DC-link(커패시터) 전류를 상전류·스위칭 함수로 재구성(초록 'DC-link current reconstruction').

### [11] 전처리 및 Feature Extraction
- 전처리: Not reported / Full text verification required (리플 성분 추출 방법 미확인)
- Feature: 재구성 전류와 vdc 리플의 관계 → ESR

### [12] 진단 기법
- Analytical: vdc + 재구성 DC-link 전류 → ESR 추정(세부 추정기 NR).
- Hyperparameter: 해당 없음

### [13] AI 모델 입력·출력
AI 모델 아님(분석적/모델 기반 방법).

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- 2-Level AC/DC/AC 컨버터용 DC-link 상태 감시 방법 제안(제목)
- 추가 센서 없이 vdc 측정 + DC-link 전류 재구성으로 온라인 ESR 추정(초록)

My interpretation:
산업계(ABB)가 2-Level 드라이브에서 '스위칭 함수 기반 전류 재구성 → ESR' 을 실제로 다룬 드문 공개 논문. 저널 등급은 낮지만 내 신호 생성 방식과 토폴로지가 정확히 일치한다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **True Online** — 초록상 주입·시퀀스 언급 없음, 추가 센서 없음. 운전 조건 제약은 본문 확인 필요.
- On-board implementation: Not reported / Full text verification required (ABB 연구소 논문이나 제어기 구현·실험 여부 스니펫 미확인)

### [16] On-board Hardware Environment
| 항목 | 값 |
|---|---|
| DSP | Not reported / Full text verification required |
| MCU | Not reported / Full text verification required |
| FPGA | Not reported / Full text verification required |
| Sampling ADC | Not reported / Full text verification required |
| Memory | Not reported / Full text verification required |
| Sampling frequency | Not reported / Full text verification required |
| Control frequency | Not reported / Full text verification required |
| Execution time | Not reported / Full text verification required |
| Inference time / model size | 해당 없음 |

### [17] Real-time 가능성
- **Real-time feasible** — 상전류×스위칭 함수 합산과 리플 대역 처리로 구성되어 제어기 주기 내 계산이 가능(해석); 시연 여부 미확인.

### [18] 실험 환경
| Parameter | Value |
|---|---|
| DC-Link Voltage | Not reported / Full text verification required |
| Output Voltage | Not reported / Full text verification required |
| Power | Not reported / Full text verification required |
| Load | Not reported / Full text verification required |
| Motor | Not reported / Full text verification required |
| Motor speed | Not reported / Full text verification required |
| Torque | Not reported / Full text verification required |
| Switching Frequency | Not reported / Full text verification required |
| Fundamental Frequency | Not reported / Full text verification required |
| Modulation | Not reported / Full text verification required |
| Capacitor | Not reported / Full text verification required |
| Sampling Frequency | Not reported / Full text verification required |

### [19] Operating Condition 다양성
- Not reported / Full text verification required

### [20] 최종 성능
- 종합: Not reported / Full text verification required
- C error: 해당 없음 / ESR error: Not reported / Full text verification required / Classification metrics: 해당 없음

### [21] Noise / Robustness
- Not reported / Full text verification required

### [22] 장점
- 토폴로지(2L AC/DC/AC)·센서 조건(추가 없음)·재구성 철학이 내 목표와 일치
- 산업 연구소 출처 → 실용 관점
- 공개 PDF 존재(로컬에서 확보 가능)

### [23] 한계
Authors' stated limitation:
- Not reported / Full text verification required

Additional limitation identified (분석자):
- 저널 영향력 낮음 → 인용 시 보조 근거
- 실험·정격·오차·노화 방식이 모두 미확인(본문 필수)
- ESR only; 필름 커패시터에는 부적합(추론)
- 재구성 오차(데드타임·샘플링 지연) 처리 여부 미확인

### [24] 내 연구 목표와의 관련성
- **Very High** — 2-Level AC/DC/AC + 기존 센서 + 재구성 + ESR + True Online — 내 목표와 조건이 가장 많이 겹친다(AI 요소만 없음).

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | 2L AC/DC/AC | 2-Level 3-Phase |
| Capacitor | DC-link | DC-Link |
| Signal | vdc + 재구성 DC-link 전류 (기존 센서) | Existing inverter signal preferred |
| Aging Target | ESR | C / ESR |
| Diagnosis | Regression(추정) | Classification or Regression |
| Online | Yes (True Online) | Yes |
| On-board | NR | Yes |
| Extra Sensor | No | Preferably No |
| AI | No | Candidate |
| Real-time | 시연 NR | Required |

### [26] 재현 가능성
- **Moderate** — 재구성 자체는 쉽지만 ESR 추출식·대역·보정이 본문에만 있다. PDF 가 공개되어 있어 로컬에서 바로 확인 가능.
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: ia, ib, ic, Sa/Sb/Sc, vdc, 검증용 idc·iC. 변화 파라미터: ESR(Radd 0 ~ +100 %), C 고정/변경 교차, 부하 3단계. 데이터셋: 조합별 정상상태 파형 → 재구성 전류 fsw 성분 vs vdc 리플.

### 선정 점수 (10 기준 × 10점)
| c1 10 | c2 10 | c3 4 | c4 10 | c5 10 | c6 8 | c7 3 | c8 8 | c9 2 | c10 7 | **Total 72** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: 제목부터 '2-Level AC/DC/AC' 이며 추가 센서 없는 재구성 기반 ESR 추정 — 내 토폴로지·신호 조건의 직접 선례.
- 집중할 Figure/Table/Equation: DC-link 전류 재구성 식(스위칭 함수 정의), ESR 추출 대역·수식, 실험/시뮬 조건 표, 오차 그림
- 동반·후속 논문: 관련 특허(개념 비교용): US 12461138 'Circuitry and methods for monitoring power conversion circuitry' — AC 측 전류+스위칭 상태로 커패시터 전류 재구성.

---

## Rank 4 — Tier A — Hasegawa & Hirose 2024 TIA

> **Evidence: Abstract-level only** — 본문 미열람. `Not reported / Full text verification required` 는 초록·스니펫에 없는 항목이며 추측으로 채우지 않았다.

### [1] 기본 논문 정보
- Title: Current-Sensor-Less Condition Monitoring of a DC-Link Capacitor Based on Analysis of a Six-Pulse Diode Rectifier Having AC and DC Inductors
- Authors: K. Hasegawa, Y. Hirose
- Year: 2024
- Journal: IEEE Transactions on Industry Applications, vol. 60, no. 6, pp. 9043–9051 (Nov./Dec. 2024)
- DOI: (확인 필요) — Kyutech 교원 목록·리포지터리에서 권/호/쪽만 확인, IEEE 페이지 미열람
- Publication Type: Journal (ECCE 2023 학회판의 저널 확장)
- 식별/출처: Kyutech repository (kyutech.repo.nii.ac.jp), 교원 업적 DB hyokadb02; 학회판 ECCE 2023
- 저자 소속: Kyushu Institute of Technology (Hasegawa 연구실). First author Hasegawa.

### [2] Converter / Inverter Topology
- Topology: 6-pulse 다이오드 정류기(AC 라인 인덕터 + DC 인덕터) + 3상 PWM 인버터 — 정류기-인버터 드라이브(보조 범위; 인버터부는 3상 PWM 인버터 = 2L 로 추정).
- Power rating: NR (2025 MR 후속: 1.5 kW) / DC-link voltage: 200 V 급 실험 시스템(초록 '200-V laboratory system') / AC output voltage: Not reported / Full text verification required
- Switching frequency: Not reported / Full text verification required / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: Not reported / Full text verification required

### [3] Classification vs Regression
- Task: **Regression (C+ESR)**
- C 와 ESR 변화를 모두 관측·추정(초록 'both ESR and capacitance changes were observed').
- Output 단위: C, ESR (단위 NR)

해당 없음(회귀/연속 지표) 또는 클래스 정의 NR.

### [4] 커패시터 기본 정보
| 항목 | 값 |
|---|---|
| Technology | Not reported / Full text verification required (전해 추정 — 리플 전류 해석 대상) |
| Manufacturer | Not reported / Full text verification required |
| Model | Not reported / Full text verification required |
| Rated C | Not reported / Full text verification required |
| Rated V | Not reported / Full text verification required |
| Rated ESR | Not reported / Full text verification required |
| Temperature rating | Not reported / Full text verification required |

### [5] 노화 모사 방식
- NR (실험에서 C·ESR 변화를 '관측' 했다고만 초록에 기재 — 커패시터 교체/저항 추가 여부 미확인)

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| — | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required |

논문에 나온 값이 스니펫·초록에 없어 표를 채우지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): Not reported / Full text verification required

### [7] C / ESR 변화 여부
- **C + ESR (둘 다 변화를 관측했으나 동시/개별 여부 NR)**

### [8] Dataset 구성
- 해당 없음(모델 기반)

### [9] 사용 신호
- 신호: 3상 AC 전원 전압, AC 라인 인덕터·DC 인덕터 값(파라미터), 인버터 출력 전력 → 커패시터 전류 계산; DC-link 전압(리플). 전류 센서 미사용.
- Sampling frequency: Not reported / Full text verification required

### [10] 센서 구성
- Existing inverter sensor only?: **Yes — 전류 센서 자체를 쓰지 않음(초록). 전원 전압 측정이 필요하므로 '인버터 기존 센서' 관점에서는 전원 전압 센서 유무에 따라 Partially 가 될 수 있음(해석).**
- 추가 센서: None (전류 센서 없음; 전원 전압 센서는 드라이브 구성에 따라 다름)
- Derived / reconstructed: Yes — 정류기 해석 모델(전원 전압 + 인덕터 + 출력 전력)로 커패시터 전류를 계산.

### [11] 전처리 및 Feature Extraction
- 전처리: 정류 리플(6f1 계열) 성분 해석 — FFT 여부 NR(관련 2019 IEEJ·2024 학회판은 FFT 사용)
- Feature: 정류 리플 전류·전압 성분 → ESR, C

### [12] 진단 기법
- Analytical: 6-pulse 정류기 리플 전류 모델 → 커패시터 전류 계산 → 리플 전압과의 관계로 ESR·C 산출.
- Hyperparameter: 해당 없음

### [13] AI 모델 입력·출력
AI 모델 아님(분석적/모델 기반 방법).

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- 전류 센서 없이 DC-link 커패시터 CM(제목·초록)
- AC·DC 인덕터를 모두 가진 6-pulse 정류기 해석으로 커패시터 전류 계산(초록)
- 200 V 실험으로 ESR·C 변화 모두 관측(초록)

My interpretation:
'커패시터 전류를 측정하지 않고 계산한다' 는 점에서 내 재구성 접근과 같은 철학이지만, 정보원이 인버터 스위칭이 아니라 정류기 리플이다. 정류기 전단 드라이브에서는 이 방법이 가장 단순하고, 인버터 측 재구성과 결합하면 C·ESR 를 두 대역에서 교차 검증할 수 있다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **True Online** — 정상 운전 중 고유 정류 리플을 이용, 주입 없음(초록).
- On-board implementation: 본 논문 NR. 같은 그룹의 2024 학회판·2025 MR 논문은 'Leafony' 소형 MCU 에서 FFT 로 ESR 감시(스니펫; 2025 MR 판 귀속은 확인 필요).

### [16] On-board Hardware Environment
| 항목 | 값 |
|---|---|
| DSP | Not reported / Full text verification required |
| MCU | Leafony 소형 MCU (학회판/후속 논문; 본 논문 귀속 NR) |
| FPGA | Not reported / Full text verification required |
| Sampling ADC | Not reported / Full text verification required |
| Memory | Not reported / Full text verification required |
| Sampling frequency | Not reported / Full text verification required |
| Control frequency | Not reported / Full text verification required |
| Execution time | Not reported / Full text verification required |
| Inference time / model size | 해당 없음 |

### [17] Real-time 가능성
- **Real-time feasible (후속 논문에서 MCU 구현 시사)** — FFT 한 번과 대수 계산으로 구성되어 소형 MCU 에서도 가능함을 같은 그룹이 보였다(스니펫).

### [18] 실험 환경
| Parameter | Value |
|---|---|
| DC-Link Voltage | 200 V 급 |
| Output Voltage | Not reported / Full text verification required |
| Power | NR (후속 1.5 kW) |
| Load | Not reported / Full text verification required |
| Motor | Not reported / Full text verification required |
| Motor speed | Not reported / Full text verification required |
| Torque | Not reported / Full text verification required |
| Switching Frequency | Not reported / Full text verification required |
| Fundamental Frequency | Not reported / Full text verification required |
| Modulation | Not reported / Full text verification required |
| Capacitor | Not reported / Full text verification required |
| Sampling Frequency | Not reported / Full text verification required |

### [19] Operating Condition 다양성
- NR (본 논문). 후속 2025 MR: 전원 전압 불평형 ≈5 % 까지 유효.

### [20] 최종 성능
- 종합: Not reported / Full text verification required (초록은 '변화를 관측' 으로만 기술)
- C error: Not reported / Full text verification required / ESR error: Not reported / Full text verification required / Classification metrics: 해당 없음

### [21] Noise / Robustness
- 후속 2025 MR 에서 전원 불평형 강건성 다룸. 부하·온도 NR.

### [22] 장점
- 전류 센서 완전 배제 → 비용·설치 최소
- C 와 ESR 동시
- True Online
- 소형 MCU 구현 계열(후속)

### [23] 한계
Authors' stated limitation:
- Not reported / Full text verification required

Additional limitation identified (분석자):
- 정류기 전단(다이오드) 드라이브에 한정 — AFE·PV·배터리 입력 2L 인버터에는 적용 불가(추론)
- 인버터 출력 전력·인덕터 값 등 파라미터 의존 → 파라미터 오차가 추정 오차로 전파(추론)
- 오차 수치·노화 샘플 미확인

### [24] 내 연구 목표와의 관련성
- **High** — 방법 철학(센서 없는 커패시터 전류 계산, C+ESR 동시)은 매우 유용하나, 정보원이 정류 리플이라 내 '인버터 신호' 목표와 다르다.

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | 다이오드 정류기 + 3상 PWM 인버터 | 2-Level 3-Phase |
| Capacitor | DC-link | DC-Link |
| Signal | 전원 전압 + 출력 전력 + vdc (전류 센서 없음) | Existing inverter signal preferred |
| Aging Target | C + ESR | C / ESR |
| Diagnosis | Regression | Classification or Regression |
| Online | Yes (True Online) | Yes |
| On-board | 후속 MCU | Yes |
| Extra Sensor | No | Preferably No |
| AI | No | Candidate |
| Real-time | 후속에서 시연 시사 | Required |

### [26] 재현 가능성
- **Moderate** — 정류기 리플 모델은 Simulink 로 재현 가능. 인덕터 값·출력 전력 추정 방법이 본문에만 있음.
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: 전원 3상 전압, vdc, (검증) iC, 출력 전력(상전류·전압). 변화 파라미터: C, ESR 각 3–5 단계, 부하 3단계, 전원 불평형. 데이터셋: 조합별 정류 리플 성분.

### 선정 점수 (10 기준 × 10점)
| c1 7 | c2 10 | c3 9 | c4 10 | c5 10 | c6 10 | c7 3 | c8 8 | c9 3 | c10 6 | **Total 76** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: 전류 센서 없이 C+ESR 를 동시에 추정한 IEEE TIA 최신 논문. '측정 대신 계산' 의 오차 처리 방식을 배울 수 있다.
- 집중할 Figure/Table/Equation: 커패시터 전류 계산식(전원 전압·인덕터·출력 전력), ESR/C 산출식, 200 V 실험 셋업 표, C·ESR 변화 관측 그림
- 동반·후속 논문: K. Hasegawa, T. Kubo, Y. Hirose, IEEJ J. Ind. Appl. 2023 (DC 인덕터만); Yamasoto & Hasegawa, Microelectronics Reliability 173:115873, 2025, DOI 10.1016/j.microrel.2025.115873 (200 V 1.5 kW, 불평형 ≈5 %); Hasegawa, Nishizawa, Omura, Microelectron. Reliab. 88–90:433–437, 2018.

---

## Rank 5 — Tier A — Sundararajan 2018 TIA

> **Evidence: Abstract-level only** — 본문 미열람. `Not reported / Full text verification required` 는 초록·스니펫에 없는 항목이며 추측으로 채우지 않았다.

### [1] 기본 논문 정보
- Title: Online Condition Monitoring System for DC-Link Capacitor in Industrial Power Converters
- Authors: P. Sundararajan et al. (전체 저자 목록 확인 필요; NTU/Rolls-Royce@NTU 그룹)
- Year: 2018
- Journal: IEEE Transactions on Industry Applications, vol. 54, no. 5, pp. 4775–4785 (Sep./Oct. 2018)
- DOI: 10.1109/TIA.2018.2845889
- Publication Type: Journal (학회판: 'Online equivalent series resistance estimation method…', Xplore 8096009)
- 식별/출처: IEEE Xplore 8378055; NTU DR-NTU 레코드; RG 325704243
- 저자 소속: Nanyang Technological University (Rolls-Royce@NTU Corporate Lab) — 리포지터리 호스팅 기준

### [2] Converter / Inverter Topology
- Topology: 전단 정류기 급전 3상 인버터(front-end rectifier-fed inverter). 맞춤 제작 인버터 + 상용 AC 드라이브(초록). 레벨 수 미명시(상용 AC 드라이브 = 2L 추정).
- Power rating: Not reported / Full text verification required / DC-link voltage: Not reported / Full text verification required / AC output voltage: Not reported / Full text verification required
- Switching frequency: NR — 방법이 유효한 '한계 스위칭 주파수' 를 규명하고 그 이하에서는 별도 해법 제안(초록) / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: Not reported / Full text verification required

### [3] Classification vs Regression
- Task: **Regression (ESR)**
- ESR 을 열화 지표로 추정. (2020 TPEL 후속: ESR + C, C 는 온도 민감 파라미터로 코어/핫스팟 온도 추정에도 사용)
- Output 단위: ESR (Ω — NR)

해당 없음(회귀/연속 지표) 또는 클래스 정의 NR.

### [4] 커패시터 기본 정보
| 항목 | 값 |
|---|---|
| Technology | Not reported / Full text verification required (전해 추정) |
| Manufacturer | Not reported / Full text verification required |
| Model | Not reported / Full text verification required |
| Rated C | Not reported / Full text verification required |
| Rated V | Not reported / Full text verification required |
| Rated ESR | Not reported / Full text verification required |
| Temperature rating | Not reported / Full text verification required |

### [5] 노화 모사 방식
- NR. 인용 문구로 고장 기준 'ESR >200 %, C <80 %' 언급(귀속 확인 필요).

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| — | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required |

논문에 나온 값이 스니펫·초록에 없어 표를 채우지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): Not reported / Full text verification required

### [7] C / ESR 변화 여부
- **ESR only (본 논문); C 변경 여부 NR**

### [8] Dataset 구성
- 해당 없음(모델 기반)

### [9] 사용 신호
- 신호: DC-link 전압과 DC-link 전류의 스위칭 주파수 성분(초록). DC-link 전류가 측정인지 재구성인지 NR.
- Sampling frequency: Not reported / Full text verification required

### [10] 센서 구성
- Existing inverter sensor only?: **Partially / NR — vdc 는 기존 센서; DC-link 전류 센서 존재 여부가 구현에 따라 다름(초록 미명시)**
- 추가 센서: NR (DC-link 전류 센서 필요 가능성)
- Derived / reconstructed: NR

### [11] 전처리 및 Feature Extraction
- 전처리: 대역통과 필터로 스위칭 주파수 성분 추출(스니펫). 2020 TPEL: Goertzel 단일 빈 DFT.
- Feature: fsw 성분 전압/전류 비 → ESR

### [12] 진단 기법
- Analytical: fsw 대역 |ΔV/ΔI| 기반 ESR 추정; 한계 fsw 이하에서 대안 해법(초록). 2020 TPEL: Goertzel 알고리즘으로 ESR·C 추출 + 온도 추정 + 자가 보정.
- Hyperparameter: 해당 없음

### [13] AI 모델 입력·출력
AI 모델 아님(분석적/모델 기반 방법).

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- 산업용 컨버터용 온라인 DC-link 커패시터 CM 시스템(제목)
- vdc·idc 의 스위칭 주파수 성분으로 ESR 추정(초록)
- 유효 한계 스위칭 주파수 규명 및 그 이하 해법(초록)
- PSpice → 맞춤 인버터 실험 → 상용 AC 드라이브 구현(초록)

My interpretation:
학술 프로토타입을 넘어 '상용 드라이브 구현' 까지 간 점이 핵심. 내 연구에서 fsw 성분 기반 ESR 추정과 Goertzel(2020) 은 경량 feature 추출기의 직접 참고가 된다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **True Online** — 정상 운전 중 스위칭 리플 성분만 사용(초록). 주입 없음.
- On-board implementation: Yes (초록: 'implemented in a commercial ac drive system') — 제어기 종류·부품 NR

### [16] On-board Hardware Environment
| 항목 | 값 |
|---|---|
| DSP | Not reported / Full text verification required |
| MCU | Not reported / Full text verification required |
| FPGA | Not reported / Full text verification required |
| Sampling ADC | Not reported / Full text verification required |
| Memory | Not reported / Full text verification required |
| Sampling frequency | Not reported / Full text verification required |
| Control frequency | Not reported / Full text verification required |
| Execution time | Not reported / Full text verification required |
| Inference time / model size | 해당 없음 |

### [17] Real-time 가능성
- **Real-time demonstrated (상용 드라이브 구현 — 초록 기준)** — 초록이 상용 AC 드라이브 시스템 구현을 명시. 실행 시간 수치는 NR.

### [18] 실험 환경
| Parameter | Value |
|---|---|
| DC-Link Voltage | Not reported / Full text verification required |
| Output Voltage | Not reported / Full text verification required |
| Power | Not reported / Full text verification required |
| Load | Not reported / Full text verification required |
| Motor | 상용 AC 드라이브(전동기 종류 NR) |
| Motor speed | Not reported / Full text verification required |
| Torque | Not reported / Full text verification required |
| Switching Frequency | Not reported / Full text verification required |
| Fundamental Frequency | Not reported / Full text verification required |
| Modulation | Not reported / Full text verification required |
| Capacitor | Not reported / Full text verification required |
| Sampling Frequency | Not reported / Full text verification required |

### [19] Operating Condition 다양성
- NR (스위칭 주파수 의존성은 분석)

### [20] 최종 성능
- 종합: 'estimation error is very low' (수치 NR)
- C error: 해당 없음(본 논문) / ESR error: Not reported / Full text verification required / Classification metrics: 해당 없음

### [21] Noise / Robustness
- fsw 의존성 분석(초록). 온도는 2020 TPEL 에서 다룸(온도 추정·자가 보정).

### [22] 장점
- 상용 드라이브 구현 → On-board 실증
- True Online, 주입 없음
- fsw 성분이라는 명확한 물리 feature
- 후속(2020)에서 Goertzel 로 연산량 최소화 + 온도까지

### [23] 한계
Authors' stated limitation:
- 한계 스위칭 주파수 이하에서는 기본 방법이 유효하지 않아 별도 해법 필요(초록)

Additional limitation identified (분석자):
- DC-link 전류 센서 필요 가능성(미확인) → 센서 조건 불리할 수 있음
- ESR only(본 논문)
- 노화 샘플·오차 수치·제어기 사양이 초록에 없음
- 2020 TPEL 검증은 T-type 3L 프로토타입 — 2L 데이터로 단정 불가

### [24] 내 연구 목표와의 관련성
- **High** — fsw 성분 ESR 추정 + 상용 드라이브 구현은 내 on-board 목표의 실증 선례. 센서 조건(idc)과 ESR 단독이 차이.

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | 정류기 급전 3상 인버터(2L 추정) | 2-Level 3-Phase |
| Capacitor | DC-link | DC-Link |
| Signal | vdc + idc 의 fsw 성분 | Existing inverter signal preferred |
| Aging Target | ESR (+C, 온도: 2020) | C / ESR |
| Diagnosis | Regression | Classification or Regression |
| Online | Yes (True Online) | Yes |
| On-board | Yes (상용 드라이브) | Yes |
| Extra Sensor | idc 센서 여부 NR | Preferably No |
| AI | No | Candidate |
| Real-time | 시연(초록) | Required |

### [26] 재현 가능성
- **Moderate** — fsw 대역 추출과 ESR 비 계산은 쉽다. 한계 fsw 조건과 대안 해법, 전류 측정 방식은 본문 확인 필요.
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: vdc, idc(또는 재구성), fsw 성분. 변화 파라미터: ESR 3–5 단계, fsw 2–3 단계(한계 fsw 확인), 부하. 데이터셋: 조합별 fsw 빈 진폭(Goertzel) → ESR.

### 선정 점수 (10 기준 × 10점)
| c1 8 | c2 10 | c3 9 | c4 10 | c5 6 | c6 8 | c7 3 | c8 8 | c9 3 | c10 6 | **Total 71** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: On-board(상용 드라이브) 구현까지 보인 True Online ESR 추정의 대표. Goertzel 후속과 함께 경량 feature 추출 설계의 근거.
- 집중할 Figure/Table/Equation: fsw 성분 ESR 식, 한계 fsw 유도, 상용 드라이브 구현 절(제어기·샘플링), 오차 표; 2020 TPEL 의 Goertzel 빈 선택·온도 보정 절
- 동반·후속 논문: Sundararajan et al., 'Condition Monitoring of DC-Link Capacitors Using Goertzel Algorithm for Failure Precursor Parameter and Temperature Estimation', IEEE TPEL 35(6):6386–6396, 2020, DOI 10.1109/TPEL.2019.2951859 (Xplore 8892651; 검증은 T-type 3L 프로토타입 — 스니펫).

---

## Rank 6 — Tier A — Park & Kwak 2023 JEET

> **Evidence: Abstract-level only** — 본문 미열람. `Not reported / Full text verification required` 는 초록·스니펫에 없는 항목이며 추측으로 채우지 않았다.

### [1] 기본 논문 정보
- Title: DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs
- Authors: Hye-Jin Park, Sangshin Kwak
- Year: 2023
- Journal: Journal of Electrical Engineering & Technology (Springer/KIEE), vol. 18, no. 3, pp. 1841–1850 (May 2023)
- DOI: 10.1007/s42835-023-01424-z
- Publication Type: Journal
- 식별/출처: Springer; CAU ScholarWorks 2019.sw.cau/66390; RG (Feb 2023)
- 저자 소속: Chung-Ang University (곽상신 연구실). First author Park, corresponding Kwak(추정).

### [2] Converter / Inverter Topology
- Topology: 3상 DC/AC 컨버터(입력 커패시터 = DC-link). 레벨 수 미명시(2L 추정). 정격 NR.
- Power rating: Not reported / Full text verification required / DC-link voltage: Not reported / Full text verification required / AC output voltage: Not reported / Full text verification required
- Switching frequency: Not reported / Full text verification required / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: Not reported / Full text verification required

### [3] Classification vs Regression
- Task: **Regression (C+ESR)**
- 커패시터 내부 상태(C, ESR) 를 딥러닝으로 추정(회귀). 분류 아님.
- Output 단위: C, ESR (단위 NR)

해당 없음(회귀/연속 지표) 또는 클래스 정의 NR.

### [4] 커패시터 기본 정보
| 항목 | 값 |
|---|---|
| Technology | Not reported / Full text verification required |
| Manufacturer | Not reported / Full text verification required |
| Model | Not reported / Full text verification required |
| Rated C | Not reported / Full text verification required |
| Rated V | Not reported / Full text verification required |
| Rated ESR | Not reported / Full text verification required |
| Temperature rating | Not reported / Full text verification required |

### [5] 노화 모사 방식
- NR. 선행 JPE 2022(단상)는 '실험 전압·전류 파형' 을 사용 — 본 3상 논문의 실험/시뮬 여부는 미확인.

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| — | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required |

논문에 나온 값이 스니펫·초록에 없어 표를 채우지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): Not reported / Full text verification required

### [7] C / ESR 변화 여부
- **C + ESR (둘 다 추정 대상; 데이터 생성 시 동시 변화 여부 NR)**

### [8] Dataset 구성
- NR (샘플 수·분할·운전점 모두 미확인). 입력 구성은 '특정 단일 주파수 성분' vs '그 성분을 포함한 넓은 대역' 두 종류를 비교.

### [9] 사용 신호
- 신호: 주파수 성분(저주파 대역 → C, 중주파 대역 → ESR; 초록). 기반 신호는 NR — 선행 JPE 2022 는 커패시터 전압·전류의 FFT 성분(2·f1, fsw 지배 성분) 사용 → 본 논문도 유사할 가능성(추론).
- Sampling frequency: Not reported / Full text verification required

### [10] 센서 구성
- Existing inverter sensor only?: **NR (커패시터 전류를 쓴다면 'No' 에 해당 — 선행 논문 기준 추론)**
- 추가 센서: NR (커패시터 전류 센서 가능성)
- Derived / reconstructed: NR

### [11] 전처리 및 Feature Extraction
- 전처리: FFT 로 주파수 성분/대역 추출(초록 취지)
- Feature: 단일 주파수 성분(저/중) 또는 대역 스펙트럼 — 차원 NR

### [12] 진단 기법
- Deep learning: DNN, CNN, Simple RNN, LSTM 4종 비교. 결과: 단일 성분 입력엔 DNN, 광대역 입력엔 CNN 이 최선(초록).
- Hyperparameter: Not reported / Full text verification required

### [13] AI 모델 입력·출력
| Item | Information |
|---|---|
| Input | 주파수 성분(단일) 또는 대역 스펙트럼 |
| Input shape | Not reported / Full text verification required |
| Preprocessing | FFT |
| Feature dimension | Not reported / Full text verification required |
| Model | DNN / CNN / Simple RNN / LSTM |
| Output | C, ESR (회귀) |
| Loss | Not reported / Full text verification required |
| Optimizer | Not reported / Full text verification required |

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- 3상 DC/AC 컨버터 입력 커패시터 C·ESR 추정에 4종 딥러닝 비교(초록)
- 저주파 대역에 C 정보, 중주파 대역에 ESR 정보가 집중됨을 제시(초록)
- 입력 유형(단일 성분 vs 대역)에 따라 최적 모델이 다름: DNN vs CNN(초록)

My interpretation:
'어느 대역이 어느 파라미터를 담는가' 를 DL 입력 설계 관점에서 정리한 점이 유용하다. 내 연구의 '재구성 전류 스펙트럼 → CNN' 은 이 논문의 광대역-CNN 결론과 맞닿지만, 신호원(상전류 재구성)과 센서 조건(기존 센서)이 다르다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **True Online (추정)** — 정상 운전 리플의 주파수 성분을 입력으로 쓰는 구조(초록)이나, 센서·운전 조건·실시간 구현은 NR.
- On-board implementation: Not reported / Full text verification required (오프라인 학습·평가로 보임 — 구현 언급 없음)

### [16] On-board Hardware Environment
| 항목 | 값 |
|---|---|
| DSP | Not reported / Full text verification required |
| MCU | Not reported / Full text verification required |
| FPGA | Not reported / Full text verification required |
| Sampling ADC | Not reported / Full text verification required |
| Memory | Not reported / Full text verification required |
| Sampling frequency | Not reported / Full text verification required |
| Control frequency | Not reported / Full text verification required |
| Execution time | Not reported / Full text verification required |
| Inference time / model size | Not reported / Full text verification required |

### [17] Real-time 가능성
- **Real-time not demonstrated** — 초록에 구현·추론 시간 정보 없음. DNN/CNN 크기에 따라 가능할 수 있음(해석).

### [18] 실험 환경
| Parameter | Value |
|---|---|
| DC-Link Voltage | Not reported / Full text verification required |
| Output Voltage | Not reported / Full text verification required |
| Power | Not reported / Full text verification required |
| Load | Not reported / Full text verification required |
| Motor | Not reported / Full text verification required |
| Motor speed | Not reported / Full text verification required |
| Torque | Not reported / Full text verification required |
| Switching Frequency | Not reported / Full text verification required |
| Fundamental Frequency | Not reported / Full text verification required |
| Modulation | Not reported / Full text verification required |
| Capacitor | Not reported / Full text verification required |
| Sampling Frequency | Not reported / Full text verification required |

### [19] Operating Condition 다양성
- Not reported / Full text verification required

### [20] 최종 성능
- 종합: 정성(모델 간 우열)만 초록에 있음; MAE/RMSE NR
- C error: Not reported / Full text verification required / ESR error: Not reported / Full text verification required / Classification metrics: 해당 없음

### [21] Noise / Robustness
- Not reported / Full text verification required

### [22] 장점
- C·ESR 동시 회귀 + DL 4종 비교라는 설계 정보
- 대역-파라미터 대응(저주파→C, 중주파→ESR) 명시
- 3상 컨버터 대상(단상 선행에서 확장)

### [23] 한계
Authors' stated limitation:
- Not reported / Full text verification required

Additional limitation identified (분석자):
- 센서 조건·실험 여부·정격·데이터셋·오차 모두 미확인(본문 필수)
- 커패시터 전류 센서를 쓴다면 on-board 조건 불리(추론)
- 운전조건 다양성·일반화 검증 NR
- 저널 등급 중간(JEET)

### [24] 내 연구 목표와의 관련성
- **Very High** — 3상 인버터 DC-link C+ESR 를 FFT 성분 → DL 회귀로 다룬 유일한 저널 후보. 내 AI 설계(입력 대역, 모델 선택)에 직접 참고.

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | 3상 DC/AC (2L 추정) | 2-Level 3-Phase |
| Capacitor | DC-link(입력 커패시터) | DC-Link |
| Signal | 주파수 성분(신호원 NR) | Existing inverter signal preferred |
| Aging Target | C + ESR | C / ESR |
| Diagnosis | Regression (DL) | Classification or Regression |
| Online | 추정 Yes | Yes |
| On-board | NR | Yes |
| Extra Sensor | NR | Preferably No |
| AI | Yes (DNN/CNN/RNN/LSTM) | Candidate |
| Real-time | 미시연 | Required |

### [26] 재현 가능성
- **Moderate** — FFT 성분 → DNN/CNN 회귀는 Python 으로 쉽게 구성. 저자의 대역 정의·데이터 생성 조건을 본문에서 확인해야 비교 가능.
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: vC(=vdc), iC(검증용; 내 연구는 재구성 전류로 대체), ia/ib/ic, 스위칭 상태. 변화 파라미터: C×ESR 격자(예 5×5), 부하·변조지수. 데이터셋: 조합별 FFT 저/중 대역 벡터 → C, ESR 회귀, 운전점 기준 분할.

### 선정 점수 (10 기준 × 10점)
| c1 9 | c2 10 | c3 4 | c4 8 | c5 5 | c6 10 | c7 4 | c8 6 | c9 3 | c10 7 | **Total 66** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: 3상 DC-link C+ESR 를 DL 로 회귀한 저널 논문. 입력 대역 설계와 모델 선택(DNN vs CNN) 결론을 그대로 실험 설계에 쓸 수 있다.
- 집중할 Figure/Table/Equation: 입력 대역 정의 표, 데이터 생성 조건(실험/시뮬, 노화 샘플), 4개 모델 구조·hyperparameter 표, C/ESR 오차 표, 단일 성분 vs 대역 비교 그림
- 동반·후속 논문: 선행(단상): H.-J. Park, (Kim), S. Kwak, J. Power Electron. 22:513–521, 2022, DOI 10.1007/s43236-021-00366-x — DNN, FFT 저/중주파 성분, 11개 입력 조합, 실험 파형.

---

## Rank 7 — Tier A — Machines 2022 (3상 AEC)

> **Evidence: Abstract-level only** — 본문 미열람. `Not reported / Full text verification required` 는 초록·스니펫에 없는 항목이며 추측으로 채우지 않았다.

### [1] 기본 논문 정보
- Title: DC-Link Electrolytic Capacitors Monitoring Techniques Based on Advanced Learning Intelligence Techniques for Three-Phase Inverters
- Authors: (확인 필요) 한 탐색 보고는 'Dang, Park, Kwak, Choi' 로 기재했으나 다른 탐색에서는 저자 미표시 — MDPI 페이지에서 확인 필요
- Year: 2022
- Journal: Machines (MDPI), vol. 10, no. 12, art. 1174 (published 7 Dec 2022)
- DOI: 10.3390/machines10121174 (MDPI 관례 패턴 — 직접 확인 안 됨)
- Publication Type: Journal (OA)
- 식별/출처: mdpi.com/2075-1702/10/12/1174; RG 366115422; CAU ScholarWorks 2019.sw.cau/66391
- 저자 소속: Chung-Ang University (ScholarWorks 호스팅 기준; 소속 줄 미확인)

### [2] Converter / Inverter Topology
- Topology: 3상 인버터(2L 추정; 레벨 수 미명시). 정격 NR.
- Power rating: Not reported / Full text verification required / DC-link voltage: Not reported / Full text verification required / AC output voltage: Not reported / Full text verification required
- Switching frequency: Not reported / Full text verification required / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: Not reported / Full text verification required

### [3] Classification vs Regression
- Task: **Regression (C+ESR 추정; 분류 여부 NR)**
- AEC 파라미터 추정('estimate the parameters of an AEC'). Figure 캡션에 C 추정 정확도·ESR 추정 항목이 있어 C 와 ESR 모두 추정으로 보임. '99.9 % accuracy' 가 분류 정확도인지 추정 정확도인지 NR.
- Output 단위: C, ESR (단위 NR)

해당 없음(회귀/연속 지표) 또는 클래스 정의 NR.

### [4] 커패시터 기본 정보
| 항목 | 값 |
|---|---|
| Technology | Aluminum electrolytic (제목) |
| Manufacturer | Not reported / Full text verification required |
| Model | Not reported / Full text verification required |
| Rated C | NR — 미귀속 단서 '107 ~ 554 µF' (다른 MDPI 논문일 가능성; 확인 필요) |
| Rated V | Not reported / Full text verification required |
| Rated ESR | Not reported / Full text verification required |
| Temperature rating | Not reported / Full text verification required |

### [5] 노화 모사 방식
- Not reported / Full text verification required (Figure 1 '열화 지시 곡선' 존재 — 실제/모사 여부 미확인)

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| — | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required |

논문에 나온 값이 스니펫·초록에 없어 표를 채우지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): Not reported / Full text verification required

### [7] C / ESR 변화 여부
- **C + ESR (추정 대상 기준; 데이터 생성 방식 NR)**

### [8] Dataset 구성
- NR

### [9] 사용 신호
- 신호: 전원(source) 전류(핵심 입력; 초록). RG 초록: 입력 전력, 커패시터 전류·전압·전력, 출력 전류·전압·전력 등 여러 신호를 FFT·DWT 로 분석해 비교.
- Sampling frequency: Not reported / Full text verification required

### [10] 센서 구성
- Existing inverter sensor only?: **Yes (초록 취지: source current 를 써서 추가 하드웨어 회피) — 다만 비교 실험에는 커패시터 전류 등도 사용**
- 추가 센서: None (제안 구성 기준)
- Derived / reconstructed: No

### [11] 전처리 및 Feature Extraction
- 전처리: FFT + 저역/고역 통과 필터(LPF1 → C, HPF → ESR; Figure 캡션), DWT
- Feature: FFT 성분, DWT 계수 + 통계 지표(statistical indexes)

### [12] 진단 기법
- 'advanced learning intelligence techniques' (모델명 NR — ANN 계열 추정, 확인 필요). 최적 조합: source current + DWT + 통계 지표(초록 요약).
- Hyperparameter: Not reported / Full text verification required

### [13] AI 모델 입력·출력
| Item | Information |
|---|---|
| Input | 전원 전류(및 비교용 기타 신호) |
| Input shape | Not reported / Full text verification required |
| Preprocessing | FFT+LPF/HPF 또는 DWT |
| Feature dimension | Not reported / Full text verification required |
| Model | 학습 기반(명칭 NR) |
| Output | C, ESR |
| Loss | Not reported / Full text verification required |
| Optimizer | Not reported / Full text verification required |

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- 전원 전류로 3상 인버터 AEC 상태 평가 → 추가 하드웨어 불필요·비용 절감(초록)
- 여러 입력 신호·전처리(FFT/DWT) 조합을 비교(초록)
- source current + DWT + 통계 지표 조합이 99.9 % 정확도(초록 요약)

My interpretation:
신호 선택 연구(어떤 신호·전처리가 가장 좋은가)로서 가치가 있다. 내 연구에서 '상전류(또는 전원 전류) 기반 feature 가 vdc 못지않게 정보를 담는다' 는 근거로 쓸 수 있으나, 정확도 정의와 데이터가 확인되기 전엔 인용을 보류해야 한다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **True Online (추정)** — 정상 운전 신호(전원 전류)만 쓰는 구조. 운전 조건·실시간 구현 NR.
- On-board implementation: Not reported / Full text verification required

### [16] On-board Hardware Environment
| 항목 | 값 |
|---|---|
| DSP | Not reported / Full text verification required |
| MCU | Not reported / Full text verification required |
| FPGA | Not reported / Full text verification required |
| Sampling ADC | Not reported / Full text verification required |
| Memory | Not reported / Full text verification required |
| Sampling frequency | Not reported / Full text verification required |
| Control frequency | Not reported / Full text verification required |
| Execution time | Not reported / Full text verification required |
| Inference time / model size | Not reported / Full text verification required |

### [17] Real-time 가능성
- **Real-time not demonstrated** — DWT+통계 지표+학습 모델은 가볍지만 구현 언급 없음.

### [18] 실험 환경
| Parameter | Value |
|---|---|
| DC-Link Voltage | Not reported / Full text verification required |
| Output Voltage | Not reported / Full text verification required |
| Power | Not reported / Full text verification required |
| Load | Not reported / Full text verification required |
| Motor | Not reported / Full text verification required |
| Motor speed | Not reported / Full text verification required |
| Torque | Not reported / Full text verification required |
| Switching Frequency | Not reported / Full text verification required |
| Fundamental Frequency | Not reported / Full text verification required |
| Modulation | Not reported / Full text verification required |
| Capacitor | Not reported / Full text verification required |
| Sampling Frequency | Not reported / Full text verification required |

### [19] Operating Condition 다양성
- Not reported / Full text verification required

### [20] 최종 성능
- 종합: '99.9 % accuracy' (정의·대상 NR)
- C error: Not reported / Full text verification required / ESR error: Not reported / Full text verification required / Classification metrics: NR (분류 여부 불명)

### [21] Noise / Robustness
- Not reported / Full text verification required

### [22] 장점
- 여러 신호·전처리 조합의 체계적 비교(신호 선택 근거)
- 전원 전류 = 기존 센서
- OA (본문 확보 쉬움)

### [23] 한계
Authors' stated limitation:
- Not reported / Full text verification required

Additional limitation identified (분석자):
- 저자·모델·정확도 정의·노화 방식 미확인
- '99.9 %' 는 단일 운전점 과적합 가능성(추론)
- MDPI 저널 → 근거 등급 중간

### [24] 내 연구 목표와의 관련성
- **High** — 3상 인버터 + 기존 센서 + 학습 기반 C/ESR 추정이라는 점에서 직접 관련. 검증 수준이 불명해 Very High 는 보류.

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | 3상 인버터(2L 추정) | 2-Level 3-Phase |
| Capacitor | DC-link AEC | DC-Link |
| Signal | 전원 전류 (기존 센서) | Existing inverter signal preferred |
| Aging Target | C + ESR | C / ESR |
| Diagnosis | 학습 기반 추정 | Classification or Regression |
| Online | 추정 Yes | Yes |
| On-board | NR | Yes |
| Extra Sensor | No | Preferably No |
| AI | Yes | Candidate |
| Real-time | 미시연 | Required |

### [26] 재현 가능성
- **Easy~Moderate** — 전원/상전류 DWT 통계 지표 → 학습 모델은 간단. 저자 조건은 OA 본문에서 바로 확인 가능.
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: 전원 전류(또는 상전류), vdc, iC(검증). 변화 파라미터: C·ESR 격자. 데이터셋: DWT 레벨별 통계 지표 벡터.

### 선정 점수 (10 기준 × 10점)
| c1 9 | c2 10 | c3 4 | c4 8 | c5 8 | c6 8 | c7 4 | c8 7 | c9 6 | c10 6 | **Total 70** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: '어떤 신호 + 어떤 전처리' 가 AEC 파라미터 추정에 가장 좋은지를 비교한 OA 논문 — 내 feature 설계의 비교 근거.
- 집중할 Figure/Table/Equation: 신호 조합 비교표(Table), 필터 주파수 범위 표(tbl6), DWT 레벨·통계 지표 정의, 정확도 정의와 결과표, 노화 곡선(Fig. 1)
- 동반·후속 논문: 같은 그룹 학회판: Dang et al., ICBIR 2023 (필름 커패시터, DWT, 99.85 %).

---

## Rank 8 — Tier B — Zhao 2023 TPEL (grey-box)

> **Evidence: Abstract-level only** — 본문 미열람. `Not reported / Full text verification required` 는 초록·스니펫에 없는 항목이며 추측으로 채우지 않았다.

### [1] 기본 논문 정보
- Title: A Transient-Modeling-Based Grey-Box Method for Online Monitoring of DC-Link Capacitors (제목 표기 VBN 레코드 기준 — 하이픈 등 정확 표기 확인 필요)
- Authors: (S.) Zhao, Hu, He, Lu, H. H. C. Iu, F. Blaabjerg, P. Davari (이름 이니셜 일부 NR)
- Year: 2023
- Journal: IEEE Transactions on Power Electronics, vol. 38, no. 11, pp. 14547–14562 (Nov. 2023)
- DOI: 10.1109/TPEL.2023.3308115
- Publication Type: Journal (2023 TPEL Second Place Prize Paper Award — VBN)
- 식별/출처: IEEE Xplore 10229504; AAU VBN(AAM PDF 547236531/FINAL_VERSION.pdf — 본 환경에서 미열람)
- 저자 소속: Southwest Jiaotong Univ., Chongqing Univ., Univ. of Western Australia, Aalborg Univ. (스니펫)

### [2] Converter / Inverter Topology
- Topology: 일반 DC-link(토폴로지 비의존). 시뮬: AC/DC 및 DC/DC 시스템; 실험: 상용 전원장치(commercial power supply). 2L 인버터 실험 아님.
- Power rating: Not reported / Full text verification required / DC-link voltage: Not reported / Full text verification required / AC output voltage: Not reported / Full text verification required
- Switching frequency: Not reported / Full text verification required / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: 상용 전원장치

### [3] Classification vs Regression
- Task: **Regression (C via damping factor α)**
- DC-link 전압 과도의 병렬 RLC 영상태 응답에서 감쇠 계수 α 를 HI 로 추출 → C 추정.
- Output 단위: α, C

해당 없음(회귀/연속 지표) 또는 클래스 정의 NR.

### [4] 커패시터 기본 정보
| 항목 | 값 |
|---|---|
| Technology | Not reported / Full text verification required |
| Manufacturer | Not reported / Full text verification required |
| Model | Not reported / Full text verification required |
| Rated C | Not reported / Full text verification required |
| Rated V | Not reported / Full text verification required |
| Rated ESR | Not reported / Full text verification required |
| Temperature rating | Not reported / Full text verification required |

### [5] 노화 모사 방식
- Not reported / Full text verification required

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| — | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required |

논문에 나온 값이 스니펫·초록에 없어 표를 채우지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): Not reported / Full text verification required

### [7] C / ESR 변화 여부
- **C (α 는 C 에 비례; ESR 변경 여부 NR)**

### [8] Dataset 구성
- 해당 없음(grey-box 모델)

### [9] 사용 신호
- 신호: DC-link 전압 과도(대신호 과도) — '극히 낮은 샘플링 주파수' 로 충분(초록)
- Sampling frequency: 수치 NR ('extremely low sampling frequency')

### [10] 센서 구성
- Existing inverter sensor only?: **Yes (전압 센서만)**
- 추가 센서: None
- Derived / reconstructed: No

### [11] 전처리 및 Feature Extraction
- 전처리: 과도 구간 분리·피팅(세부 NR)
- Feature: 감쇠 계수 α

### [12] 진단 기법
- Grey-box: 과도 등가회로 모델(TECM) + 파라미터 피팅. 토폴로지·제어 지식 최소 요구(초록).
- Hyperparameter: 해당 없음

### [13] AI 모델 입력·출력
AI 모델 아님(분석적/모델 기반 방법).

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- 과도 모델링 기반 grey-box 온라인 감시(제목)
- α 를 HI 로 하는 TECM — 토폴로지·제어 지식 최소(초록)
- 극히 낮은 샘플링 요구(초록)
- α·C 추정 오차 1 % 미만(실험, 초록)

My interpretation:
'전압 센서 하나 + 자연 과도 + 저샘플링' 으로 1 % 미만을 달성한 점이 강점. 연속 감시가 아니라 과도 이벤트가 있을 때만 갱신되므로 True Online 과는 구분해야 한다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **Quasi-Online (이벤트형: 자연 발생 대신호 과도 필요)** — 정상 운전을 멈추지는 않지만 과도가 있어야 추정(초록 취지).
- On-board implementation: Not reported / Full text verification required

### [16] On-board Hardware Environment
| 항목 | 값 |
|---|---|
| DSP | Not reported / Full text verification required |
| MCU | Not reported / Full text verification required |
| FPGA | Not reported / Full text verification required |
| Sampling ADC | Not reported / Full text verification required |
| Memory | Not reported / Full text verification required |
| Sampling frequency | 극저 샘플링(수치 NR) |
| Control frequency | Not reported / Full text verification required |
| Execution time | Not reported / Full text verification required |
| Inference time / model size | 해당 없음 |

### [17] Real-time 가능성
- **Real-time feasible** — 저샘플링 과도 피팅은 계산량이 작다(해석). 구현 시연 NR.

### [18] 실험 환경
| Parameter | Value |
|---|---|
| DC-Link Voltage | Not reported / Full text verification required |
| Output Voltage | Not reported / Full text verification required |
| Power | Not reported / Full text verification required |
| Load | 상용 전원장치 |
| Motor | 해당 없음 |
| Motor speed | 해당 없음 |
| Torque | 해당 없음 |
| Switching Frequency | Not reported / Full text verification required |
| Fundamental Frequency | Not reported / Full text verification required |
| Modulation | Not reported / Full text verification required |
| Capacitor | Not reported / Full text verification required |
| Sampling Frequency | Not reported / Full text verification required |

### [19] Operating Condition 다양성
- Not reported / Full text verification required

### [20] 최종 성능
- 종합: α·C 오차 <1 % (실험, 초록)
- C error: <1 % / ESR error: 해당 없음 / Classification metrics: 해당 없음

### [21] Noise / Robustness
- 토폴로지·제어 지식 최소 요구(초록). 노이즈·온도 NR.

### [22] 장점
- 전압 센서만
- 저샘플링 → 저가 구현
- <1 % 실험 정확도
- 수상 논문(방법 품질)

### [23] 한계
Authors' stated limitation:
- Not reported / Full text verification required

Additional limitation identified (분석자):
- 2L 인버터 실험 아님(상용 전원장치)
- 과도 이벤트 의존 → 연속 감시 불가
- C only
- 노화 샘플 NR

### [24] 내 연구 목표와의 관련성
- **Medium** — 물리 모델·저샘플링 설계의 참고. 내 목표(연속 True Online, C+ESR, 2L)와는 구조가 다름.

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | 일반(실험: 전원장치) | 2-Level 3-Phase |
| Capacitor | DC-link | DC-Link |
| Signal | vdc 과도 | Existing inverter signal preferred |
| Aging Target | C(α) | C / ESR |
| Diagnosis | Regression | Classification or Regression |
| Online | 이벤트형 | Yes |
| On-board | NR | Yes |
| Extra Sensor | No | Preferably No |
| AI | No | Candidate |
| Real-time | 미시연 | Required |

### [26] 재현 가능성
- **Moderate** — 과도 RLC 피팅은 쉽지만 TECM 정의·과도 검출 로직은 본문 필요. AAM PDF 가 공개되어 로컬 확보 가능.
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: vdc(부하 스텝 전후), 부하 전류. 변화 파라미터: C 단계. 데이터셋: 과도 구간별 α.

### 선정 점수 (10 기준 × 10점)
| c1 5 | c2 10 | c3 8 | c4 7 | c5 10 | c6 8 | c7 3 | c8 8 | c9 8 | c10 6 | **Total 73** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: 전압 센서만으로 1 % 미만을 낸 물리 모델(과도) 기준점. 내 리플 기반 방법의 '보조 경로(과도 시 C 교정)' 로 검토.
- 집중할 Figure/Table/Equation: TECM 유도(병렬 RLC, α 정의), 샘플링 요구 분석, 실험 셋업·오차 표
- 동반·후속 논문: 같은 흐름: Dai, Zhao, Han, Sun, Chen, IEEE JESTPE 12(2):2281–2291, 2024, DOI 10.1109/JESTPE.2024.3370616 (부하 변화 과도 + 전류 적분 재구성, 저샘플링).

---

## Rank 9 — Tier B — Al-Wesabi 2025 Results in Eng.

> **Evidence: Abstract-level only** — 본문 미열람. `Not reported / Full text verification required` 는 초록·스니펫에 없는 항목이며 추측으로 채우지 않았다.

### [1] 기본 논문 정보
- Title: Capacitance estimation algorithm based on DC-link voltage ripples using hybrid machine learning techniques in power electronics converters
- Authors: Ibrahim AL-Wesabi, Abdullrahman A. Al-Shamma'a, Hassan M. Hussein Farh, (Al Dawood), (Mwakipunda), (Xu) — ScienceDirect 저자 목록(일부 이름 NR)
- Year: 2025
- Journal: Results in Engineering (Elsevier, OA), vol. 27, art. 106216
- DOI: (확인 필요) PII S2590123025022881
- Publication Type: Journal (OA)
- 식별/출처: sciencedirect.com/science/article/pii/S2590123025022881
- 저자 소속: Not reported / Full text verification required

### [2] Converter / Inverter Topology
- Topology: 전력전자 컨버터 일반(풍력 터빈 컨버터 맥락 언급). 2L 여부 NR.
- Power rating: Not reported / Full text verification required / DC-link voltage: Not reported / Full text verification required / AC output voltage: Not reported / Full text verification required
- Switching frequency: Not reported / Full text verification required / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: Not reported / Full text verification required

### [3] Classification vs Regression
- Task: **Regression (C)**
- DC-link 커패시턴스 연속 추정. (한 탐색은 'C and ESR' 로 보고 — ESR 포함 여부 확인 필요)
- Output 단위: C (µF)

해당 없음(회귀/연속 지표) 또는 클래스 정의 NR.

### [4] 커패시터 기본 정보
| 항목 | 값 |
|---|---|
| Technology | Not reported / Full text verification required |
| Manufacturer | Not reported / Full text verification required |
| Model | Not reported / Full text verification required |
| Rated C | Not reported / Full text verification required |
| Rated V | Not reported / Full text verification required |
| Rated ESR | Not reported / Full text verification required |
| Temperature rating | Not reported / Full text verification required |

### [5] 노화 모사 방식
- Not reported / Full text verification required

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| — | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required |

논문에 나온 값이 스니펫·초록에 없어 표를 채우지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): Not reported / Full text verification required

### [7] C / ESR 변화 여부
- **C only (초록 기준)**

### [8] Dataset 구성
- NR

### [9] 사용 신호
- 신호: DC-link 전압 리플; '컨버터의 접근 가능한 입·출력 단자 데이터' 만 사용(초록). 불확실 단서: 100 Hz·300 Hz 정류 리플 고조파 사용(이전 판 귀속 가능).
- Sampling frequency: Not reported / Full text verification required

### [10] 센서 구성
- Existing inverter sensor only?: **Yes (초록: 'no extra sensors or hardware')**
- 추가 센서: None
- Derived / reconstructed: No

### [11] 전처리 및 Feature Extraction
- 전처리: Not reported / Full text verification required
- Feature: vdc 리플 기반 특징(정의 NR)

### [12] 진단 기법
- ML 회귀 비교: RF, KNN, ANN, GB, DT, LR (+BR) → 하이브리드 ANN-GB-LR 제안.
- Hyperparameter: Not reported / Full text verification required

### [13] AI 모델 입력·출력
| Item | Information |
|---|---|
| Input | vdc 리플(및 단자 데이터) |
| Input shape | Not reported / Full text verification required |
| Preprocessing | Not reported / Full text verification required |
| Feature dimension | Not reported / Full text verification required |
| Model | ANN-GB-LR 하이브리드 |
| Output | C |
| Loss | Not reported / Full text verification required |
| Optimizer | Not reported / Full text verification required |

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- 접근 가능한 단자 데이터만으로 C 예측(초록)
- 하이브리드 ANN-GB-LR 이 평균 오차 0.142 %, R²≈1 (초록)
- RMSE 0.0070 µF, MAE 0.0049 µF (highlights — 단위 타당성 의문)

My interpretation:
수치는 가장 작지만 토폴로지·실험 여부·노화 방식이 불명해 '시뮬레이션 내 보간 성능' 일 가능성을 배제할 수 없다. 회귀 모델 비교 프로토콜(6종 + 하이브리드)은 참고 가치가 있다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **True Online (주장)** — 정상 운전 리플만 사용한다는 초록 취지. 실험·구현 NR.
- On-board implementation: Not reported / Full text verification required

### [16] On-board Hardware Environment
| 항목 | 값 |
|---|---|
| DSP | Not reported / Full text verification required |
| MCU | Not reported / Full text verification required |
| FPGA | Not reported / Full text verification required |
| Sampling ADC | Not reported / Full text verification required |
| Memory | Not reported / Full text verification required |
| Sampling frequency | Not reported / Full text verification required |
| Control frequency | Not reported / Full text verification required |
| Execution time | Not reported / Full text verification required |
| Inference time / model size | Not reported / Full text verification required |

### [17] Real-time 가능성
- **Real-time not demonstrated** — 구현·추론 시간 언급 없음.

### [18] 실험 환경
| Parameter | Value |
|---|---|
| DC-Link Voltage | Not reported / Full text verification required |
| Output Voltage | Not reported / Full text verification required |
| Power | Not reported / Full text verification required |
| Load | Not reported / Full text verification required |
| Motor | Not reported / Full text verification required |
| Motor speed | Not reported / Full text verification required |
| Torque | Not reported / Full text verification required |
| Switching Frequency | Not reported / Full text verification required |
| Fundamental Frequency | Not reported / Full text verification required |
| Modulation | Not reported / Full text verification required |
| Capacitor | Not reported / Full text verification required |
| Sampling Frequency | Not reported / Full text verification required |

### [19] Operating Condition 다양성
- Not reported / Full text verification required

### [20] 최종 성능
- 종합: 평균 C 오차 0.142 % (하이브리드); 비교 DT 0.624 / GB 0.586 / BR 0.182 / KNN 0.322 / RF 0.304 %; 최대 오차 1.1–1.3 %(모델별)
- C error: 0.142 % 평균, RMSE 0.0070 µF, MAE 0.0049 µF (단위 확인 필요) / ESR error: NR/해당 없음 / Classification metrics: 해당 없음

### [21] Noise / Robustness
- Not reported / Full text verification required

### [22] 장점
- 센서 추가 없음
- 정량 성능이 가장 상세(모델 비교표)
- OA

### [23] 한계
Authors' stated limitation:
- Not reported / Full text verification required

Additional limitation identified (분석자):
- 토폴로지·실험 여부·노화 방식 NR → 성능 해석 불가
- C only
- RMSE/MAE 의 µF 단위가 DC-link 용량 대비 비현실적으로 작음(단위 오기 가능)
- 저널 등급 중간

### [24] 내 연구 목표와의 관련성
- **Medium** — AI 회귀 벤치마크 수치로만 유용. 2L·on-board 조건 미확인.

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | NR | 2-Level 3-Phase |
| Capacitor | DC-link | DC-Link |
| Signal | vdc 리플(단자 데이터) | Existing inverter signal preferred |
| Aging Target | C | C / ESR |
| Diagnosis | Regression (ML) | Classification or Regression |
| Online | 주장 Yes | Yes |
| On-board | NR | Yes |
| Extra Sensor | No | Preferably No |
| AI | Yes | Candidate |
| Real-time | 미시연 | Required |

### [26] 재현 가능성
- **Easy (시뮬레이션 기준)** — vdc 리플 특징 → 회귀 비교는 즉시 가능. 저자 데이터 조건은 OA 본문에서 확인.
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: vdc, 입·출력 단자 전압·전류. 변화 파라미터: C 다단계. 데이터셋: 운전점×C 리플 특징 → 회귀 6종 비교.

### 선정 점수 (10 기준 × 10점)
| c1 5 | c2 10 | c3 4 | c4 9 | c5 9 | c6 8 | c7 4 | c8 6 | c9 9 | c10 6 | **Total 70** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: 회귀 모델 6종 + 하이브리드의 정량 비교. 내 회귀 실험의 '비교 모델 세트' 로 바로 차용.
- 집중할 Figure/Table/Equation: 특징 정의 절, 데이터 생성 조건(시뮬/실험, 운전점), 모델별 오차 표(단위 확인), 하이브리드 구조 그림
- 동반·후속 논문: 관련: Abo-Khalil et al., Energies 12(12):2369, 2019 (PSO-SVR C, 3상 B2B, 실험).

---

## Rank 10 — Tier B — Liao 2020 MPE (ER rule)

> **Evidence: Abstract-level only** — 본문 미열람. `Not reported / Full text verification required` 는 초록·스니펫에 없는 항목이며 추측으로 채우지 않았다.

### [1] 기본 논문 정보
- Title: Fault Diagnosis of Capacitance Aging in DC Link Capacitors of Voltage Source Inverters Using Evidence Reasoning Rule
- Authors: Linhao Liao, Haibo Gao, Yelan He, Xiaobin Xu, Zhiguo Lin, Yajie Chen, Fubing You
- Year: 2020
- Journal: Mathematical Problems in Engineering (Hindawi/Wiley, OA), vol. 2020, art. 5724019, pp. 1–12 (published 31 Mar 2020)
- DOI: 10.1155/2020/5724019
- Publication Type: Journal (OA)
- 식별/출처: onlinelibrary.wiley.com/doi/10.1155/2020/5724019; hindawi.com; ideas.repec.org hin/jnlmpe/5724019
- 저자 소속: Not reported / Full text verification required

### [2] Converter / Inverter Topology
- Topology: 전압형 인버터(VSI) 시뮬레이션. 레벨 수 미명시(일반 VSI = 2L 추정).
- Power rating: Not reported / Full text verification required / DC-link voltage: Not reported / Full text verification required / AC output voltage: Not reported / Full text verification required
- Switching frequency: Not reported / Full text verification required / Fundamental frequency: Not reported / Full text verification required / Modulation: Not reported / Full text verification required / Load·motor: Not reported / Full text verification required

### [3] Classification vs Regression
- Task: **Classification (3 ranges: normal / incipient fault / failed) — 노화 등급 판정**
- C 잔존율 구간으로 등급 정의. '등급 추정(aging fault level)' 이라 소프트 분류(증거 융합 신뢰도)일 수 있음.
- Output 단위: 등급(및 증거 융합 신뢰도)

| Class | 의미 | C | ESR |
|---|---|---|---|
| 0 | Normal | C = 초기값의 90–100 % | Not reported / Full text verification required |
| 1 | Incipient fault | C = 초기값의 80–90 % | Not reported / Full text verification required |
| 2 | Failed (no longer incipient) | C < 초기값의 80 % | Not reported / Full text verification required |

### [4] 커패시터 기본 정보
| 항목 | 값 |
|---|---|
| Technology | Not reported / Full text verification required |
| Manufacturer | 해당 없음(시뮬) |
| Model | 해당 없음 |
| Rated C | 7500 µF (시뮬레이션 초기 설정값, 본문 스니펫) |
| Rated V | Not reported / Full text verification required |
| Rated ESR | Not reported / Full text verification required |
| Temperature rating | Not reported / Full text verification required |

### [5] 노화 모사 방식
- Simulation — C 를 초기값 대비 여러 수준으로 감소. 서론 기준: C −20 % 또는 ESR ×2 = 수명 종료.

### [6] Aging Sample 파라미터
| Sample | Health State | C | C Change | ESR | ESR Change |
|---|---|---:|---:|---:|---:|
| S1 | Normal | 초기값(7500 µF)의 90–100 % (µF 수치 NR) | 0 ~ −10 % | Not reported / Full text verification required | Not reported / Full text verification required |
| S2 | Incipient fault | 초기값의 80–90 % (µF 수치 NR) | −10 ~ −20 % | Not reported / Full text verification required | Not reported / Full text verification required |
| S3 | Failed | 초기값의 <80 % (µF 수치 NR) | < −20 % | Not reported / Full text verification required | Not reported / Full text verification required |

구간 경계(%)만 본문 스니펫에 있음. 구간 내 개별 시뮬 값·µF 환산값·ESR 설정은 논문 표기가 확인되지 않아 적지 않았다(추정 금지 규칙).
- Radd (ESR 모사 직렬 저항): 해당 없음(시뮬; ESR 변경 여부 NR)

### [7] C / ESR 변화 여부
- **C only (스니펫 기준)**

### [8] Dataset 구성
- NR (샘플 수·분할 미확인; '증거' 는 vdc 특징)

### [9] 사용 신호
- 신호: DC-link 전압 특징(진단 증거)
- Sampling frequency: Not reported / Full text verification required

### [10] 센서 구성
- Existing inverter sensor only?: **Yes (vdc 만)**
- 추가 센서: None
- Derived / reconstructed: No

### [11] 전처리 및 Feature Extraction
- 전처리: Not reported / Full text verification required
- Feature: vdc 에서 추출한 특징(종류 NR) → 각 특징을 증거로 변환

### [12] 진단 기법
- Evidence Reasoning(ER) rule 융합(증거 가중치 조정 가능) vs BP 신경망 비교.
- Hyperparameter: Not reported / Full text verification required

### [13] AI 모델 입력·출력
| Item | Information |
|---|---|
| Input | vdc 특징 |
| Input shape | Not reported / Full text verification required |
| Preprocessing | Not reported / Full text verification required |
| Feature dimension | Not reported / Full text verification required |
| Model | ER rule (vs BP-NN) |
| Output | 노화 등급(3 구간) |
| Loss | 해당 없음 |
| Optimizer | 해당 없음 |

### [14] 저자 주장 Contribution vs 내 해석
Authors' claimed contributions (초록·스니펫에서 확인된 범위):
- vdc 특징을 증거로 ER rule 로 융합해 노화 등급 추정(초록)
- BP-NN 보다 우수(초록)
- 증거별 가중치 조정 가능(초록)
- ANN 은 학습 샘플 수에 정확도가 제한됨을 지적(서론)

My interpretation:
이 조사에서 '등급 경계(90/80 %)' 를 명시한 유일한 저널 후보. 내 분류 라벨 설계(정상/초기/고장) 의 출발점으로 쓸 수 있으나, 시뮬레이션 전용·C only·특징 정의 불명이라 방법 자체보다 라벨 정의를 참고한다(해석).

### [15] On-board / Online 여부
- Diagnosis Type: **Quasi-Online/주장 Online (시뮬레이션)** — 'online monitoring method' 라 하나 시뮬레이션만, 구현 없음.
- On-board implementation: No (시뮬레이션)

### [16] On-board Hardware Environment
| 항목 | 값 |
|---|---|
| DSP | 해당 없음 |
| MCU | 해당 없음 |
| FPGA | 해당 없음 |
| Sampling ADC | 해당 없음 |
| Memory | 해당 없음 |
| Sampling frequency | Not reported / Full text verification required |
| Control frequency | Not reported / Full text verification required |
| Execution time | Not reported / Full text verification required |
| Inference time / model size | Not reported / Full text verification required |

### [17] Real-time 가능성
- **Offline post-processing only** — 시뮬레이션 데이터의 후처리.

### [18] 실험 환경
| Parameter | Value |
|---|---|
| DC-Link Voltage | Not reported / Full text verification required |
| Output Voltage | Not reported / Full text verification required |
| Power | Not reported / Full text verification required |
| Load | Not reported / Full text verification required |
| Motor | Not reported / Full text verification required |
| Motor speed | Not reported / Full text verification required |
| Torque | Not reported / Full text verification required |
| Switching Frequency | Not reported / Full text verification required |
| Fundamental Frequency | Not reported / Full text verification required |
| Modulation | Not reported / Full text verification required |
| Capacitor | 7500 µF(초기) |
| Sampling Frequency | Not reported / Full text verification required |

### [19] Operating Condition 다양성
- Not reported / Full text verification required

### [20] 최종 성능
- 종합: BP-NN 대비 우수(수치 NR)
- C error: 해당 없음 / ESR error: 해당 없음 / Classification metrics: Accuracy/F1/혼동행렬 NR

### [21] Noise / Robustness
- 증거 가중치 조정으로 강건성 조절 가능(초록 취지). 노이즈·운전조건 NR.

### [22] 장점
- 등급 경계(90/80 %) 명시
- vdc 만 사용
- 소표본에서 ANN 대안(ER rule)
- OA

### [23] 한계
Authors' stated limitation:
- (서론) ANN 은 학습 샘플 수에 제한 — 저자가 ER rule 로 대체한 동기

Additional limitation identified (분석자):
- 시뮬레이션 전용, 실험 없음
- C only, ESR 미고려
- 특징·성능 수치 NR
- 저널 등급 낮음(MPE)

### [24] 내 연구 목표와의 관련성
- **Medium** — 분류 라벨 설계 참고용. 2L 실험·on-board·ESR 요소 없음.

### [25] 내 연구와의 비교
| Item | Paper | My Target |
|---|---|---|
| Topology | VSI 시뮬(2L 추정) | 2-Level 3-Phase |
| Capacitor | DC-link | DC-Link |
| Signal | vdc 특징 | Existing inverter signal preferred |
| Aging Target | C (3 구간) | C / ESR |
| Diagnosis | Classification(3) | Classification or Regression |
| Online | 시뮬 | Yes |
| On-board | No | Yes |
| Extra Sensor | No | Preferably No |
| AI | ER rule / BP-NN | Candidate |
| Real-time | 후처리 | Required |

### [26] 재현 가능성
- **Easy** — Simulink 에서 C 를 90/80 % 경계로 바꾸고 vdc 특징을 뽑는 것은 바로 가능. ER rule 구현은 본문 수식 필요(OA).
- MATLAB/Simulink + 실험 인버터 기준 준비물: 저장 신호: vdc. 변화 파라미터: C 100→70 % 를 2.5–5 % 간격. 데이터셋: 구간별 라벨 + vdc 특징.

### 선정 점수 (10 기준 × 10점)
| c1 7 | c2 10 | c3 2 | c4 6 | c5 8 | c6 6 | c7 6 | c8 6 | c9 3 | c10 8 | **Total 62** |
|---|---|---|---|---|---|---|---|---|---|---|

### 읽기 포인트
- 왜 읽어야 하는가: 분류 등급 정의(정상 90–100 % / 초기 80–90 % / 고장 <80 %)를 명시한 유일한 후보 — 라벨 설계의 출발점.
- 집중할 Figure/Table/Equation: 등급 정의 표, 특징(증거) 정의, ER 융합 수식, BP-NN 비교 결과표
- 동반·후속 논문: 분류 참고(학회): Seferian, Bazzi, Hajj, ECCE 2020 (3 클래스 healthy/half/fully degraded, 99 %, 저가 MCU, 단상 PV 시뮬).

---

## 8. Aging Emulation Comparison

| Paper | 노화 구현 | C / ESR 변화 | Radd | 샘플 표 |
|---|---|---|---|---|
| Ghadrdan 2022 TPEL | NR | Not reported / Full text verification required | Not reported / Full text verif | 없음 |
| Örüklü & Ağalar 2025 TIE | NR | C only | Not reported / Full text verif | 없음 |
| Lipnicki & Lewandowski 2017 PED | Not reported / Full text verification required | ESR only | Not reported / Full text verif | 없음 |
| Hasegawa & Hirose 2024 TIA | NR | C + ESR | Not reported / Full text verif | 없음 |
| Sundararajan 2018 TIA | NR | ESR only | Not reported / Full text verif | 없음 |
| Park & Kwak 2023 JEET | NR | C + ESR | Not reported / Full text verif | 없음 |
| Machines 2022 (3상 AEC) | Not reported / Full text verification required | C + ESR | Not reported / Full text verif | 없음 |
| Zhao 2023 TPEL (grey-box) | Not reported / Full text verification required | C | Not reported / Full text verif | 없음 |
| Al-Wesabi 2025 Results in Eng. | Not reported / Full text verification required | C only | Not reported / Full text verif | 없음 |
| Liao 2020 MPE (ER rule) | Simulation | C only | 해당 없음(시뮬; ESR 변경 여부 NR) | 표 있음(구간) |

(사실) 10편 중 노화 구현 방식이 초록·스니펫에서 확인된 것은 Liao 2020(시뮬레이션에서 C 감소)뿐이며, 실험 논문(Ghadrdan, Örüklü, Hasegawa, Sundararajan, Zhao)은 '실험 검증' 만 언급한다. Top 10 밖에서는 Lee 2008 TIA(가속 열화 커패시터), Nakirimoto SBAI 2023(커패시터 지그 + 노화 샘플), Raqib/Nottingham(가속 노화 커패시터, Siemens G120C), Baumann 2024(가속 열화 + 현장 153대)가 실제 노화를 사용했다.
(해석) 저널 Top 10 에서 '실제 가속 노화' 를 명시한 2-Level 논문은 없고, 파라미터 모사(커패시터 교체/저항 추가)인지조차 초록에서 드러나지 않는다 → 본문 확인이 반드시 필요한 1순위 항목.

---

## 9. C / ESR Sample Comparison

| Paper | C 값(샘플) | ESR 값(샘플) | 동시 변화 |
|---|---|---|---|
| Ghadrdan 2022 TPEL | Not reported / Full text verification required | Not reported / Full text verification required | Not reported / Full text verification required |
| Örüklü & Ağalar 2025 TIE | Not reported / Full text verification required | Not reported / Full text verification required | C only |
| Lipnicki & Lewandowski 2017 PED | Not reported / Full text verification required | Not reported / Full text verification required | ESR only |
| Hasegawa & Hirose 2024 TIA | Not reported / Full text verification required | Not reported / Full text verification required | C + ESR |
| Sundararajan 2018 TIA | Not reported / Full text verification required | Not reported / Full text verification required | ESR only |
| Park & Kwak 2023 JEET | Not reported / Full text verification required | Not reported / Full text verification required | C + ESR |
| Machines 2022 (3상 AEC) | Not reported / Full text verification required | Not reported / Full text verification required | C + ESR |
| Zhao 2023 TPEL (grey-box) | Not reported / Full text verification required | Not reported / Full text verification required | C |
| Al-Wesabi 2025 Results in Eng. | Not reported / Full text verification required | Not reported / Full text verification required | C only |
| Liao 2020 MPE (ER rule) | 초기값(7500 µF)의 90–100 % (µF 수치 NR); 초기값의 80–90 % (µF 수치 NR); 초기값의 <80 % (µF 수치 NR) | Not reported / Full text verification required; Not reported / Full text verification required; Not reported / Full text verification required | C only |

(사실) 샘플별 수치를 제시할 수 있는 논문은 Liao 2020(초기 7500 µF, 구간 90–100 / 80–90 / <80 %)뿐이다. 표의 µF 환산은 분석자가 비율로 계산한 값이며 논문 표기가 아니다. 나머지 9편은 `Not reported / Full text verification required`.
(해석) 문헌 공통의 EoL 기준(전해: C −20 %, ESR ×2; Amaral 2023·Liao 2020 서론, Sundararajan 인용 'ESR >200 %, C <80 %', Abo-Khalil 2019 'C 25 % 변화')을 기준으로 내 샘플 격자를 설계하되, 각 논문의 실제 샘플 값은 본문 확보 후 이 표를 갱신한다.

---

## 10. Classification Papers (요청 항목 [28])

Top 10 중 분류형은 Liao 2020(3 구간)뿐이다. 분류 설계 참고를 위해 Top 10 밖(학회 포함)을 명시 표기하여 함께 적는다.

| Paper | Classes | Aging Parameter per Class | Input Signal | Preprocessing | Model | Samples | Accuracy | On-board |
|---:|---:|---|---|---|---|---:|---:|---|
| Örüklü & Ağalar 2025 TIE | 회귀(클래스 없음) | Not reported / Full text verification required | DC-link 전압 리플 (PSD 입력) | PSD | ML 회귀 (명칭 NR; GPR 은 후속 논문) | NR (샘플 수·분할·운전점 종류 모두 미확인) | 'high accuracy' (수치 NR). '<2 % 평균 예측 오차' 는 후속 논문 귀 | Not reported / Full text verification re |
| Park & Kwak 2023 JEET | 회귀(클래스 없음) | Not reported / Full text verification required | 주파수 성분(저주파 대역 → C, 중주파 대역 → ESR; 초록) | FFT 로 주파수 성분/대역 추출 | DNN / CNN / Simple RNN / LSTM | NR (샘플 수·분할·운전점 모두 미확인) | 정성(모델 간 우열)만 초록에 있음; MAE/RMSE NR | Not reported / Full text verification re |
| Machines 2022 (3상 AEC) | 회귀(클래스 없음) | Not reported / Full text verification required | 전원(source) 전류(핵심 입력; 초록) | FFT + 저역/고역 통과 필터 | 학습 기반(명칭 NR) | NR | '99.9 % accuracy' (정의·대상 NR) | Not reported / Full text verification re |
| Al-Wesabi 2025 Results in Eng. | 회귀(클래스 없음) | Not reported / Full text verification required | DC-link 전압 리플; '컨버터의 접근 가능한 입·출력 단자 데이터' 만 사용(초록) | Not reported / Full text verification re | ANN-GB-LR 하이브리드 | NR | 평균 C 오차 0.142 % (하이브리드); 비교 DT 0.624 / GB 0.586 /  | Not reported / Full text verification re |
| Liao 2020 MPE (ER rule) | 3 ranges: Normal / Incipient fault / Failed (no longer incipient) | 초기값(7500 µF)의 90–100 % (µF 수치 NR); 초기값의 80–90 % (µF 수치 NR); 초기값의 <80 % (µF 수치 NR) | DC-link 전압 특징(진단 증거) | Not reported / Full text verification re | ER rule (vs BP-NN) | NR (샘플 수·분할 미확인; '증거' 는 vdc 특징) | BP-NN 대비 우수(수치 NR) | No |
| (Top 10 외·학회) Seferian ECCE 2020 | 3: healthy / half / fully degraded | NR | 단상 PV 인버터 신호(시뮬) | NR | 데이터 기반 분류 | NR | 99 % (시뮬) | 저가 MCU 테스트(부품 NR) |
| (Top 10 외·학회) EMI-CWT-SVM, Xplore 9694516 | 5 단계 | NR | DC 버스 전도 EMI 15–43 MHz (추가 측정) | CWT 이미지 | SVM | 대량 필요(리뷰) | 최대 100 % | NR |
| (Top 10 외) Amaral 2023 Electronics | ESR 임계 분류(수 NR) | NR | 컨버터 신호(시뮬) | STLSP ESR | Random Forest | NR | NR | No(시뮬) |
| (Top 10 외) Nakirimoto SBAI 2023 | 회귀(C) | NR | 시간영역 파라미터 | 통계 | ANN | 지그 학습 + 노화 샘플 평가 | <2.4 % (다중 조건) | 소프트웨어만 |
| (Top 10 외) CNN-Attention IPEMC 2024 | 회귀(C+ESR) | NR | 커패시터 전압 | NR | CNN-Attention | NR | <1 % | NR |

(사실) 클래스 수는 3(Liao, Seferian) 또는 5(EMI-SVM) 이며, 클래스별 C/ESR 값이 스니펫에 나타난 것은 Liao 의 구간(90/80 %)뿐이다. (해석) 2-Level 실험 + 클래스별 C/ESR 공개 + On-board 추론을 갖춘 분류 저널 논문은 이번 탐색에서 발견되지 않았다.

---

## 11. Regression Papers (요청 항목 [29])

| Paper | Target | C Range | ESR Range | Input | Algorithm | Error | Online | On-board |
|---|---|---|---|---|---|---|---|---|
| Ghadrdan 2022 TPEL | Regression-type indicator (DF | Not reported / Full text verification required | Not reported / Full text verification required | 컨버터 출력(AC) 상전류 → 커패시터 전류의 스위칭 주파수 성분 재구성; DC-link 전압(리플) | Analytical: 재구성 전류·전압 리플의 fsw 성분으로 DF 계산 → EoL 임계  | 수치 NR ('acceptable accuracy' 만 초록에 있음) | True Online | Not reported / Full text verification re |
| Örüklü & Ağalar 2025 TIE | C | Not reported / Full text verification required | Not reported / Full text verification required | DC-link 전압 리플 (PSD 입력) | ML 기반 회귀 — 알고리즘명 초록 미표시 | 'high accuracy' (수치 NR). '<2 % 평균 예측 오차' 는 후속 논문 귀속 가능성 → 미채 | True Online | Not reported / Full text verification re |
| Lipnicki & Lewandowski 2017 PED | ESR | Not reported / Full text verification required | Not reported / Full text verification required | DC-link 전압 측정 + DC-link 전류 재구성(초록) | Analytical: vdc + 재구성 DC-link 전류 → ESR 추정(세부 추정기 N | Not reported / Full text verification required | True Online | Not reported / Full text verification re |
| Hasegawa & Hirose 2024 TIA | C+ESR | Not reported / Full text verification required | Not reported / Full text verification required | 3상 AC 전원 전압, AC 라인 인덕터·DC 인덕터 값(파라미터), 인버터 출력 전력 → 커패시터 전류 계 | Analytical: 6-pulse 정류기 리플 전류 모델 → 커패시터 전류 계산 → 리플 | Not reported / Full text verification required (초록은 '변화를 관측' | True Online | 본 논문 NR. 같은 그룹의 2024 학회판·2025 MR 논문은 'Le |
| Sundararajan 2018 TIA | ESR | Not reported / Full text verification required | Not reported / Full text verification required | DC-link 전압과 DC-link 전류의 스위칭 주파수 성분(초록) | Analytical: fsw 대역 /ΔV/ΔI/ 기반 ESR 추정; 한계 fsw 이하에서  | 'estimation error is very low' (수치 NR) | True Online | Yes |
| Park & Kwak 2023 JEET | C+ESR | Not reported / Full text verification required | Not reported / Full text verification required | 주파수 성분(저주파 대역 → C, 중주파 대역 → ESR; 초록) | Deep learning: DNN, CNN, Simple RNN, LSTM 4종 비교 | 정성(모델 간 우열)만 초록에 있음; MAE/RMSE NR | True Online | Not reported / Full text verification re |
| Machines 2022 (3상 AEC) | C+ESR 추정; 분류 여부 NR | Not reported / Full text verification required | Not reported / Full text verification required | 전원(source) 전류(핵심 입력; 초록) | 'advanced learning intelligence techniques' (모델명 N | '99.9 % accuracy' (정의·대상 NR) | True Online | Not reported / Full text verification re |
| Zhao 2023 TPEL (grey-box) | C via damping factor α | Not reported / Full text verification required | Not reported / Full text verification required | DC-link 전압 과도(대신호 과도) — '극히 낮은 샘플링 주파수' 로 충분(초록) | Grey-box: 과도 등가회로 모델(TECM) + 파라미터 피팅 | α·C 오차 <1 % (실험, 초록) | Quasi-Online | Not reported / Full text verification re |
| Al-Wesabi 2025 Results in Eng. | C | Not reported / Full text verification required | Not reported / Full text verification required | DC-link 전압 리플; '컨버터의 접근 가능한 입·출력 단자 데이터' 만 사용(초록) | ML 회귀 비교: RF, KNN, ANN, GB, DT, LR (+BR) → 하이브리드 A | 평균 C 오차 0.142 % (하이브리드); 비교 DT 0.624 / GB 0.586 / BR 0.182 / | True Online | Not reported / Full text verification re |
| (Top 10 외) Zhu 2022 JPE | C | NR | NR | vdc + idc(회생) | RLS + 이상치 제거 | NR | 이벤트형 | NR |
| (Top 10 외) Nguyen/Le/Lee 2015 JPE | ESR | NR | NR | 고정자 전류 + 스위칭 상태 재구성 | 주입 + RLS | ≈1.2 % | Quasi | NR |
| (Top 10 외) Wei 2024 TPEL | C | NR | NR | vdc 방전 | RLS | <1 % | 정지 후 | 기존 제어 HW |
| (Top 10 외) Ghadrdan 2023 JESTPE | C | NR | NR | vdc + 입력 상전류 과도 | 과도 모델 | <1 % vs LCR | Quasi | NR |
| (Top 10 외) Dai 2024 JESTPE | C | NR | NR | vdc 과도 + 전류 적분 재구성 | 선형 피팅 | NR | 이벤트형 | NR |

---

## 12. Signal Comparison

| Paper | 입력 신호 | Existing sensor only | 추가 센서 | 재구성 | Sampling |
|---|---|---|---|---|---|
| Ghadrdan 2022 TPEL | 컨버터 출력(AC) 상전류 → 커패시터 전류의 스위칭 주파수 성분 재구성; DC-link 전압(리플) | Yes | None | Yes | Not reported / Full text verification re |
| Örüklü & Ağalar 2025 TIE | DC-link 전압 리플 (PSD 입력) | Yes | None | No | 수치 NR ('does not require a high sampling |
| Lipnicki & Lewandowski 2017 PED | DC-link 전압 측정 + DC-link 전류 재구성(초록) | Yes | None | Yes | Not reported / Full text verification re |
| Hasegawa & Hirose 2024 TIA | 3상 AC 전원 전압, AC 라인 인덕터·DC 인덕터 값(파라미터), 인버터 출력 전력 → 커패시터 전류 계산; DC-link 전압(리플) | Yes | None | Yes | Not reported / Full text verification re |
| Sundararajan 2018 TIA | DC-link 전압과 DC-link 전류의 스위칭 주파수 성분(초록) | Partially / NR | NR | NR | Not reported / Full text verification re |
| Park & Kwak 2023 JEET | 주파수 성분(저주파 대역 → C, 중주파 대역 → ESR; 초록) | NR | NR | NR | Not reported / Full text verification re |
| Machines 2022 (3상 AEC) | 전원(source) 전류(핵심 입력; 초록) | Yes | None | No | Not reported / Full text verification re |
| Zhao 2023 TPEL (grey-box) | DC-link 전압 과도(대신호 과도) — '극히 낮은 샘플링 주파수' 로 충분(초록) | Yes | None | No | 수치 NR ('extremely low sampling frequency |
| Al-Wesabi 2025 Results in Eng. | DC-link 전압 리플; '컨버터의 접근 가능한 입·출력 단자 데이터' 만 사용(초록) | Yes | None | No | Not reported / Full text verification re |
| Liao 2020 MPE (ER rule) | DC-link 전압 특징(진단 증거) | Yes | None | No | Not reported / Full text verification re |

(사실) vdc(리플/과도/PSD) 사용 6편, 출력·전원 상전류 기반(재구성 포함) 3편(Ghadrdan, Lipnicki, Machines), 정류기 모델 계산 1편(Hasegawa), vdc+idc 1편(Sundararajan). 커패시터 전류 직접 측정을 전제로 한 Top 10 논문은 없으나 Park & Kwak 2023 의 신호원은 NR(선행 논문은 커패시터 전압·전류 사용).

---

## 13. Preprocessing Comparison

| Paper | 전처리 | Feature |
|---|---|---|
| Ghadrdan 2022 TPEL | 스위칭 주파수 성분 추출(방법: 필터/FFT 여부 NR) | fsw 대역 커패시터 전류·전압 성분 → DF 계산 |
| Örüklü & Ağalar 2025 TIE | PSD(power spectral density) 계산 — 창·길이·정규화 NR | vdc 리플 PSD (주파수 빈 선택·차원 NR) |
| Lipnicki & Lewandowski 2017 PED | Not reported / Full text verification required (리플 성분 추출 방법 미확인) | 재구성 전류와 vdc 리플의 관계 → ESR |
| Hasegawa & Hirose 2024 TIA | 정류 리플(6f1 계열) 성분 해석 — FFT 여부 NR(관련 2019 IEEJ·2024 학회판은 FFT 사용) | 정류 리플 전류·전압 성분 → ESR, C |
| Sundararajan 2018 TIA | 대역통과 필터로 스위칭 주파수 성분 추출(스니펫). 2020 TPEL: Goertzel 단일 빈 DFT. | fsw 성분 전압/전류 비 → ESR |
| Park & Kwak 2023 JEET | FFT 로 주파수 성분/대역 추출(초록 취지) | 단일 주파수 성분(저/중) 또는 대역 스펙트럼 — 차원 NR |
| Machines 2022 (3상 AEC) | FFT + 저역/고역 통과 필터(LPF1 → C, HPF → ESR; Figure 캡션), DWT | FFT 성분, DWT 계수 + 통계 지표(statistical indexes) |
| Zhao 2023 TPEL (grey-box) | 과도 구간 분리·피팅(세부 NR) | 감쇠 계수 α |
| Al-Wesabi 2025 Results in Eng. | Not reported / Full text verification required | vdc 리플 기반 특징(정의 NR) |
| Liao 2020 MPE (ER rule) | Not reported / Full text verification required | vdc 에서 추출한 특징(종류 NR) → 각 특징을 증거로 변환 |

(사실) 주파수 영역(fsw 성분·PSD·FFT 대역·DWT) 이 8편, 시간 영역 과도 피팅 1편(Zhao), 증거 특징 1편(Liao). STFT/CWT 이미지 → 2D-CNN 은 저널 Top 10 에 없음(학회 EMI-CWT-SVM 만).

---

## 14. Diagnosis Algorithm Comparison

| Paper | 유형 | 알고리즘 | Hyperparameter |
|---|---|---|---|
| Ghadrdan 2022 TPEL | Analytical | Analytical: 재구성 전류·전압 리플의 fsw 성분으로 DF 계산 → EoL 임계 비교 | 해당 없음 |
| Örüklü & Ağalar 2025 TIE | AI | ML 기반 회귀 — 알고리즘명 초록 미표시 | Not reported / Full text verif |
| Lipnicki & Lewandowski 2017 PED | Analytical | Analytical: vdc + 재구성 DC-link 전류 → ESR 추정(세부 추정기 NR) | 해당 없음 |
| Hasegawa & Hirose 2024 TIA | Analytical | Analytical: 6-pulse 정류기 리플 전류 모델 → 커패시터 전류 계산 → 리플 전압과의 관계로 ESR·C 산출 | 해당 없음 |
| Sundararajan 2018 TIA | Analytical | Analytical: fsw 대역 /ΔV/ΔI/ 기반 ESR 추정; 한계 fsw 이하에서 대안 해법(초록) | 해당 없음 |
| Park & Kwak 2023 JEET | AI | Deep learning: DNN, CNN, Simple RNN, LSTM 4종 비교 | Not reported / Full text verif |
| Machines 2022 (3상 AEC) | AI | 'advanced learning intelligence techniques' (모델명 NR — ANN 계열 추정, 확인 필요 | Not reported / Full text verif |
| Zhao 2023 TPEL (grey-box) | Analytical | Grey-box: 과도 등가회로 모델(TECM) + 파라미터 피팅 | 해당 없음 |
| Al-Wesabi 2025 Results in Eng. | AI | ML 회귀 비교: RF, KNN, ANN, GB, DT, LR (+BR) → 하이브리드 ANN-GB-LR 제안 | Not reported / Full text verif |
| Liao 2020 MPE (ER rule) | AI | Evidence Reasoning(ER) rule 융합(증거 가중치 조정 가능) vs BP 신경망 비교 | Not reported / Full text verif |

(사실) 해석적 5편(DF 계산, 재구성 ESR, 정류 리플 모델, fsw 성분 비/Goertzel, grey-box 과도), AI 5편(ML 회귀 2, DL 회귀 1, 학습 기반 1, ER rule 1). RLS/Kalman 계열은 Top 10 밖(Nguyen 2015, Zhu 2022, Wei 2024)에 분포.

---

## 15. Online / On-board Comparison

| Paper | Diagnosis Type | 근거 | On-board 구현 | Real-time 판단 |
|---|---|---|---|---|
| Ghadrdan 2022 TPEL | True Online | 초록상 주입·시퀀스 없이 정상 운전 중 스위칭 성분을 이용(사실). 상세 운전조건 제약은 본문 확인 필요. | Not reported / Full text verification required | Real-time feasible |
| Örüklü & Ağalar 2025 TIE | True Online | 정상 운전 중 vdc 리플만 사용, 주입·회로 없음(초록). | Not reported / Full text verification required | Real-time feasible |
| Lipnicki & Lewandowski 2017 PED | True Online | 초록상 주입·시퀀스 언급 없음, 추가 센서 없음. 운전 조건 제약은 본문 확인 필요. | Not reported / Full text verification required | Real-time feasible |
| Hasegawa & Hirose 2024 TIA | True Online | 정상 운전 중 고유 정류 리플을 이용, 주입 없음(초록). | 본 논문 NR. 같은 그룹의 2024 학회판·2025 MR 논문은 'Leafony' 소형  | Real-time feasible (후속 논문에서 MCU 구현 시사) |
| Sundararajan 2018 TIA | True Online | 정상 운전 중 스위칭 리플 성분만 사용(초록). 주입 없음. | Yes | Real-time demonstrated (상용 드라이브 구현 — 초록 기준) |
| Park & Kwak 2023 JEET | True Online (추정) | 정상 운전 리플의 주파수 성분을 입력으로 쓰는 구조(초록)이나, 센서·운전 조건·실시간 구현은 NR. | Not reported / Full text verification required | Real-time not demonstrated |
| Machines 2022 (3상 AEC) | True Online (추정) | 정상 운전 신호(전원 전류)만 쓰는 구조. 운전 조건·실시간 구현 NR. | Not reported / Full text verification required | Real-time not demonstrated |
| Zhao 2023 TPEL (grey-box) | Quasi-Online (이벤트형: 자연 발생 대신호 과도 필요) | 정상 운전을 멈추지는 않지만 과도가 있어야 추정(초록 취지). | Not reported / Full text verification required | Real-time feasible |
| Al-Wesabi 2025 Results in Eng. | True Online (주장) | 정상 운전 리플만 사용한다는 초록 취지. 실험·구현 NR. | Not reported / Full text verification required | Real-time not demonstrated |
| Liao 2020 MPE (ER rule) | Quasi-Online/주장 Online (시뮬레이션) | 'online monitoring method' 라 하나 시뮬레이션만, 구현 없음. | No | Offline post-processing only |

---

## 16. Hardware Environment Comparison

| Paper | DSP | MCU | FPGA | Sampling | Execution time | Inference/model size |
|---|---|---|---|---|---|---|
| Ghadrdan 2022 TPEL | Not reported / Full text verification required | Not reported / Full text verification re | Not reported / Full text verification required | Not reported / Full text verif | Not reported / Full text verification required | 해당 없음 |
| Örüklü & Ağalar 2025 TIE | Not reported / Full text verification required | Not reported / Full text verification re | Not reported / Full text verification required | 저샘플링 강조(수치 NR) | Not reported / Full text verification required | Not reported / Full text verif |
| Lipnicki & Lewandowski 2017 PED | Not reported / Full text verification required | Not reported / Full text verification re | Not reported / Full text verification required | Not reported / Full text verif | Not reported / Full text verification required | 해당 없음 |
| Hasegawa & Hirose 2024 TIA | Not reported / Full text verification required | Leafony 소형 MCU (학회판/후속 논문; 본 논문 귀속 NR) | Not reported / Full text verification required | Not reported / Full text verif | Not reported / Full text verification required | 해당 없음 |
| Sundararajan 2018 TIA | Not reported / Full text verification required | Not reported / Full text verification re | Not reported / Full text verification required | Not reported / Full text verif | Not reported / Full text verification required | 해당 없음 |
| Park & Kwak 2023 JEET | Not reported / Full text verification required | Not reported / Full text verification re | Not reported / Full text verification required | Not reported / Full text verif | Not reported / Full text verification required | Not reported / Full text verif |
| Machines 2022 (3상 AEC) | Not reported / Full text verification required | Not reported / Full text verification re | Not reported / Full text verification required | Not reported / Full text verif | Not reported / Full text verification required | Not reported / Full text verif |
| Zhao 2023 TPEL (grey-box) | Not reported / Full text verification required | Not reported / Full text verification re | Not reported / Full text verification required | 극저 샘플링(수치 NR) | Not reported / Full text verification required | 해당 없음 |
| Al-Wesabi 2025 Results in Eng. | Not reported / Full text verification required | Not reported / Full text verification re | Not reported / Full text verification required | Not reported / Full text verif | Not reported / Full text verification required | Not reported / Full text verif |
| Liao 2020 MPE (ER rule) | 해당 없음 | 해당 없음 | 해당 없음 | Not reported / Full text verif | Not reported / Full text verification required | Not reported / Full text verif |

(사실) 부품번호·샘플링 주파수·실행/추론 시간은 10편 모두 초록·스니펫에 없다. 구현 사실만 확인: Sundararajan 2018(상용 AC 드라이브), Hasegawa 계열 후속(Leafony 소형 MCU 로 FFT). Top 10 밖: Soliman 2015(ANN 을 DSP 에 구현, 부품 NR), Seferian ECCE 2020(저가 MCU 테스트), Chaiyakhot ICEMS 2022(DSP, 부품 NR).

### 실험 환경 요약
| Paper | Vdc | Power | Load/Motor | fsw | Capacitor |
|---|---|---|---|---|---|
| Ghadrdan 2022 TPEL | Not reported / Full  | Not reported / Full text  | Not reported / Full text  | Not reported / Full  | Not reported / Full text  |
| Örüklü & Ağalar 2025 TIE | Not reported / Full  | Not reported / Full text  | Not reported / Full text  | Not reported / Full  | Not reported / Full text  |
| Lipnicki & Lewandowski 2017 PED | Not reported / Full  | Not reported / Full text  | Not reported / Full text  | Not reported / Full  | Not reported / Full text  |
| Hasegawa & Hirose 2024 TIA | 200 V 급 | NR (후속 1.5 kW) | Not reported / Full text  | Not reported / Full  | Not reported / Full text  |
| Sundararajan 2018 TIA | Not reported / Full  | Not reported / Full text  | Not reported / Full text  | Not reported / Full  | Not reported / Full text  |
| Park & Kwak 2023 JEET | Not reported / Full  | Not reported / Full text  | Not reported / Full text  | Not reported / Full  | Not reported / Full text  |
| Machines 2022 (3상 AEC) | Not reported / Full  | Not reported / Full text  | Not reported / Full text  | Not reported / Full  | Not reported / Full text  |
| Zhao 2023 TPEL (grey-box) | Not reported / Full  | Not reported / Full text  | 상용 전원장치 | Not reported / Full  | Not reported / Full text  |
| Al-Wesabi 2025 Results in Eng. | Not reported / Full  | Not reported / Full text  | Not reported / Full text  | Not reported / Full  | Not reported / Full text  |
| Liao 2020 MPE (ER rule) | Not reported / Full  | Not reported / Full text  | Not reported / Full text  | Not reported / Full  | 7500 µF(초기) |

---

## 17. Performance Comparison

| Paper | Task | C error | ESR error | Classification | 운전조건 다양성 | Robustness |
|---|---|---|---|---|---|---|
| Ghadrdan 2022 TPEL | Regression-type indicator (DF) | 해당 없음(DF 지표) | 해당 없음(DF 지표) | 해당 없음 | NR. 초록은 fsw·ESL·필터 '요인' 영향 분석을 언급하나 부하·변조지수 변화 실험  | fsw·ESL·계통 필터 영향 분석(초록). 측정 노이즈·온도·부하 변화 검증 여부 NR. |
| Örüklü & Ağalar 2025 TIE | Regression (C) | Not reported / Full text verification re | 해당 없음(C only) | 해당 없음 | NR for this paper. 후속(2026 TPEL GPR) 초록에 '여러 부하·출력 | 저샘플링 강건성 주장(초록). 노이즈·온도·미학습 운전조건 검증 NR. |
| Lipnicki & Lewandowski 2017 PED | Regression (ESR) | 해당 없음 | Not reported / Full text verification re | 해당 없음 | Not reported / Full text verification required | Not reported / Full text verification required |
| Hasegawa & Hirose 2024 TIA | Regression (C+ESR) | Not reported / Full text verification re | Not reported / Full text verification re | 해당 없음 | NR (본 논문). 후속 2025 MR: 전원 전압 불평형 ≈5 % 까지 유효. | 후속 2025 MR 에서 전원 불평형 강건성 다룸. 부하·온도 NR. |
| Sundararajan 2018 TIA | Regression (ESR) | 해당 없음(본 논문) | Not reported / Full text verification re | 해당 없음 | NR (스위칭 주파수 의존성은 분석) | fsw 의존성 분석(초록). 온도는 2020 TPEL 에서 다룸(온도 추정·자가 보정). |
| Park & Kwak 2023 JEET | Regression (C+ESR) | Not reported / Full text verification re | Not reported / Full text verification re | 해당 없음 | Not reported / Full text verification required | Not reported / Full text verification required |
| Machines 2022 (3상 AEC) | Regression (C+ESR 추정; 분류 여부 NR) | Not reported / Full text verification re | Not reported / Full text verification re | NR (분류 여부 불명) | Not reported / Full text verification required | Not reported / Full text verification required |
| Zhao 2023 TPEL (grey-box) | Regression (C via damping factor α) | <1 % | 해당 없음 | 해당 없음 | Not reported / Full text verification required | 토폴로지·제어 지식 최소 요구(초록). 노이즈·온도 NR. |
| Al-Wesabi 2025 Results in Eng. | Regression (C) | 0.142 % 평균, RMSE 0.0070 µF, MAE 0.0049 µ | NR/해당 없음 | 해당 없음 | Not reported / Full text verification required | Not reported / Full text verification required |
| Liao 2020 MPE (ER rule) | Classification (3 ranges: normal / incipient fault / failed) — 노화 등급 판정 | 해당 없음 | 해당 없음 | Accuracy/F1/혼동행렬 NR | Not reported / Full text verification required | 증거 가중치 조정으로 강건성 조절 가능(초록 취지). 노이즈·운전조건 NR. |

(사실) 수치가 있는 것은 Zhao 2023(α·C <1 %), Al-Wesabi 2025(평균 0.142 %, 최대 1.1–1.3 %), Machines 2022('99.9 %', 정의 NR)뿐. 운전조건 다양성을 본 논문 초록에서 확인한 것은 없음(Örüklü 의 다중 조건은 후속 논문 귀속 가능, Hasegawa 의 불평형은 후속 2025 MR).

---

## 18. Relation to My Research

| Paper | Relevance | 이유 | 재현 |
|---|---|---|---|
| Ghadrdan 2022 TPEL | Very High | 2L(추정) 3상 컨버터, 기존 센서, True Online, 커패시터 전류 재구성 — 내 목표 파이프라인의 신호 생성 단계와 가장 가깝다. 단 AI·분류 요소는 | Moderate |
| Örüklü & Ağalar 2025 TIE | Very High | 2L(추정) 3상 AC/DC/AC + 기존 센서 + True Online + ML 회귀 — 내 목표 파이프라인과 구조가 같다. 입력 신호·대상만 다름. | Moderate |
| Lipnicki & Lewandowski 2017 PED | Very High | 2-Level AC/DC/AC + 기존 센서 + 재구성 + ESR + True Online — 내 목표와 조건이 가장 많이 겹친다(AI 요소만 없음). | Moderate |
| Hasegawa & Hirose 2024 TIA | High | 방법 철학(센서 없는 커패시터 전류 계산, C+ESR 동시)은 매우 유용하나, 정보원이 정류 리플이라 내 '인버터 신호' 목표와 다르다. | Moderate |
| Sundararajan 2018 TIA | High | fsw 성분 ESR 추정 + 상용 드라이브 구현은 내 on-board 목표의 실증 선례. 센서 조건(idc)과 ESR 단독이 차이. | Moderate |
| Park & Kwak 2023 JEET | Very High | 3상 인버터 DC-link C+ESR 를 FFT 성분 → DL 회귀로 다룬 유일한 저널 후보. 내 AI 설계(입력 대역, 모델 선택)에 직접 참고. | Moderate |
| Machines 2022 (3상 AEC) | High | 3상 인버터 + 기존 센서 + 학습 기반 C/ESR 추정이라는 점에서 직접 관련. 검증 수준이 불명해 Very High 는 보류. | Easy~Moderate |
| Zhao 2023 TPEL (grey-box) | Medium | 물리 모델·저샘플링 설계의 참고. 내 목표(연속 True Online, C+ESR, 2L)와는 구조가 다름. | Moderate |
| Al-Wesabi 2025 Results in Eng. | Medium | AI 회귀 벤치마크 수치로만 유용. 2L·on-board 조건 미확인. | Easy (시뮬레이션 기준) |
| Liao 2020 MPE (ER rule) | Medium | 분류 라벨 설계 참고용. 2L 실험·on-board·ESR 요소 없음. | Easy |

내 목표 파이프라인(2-Level 3상 → DC-link 노화 → 기존 신호 → On-board/Online → 분류/회귀 → 실시간)과의 대응:
- 신호 생성(상전류 + 스위칭 상태 → 커패시터 전류 재구성): Ghadrdan 2022, Lipnicki 2017 (+Top 10 밖 Nguyen/Le/Lee 2015, Xplore 9465734, US 12461138).
- 기존 센서 단일 신호(vdc) 경로: Örüklü 2025, Zhao 2023, Al-Wesabi 2025, Liao 2020.
- C+ESR 동시: Hasegawa 2024(모델), Park & Kwak 2023(DL).
- 경량 on-board feature: Sundararajan 2018/2020(fsw 성분, Goertzel), Hasegawa 후속(MCU FFT).
- AI 설계: Park & Kwak(입력 대역·모델 선택), Machines 2022(신호·전처리 비교), Al-Wesabi(회귀 모델 비교), Liao(라벨 정의).

---

## 19. Research Gap (요청 항목 31)

사용자 31절 기준으로 실제 조사 결과에 근거해 판단한다.

| # | Gap | 근거(사실) | 판단 |
|---|---|---|---|
| G1 | "기존 센서 + raw 전류/전압 파형 + AI 분류/회귀 + on-board 추론" 의 완결 연구 | AI 5편 중 on-board 추론을 보인 저널 논문 0편(16절) | **충분히 연구되지 않음** |
| G2 | C + ESR 동시 진단(2-Level, True Online, 기존 센서) | Hasegawa(정류 리플, 전류 센서 없음)·Park & Kwak(센서 NR)만; 인버터 스위칭 신호 기반 동시 추정 0편 | 공백 |
| G3 | 다중 운전조건 진단·domain generalization | Top 10 초록 중 다중 조건 명시 0편; Top 10 밖 Nakirimoto(여러 운전조건 <2.4 %), CNN-Attention(부하·속도·전압) | 공백(저널 수준) |
| G4 | 온도 강건성 | Sundararajan 2020(온도 추정)·Pu 2013·Baumann 2024 만; AI 논문 0편 | 공백 |
| G5 | 센서리스(전류 센서 없음) | Hasegawa 계열(정류기 전단 한정), Ghadrdan·Lipnicki(상전류 재구성) | 부분 해결, 인버터 스위칭 기반은 ESR/DF 단독 |
| G6 | 실제 자연/가속 노화 데이터셋 | Top 10 저널 0편 명시; Lee 2008, Raqib 2021, Baumann 2024, Nakirimoto 2023 만 | 공백 |
| G7 | 경량 NN / 실시간 on-board AI | 저널 0편(학회: Seferian 저가 MCU, Soliman DSP 2015) | 공백 |
| G8 | 불확실성 추정 | Örüklü 후속(GPR, 2026 TPEL 귀속 확인 필요), arXiv 2609.00218 | 초기 단계 |
| G9 | Transfer learning / domain adaptation | 저널·학회 모두 0편 | 공백 |
| G10 | Physics-informed ML | Qie 2025 TIE(사전충전, C), AAU IPEMC 2024(C+L) | 초기 단계, 리플 기반 없음 |
| G11 | 분류 라벨(클래스별 C/ESR) 공개 | Liao 2020 구간만; 나머지 NR | 공백 |
| G12 | 재구성 전류 스펙트럼 feature(여러 고조파 빈) → AI | Ghadrdan(DF 단일 지표), Lipnicki(ESR 단일) — 스펙트럼 벡터 입력 AI 0편 | 공백(내 연구 차별점) |

---

## 20. Recommended Research Direction

1. **신호**: 상전류 ia/ib/ic + 스위칭 함수 Sa/Sb/Sc(제어기 내부) + vdc 만 사용 → 커패시터 전류 재구성(Ghadrdan·Lipnicki 선례). 커패시터 전류 센서는 검증용으로만.
2. **Feature**: 재구성 전류·vdc 의 (a) fsw 및 측대파 빈(ESR 민감; Sundararajan 2018/2020 Goertzel) + (b) 저주파(6f1·2f1 또는 부하 리플) 빈(C 민감; Park & Kwak 의 대역-파라미터 대응) 을 소수 빈 벡터로 구성. 운전점 변수(변조지수·부하 전류·f1·fsw)를 feature 에 포함해 조건 정규화.
3. **노화 샘플**: 파라미터 모사 격자 — C {100, 95, 90, 85, 80, 70} % × ESR {×1, ×1.25, ×1.5, ×2, ×3} 를 교차(문헌 EoL 기준 C −20 %, ESR ×2 를 중앙에 둠), Radd 직렬 저항으로 ESR 구현(값 기록), 가능하면 가속 노화 샘플 2–3개 추가(Lee 2008·Raqib 방식).
4. **라벨**: 회귀(C, ESR 동시) 를 기본으로 하고, 분류는 Liao 구간(정상 ≥90 % / 초기 80–90 % / 고장 <80 %) + ESR 축(×1.5, ×2) 을 결합한 다중 라벨로 병행.
5. **모델**: 1단계 — 해석적 기준선(DF, fsw 성분 ESR, 과도 C). 2단계 — 경량 DNN/1D-CNN(Park & Kwak 결론: 단일 빈엔 DNN, 대역엔 CNN) + GPR(불확실성). 비교군: Al-Wesabi 의 6종 회귀.
6. **On-board**: Goertzel/슬라이딩 DFT 로 빈을 제어기 안에서 계산하고, 모델은 양자화된 소형 NN 으로 DSP/MCU 추론 시간을 보고(저널 공백 G7).
7. **검증**: 부하·속도·변조지수·fsw·온도를 바꾼 운전점 기준 train/test 분리(G3), 노이즈·센서 이득 오차 주입(G4), Hasegawa 식 정류 리플 경로가 있으면 교차 검증.

---

## 21. Reading Priority (요청 항목 32)

### Tier S — 지금 먼저
- **1위 Ghadrdan 2022 TPEL** — 왜: '출력 상전류 → 커패시터 전류 스위칭 성분 재구성 → fsw 대역 지표' 의 IEEE TPEL 선례. 내 신호 생성 단계의 근거 논문. / 집중: 재구성 수식(출력 전류→커패시터 전류), DF 정의·EoL 기준, fsw/ESL/필터 영향 절과 해당 Figure, 실험 셋업 표
- **2위 Örüklü & Ağalar 2025 TIE** — 왜: 기존 센서(vdc)만으로 True Online ML 회귀를 IEEE TIE 에 실은 최신 논문. 내 AI 파이프라인의 직접 비교군. / 집중: PSD 입력 정의(주파수 범위·분해능), 사용 ML 모델과 hyperparameter, 노화 샘플 표, 실험 셋업 표, 오차 표/그림, 저샘플링 실험 절
- **3위 Lipnicki & Lewandowski 2017 PED** — 왜: 제목부터 '2-Level AC/DC/AC' 이며 추가 센서 없는 재구성 기반 ESR 추정 — 내 토폴로지·신호 조건의 직접 선례. / 집중: DC-link 전류 재구성 식(스위칭 함수 정의), ESR 추출 대역·수식, 실험/시뮬 조건 표, 오차 그림

### Tier A — 그 다음
- **4위 Hasegawa & Hirose 2024 TIA** — 왜: 전류 센서 없이 C+ESR 를 동시에 추정한 IEEE TIA 최신 논문. '측정 대신 계산' 의 오차 처리 방식을 배울 수 있다. / 집중: 커패시터 전류 계산식(전원 전압·인덕터·출력 전력), ESR/C 산출식, 200 V 실험 셋업 표, C·ESR 변화 관측 그림
- **5위 Sundararajan 2018 TIA** — 왜: On-board(상용 드라이브) 구현까지 보인 True Online ESR 추정의 대표. Goertzel 후속과 함께 경량 feature 추출 설계의 근거. / 집중: fsw 성분 ESR 식, 한계 fsw 유도, 상용 드라이브 구현 절(제어기·샘플링), 오차 표; 2020 TPEL 의 Goertzel 빈 선택·온도 보정 절
- **6위 Park & Kwak 2023 JEET** — 왜: 3상 DC-link C+ESR 를 DL 로 회귀한 저널 논문. 입력 대역 설계와 모델 선택(DNN vs CNN) 결론을 그대로 실험 설계에 쓸 수 있다. / 집중: 입력 대역 정의 표, 데이터 생성 조건(실험/시뮬, 노화 샘플), 4개 모델 구조·hyperparameter 표, C/ESR 오차 표, 단일 성분 vs 대역 비교 그림
- **7위 Machines 2022 (3상 AEC)** — 왜: '어떤 신호 + 어떤 전처리' 가 AEC 파라미터 추정에 가장 좋은지를 비교한 OA 논문 — 내 feature 설계의 비교 근거. / 집중: 신호 조합 비교표(Table), 필터 주파수 범위 표(tbl6), DWT 레벨·통계 지표 정의, 정확도 정의와 결과표, 노화 곡선(Fig. 1)

### Tier B — 필요할 때
- **8위 Zhao 2023 TPEL (grey-box)** — 왜: 전압 센서만으로 1 % 미만을 낸 물리 모델(과도) 기준점. 내 리플 기반 방법의 '보조 경로(과도 시 C 교정)' 로 검토. / 집중: TECM 유도(병렬 RLC, α 정의), 샘플링 요구 분석, 실험 셋업·오차 표
- **9위 Al-Wesabi 2025 Results in Eng.** — 왜: 회귀 모델 6종 + 하이브리드의 정량 비교. 내 회귀 실험의 '비교 모델 세트' 로 바로 차용. / 집중: 특징 정의 절, 데이터 생성 조건(시뮬/실험, 운전점), 모델별 오차 표(단위 확인), 하이브리드 구조 그림
- **10위 Liao 2020 MPE (ER rule)** — 왜: 분류 등급 정의(정상 90–100 % / 초기 80–90 % / 고장 <80 %)를 명시한 유일한 후보 — 라벨 설계의 출발점. / 집중: 등급 정의 표, 특징(증거) 정의, ER 융합 수식, BP-NN 비교 결과표

---

## 22. 최종 질문 Q1–Q14 (요청 항목 30)

**Q1. 가장 많이 쓰는 방식:** (사실) 2-Level 계열 저널 후보에서 가장 많은 것은 "DC-link 전압 리플·과도를 해석적 모델 또는 ML 로 C 에 사상" 하는 방식이고, 그 다음이 "스위칭 주파수(또는 정류 6f1) 대역 전류·전압 성분으로 ESR/DF" 이다. 주입형·회생형·정지형은 Top 10 밖 다수(Nguyen, Zhu, Meng, Wei, Wu, Ghadrdan 2023).

**Q2. 분류 vs 회귀:** (사실) 회귀(연속 추정)가 압도적. Top 10 중 분류는 Liao 2020 뿐, 후보 전체에서도 분류는 Liao, Amaral 2023, Seferian ECCE 2020, EMI-SVM, NITK 2022 정도(저널 2, 학회·미확정 3).

**Q3. 분류 클래스 수:** (사실) 3 클래스(Liao: normal/incipient/failed; Seferian: healthy/half/fully degraded)가 기본, 5 단계(EMI-SVM) 1건. 4 클래스 사례는 확인되지 않음.

**Q4. 클래스별 C/ESR 변화량:** (사실) 확인된 것은 Liao 2020 의 C 구간(90–100 % / 80–90 % / <80 %)뿐. ESR 클래스 정의는 어느 논문에서도 스니펫에 없음 → `Not reported / Full text verification required`. (해석) 문헌 EoL 기준(C −20 %, ESR ×2)이 구간 경계로 쓰인다.

**Q5. 가속 노화 vs 파라미터 모사:** (사실) Top 10 저널에서 어느 쪽도 초록에 명시되지 않음(Liao 는 시뮬). 후보 전체에서 가속 노화 명시는 Lee 2008, Raqib 2021/thesis, Baumann 2024, Nakirimoto 2023(노화 샘플), Rojas-Dueñas 2021 — 소수. (해석) 발표 수로는 파라미터 모사·시뮬이 더 많을 것으로 보이나 본문 확인 전엔 단정하지 않는다.

**Q6. 가장 많이 쓰는 신호:** (사실) DC-link 전압(10편 중 6편 단독 또는 주), 다음이 출력/전원 상전류(3편), DC-link 전류(1편). 스위칭 상태를 feature 로 쓰는 논문은 재구성 단계에서만 등장(Ghadrdan, Lipnicki).

**Q7. 추가 센서 없이 가능한 연구:** Ghadrdan 2022, Örüklü 2025, Lipnicki 2017, Hasegawa 2024(전류 센서 자체 불필요), Machines 2022(전원 전류), Zhao 2023(vdc), Al-Wesabi 2025(단자 데이터), Liao 2020(vdc). Partially/NR: Sundararajan 2018(idc), Park & Kwak 2023.

**Q8. True Online 연구:** Ghadrdan 2022, Örüklü 2025, Lipnicki 2017, Hasegawa 2024, Sundararajan 2018(+2020), Machines 2022(추정), Al-Wesabi 2025(주장). 이벤트형: Zhao 2023. 시뮬: Liao 2020. Top 10 밖 True Online: HIT 2021, Xiang 2021(추가 센서), Wechsler 2012, Yamasoto 2025, Ahmad 2018(단상).

**Q9. DSP/MCU On-board 구현:** (사실) Sundararajan 2018(상용 AC 드라이브 구현), Hasegawa 계열 후속(Leafony 소형 MCU FFT; 2024 학회판/2025 MR 귀속 확인 필요). Top 10 밖: Soliman 2015(ANN on DSP), Seferian ECCE 2020(저가 MCU), Chaiyakhot ICEMS 2022(DSP). 부품번호·실행시간은 전부 NR.

**Q10. 최고 분류 성능:** (사실) 수치가 있는 것은 EMI-CWT-SVM(최대 100 %, 추가 EMI 측정, venue 미확인), Seferian ECCE 2020(99 %, 시뮬), Machines 2022('99.9 %', 정의 NR). Liao 2020 은 수치 NR. (해석) 모두 시뮬 또는 정의 불명이라 비교 가치가 낮다.

**Q11. 최저 회귀 오차:** (사실) Al-Wesabi 2025 평균 0.142 %(C, 조건 NR), Zhao 2023 <1 %(α·C, 실험), Top 10 밖 Abo-Khalil & Lee 2008 <0.15 %·Abo-Khalil 2012 <0.146 %(주입형), Wei 2024 <1 %(정지), HIT 2021 <1 %, Nguyen 2015 <1 %(C)·1.2 %(ESR). ESR 회귀 수치는 Nguyen/Le/Lee 1.2 %, Energies 2022 maglev <1 % 외 NR.

**Q12. 운전조건 변화 검증:** (사실) Top 10 초록에서 명시 0편. 후보 전체: Nakirimoto SBAI 2023(여러 운전조건), CNN-Attention IPEMC 2024(부하·속도·전압), Yamasoto 2025(전원 불평형), Wechsler 2012(토크·속도 독립), Processes 2025(변조지수·PWM LUT 보상), Örüklü 후속 GPR(부하·출력 주파수; 귀속 확인 필요).

**Q13. 가장 큰 공백:** 19절 G1·G2·G12 — "2-Level 3상 인버터의 기존 센서(상전류·스위칭 상태·vdc)로 재구성한 커패시터 전류의 스펙트럼 feature 를 입력으로 C 와 ESR 을 동시에(회귀/분류) 추정하고, 다중 운전조건에서 검증하며, DSP/MCU 에서 실시간 추론까지 보인 저널 논문" 이 없다. 부수적으로 클래스별 C/ESR 공개(G11)와 실제 노화 데이터(G6)도 공백.

**Q14. 가장 유망한 접근:** 20절. 요약하면 `상전류+스위칭 함수+vdc(기존 센서) → 커패시터 전류 재구성 → Goertzel/SDFT 소수 빈(fsw 측대파 = ESR, 저주파 = C) + 운전점 변수 → 경량 DNN/1D-CNN(또는 GPR) 회귀 C·ESR(+등급 분류) → 운전점 기준 분리 검증 → DSP/MCU 추론 시간 보고`. 해석적 기준선(DF, fsw 성분 ESR)을 같은 데이터로 함께 보고하면 Ghadrdan·Sundararajan 과 직접 비교가 된다.

---

## 부록 A. 서지 검증 대기 목록
- DOI 미확인: Hasegawa & Hirose 2024 TIA, Örüklü & Ağalar 2025 TIE(검색 미표시), Machines 2022(패턴), Al-Wesabi 2025(PII 만), Meng & Zhang TPEL, HIT 2021 TPEL(저자), Wei 2024 TPEL, Baumann 2024 권/쪽, Nguyen/Le/Lee 2015 JPE DOI, Qie 2025 TIE DOI, Li 2022 TPEL(재검색 미검출).
- 저자 미확인: Machines 2022, HIT 2021 letter, Sundararajan 2018 전체 저자, Zhao 2023 이니셜, Al-Wesabi 2025 일부.
- 귀속 주의: Örüklü '<2 %·GPR·다중 조건' (2026 TPEL 후속 가능), Hasegawa 'Leafony MCU'(학회판/2025 MR), Machines '107–554 µF', Abo-Khalil '1000–5000 µF 100 µF 간격'(다른 논문).
- 로컬 PC 에서: `pwsh -File harness\tools\Search-Papers.ps1 -Query "<제목>" -Source all` 로 Crossref type·권·쪽·DOI 확인 후 본 표와 CSV 갱신. OA 본문 확보 우선순위: Zhao 2023(VBN AAM), Lipnicki 2017(yadda PDF), Machines 2022, Al-Wesabi 2025, Liao 2020, Amaral 2023.

## 부록 B. 사실 / 해석 / 추론 표기
- (사실) = 초록·스니펫 인용. (해석) = 분석자 해석. (추론) = 회로 이론·선행 논문에서 유도. 수치는 초록·스니펫에 있는 것만 기재했으며, `Not reported / Full text verification required` 는 본문 확인 전까지 비워 둔다.
