# Agent C — Literature Researcher 2: AI 기반 아크 고장 진단 (연구실 외부 선행연구)

- 작성일: 2026-10-07
- 범위: F(ML/DL 아크 검출), G(AC/DC, series/parallel, PV DC arc, UL 1699/IEC 62606), H(부하 일반화·미관측 부하·domain adaptation/transfer learning), 경량/임베디드
- 도구 제약: WebSearch만 사용. **세션 공유 WebSearch 한도(200회/turn)가 작업 도중 소진되어** 일부 DOI 확인(ArcNet, DA-DCGAN, Siegel 2018)과 일부 논문의 저자·게재지 확인을 끝내지 못했다. 해당 항목은 V2/X로 남겨 두었다. 후속 메시지로 검색을 이어 가면 보강할 수 있다.
- 검증 등급: **V1** = 제목·제1저자·게재지·연도 일치 + DOI 문자열을 검색결과 URL/스니펫에서 직접 확인 / **V2** = 서지 일치, DOI 미확인(또는 arXiv 프리프린트) / **X** = 서지 확인 실패(핵심 선정 제외)
- 세부 내용(데이터 규모, 부하, split, 성능 등)은 **검색 스니펫/초록 수준에서 확인한 것만** 적었다. 원문(PDF) 본문은 읽지 못했다.

---

## 1) 후보 표 (외부 연구, 18편)

