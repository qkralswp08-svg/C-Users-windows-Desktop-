# Agent B1 — Literature Researcher: 전력전자 커패시터·반도체 소자 AI 상태진단 (분야 A/B/C/E/I + RUL)

작성일: 2026-10-07 · 근거 수준: **검색결과(제목/URL/스니펫) 수준 — 본문 미열람**

## 0. 검증 방법과 한계 (먼저 읽을 것)

- 도구: WebSearch 만 사용(Crossref/doi.org/IEEE Xplore/OpenAlex 등 직접 조회는 egress 차단으로 수행하지 않음).
- **검색 한도 소진**: 이번 세션에서 약 33회 검색 후 공유 WebSearch 한도(200회/turn, 여러 에이전트 공유)가 소진되어, 커패시터 RUL(D14, D16), D1, D8, 추가 리뷰 논문 검색은 **수행하지 못했다**. 해당 항목은 이전 보고서 서지를 그대로 옮기고 등급 X(이번 세션 미재검증)로 표시했다. 사용자가 후속 메시지를 보내면 재검색 가능.
- 등급 정의
  - **V1**: 제목 + 제1저자 + 저널/학회 + 연도 일치, DOI 문자열을 검색결과(URL 또는 스니펫/요약)에서 직접 확인.
  - **V2**: 서지 일치, DOI 미확인 → DOI 칸 "미확인".
  - **X**: 제1저자·연도·학회 중 하나 이상 미확인, 또는 이번 세션 미검색 → 후보 목록에만, 핵심 선정 금지.
  - **V1†**: DOI·제목·저자·저널은 확인, **연도만** 이번 세션 검색결과에서 확인 못 함(이전 보고서 값 2026). 핵심 선정에서 제외.
- DOI 는 모두 WebSearch 결과 요약(검색된 저장소 페이지 스니펫 기반)에서 읽은 문자열이다. doi.org 해석으로 교차 확인하지는 못했다.
- 이전 조사(`papers/index.md`, `workspace/reports/2026-09-29-...survey.md`)와의 대응은 각 항목 비고에 적었다.

---

## 1. 후보 논문 목록 (18편)

| ID | 제목 | 저자 | 연도 | 저널/학회 | 권호 | DOI | 등급 | 근거 URL | 분야 |
|---|---|---|---|---|---|---|---|---|---|
| B1-01 | An Overview of Artificial Intelligence Applications for Power Electronics | Shuai Zhao, Frede Blaabjerg, Huai Wang | 2021 | IEEE Trans. Power Electron. | 36(4):4633–4658 | 10.1109/TPEL.2020.3024914 | V1 | https://vbn.aau.dk/ws/files/431659513/An_Overview_of_Artificial_Intelligence_Applications_for_Power_Electronics.pdf ; https://vbn.aau.dk/da/publications/an-overview-of-artificial-intelligence-applications-for-power-ele | A |
| B1-02 | Deep learning-based estimation technique for capacitance and ESR of input capacitors in single-phase DC/AC converters | Hye-Jin Park, Jae-Chang Kim, Sangshin Kwak | 2022 | J. Power Electron. | 22(3):513–521 | 10.1007/s43236-021-00366-x | V1 | https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/52713?mode=full | B, C |
| B1-03 | DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs | H.-J. Park, Sangshin Kwak | 2023 | J. Electr. Eng. Technol. (JEET) | 18(3):1841–1850 | 10.1007/s42835-023-01424-z | V1 | https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/66390?mode=full | B, C |
| B1-04 | Machine learning-based condition monitoring for dc-link capacitors in ac/dc/ac converters | K. Örüklü, Ş. Ağalar | 2024(참고문헌 표기) | IEEE Trans. Ind. Electron. | 72(4):4227–4237 | 미확인 | V2 | https://arxiv.org/pdf/2609.00218 (해당 arXiv 논문의 참고문헌 목록에서 서지 확인) | B, C |
| B1-05 | Artificial neural network based DC-link capacitance estimation in a diode-bridge front-end inverter system (URL slug·검색어 기준, 전체 제목 원문 미확인) | 미확인(AAU 저장소; 제1저자 검색결과에 미표기) | 2017 | IEEE IFEEC 2017 – ECCE Asia | — | 미확인 | X | https://vbn.aau.dk/da/publications/artificial-neural-network-based-dc-link-capacitance-estimation-in | B, C |
| B1-06 | Capacitance estimation algorithm based on DC-link voltage harmonics using artificial neural network in three-phase motor drive systems | 미확인 | 미확인 | 미확인 | — | 미확인 | X | https://vbn.aau.dk/en/publications/capacitance-estimation-algorithm-based-on-dc-link-voltage-harmoni | B, C |
| B1-07 | Machine learning based condition monitoring of a DC-link capacitor in a Back-to-Back converter | 미확인(NITK 저장소) | 2022 | IEEE ICA-ACCA 2022 | pp. 1–5 | 10.1109/ICA-ACCA56767.2022.10006052 (검색결과에서 확인) | X(제1저자 미확인) | https://idr.nitk.ac.in/handle/123456789/29813 | B |
| B1-08 | Generative Physics-Informed Machine Learning Method for DC-Link Capacitance [Estimation …] (제목 후반부 원문 미확인) | Tianhao Qie, Xinan Zhang, Chaoqun Xiang, Shuai Zhao, Chaoqiang Jiang, Herbert H. C. Iu, Tyrone Fernando | 2025 (online 2024-10-21) | IEEE Trans. Ind. Electron. | 72(5):5461–5471 | 미확인 | V2 | https://scholars.cityu.edu.hk/en/publications/generative-physics-informed-machine-learning-method-for-dc-link-c/ | C, I |
| B1-09 | A Highly Accurate Generative Learning-Based DC-Link Capacitance Estimation Approach for Electrified Railway Traction Systems | Jianwei Zhao, Tianhao Qie, Xinan Zhang, Herbert Ho Ching Iu, Tyrone Fernando, Chaoqun Xiang | (2026, 이전 보고서 값; 이번 세션 미확인) | IET Power Electron. | 미확인 | 10.1049/pel2.70151 | V1† | https://www.citedrive.com/en/discovery/a-highly-accurate-generative-learningbased-dclink-capacitance-estimation-approach-for-electrified-railway-traction-systems/ | C |
| B1-10 | DC-Link Electrolytic Capacitors Monitoring Techniques Based on Advanced Learning Intelligence Techniques for Three-Phase Inverters | H. Dang et al.(이전 보고서) | 2022 | Machines | 10(12):1174 | 미확인 | X(이번 세션 검색 미발견) | (이전 보고서) https://www.mdpi.com/2075-1702/10/12/1174 | B |
| B1-11 | Capacitor Aging State Evaluation and a Remaining-Useful-Life Prediction Method Based on a CNN-LSTM Network Considering the Impact of Parameter Dispersion | 미확인 | 2025 | Electronics | 14(22):4452 | (이전 보고서 기재 10.3390/electronics14224452, 이번 세션 미재검증) | X(검색 한도 소진) | (이전 보고서) https://doi.org/10.3390/electronics14224452 | C(RUL) |
| B1-12 | Using LSTM neural network to predict remaining useful life of electrolytic capacitors in dynamic operating conditions | A. F. Shahraki et al.(이전 보고서) | 2023 | Proc. IMechE Part O | — | (이전 보고서 기재 10.1177/1748006X221087503, 이번 세션 미재검증) | X(검색 한도 소진) | (이전 보고서) https://journals.sagepub.com/doi/abs/10.1177/1748006X221087503 | C(RUL) |
| B1-13 | Data-Driven Approach for Fault Prognosis of SiC MOSFETs | Weiqiang Chen, Lingyi Zhang, Krishna Pattipati, Ali M. Bazzi, Shailesh Joshi, Ercan M. Dede | 2020 | IEEE Trans. Power Electron. | 35(4) | 10.1109/TPEL.2019.2936850 | V1 | https://scholarworks.aub.edu.lb/items/754c3e2e-de72-4796-9e71-c94187f20319/full | E |
| B1-14 | Machine Learning Pipeline for Power Electronics State of Health Assessment and Remaining Useful Life Prediction | Civan Lezgin Kahraman, Darius Roman, Lucas Kirschbaum, David Flynn, Jonathan Swingler | 2024 | IEEE Access | 12:136727–136746 | 10.1109/ACCESS.2024.3460177 | V1 | https://researchportal.hw.ac.uk/en/publications/machine-learning-pipeline-for-power-electronics-state-of-health-a/ ; https://doaj.org/article/10811e92f8b043028aec1f6d967d21f6 | E(RUL) |
| B1-15 | Estimating of IGBT Bond Wire Lift-Off Trend Using Convolutional Neural Network (CNN) | Thatree Mamee, Zaiqi Lou, Katsuhiro Hata, Makoto Takamiya, Takayasu Sakurai, Shin-Ichi Nishizawa, Wataru Saito | 2024 | IEEE Access | 12:96936–96945 | 미확인 | V2 | https://doaj.org/article/56cc239cec64451d8dbdeb6da0aa6792 ; https://ieeexplore.ieee.org/document/10597428 (문서번호만 노출, 해당 논문으로 추정) | E |
| B1-16 | Detection of Wire Lift-Off in Si-IGBTs and SiC-MOSFETs Using Machine Learning on Switching Waveforms | 미확인 | 미확인 | 미확인 | — | 미확인 | X | https://kirim.kmutt.ac.th/converis/portal/detail/Publication/1561884546?lang=en_GB | E |
| B1-17 | Parameter Estimation of Power Electronic Converters With Physics-Informed Machine Learning | Shuai Zhao, Yingzhou Peng, Yi Zhang, Huai Wang | 2022 | IEEE Trans. Power Electron. | 37(10):11567–11578 | 10.1109/TPEL.2022.3176468 | V1 | https://research.polyu.edu.hk/en/publications/parameter-estimation-of-power-electronic-converters-with-physics-/ ; https://vbn.aau.dk/files/519289832/Parameter_Estimation_of_Power_Electronic_Converters_With_Physics_Informed_Machine_Learning.pdf | I |
| B1-18 | Physics-informed Neural Network Approach for Early Degradation Trajectory Prediction of Power Semiconductor Modules | 미확인(AAU/PolyU 저장소; 제1저자 검색결과에 미표기) | 2025 | IEEE APEC 2025 | — | 미확인 | X | https://vbn.aau.dk/en/publications/physics-informed-neural-network-approach-for-early-degradation-tr/ | E, I(RUL) |