| ID | 제목 | 저자 | 연도 | 저널/학회 | 권호 | DOI | 등급 | 근거 URL | AC/DC | series/parallel |
|---|---|---|---|---|---|---|---|---|---|---|
| C-01 | ArcNet: Series AC Arc Fault Detection Based on Raw Current and Convolutional Neural Network | Yao Wang, Linming Hou, Kamal Chandra Paul, Yunsheng Ban, Chen Chen, Tiefu Zhao | 2022 | IEEE Transactions on Industrial Informatics | 18(1), pp. 77–86 | 미확인 | V2 | https://dblp.org/pid/303/5658 , https://typeset.io/authors/yao-wang-lbawc9qs57 | AC | series |
| C-02 | Efficient-ArcNet: Series AC Arc Fault Detection using Lightweight Convolutional Neural Network | 미확인 (Zhao 그룹으로 추정, 확인하지 못함) | 미확인 | 미확인 (IEEE Xplore 9947475 문서와 연결되는지 확인하지 못함) | 미확인 | 미확인 | X | https://www.mdpi.com/2079-9292/12/22/4617 (2차 인용), https://ieeexplore.ieee.org/document/9947475 | AC | series |
| C-03 | DA-DCGAN: An effective methodology for DC series arc fault diagnosis in photovoltaic systems | S. Lu, T. Sirojan, B. T. Phung, D. Zhang, E. Ambikairajah | 2019 | IEEE Access | 미확인 | 미확인 | V2 | https://aimspress.com/aimspress-data/era/2024/1/PDF/era-32-01-016.pdf (2차 인용), https://pen.ius.edu.ba/index.php/pen/article/view/1202 | DC (PV) | series |
| C-04 | Artificial Intelligence for DC Arc Fault Detection in Photovoltaic Systems (리뷰) | Kamal Chandra Paul 외 (Chen Chen, Yao Wang, Tiefu Zhao 포함; 나머지 공저자 표기는 다시 확인해야 함) | 2025 | IEEE Access | 미확인 | 10.1109/ACCESS.2025.3572521 | V1 | https://doaj.org/article/9e9435d5f93840fa82ee38a532eb8da7 | DC (PV) | series |
| C-05 | TL–LEDarcNet: Transfer Learning Method for Low-Energy Series DC Arc-Fault Detection in Photovoltaic Systems | Yoondong Sung, Gihwan Yoon, Ji-Hoon Bae, Suyong Chae | 2022 | IEEE Access | 10, pp. 100725–100735 | 10.1109/ACCESS.2022.3208115 | V1 | https://doaj.org/article/f8acb1683e4f4f9e9af687863463b566 | DC (PV) | series |
| C-06 | Why AI: A Comparative Study for Detection Methods in DC Series Arc Fault | Y. Mao, S. Safa, G. Smith, L. Wurth, R. Weiss, J. Hagemeyer | 2025 | IEEE Access | 미확인 | 10.1109/ACCESS.2025.3548309 | V1 | https://cris.fau.de/publications/337993174 | DC | series |
| C-07 | A Lightweight, Transferable, and Self-Adaptive Framework for Intelligent DC Arc-Fault Detection in Photovoltaic Systems | Xiaoke Yang, Long Gao, Haoyu He, Hanyuan Hang, Qi Liu, Shuai Zhao, Qiantu Tuo, Rui Li | 2026 | arXiv preprint (arXiv:2603.25749) | – | 없음 (arXiv ID) | V2 (프리프린트) | https://arxiv.org/abs/2603.25749 | DC (PV) | 확인되지 않음 (AFCI 맥락) |
| C-08 | Real-time Deep Neural Networks for internet-enabled arc-fault detection | J. E. Siegel 외 (Pratt, Sun, Sarma로 알려져 있으나 검색결과로 전체 확인 못 함) | 2018 | Engineering Applications of Artificial Intelligence | 74, pp. 35–42 | 미확인 | V2 (기간 밖) | https://dspace.mit.edu/handle/1721.1/121372 | AC (가정용 콘센트 맥락) | 확인되지 않음 |
| C-09 | Ensemble machine learning based adaptive arc fault detection for DC distribution systems | Vu Le, Xiu Yao | 2019 | 미확인 (학회로 추정, 확인하지 못함) | 미확인 | 미확인 | X | https://researchconnect.buffalo.edu/en/publications/ensemble-machine-learning-based-adaptive-arc-fault-detection-for-/ | DC | 확인되지 않음 |
| C-10 | Advancements in Arc Fault Detection for Electrical Distribution Systems: A Comprehensive Review from Artificial Intelligence Perspective (리뷰) | Kriti Thakur, Divyanshi Dwivedi, K. Victor Sam Moses Babu, Alivelu Manga Parimi, Pradeep Kumar Yemula, Pratyush Chakraborty, Mayukha Pal | 2023 | arXiv preprint (arXiv:2311.16804) | – | 없음 (저널판 확인 못 함) | V2 (프리프린트) | https://arxiv.org/pdf/2311.16804 | AC/DC | 둘 다 (리뷰) |
| C-11 | AC series arc fault detection based on RLC arc model and convolutional neural network | Run Jiang, Yilong Wang, Xiaoqing Gao, Guanghai Bao, Qiteng Hong, Campbell Booth | 2023 | IEEE Sensors Journal | 23(13), pp. 14618–14627 | 10.1109/JSEN.2023.3280009 | V1 | https://strathprints.strath.ac.uk/86091 | AC | series |
| C-12 | Machine learning approach to detect arc faults based on regular coupling features | Run Jiang, Guanghai Bao, Qiteng Hong, Campbell Booth | 2023 (early access 2022) | IEEE Transactions on Industrial Informatics | 19(3), pp. 2761–2771 | 10.1109/TII.2022.3153333 | V1 | https://strathprints.strath.ac.uk/79813 | AC (추정; 스니펫에 AC/DC 명시 없음) | series |
| C-13 | Adaptive Detection Method for Arc Faults in Low Voltage Power Supply Systems | Silei Chen, Yutian Liu, Jiahao Mi, Zhouruixing Wang, Ping Gao, Xingwen Li | 2024 | 미확인 | 미확인 | 미확인 | X | https://scholar.xjtu.edu.cn/zh/publications/adaptive-detection-method-for-arc-faults-in-low-voltage-power-sup/ | AC (IEC 62606, GB/T 31143 기준) | series + parallel |
| C-14 | Series-arc-fault diagnosis using feature fusion-based deep learning model | Choi 외 (제1저자 성 "Choi"만 확인, 이름과 공저자는 확인 못 함) | 2024 | ETRI Journal | 46(6), pp. 1061–1074 | 10.4218/etrij.2023-0457 | V1 | https://onlinelibrary.wiley.com/doi/10.4218/etrij.2023-0457 , https://ksp.etri.re.kr/ksp/article/read?id=68928 | AC (UL1699 기준으로 추정) | series |
| C-15 | Lightweight AC Arc Fault Diagnosis via Fourier Transform Inspired Multi-frequency Neural Network | Qianchao Wang, Chuanzhen Jia, Yuxuan Ding, Zhe Li, Yaping Du | 2025 | arXiv preprint (arXiv:2510.26093) | – | 없음 | V2 (프리프린트) | https://arxiv.org/pdf/2510.26093 | AC | 확인되지 않음 |
| C-16 | Arc-Fault Detection Using Stage-Wise Alignment and Feature Fusion of Dual Learnable Time–Frequency Representations | 미확인 | 2026 | Sensors (MDPI) | 미확인 | 10.3390/s26165095 (URL) | X (저자 미확인) | https://pmc.ncbi.nlm.nih.gov/articles/PMC13517359/ | 확인되지 않음 | 확인되지 않음 |
| C-17 | Diagnosis of series DC arc faults – a machine learning approach | R. D. Telford 외 | 2016 | IEEE Transactions on Industrial Informatics | 미확인 | 미확인 | V2 (기간 밖, 기준선) | https://strathprints.strath.ac.uk/58843/7/Telford_etal_IEEETII2016_Diagnosis_of_series_DC_arc_faults.pdf | DC | series |
| C-18 | Lightweight transfer nets and adversarial data augmentation for photovoltaic series arc fault detection with limited fault data (LTCNN-ADA) | 미확인 (Rui Ma 공저자 확인) | 미확인 | 미확인 | 미확인 | 미확인 | X | https://scholarship.miami.edu/esploro/outputs/journalArticle/Lightweight-transfer-nets-and-adversarial-data/991032861016302976 | DC (PV) | series |