**집계**: 후보 18편 — V1 6편(B1-01, 02, 03, 13, 14, 17), V1† 1편(B1-09), V2 3편(B1-04, 08, 15), X 8편(B1-05, 06, 07, 10, 11, 12, 16, 18).

**이전 조사(D-시리즈) 재검증 결과**
- D2 → B1-02: 서지·DOI 일치 확인(V1). 권호 22(3), 쪽 513–521 추가 확인.
- D6 → B1-03: 저자 **Park, H.-J.; Kwak, Sangshin**, 18(3):1841–1850, DOI 확인(V1). 이전 "(확인 필요)" 해소.
- D3 → B1-04: 저자 **K. Örüklü, Ş. Ağalar** 확인(arXiv 참고문헌). DOI 는 여전히 미확인(V2). 연도는 참고문헌에 2024, 권호 72(4) 는 2025년 권이므로 early access 2024 / 정식 2025 로 추정(확인하지 못함).
- D10 → B1-09: 저자 6인과 DOI 확인, 연도 미확인(V1†).
- D1 → B1-10: 이번 세션 검색에서 발견하지 못함(X).
- D14, D16 → B1-11, B1-12: 검색 한도 소진으로 미재검증(X).
- 참고: 이전 index 의 R3(Zhao, Davari, Lu, Wang, Blaabjerg, TPEL 36(4) 2021, 커패시터 CM overview)와 B1-01(Shuai Zhao 외, TPEL 36(4) 2021, AI overview)은 **서로 다른 논문**이다. 과제에서 말한 "Zhao 2021 TPEL overview" 가 어느 쪽인지 문맥상 불분명하여 B1-01 을 신규로 추가하고 R3 는 기존 index 항목으로 둔다.

---

## 2. 핵심 논문 (8편) 상세

선정 기준: V1/V2 만, 연구실 4개 테마(커패시터 AI 진단 / SiC 등 소자 열화 / Edge AI / 일반화) 관련성, 분야 A·B·C·E·I 를 모두 포괄.
선정: **B1-01, B1-02, B1-03, B1-08, B1-13, B1-14, B1-15, B1-17**.
준핵심(서지 V2, 세부 내용은 이번 세션 미재검증): B1-04 — 3절·4절에서 이전 보고서 기재 내용을 표시와 함께 인용.

표기: "확인되지 않음" = 논문에서 확인되지 않음(초록/스니펫 수준). "(해석)" = 연구자 해석.

### 2.1 B1-01 — An Overview of Artificial Intelligence Applications for Power Electronics

| 항목 | 내용 |
|---|---|
| 논문 제목 | An Overview of Artificial Intelligence Applications for Power Electronics |
| 저자 | Shuai Zhao, Frede Blaabjerg, Huai Wang |
| 연도 | 2021 |
| 저널·학회 | IEEE Transactions on Power Electronics, 36(4):4633–4658 |
| DOI | 10.1109/TPEL.2020.3024914 (V1) |
| 진단 대상 | 리뷰. 전력전자 life-cycle 3단계(design, control, maintenance) 전반. 진단은 maintenance 단계에 해당 |
| 입력 신호 | 해당 없음(리뷰) |
| AI 모델 | 4범주로 분류: expert system, fuzzy logic, metaheuristic method, machine learning |
| 학습 방식 | AI task 를 optimization, classification, regression, data structure exploration 으로 구분 |
| 데이터 규모 | 500편 이상 문헌 검토(초록) |
| 운전조건 | 해당 없음 |
| 성능 지표 | 해당 없음 |
| 일반화 시험 여부 | 해당 없음. 초록에 "practical implementation challenges" 를 다룬다고 되어 있으나 일반화(조건 split 등)를 다루는지는 확인되지 않음 |
| 실험 vs 시뮬레이션 | 해당 없음 |
| fault severity 고려 | 확인되지 않음 |
| Edge 적용 여부 | 확인되지 않음 |
| 연구실과의 관련성 | 높음(서론·위치 설정용). 연구실 과제(정상/노화 이진 분류)는 이 리뷰의 maintenance × classification 칸에 해당(해석) |
| 한계 | 2020년까지 문헌. 커패시터·소자 진단 세부 비교는 본문 미열람으로 확인하지 못함 |

### 2.2 B1-02 — Deep learning-based estimation technique for capacitance and ESR of input capacitors in single-phase DC/AC converters

| 항목 | 내용 |
|---|---|
| 논문 제목 | Deep learning-based estimation technique for capacitance and ESR of input capacitors in single-phase DC/AC converters |
| 저자 | Hye-Jin Park, Jae-Chang Kim, Sangshin Kwak |
| 연도 | 2022 (3월) |
| 저널·학회 | Journal of Power Electronics, 22(3):513–521 |
| DOI | 10.1007/s43236-021-00366-x (V1) |
| 진단 대상 | 단상 DC/AC 컨버터 입력 커패시터의 capacitance, ESR (연속값 추정) |
| 입력 신호 | 실험으로 수집한 커패시터 **전압·전류**의 FFT 성분. 2×기본파(2f) 성분과 스위칭 주파수(fsw) 성분이 지배적이라고 분석한 뒤, 가장 지배적인 low-frequency·mid-frequency 성분을 추출 |
| AI 모델 | DNN |
| 학습 방식 | 지도학습 회귀(“estimate”, C·ESR 값 출력으로 판단). 손실함수·구조는 확인되지 않음 |
| 데이터 규모 | 확인되지 않음 |
| 운전조건 | 확인되지 않음 |
| 성능 지표 | 정량 수치 확인되지 않음. 정성 결과: C 추정은 mid-frequency 성분을 함께 쓸 때 low-frequency 단독보다 우수, ESR 추정은 mid-frequency 의 커패시터 전압·전류를 모두 쓸 때 우수 |
| 일반화 시험 여부 | 확인되지 않음(random split / 조건 split / 새 조건 모두 초록에 없음) |
| 실험 vs 시뮬레이션 | 실험 파형 수집(초록) |
| fault severity 고려 | C·ESR 연속값 추정이므로 노화 정도를 연속적으로 다룸(해석) |
| Edge 적용 여부 | 확인되지 않음 |
| 연구실과의 관련성 | **매우 높음**. 중앙대(CAU) 저장소 등록 논문(Kwak). 리플 파형 → FFT 대역 선택(2f, fsw) → 신경망이라는 구조가 연구실 코드(리플 파형 window 입력)와 직접 비교 대상. 이 논문은 회귀, 연구실은 이진 분류 |
| 한계 | 단상 토폴로지. 커패시터 전압·전류를 직접 측정(전류 센서 필요)하는 구성으로 보임(해석). 미관측 운전조건 시험 여부 확인되지 않음 |

### 2.3 B1-03 — DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs

| 항목 | 내용 |
|---|---|
| 논문 제목 | DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs |
| 저자 | H.-J. Park, Sangshin Kwak |
| 연도 | 2023 (5월) |
| 저널·학회 | Journal of Electrical Engineering & Technology, 18(3):1841–1850 |
| DOI | 10.1007/s42835-023-01424-z (V1) |
| 진단 대상 | 3상 DC/AC 컨버터 입력(DC) 커패시터의 capacitance, ESR |
| 입력 신호 | 서로 다른 주파수 대역의 입력(특정 주파수 성분 vs 넓은 주파수 대역). "low-frequency 성분은 capacitance 에, mid-frequency 성분은 ESR 에 지배적" 이라는 특성을 이용. 원 신호 종류(전압/전류 지점)는 확인되지 않음 |
| AI 모델 | DNN, CNN, Simple RNN, LSTM 4종 비교 |
| 학습 방식 | 지도학습 회귀(추정). 세부 확인되지 않음 |
| 데이터 규모 | 확인되지 않음 |
| 운전조건 | 확인되지 않음 |
| 성능 지표 | 정량 수치 확인되지 않음. 정성: 특정 주파수 성분 입력 시 DNN 이 우수, 넓은 대역 입력 시 CNN 이 최고 |
| 일반화 시험 여부 | 확인되지 않음 |
| 실험 vs 시뮬레이션 | 확인되지 않음(스니펫에 없음) |
| fault severity 고려 | 연속값 추정(해석) |
| Edge 적용 여부 | 확인되지 않음 |
| 연구실과의 관련성 | **매우 높음**. 3상, CAU(Kwak) 선행, 여러 DL 모델 비교라는 구조가 연구실의 CNN/LSTM/MLP/RF 비교와 같음. "입력 표현에 따라 최적 모델이 바뀐다" 는 결과는 연구실 비교 실험에서 입력 표현(원파형 vs 스펙트럼 대역)을 통제 변수로 두어야 한다는 근거(해석) |
| 한계 | 초록 기준 RF 등 고전 ML 비교 없음. 일반화·데이터 규모 미확인 |