### 1-a) 연구실(곽상신 교수, CAU) 논문으로 판단되거나 추정되는 항목 — 별도 표시만 하고 핵심 선정에서 제외

| ID | 제목 | 게재지·연도 | 연구실 판단 근거 | 근거 URL |
|---|---|---|---|---|
| L-01 | Series DC Arc Fault Detection Using Machine Learning Algorithms | IEEE Access, 2021 | CAU ScholarWorks 등재 | https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/50141 |
| L-02 | Different Domains Based Machine and Deep Learning Diagnosis for DC Series Arc Failure | IEEE Access, 2021 | 추정 (저자 확인 못 함) | https://doaj.org/article/fbc77fdeb5a94f7cb3793853f284a81f |
| L-03 | DC Series Arc Failure Diagnosis Using Artificial Machine Learning With Switching Frequency Component Elimination Technique | IEEE Access, 2023 | 추정 (저자 확인 못 함) | https://doaj.org/article/e642b659cab94f02bc6358a3492c30c2 (연결 여부는 확인하지 못함) |
| L-04 | DC Series Arc Fault Diagnosis Scheme Based on Hybrid Time and Frequency Features Using Artificial Learning Models | Machines, 2024 | Dang H.-L., Kwak S., Choi S. 공저 (검색결과) | https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/72999 |
| L-05 | DC series arc diagnosis based on deep-learning algorithm with frequency-domain characteristics | 미확인 | CAU ScholarWorks 등재 | https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/51657 |

### 1-b) 검색 중 확인했지만 서지가 확인되지 않아 표에서 뺀 항목 (X, 참고용)
- "A Novel Methodology for Series Arc Fault Detection by Temporal Domain Visualization and Convolutional Neural Network" (PMC6983122, Sensors 계열로 추정). 저자를 확인하지 못함.
- "Series AC Arc Fault Detection Method Based on High-Frequency Coupling Sensor and Convolution Neural Network" (PMC7506653, Sensors 2020). 3-layer CNN이 직렬 아크와 **부하 종류를 동시에 식별**한다는 스니펫만 확인함.
- "Series Arc Fault Detection Based on Multimodal Feature Fusion" (Sensors, DOI 10.3390/s23177646 URL). 저자를 확인하지 못함.
- "Series arc fault detection based on continuous wavelet transform and DRSN-CW with limited source data" (Scientific Reports 2022, s41598-022-17235-7). 저자를 확인하지 못함.
- "MDJA-Trans … load-aware low-voltage AC arc fault detection" (Springer Energy Informatics 2026 URL). 서지를 확인하지 못함.

---

## 2) 핵심 논문 상세 (8편: 부하 일반화 3편, 임베디드·실시간 3편, 리뷰 1편, 방법론 비교 1편)

> 표기: "확인되지 않음" = 논문에서 확인되지 않음(초록 수준). [해석] = 이 문서 작성자의 해석.

### K1. C-11 — AC series arc fault detection based on RLC arc model and convolutional neural network (V1)
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재지 | Run Jiang, Yilong Wang, Xiaoqing Gao, Guanghai Bao, Qiteng Hong, Campbell Booth / 2023 / IEEE Sensors Journal 23(13) 14618–14627 |
| DOI | 10.1109/JSEN.2023.3280009 |
| 진단 대상 | AC series arc fault (검출, 이진) |
| 입력 신호 | 전류. 복잡한 특징을 가진 전류를 몇 가지 진동(oscillation) 신호 유형으로 단순화해 다룸 |
| AI 모델 | 1-D CNN (1DCNN) |
| 학습 방식 | 지도학습. **고주파 RLC 아크 모델로 학습 데이터를 생성**함(부하 유형, 초기 위상각, Bernoulli-sequence 주파수를 조절) |
| 데이터 규모 | 확인되지 않음 |
| 운전조건(부하) | 미관측(unknown) 부하 9종에서 시험. 부하 명칭은 확인되지 않음 |
| 성능 지표 | 미관측 부하 9종 평균 검출 정확도 99.33% |
| 일반화 시험 | **있음**: 학습에 쓰지 않은 부하 9종에서 평가 |
| 실험 vs 시뮬 | 학습 데이터는 모델로 생성(시뮬). 시험 데이터가 실측인지는 초록에서 명시를 확인하지 못함(실측으로 추정) |
| severity | 확인되지 않음 |
| Edge 적용 | 확인되지 않음 |
| 연구실과의 관련성 | "부하 범용 아크 진단"과 직접 관련됨. [해석] 물리 기반 아크 모델로 부하 다양성을 합성하는 방식은 연구실의 MATLAB/Simulink 시뮬레이션 역량과 결합하기 쉽다 |
| 한계 | AC series만 다룸. DC, parallel, 인버터·SMPS형 부하 포함 여부는 확인하지 못함. sim-to-real 차이에 대한 정량 분석이 있는지는 확인되지 않음 |

### K2. C-12 — Machine learning approach to detect arc faults based on regular coupling features (V1)
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재지 | Run Jiang, Guanghai Bao, Qiteng Hong, Campbell Booth / 2023 (early access 2022) / IEEE Transactions on Industrial Informatics 19(3) 2761–2771 |
| DOI | 10.1109/TII.2022.3153333 |
| 진단 대상 | series arc fault (SAF) 검출. AC로 추정(스니펫에 명시 없음) |
| 입력 신호 | 전류에서 뽑은 regular coupling features(RCF): 시간영역 2개(impulse-factor analysis IFA, covariance-matrix analysis CMA)와 주파수영역 1개(multiple frequency-band analysis MFA) |
| AI 모델 | ML 분류기. 종류는 확인되지 않음 |
| 학습 방식 | **단일 부하 회로 샘플로만 학습** |
| 데이터 규모 | 확인되지 않음 |
| 운전조건(부하) | 학습: 단일 부하 회로 / 시험: **미관측 다중부하(multi-load) 회로** |
| 성능 지표 | "generalization ability와 detection accuracy가 크게 향상됨"까지만 확인. 수치는 확인되지 않음 |
| 일반화 시험 | **있음**: 단일 부하에서 미관측 다중부하로 넘어가는 cross-condition 평가 |
| 실험 vs 시뮬 | 실험 (experimental results) |
| severity | 확인되지 않음 |
| Edge 적용 | 확인되지 않음 |
| 연구실과의 관련성 | "부하 범용" 진단에서 **도메인 지식 기반 특징 설계가 일반화를 이끈 사례**다. 연구실의 시간·주파수 하이브리드 특징 접근(L-04)과 비교 기준으로 쓸 수 있다 |
| 한계 | 성능 수치와 분류기 종류를 초록 수준에서 확인하지 못함. DC 적용 여부 확인되지 않음 |