### 2.4 B1-08 — Generative Physics-Informed Machine Learning Method for DC-Link Capacitance [Estimation …]

| 항목 | 내용 |
|---|---|
| 논문 제목 | Generative Physics-Informed Machine Learning Method for DC-Link Capacitance … (제목 후반부 원문 미확인) |
| 저자 | Tianhao Qie, Xinan Zhang, Chaoqun Xiang, Shuai Zhao, Chaoqiang Jiang, Herbert H. C. Iu, Tyrone Fernando |
| 연도 | 2025 (online 2024-10-21) |
| 저널·학회 | IEEE Transactions on Industrial Electronics, 72(5):5461–5471 |
| DOI | 미확인 (V2) |
| 진단 대상 | 차량용 전력 시스템 DC-link capacitance (pre-charging 과정에서 추정) |
| 입력 신호 | pre-charging 과정의 신호(구체 변수 확인되지 않음) |
| AI 모델 | diffusion 알고리즘(학습 데이터 증강) + physics-informed LSTM (PILSTM) |
| 학습 방식 | 소규모 실험 데이터 → diffusion 으로 증강 → PILSTM 지도 회귀. 물리 지식 결합 방식(손실항/구조)은 확인되지 않음 |
| 데이터 규모 | "small input experimental dataset"(수치 확인되지 않음) |
| 운전조건 | pre-charging 구간(정상 운전 중 아님) |
| 성능 지표 | 정량 수치 확인되지 않음. "superior accuracy, strong robustness to measurement noises" 주장 |
| 일반화 시험 여부 | 확인되지 않음(노이즈 강건성 주장만 있음) |
| 실험 vs 시뮬레이션 | 실험 검증(초록) |
| fault severity 고려 | 연속 C 추정(해석) |
| Edge 적용 여부 | 확인되지 않음 |
| 연구실과의 관련성 | 높음. 오실로스코프 실험 파형 수가 제한되는 연구실 상황에서 "생성 모델 증강 + 물리 결합" 이 대안 경로. 단 연구실은 정상 운전 리플 기반이라 신호 구간이 다름 |
| 한계 | pre-charge 구간 한정(quasi-online, 해석). 생성 데이터가 미관측 운전조건을 대변하는지 확인되지 않음 |

### 2.5 B1-17 — Parameter Estimation of Power Electronic Converters With Physics-Informed Machine Learning

| 항목 | 내용 |
|---|---|
| 논문 제목 | Parameter Estimation of Power Electronic Converters With Physics-Informed Machine Learning |
| 저자 | Shuai Zhao, Yingzhou Peng, Yi Zhang, Huai Wang |
| 연도 | 2022 (10월) |
| 저널·학회 | IEEE Transactions on Power Electronics, 37(10):11567–11578 |
| DOI | 10.1109/TPEL.2022.3176468 (V1) |
| 진단 대상 | 컨버터 부품 파라미터(구체 파라미터 목록은 확인되지 않음), case study: dc-dc Buck 컨버터 |
| 입력 신호 | 확인되지 않음 |
| AI 모델 | DNN 과 컨버터 dynamic model 을 결합한 PIML |
| 학습 방식 | physics-informed(신경망과 동적 모델 결합). 세부 확인되지 않음 |
| 데이터 규모 | 확인되지 않음. 순수 데이터 기반 방법의 training data·accuracy·robustness 문제를 극복한다고 주장 |
| 운전조건 | 확인되지 않음 |
| 성능 지표 | 확인되지 않음 |
| 일반화 시험 여부 | 확인되지 않음 |
| 실험 vs 시뮬레이션 | 확인되지 않음 |
| fault severity 고려 | 파라미터 연속 추정(해석) |
| Edge 적용 여부 | 확인되지 않음 |
| 연구실과의 관련성 | 중~높음. 물리 모델 결합 학습의 대표 레퍼런스(분야 I). 3상 인버터 DC-link 에 적용하려면 DC-link 리플 전류·전압 모델(스위칭 함수 기반)이 필요(추론) |
| 한계 | Buck 컨버터 case study. 인버터·DC-link 커패시터 적용은 확인되지 않음 |

### 2.6 B1-13 — Data-Driven Approach for Fault Prognosis of SiC MOSFETs

| 항목 | 내용 |
|---|---|
| 논문 제목 | Data-Driven Approach for Fault Prognosis of SiC MOSFETs |
| 저자 | Weiqiang Chen, Lingyi Zhang, Krishna Pattipati, Ali M. Bazzi, Shailesh Joshi, Ercan M. Dede |
| 연도 | 2020 (4월) |
| 저널·학회 | IEEE Transactions on Power Electronics, 35(4) |
| DOI | 10.1109/TPEL.2019.2936850 (V1) |
| 진단 대상 | SiC MOSFET 고장 예지(prognosis) |
| 입력 신호 | 소자 전압, 전류, 온도 등 특성의 열화에 따른 변화 추세 |
| AI 모델 | unsupervised learning(구체 알고리즘 확인되지 않음) |
| 학습 방식 | 비지도 |
| 데이터 규모 | 확인되지 않음 |
| 운전조건 | 확인되지 않음 |
| 성능 지표 | 확인되지 않음. system noise·data error 영향을 피할 수 있다고 주장. "SiC 소자 prognostics 를 다룬 첫 연구" 라고 주장 |
| 일반화 시험 여부 | 확인되지 않음 |
| 실험 vs 시뮬레이션 | 확인되지 않음 |
| fault severity 고려 | 열화 추세 기반 예지 → 진행 정도를 다룸(해석) |
| Edge 적용 여부 | "offline 분석에 한정되지 않고 online 구현을 목표" (초록). 실제 임베디드 구현 여부 확인되지 않음 |
| 연구실과의 관련성 | 높음(연구실 테마 2: SiC 열화 AI 진단). 비지도 접근은 노화 라벨이 부족한 실험 환경에서 참고 |
| 한계 | 알고리즘·데이터·성능 모두 초록에서 확인되지 않음 |

### 2.7 B1-14 — Machine Learning Pipeline for Power Electronics State of Health Assessment and Remaining Useful Life Prediction

| 항목 | 내용 |
|---|---|
| 논문 제목 | Machine Learning Pipeline for Power Electronics State of Health Assessment and Remaining Useful Life Prediction |
| 저자 | Civan Lezgin Kahraman, Darius Roman, Lucas Kirschbaum, David Flynn, Jonathan Swingler |
| 연도 | 2024 |
| 저널·학회 | IEEE Access, 12:136727–136746 |
| DOI | 10.1109/ACCESS.2024.3460177 (V1) |
| 진단 대상 | power MOSFET 의 SoH(healthy / pre-failure)와 RUL |
| 입력 신호 | MOSFET 열화 데이터(저항 열화 궤적 예측 언급) |
| AI 모델 | 2단계: (1) non-parametric 분류기 — Random Forest, (2) 회귀 — Bayesian Ridge (pre-failure 판정 시에만 동작) |
| 학습 방식 | 지도 분류 + 회귀 |
| 데이터 규모 | power MOSFET 20개 stress test |
| 운전조건 | "실제 운전 조건을 모사한 stress test"(세부 확인되지 않음) |
| 성능 지표 | 분류 평균 정확도 80%, RUL 회귀 평균 RMSPE 1.25% |
| 일반화 시험 여부 | 확인되지 않음(소자 단위 split 여부 미확인) |
| 실험 vs 시뮬레이션 | 가속 stress test 실측 데이터(자체/공개 데이터 여부 확인되지 않음) |
| fault severity 고려 | ○ (healthy / pre-failure 2단계 + RUL) |
| Edge 적용 여부 | "computationally efficient" 주장. 임베디드 구현 확인되지 않음 |
| 연구실과의 관련성 | 중~높음. "분류 → 조건부 회귀" 2단계 구조는 연구실 이진 분류를 노화 정도 추정으로 확장할 때의 설계 참고. RF 사용은 연구실 RF 비교군과 대응 |
| 한계 | 소자 단품 시험이며 컨버터 운전 신호가 아님. 표본 20개로 소량. 분류 정확도 80% 로 높지 않음 |

### 2.8 B1-15 — Estimating of IGBT Bond Wire Lift-Off Trend Using Convolutional Neural Network (CNN)