### K3. C-07 — A Lightweight, Transferable, and Self-Adaptive Framework for Intelligent DC Arc-Fault Detection in Photovoltaic Systems (V2, 프리프린트)
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재지 | Xiaoke Yang, Long Gao, Haoyu He, Hanyuan Hang, Qi Liu, Shuai Zhao, Qiantu Tuo, Rui Li / 2026 / arXiv:2603.25749 (동료심사 전) |
| DOI | 없음 (arXiv ID) |
| 진단 대상 | 주거용 PV의 DC arc fault (AFCI). series/parallel 구분은 확인되지 않음 |
| 입력 신호 | 스펙트럼 표현. 원신호 종류(전류 등)는 초록에서 명시를 확인하지 못함 |
| AI 모델 | LD-Spec(스펙트럼 기반 경량 NN), LD-Align(이종 인버터 하드웨어 사이의 표현 정렬), LD-Adapt(클라우드-엣지 협업 자기적응 업데이트, 미관측 운전조건 감지) |
| 학습 방식 | 지도학습 + cross-hardware representation alignment(도메인 정렬) + 현장 지속 업데이트 |
| 데이터 규모 | 확인되지 않음 |
| 운전조건 | 여러 인버터 플랫폼(하드웨어 이질성), 장기 운전조건 drift, 환경 노이즈, nuisance trip이 잘 나는 조건 |
| 성능 지표 | Accuracy 0.9999, F1 0.9996, **false-trip rate 0%** (nuisance-trip-prone 조건) |
| 일반화 시험 | **있음 (cross-hardware, 미관측 운전조건 감지)**. 부하 종류 일반화와는 다른 축이다 |
| 실험 vs 시뮬 | 하드웨어 실험 (extensive hardware experiments) |
| severity | 확인되지 않음 |
| Edge 적용 | on-device inference를 겨냥함. 탑재 기기(MCU 종류 등)는 확인되지 않음 |
| 연구실과의 관련성 | "인버터 스위칭 노이즈에 강인한 진단", "MCU 탑재", "부하/조건 범용"을 한 프레임으로 묶은 최신 사례다. 인버터 스위칭 스펙트럼 간섭을 명시적 문제로 정의한 점이 연구실의 switching-frequency 제거 접근(L-03)과 연결된다 |
| 한계 | 프리프린트라 검증되지 않음. AC 미포함. 클라우드 의존(LD-Adapt)이 독립형 AFCI 제품 요건과 맞는지 불분명함 |

### K4. C-05 — TL–LEDarcNet (V1)
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재지 | Yoondong Sung, Gihwan Yoon, Ji-Hoon Bae, Suyong Chae / 2022 / IEEE Access 10, 100725–100735 |
| DOI | 10.1109/ACCESS.2022.3208115 |
| 진단 대상 | PV 시스템의 **저에너지(low-energy)** series DC arc |
| 입력 신호 | 센싱 전류 |
| AI 모델 | 1-layer LSTM + 경량 1D-CNN |
| 학습 방식 | 2단계 학습(transfer learning 기반) |
| 데이터 규모 | 확인되지 않음 |
| 운전조건(부하) | 확인되지 않음 |
| 성능 지표 | 정확도 95.8% |
| 일반화 시험 | 확인되지 않음 (TL은 2단계 학습에 쓰였고, cross-load 평가 여부는 확인되지 않음) |
| 실험 vs 시뮬 | 확인되지 않음 (실측 전류로 추정) |
| severity | "저에너지 아크"를 대상으로 한 점이 에너지 수준 관점과 맞닿음. severity 등급 분류는 확인되지 않음 |
| Edge 적용 | **single-board computer에서 실시간 동작** 확인 |
| 연구실과의 관련성 | 국내 연구(외부)로 DC arc + 경량 + 실시간 탑재 사례. MCU 탑재 목표의 중간 단계 비교 기준으로 쓸 수 있다 |
| 한계 | SBC는 MCU보다 자원이 크다. 정확도 95.8%로 다른 연구보다 낮다. 부하 일반화 평가가 확인되지 않음 |

### K5. C-01 — ArcNet (V2: DOI 미확인)
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재지 | Yao Wang, Linming Hou, Kamal Chandra Paul, Yunsheng Ban, Chen Chen, Tiefu Zhao / 2022 / IEEE Transactions on Industrial Informatics 18(1) 77–86 |
| DOI | 미확인 |
| 진단 대상 | AC series arc |
| 입력 신호 | **raw current** (전처리·특징추출 없음), 10 kHz 샘플링 |
| AI 모델 | CNN (ArcNet) |
| 학습 방식 | 지도학습 |
| 데이터 규모 | 확인되지 않음 |
| 운전조건(부하) | **IEC 62606**에 따른 부하 8종. 아크 유형 2가지(케이블 느슨한 접속, 절연 열화) |
| 성능 지표 | 최대 99.47% (10 kHz). 평균 실행시간 31 ms/sample(1 cycle) |
| 일반화 시험 | 확인되지 않음 (split 방식, 미관측 부하 시험 여부 확인되지 않음) |
| 실험 vs 시뮬 | 실측 DB (IEC 62606 기준 수집) |
| severity | 확인되지 않음 |
| Edge 적용 | "practical hardware deployment 가능성"을 실행시간으로 제시함. 하드웨어 기종은 확인되지 않음 |
| 연구실과의 관련성 | AC arc DL의 대표 기준선. 저샘플링 raw-current 방식은 MCU 탑재와 맞는다 |
| 한계 | 학습에 쓴 부하와 같은 부하 안에서의 성능일 가능성이 있음(확인 필요). DC 미적용 |