| 항목 | 내용 |
|---|---|
| 논문 제목 | Estimating of IGBT Bond Wire Lift-Off Trend Using Convolutional Neural Network (CNN) |
| 저자 | Thatree Mamee, Zaiqi Lou, Katsuhiro Hata, Makoto Takamiya, Takayasu Sakurai, Shin-Ichi Nishizawa, Wataru Saito |
| 연도 | 2024 |
| 저널·학회 | IEEE Access, 12:96936–96945 |
| DOI | 미확인 (V2) |
| 진단 대상 | IGBT 모듈 bond wire lift-off |
| 입력 신호 | 게이트 전압 파형 V_ge (Digital Gate Driver IC 로 생성·수집, 스위칭 모드 CVC / 2-sVC) |
| AI 모델 | CNN |
| 학습 방식 | 지도 분류(4등급) |
| 데이터 규모 | 확인되지 않음 |
| 운전조건 | 두 스위칭 모드(CVC, 2-sVC). 부하·온도 등 운전조건 변화는 확인되지 않음 |
| 성능 지표 | 정량 수치 확인되지 않음. "high accuracy", 2-sVC 모드 파형이 CVC 보다 정확도 높음 |
| 일반화 시험 여부 | 확인되지 않음 |
| 실험 vs 시뮬레이션 | 실측(DGD IC 구현 후 파형 수집) |
| fault severity 고려 | **○** — no / light / medium / heavy damage 4등급 |
| Edge 적용 여부 | 확인되지 않음(게이트 드라이버 IC 기반이라 온보드 진단 가능성은 있음 — 해석) |
| 연구실과의 관련성 | 높음. 원파형 직접 입력 CNN + severity 등급이라는 점에서 연구실 이진 분류의 다등급 확장 참고. 측정 모드에 따라 정확도가 달라진다는 결과는 "운전/측정 조건이 분류 성능에 영향" 의 근거 |
| 한계 | 새 소자·새 조건 일반화 미확인. 필요한 샘플링 속도·데이터 규모 미확인 |

(참고) 같은 검색에서 "turn-off V_ge 파형으로 약 99% 정확도, 2.5 GS/s → 100 MS/s 다운샘플링에도 유지" 라는 스니펫이 있었으나 어느 논문(B1-15 또는 동일 그룹의 학회 논문)의 내용인지 특정할 수 없어 B1-15 에 귀속하지 않았다.

---

## 3. 분야별 연구동향 요약 (근거 ID 인용)

**A. AI 기반 전력전자 상태감시(리뷰)**
- B1-01 은 500편 이상을 design/control/maintenance × optimization/classification/regression/data exploration 으로 분류했다. 진단은 maintenance 단계의 분류·회귀 과제로 정리된다.
- 커패시터 CM 리뷰(index R1–R3, 이번 세션 미재검증)와 AI 리뷰(B1-01)는 별개 계열이며, "커패시터 + AI" 를 함께 다룬 리뷰는 이번 세션에서 추가로 찾지 못했다(검색 한도 소진으로 탐색 불완전).
- 검색 범위 안의 AI 진단 논문은 대부분 단일 부품(커패시터 B1-02/03/08, 소자 B1-13/14/15)을 대상으로 하며, 컨버터 수준 통합 진단은 이번 후보에 없다.

**B. DC-link 커패시터 ML/DL 상태감시**
- 입력은 크게 (i) 커패시터 v·i 의 FFT 성분(B1-02: 2f, fsw), (ii) 주파수 대역 입력(B1-03), (iii) DC-link 전압 리플(B1-04 — 이전 보고서 기준 PSD; B1-07 — wavelet 분해), (iv) 출력전류+DC-link 리플(B1-05, 이전 보고서·AAU 페이지 스니펫), (v) pre-charge 과도(B1-08) 로 나뉜다.
- 모델은 ANN/DNN(B1-02, 05, 06), DNN·CNN·RNN·LSTM 비교(B1-03), GPR(B1-04, 이전 보고서), KNN/SVM/NB(B1-07, SVM 우수)로 다양하다.
- 같은 데이터에서 입력 표현이 바뀌면 최적 모델이 바뀐다는 결과(B1-03: 특정 성분 → DNN, 넓은 대역 → CNN)가 있어, 모델 비교는 입력 표현과 묶어서 해석해야 한다.
- 토폴로지는 단상 DC/AC(B1-02), 3상 DC/AC(B1-03), AC/DC/AC·B2B(B1-04, 05, 07), 차량 전원(B1-08)이며, 3L-NPC 대상 ML 논문은 이번 후보에 없다(이전 보고서 13절의 사실과 일치).

**C. 커패시터 열화·ESR·C 추정(회귀/분류/RUL)**
- 회귀가 주류: C·ESR 동시 추정(B1-02, 03), C 단독(B1-04, 05, 06, 08, 09).
- 소규모 실험 데이터 문제에 대해 생성 모델 증강이 등장했다: VAE+LSTM(B1-09), diffusion+PILSTM(B1-08). 같은 연구 그룹(Qie, Zhang, Iu, Fernando, Xiang)의 연속 연구다.
- 노이즈 강건성 주장(B1-08, 09)은 있으나 미관측 운전조건 시험은 초록에서 확인되지 않는다.
- 커패시터 RUL(B1-11 CNN-LSTM, B1-12 LSTM)은 단품 열화 궤적 기반이며 이번 세션에서 재검증하지 못했다.

**E. 반도체(IGBT, SiC MOSFET) 열화 AI 진단**
- 입력은 소자 전기·열 특성 추세(B1-13), 저항 열화 궤적(B1-14), 게이트 전압 파형(B1-15), 스위칭 파형(B1-16, X)이다.
- 학습 방식은 비지도 예지(B1-13), 분류+회귀 2단계(B1-14), CNN 다등급 분류(B1-15)로 다양하다.
- severity 를 명시적으로 등급화한 것은 B1-15(4등급), 단계화한 것은 B1-14(healthy/pre-failure + RUL)이다.
- 데이터는 가속 stress test·power cycling 기반 단품 시험이 주류다(B1-14: 20개, B1-18: IGBT 18개 — B1-18 은 X 등급이라 참고만).

**I. Physics-informed ML**
- 컨버터 동적 모델과 DNN 결합 파라미터 추정(B1-17, Buck), 물리 결합 LSTM(B1-08, DC-link C), VCE 온도 의존성 보정 + 물리 손실항 LSTM(B1-18, IGBT 열화 궤적, X 등급)이 확인되었다.
- 공통 동기는 "데이터 부족·정확도·강건성"(B1-17 초록) 과 "소규모 실험 데이터"(B1-08) 이다.
- B1-18 은 초기 40% 데이터로 EOL 예측 정확도 약 90% 를 주장한다(스니펫, X 등급 — 저자 미확인).
- 인버터 DC-link 커패시터를 정상 운전 리플로 진단하는 PIML 은 이번 후보에서 찾지 못했다.

**RUL**
- 소자: B1-14(MOSFET, RMSPE 1.25%), B1-18(IGBT, X). 커패시터: B1-11, B1-12(X, 미재검증).
- RUL 연구는 모두 단품 가속시험 데이터 기반으로 보이며, 컨버터 운전 중 측정 신호로 RUL 을 예측한 사례는 이번 후보에 없다.

---

## 4. 선행연구의 공통 한계 (근거 ID)

1. **일반화 평가가 초록 수준에서 보이지 않음**: 핵심 8편 중 random split / 조건 split / 새 조건 시험을 명시한 논문이 없다(B1-02, 03, 08, 13, 14, 15, 17 모두 "확인되지 않음"). 다중 운전조건 실험을 명시한 것은 이전 보고서 기준 B1-04(부하·출력주파수, 이번 세션 미재검증) 정도다. 본문을 읽지 못했으므로 "평가하지 않았다" 가 아니라 "확인되지 않았다" 이다. 연구실의 미관측 조건(f0, fsw, 출력전압, 부하저항) 일반화 시험은 이 공백을 직접 겨냥한다(해석).
2. **소규모 실험 데이터**: 생성 증강(B1-08, 09)과 PIML(B1-17)이 "데이터 부족" 을 동기로 명시한다. 소자 쪽도 표본 20개(B1-14), 18개(B1-18) 수준이다.
3. **단품·가속시험 의존**: RUL·소자 연구(B1-11, 12, 14, 18)는 부품 단품 시험 데이터이며, 컨버터 운전 중 신호와의 연결이 확인되지 않는다.
4. **측정 지점·센서 의존**: B1-02 는 커패시터 전압·전류를 직접 사용한다. B1-15 는 디지털 게이트 드라이버 IC 가 필요하다. 현장 인버터에서 쓸 수 있는 신호인지가 공통 쟁점(해석).
5. **특정 구간·토폴로지 한정**: pre-charge 구간(B1-08), Buck(B1-17), 단상(B1-02). 3L-NPC 대상 ML 논문은 후보에 없다.
6. **성능 지표 비통일**: RMSPE(B1-14), 정확도(B1-14, 15), 정성 비교(B1-02, 03), 주장만(B1-08, 13). 논문 간 정량 비교가 불가능하다.
7. **Severity 처리 방식 분산**: 연속 회귀(B1-02, 03, 08), 다등급(B1-15), 2단계(B1-14), 이진 또는 미확인(B1-07). 정상/노화 이진 분류는 노화 정도 정보를 버린다(해석).
8. **Edge 구현 보고 부족**: online 구현 목표(B1-13), 계산 효율 주장(B1-14) 외에 MCU 구현·추론 시간·메모리 보고는 후보 전체에서 확인되지 않는다.

---

## 5. 미완료 항목 (후속 검색 필요)
- B1-04, B1-08, B1-15 의 DOI 확인.
- B1-05, B1-06, B1-07, B1-16, B1-18 의 제1저자 확인 → V1/V2 승격 가능.
- B1-09 연도 확인.
- 커패시터 RUL(B1-11, B1-12), D1(B1-10), D8(Random Forest, Electronics 2023) 재검증.
- "AI 기반 전력전자 상태감시/PHM 리뷰"(2022 이후) 추가 탐색 — 이번 세션은 B1-01 하나만 확보.
- Edge AI(MCU 구현) 커패시터/소자 진단 논문 탐색 — 이번 세션 미수행.