### K6. C-06 — Why AI: A Comparative Study for Detection Methods in DC Series Arc Fault (V1)
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재지 | Y. Mao, S. Safa, G. Smith, L. Wurth, R. Weiss, J. Hagemeyer / 2025 / IEEE Access |
| DOI | 10.1109/ACCESS.2025.3548309 |
| 진단 대상 | DC series arc |
| 입력 신호 | 확인되지 않음 (저샘플링 장치 전제) |
| AI 모델 | AI 기반 방법과 rule-based 방법 비교. 개별 모델은 확인되지 않음 |
| 학습 방식 | 확인되지 않음 |
| 데이터 규모 | 확인되지 않음 |
| 운전조건 | "varying conditions". 세부 조건은 확인되지 않음 |
| 성능 지표 | 두 방법의 장단점을 통계적으로 비교. 수치는 확인되지 않음 |
| 일반화 시험 | **조건 변화에 대한 적응성 비교**가 핵심 결론: AI가 더 적응적이고, 도메인 지식 기반 사전 특징추출을 결합하면 전반 성능이 좋아짐 |
| 실험 vs 시뮬 | 문헌 검토 + 실험 검증 |
| severity | 확인되지 않음 |
| Edge 적용 | **저샘플링·저연산 자원 제약 장치**의 산업 적용을 목표로 함 |
| 연구실과의 관련성 | "임계값 대신 왜 AI인가"에 대한 외부 근거. MCU용 저샘플링 설계 논리를 뒷받침함 |
| 한계 | 세부 모델·데이터·수치를 초록 수준에서 확인하지 못함. AC 미포함 |

### K7. C-14 — Series-arc-fault diagnosis using feature fusion-based deep learning model (V1)
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재지 | Choi 외 (제1저자 성만 확인) / 2024 / ETRI Journal 46(6) 1061–1074 |
| DOI | 10.4218/etrij.2023-0457 |
| 진단 대상 | 배전계통 series arc (UL1699 기준이므로 AC로 추정) |
| 입력 신호 | 시간영역 + 주파수영역 특징 (전류로 추정) |
| AI 모델 | 1D-CNN + LSTM + attention, feature fusion |
| 학습 방식 | transfer learning 기반 단계적(stagewise) 학습 |
| 데이터 규모 | 확인되지 않음 |
| 운전조건(부하) | 부하 5종 (명칭은 확인되지 않음). **UL1699 준거 아크 발생기**로 데이터 수집 |
| 성능 지표 | 정확도 99.99%. TL과 attention이 없는 fusion 모델보다 약 1.7%p 향상 |
| 일반화 시험 | 확인되지 않음 (5종 부하 내 분류) |
| 실험 vs 시뮬 | 실험 |
| severity | 확인되지 않음 |
| Edge 적용 | 확인되지 않음 |
| 연구실과의 관련성 | 국내 외부 그룹의 표준 준거 데이터 + TL 사례(연구실 소속 여부는 확인하지 못함). 표준 준거 시험 데이터 구축 방식의 비교 대상 |
| 한계 | 미관측 부하 시험이 없어 보임(확인 필요). 모델이 무거워 MCU 탑재와는 거리가 있음 [해석] |

### K8. C-04 — Artificial Intelligence for DC Arc Fault Detection in Photovoltaic Systems (리뷰, V1)
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재지 | Kamal Chandra Paul 외 (Chen Chen, Yao Wang, Tiefu Zhao 포함) / 2025 / IEEE Access |
| DOI | 10.1109/ACCESS.2025.3572521 |
| 진단 대상 | PV DC series arc (리뷰) |
| 다루는 범위 | 데이터 전처리, 특징추출, 모델 최적화, **하드웨어 구현** |
| 실험/일반화/Edge | 리뷰라 해당 없음. 세부 결론은 본문을 확인하지 못함 |
| 연구실과의 관련성 | DC arc AI 연구 지형도. 연구실 DC arc 논문의 위치를 정할 때 참고 |
| 한계 | AC arc는 범위 밖. AC/DC 통합 관점은 C-10(arXiv 리뷰)으로 보완 필요 |

---

## 3) 동향 요약 (근거 ID 인용)

### 3-1. 신호처리·임계값 방식 vs AI 방식
- **사실**: C-06은 rule-based와 AI 기반 DC series arc 검출을 직접 비교했다. AI 쪽이 **변화하는 조건에 더 적응적**이고, **도메인 지식 기반 사전 특징추출과 결합**하면 전반 성능이 좋아진다고 결론지었다. 대상은 저샘플링·저연산 장치다.
- **사실**: C-07은 기존 AFCI의 강인성을 떨어뜨리는 요인으로 인버터 스위칭 스펙트럼 간섭, 컨버터 하드웨어 이질성, 장기 운전조건 drift, 환경 노이즈를 들었다. 고정 스펙트럼 대역과 임계값에 기대는 방식은 이런 요인에 취약하다는 것이 문제 정의다.
- **사실**: 성공한 일반화 사례는 "순수 end-to-end"가 아니다. C-12는 손으로 설계한 RCF(IFA, CMA, MFA) + ML이고, C-11은 물리 모델(RLC arc model)로 데이터를 합성한 뒤 1D-CNN을 쓴다. 반면 end-to-end raw current CNN인 C-01과 TL feature fusion인 C-14는 고정 부하 집합(8종, 5종)에서 99.47%, 99.99%를 보고했지만, 미관측 부하 평가는 초록에서 확인되지 않는다.
- **해석**: 문헌상 주류는 "도메인 지식 특징/물리 모델 + 데이터 기반 분류기"의 하이브리드로 수렴하는 중이다(C-06, C-11, C-12).

### 3-2. 부하 일반화 문제
- **사실**: 미관측 부하 평가를 명시한 V1 연구는 C-11(미관측 부하 9종, 평균 99.33%)과 C-12(단일 부하 학습, 미관측 다중부하 시험) 두 편이다. 둘 다 같은 그룹(Strathclyde, Jiang/Booth)이다.
- **사실**: domain adaptation 계열은 C-03(DA-DCGAN, PV DC), C-07(LD-Align, 이종 인버터 정렬), C-13(LMMD + DSAN, 미관측 series/parallel 조건에서 평균 21% 향상; 게재지 미확인 X), C-18(LTCNN-ADA, 소량의 target-domain 고장 데이터; X)이 있다.
- **사실**: C-16(X)은 "unseen measurement sessions **within evaluated load categories**"에서의 강건성을 보고했다. 즉 일부 "일반화" 주장은 **같은 부하 종류의 다른 세션**에 대한 것이지 **미관측 부하 종류**에 대한 것이 아니다.
- **해석**: 평가 프로토콜(leave-one-load-out, 미관측 부하 비율, 인버터 부하 포함 여부)이 표준화되어 있지 않아 논문 사이의 수치를 직접 비교할 수 없다. 99% 이상 보고 연구(C-01, C-14) 대부분은 split 방식을 초록에서 확인할 수 없다.

### 3-3. 실시간성 / 오검출(nuisance tripping)
- **사실**: 실행시간과 탑재 근거 — C-01 31 ms/1 cycle(10 kHz), C-05 SBC 실시간 동작(95.8%), C-08 trigger-to-trip 200 ms 미만(2018, IoT), C-09 Udoo X86 Ultra 보드 실시간 검증 + adaptive normalization으로 mistrigger 감소(X).
- **사실**: nuisance trip을 정량 지표로 보고한 것은 C-07(nuisance-trip-prone 조건에서 false-trip 0%)이 확인된 유일한 사례다(프리프린트). 경량화 계열로는 C-02(EffNet 블록, 99.36%; X)와 C-15(arXiv)가 있다.
- **해석**: "임베디드"로 보고된 플랫폼이 대부분 SBC/x86급(C-05, C-09)이다. Cortex-M급 MCU에 양자화 모델을 올리고 메모리·지연을 보고한 외부 연구는 이번 검색 범위에서 확인하지 못했다. FPGA 구현 사례도 확인하지 못했다.

---

## 4) 연구 공백 (Research Gap) — 연구실 방향과 연결

1. **AC/DC 통합 아크 진단의 부재**
   근거: 확인된 외부 연구는 AC(C-01, C-11, C-12, C-14, C-15; IEC 62606/UL1699)와 DC(C-03, C-04, C-05, C-06, C-07; PV/UL 1699B 맥락)로 완전히 나뉜다. 리뷰도 DC 전용(C-04)과 배전계통 전반(C-10)으로 갈린다. 하나의 특징 공간이나 모델로 AC와 DC 아크를 함께 다루는 연구는 이번 검색 범위에서 확인하지 못했다.
   제안: AC zero-crossing 의존 특징과 DC 광대역 노이즈 특징을 공통 표현(정규화 스펙트럼, 다중대역 에너지)으로 정렬한 단일 모델. C-07의 representation alignment를 AC↔DC 도메인 정렬로 확장하는 방안.

2. **미관측 부하, 특히 전력전자 부하에 대한 표준화된 일반화 평가 부재**
   근거: 미관측 부하를 명시적으로 평가한 V1은 C-11과 C-12뿐이고, 둘 다 AC series에 한정된다. 인버터 스위칭 간섭은 PV 측(C-07)에서만 문제로 정의되었다. 고정 부하 집합에서의 고정확도(C-01, C-14)는 split 방식을 확인할 수 없다.
   제안: IEC 62606/UL 1699B 부하군 기반 leave-one-load-out 프로토콜 + 인버터/SMPS/모터 드라이브 부하를 미관측 시험군으로 포함. 연구실의 switching-frequency 제거 기법(L-03)과 DA(C-03, C-13)를 결합해 비교.

3. **MCU급 실시간 구현과 일반화를 동시에 만족한 연구 부재**
   근거: 실시간 근거는 SBC/x86(C-05, C-09)이나 실행시간 추정(C-01) 수준이다. 일반화를 보인 C-11과 C-12는 Edge 구현이 확인되지 않는다. C-06은 저샘플링 장치를 겨냥하지만 MCU 구현 수치는 확인되지 않는다.
   제안: 저샘플링(수 kHz~10 kHz) 입력, 양자화된 경량 CNN, MCU 메모리·지연·전력 보고, 미관측 부하 시험을 한 번에 묶은 평가.

4. **아크 검출과 컨버터 열화의 상호작용 및 통합 진단 부재**
   근거: C-07은 "장기 운전조건 drift"와 "인버터 스위칭 간섭"을 오검출 원인으로 들었다. 그러나 컨버터 부품 열화(DC-link 커패시터 C 감소, ESR 증가 등)가 아크 검출 특징에 미치는 영향이나 두 진단을 함께 하는 연구는 이번 검색에서 확인하지 못했다.
   [추론] 커패시터 열화는 DC-link 리플을 키우고 스위칭 고조파 분포를 바꾼다. 이 변화가 DC arc의 광대역 특징 대역과 겹치면 오검출이나 미검출의 원인이 될 수 있다. 같은 전류 센서로 "아크(과도·광대역)"와 "열화(정상상태 고조파 크기·위상 변화)"를 다중 출력으로 진단하는 모델은 공백이다. 본 작업공간의 NPC 인버터 DC-link 커패시터 노화 연구와 직접 연결된다.

5. **severity(아크 에너지, 진행 단계) 추정 부재**
   근거: 모든 핵심 논문에서 severity 등급 분류는 확인되지 않는다. "저에너지 아크"를 대상으로 한 C-05만 에너지 수준 관점에 가깝다.
   제안: 아크 에너지 또는 지속시간 기반 다등급 출력. 차단 판단과 예지보전 판단을 분리할 수 있다.

---

## 5) 확인하지 못한 항목 (후속 검색 시 우선순위)
- C-01 ArcNet DOI, C-03 DA-DCGAN DOI·권호, C-08 Siegel DOI
- C-02 Efficient-ArcNet 서지(저자, 게재지, 연도), C-13 Chen 2024 게재지, C-18 LTCNN-ADA 저자·게재지(International Journal of Electrical Power & Energy Systems로 기억하지만 검색으로 확인하지 못함)
- C-14 제1저자 전체 이름과 연구실 관련 여부
- UL 1699B 시험 데이터를 명시적으로 쓴 DL 연구, FPGA 구현 사례, Cortex-M MCU 구현 사례
