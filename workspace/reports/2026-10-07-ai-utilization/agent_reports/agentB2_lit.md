# Agent B2 — Literature Researcher 산출물
## 인버터/컨버터 고장진단 DL · 운전조건 일반화(DA/DG) · 자기지도 · 이상탐지 · XAI · 멀티모달

- 작성일: 2026-10-07
- 탐색 수단: WebSearch만 사용함 (Crossref/doi.org/IEEE Xplore/OpenAlex 등 직접 조회는 사용하지 않음). 근거는 검색결과의 제목, URL, 스니펫과 검색 도구가 붙인 요약문이다.
- **중요한 한계**: 탐색 도중 세션 전체 WebSearch 한도(200회/turn, 모든 에이전트 공용)가 소진되어 추가 검색을 할 수 없었다. 그래서 일부 논문은 DOI, 권호, 저자 보완을 끝내지 못했고 O(멀티모달) 분야의 전력전자 직접 사례도 더 찾지 못했다. 후속 메시지로 검색을 이어가면 X 등급 항목을 V1/V2로 올릴 수 있다.
- 등급 정의: **V1** = 제목, 제1저자 이상, 저널/학회, 연도가 일치하고 DOI 문자열까지 검색결과(URL/스니펫)에서 직접 확인함 / **V2** = 서지는 일치하나 DOI 미확인 / **X** = 제1저자 또는 게재처를 확인하지 못함(핵심 논문 선정 대상에서 제외)
- 표기: 아래 "스니펫"은 검색결과 초록 또는 요약 수준의 정보다. 본문(PDF)은 하나도 읽지 않았다.

---

## 1) 후보 논문 목록

| ID | 제목 | 저자 | 연도 | 저널/학회 | 권호 | DOI | 등급 | 근거 URL | 분야 |
|---|---|---|---|---|---|---|---|---|---|
| B2-01 | Domain-Adversarial Training of Neural Networks | Yaroslav Ganin, Evgeniya Ustinova, Hana Ajakan, Pascal Germain, Hugo Larochelle, François Laviolette, Mario Marchand, Victor Lempitsky | 2016 | Journal of Machine Learning Research (JMLR) | Vol.17, No.59, pp.1–35 | 미확인 (arXiv:1505.07818 은 URL로 확인) | V2 | https://www.jmlr.org/papers/v17/15-239.html ; https://arxiv.org/abs/1505.07818 | J (방법론 원전) |
| B2-02 | Data Mining Applications to Fault Diagnosis in Power Electronic Systems: A Systematic Review | Arash Moradzadeh, Behnam Mohammadi-Ivatloo, Kazem Pourhossein, Amjad Anvari-Moghaddam | 2022 | IEEE Transactions on Power Electronics | Vol.37, No.5, pp.6026–6050 | 10.1109/TPEL.2021.3131293 | V1 | https://vbn.aau.dk/da/publications/data-mining-applications-to-fault-diagnosis-in-power-electronic-s ; https://vbn.aau.dk/files/454611386/FINAL_VERSION.pdf | D (리뷰) |
| B2-03 | Review for AI-based Open-Circuit Faults Diagnosis Methods in Power Electronics Converters | Chuang Liu, Lei Kou, Guowei Cai, Zihan Zhao, Zhe Zhang | 2020 (arXiv 2022) | Power System Technology (电网技术) | Vol.44, No.8, pp.2957–2970 | 미확인 | V2 | https://arxiv.org/abs/2209.14058v1 | D (리뷰) |
| B2-04 | A Transferable Deep Learning Network for IGBT Open-circuit Fault Diagnosis in Three-phase Inverters | Yongjie Liu, Ariya Sangwongwanich, Yibin Zhang, Shuyu Ou, Huai Wang | 2024 | IEEE APEC 2024 | 미확인 | 미확인 | V2 | https://research.polyu.edu.hk/en/publications/a-transferable-deep-learning-network-for-igbt-open-circuit-fault-/ ; https://elsevier.forskningsportal.dk/display/pub-2-s2.0-85192754521 | D, J |
| B2-05 | A Deep Learning Network based Robust Fault Diagnosis Method for IGBT Open Circuit | Yongjie Liu, Ariya Sangwongwanich, Yi Zhang, Rui Kong, Yingzhou Peng, Khalifa Al Hosani, Huai Wang | 2024 | IEEE IPEMC 2024-ECCE Asia | 미확인 | 미확인 | V2 | https://khazna.ku.ac.ae/en/publications/a-deep-learning-network-based-robust-fault-diagnosis-method-for-i/ | D, J |
| B2-06 | A New Weighted Mechanism-Based Partial Transfer Fault Diagnosis Method for Voltage Source Inverter | Jun Zhu, Yuanfan Wang, Hao Yan, Siliang Lu, Weilin Li | 2025 | IEEE Transactions on Transportation Electrification | Vol.11, No.3, pp.7588–7598 | 미확인 | V2 | https://pure.nwpu.edu.cn/en/publications/a-new-weighted-mechanism-based-partial-transfer-fault-diagnosis-m/ | J, D |
| B2-07 | Lifelong Learning-Enabled Fractional Order-Convolutional Encoder Model for Open-Circuit Fault Diagnosis of Power Converters Under Multi-Conditions | Tao Li, Enyu Wang, Jun Yang | 2025 | Sensors (MDPI) | Vol.25, No.6, 1884 | 10.3390/s25061884 | V1 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11945422/ ; https://www.mdpi.com/resolver?pii=s25061884 | J, D |
| B2-08 | Explainable Deep Learning Fault Detection Method for Multilevel Inverters | Hasan Ali Gamal Al-Kaf, Samer Saleh Hakami, Kyo-Beum Lee | 2026 | IEEE Transactions on Industrial Informatics | Vol.22, No.1, pp.579–590 | 미확인 | V2 | https://pure.kfupm.edu.sa/en/publications/explainable-deep-learning-fault-detection-method-for-multilevel-i/ ; https://pel.ajou.ac.kr/paper/2402 | N, D |
| B2-09 | Explainable Machine Learning Method for Open Fault Detection of NPC Inverter Using SHAP and LIME | Hasan Ali Gamal Al-kaf, Kyo-Beum Lee | 2023 | 2023 IEEE Conference on Energy Conversion (CENCON) | pp.14–19 | 미확인 | V2 | https://pure.kfupm.edu.sa/en/publications/explainable-machine-learning-method-for-open-fault-detection-of-n/ ; https://aurora.ajou.ac.kr/handle/2018.oak/36933 | N |
| B2-10 | Explainable Artificial Intelligence (XAI) techniques for energy and power systems: Review, challenges and opportunities | R. Machlev, L. Heistrene, M. Perl, K. Y. Levy, J. Belikov, S. Mannor, Y. Levron | 2022 | Energy and AI (Elsevier) | Vol.9, 100169 | 10.1016/j.egyai.2022.100169 | V1 | https://cris.iucc.ac.il/en/publications/explainable-artificial-intelligence-xai-techniques-for-energy-and/ ; https://doaj.org/article/6984422d40a64f4497b21db3cfbb1370 | N (리뷰) |
| B2-11 | Self-supervised feature learning for motor fault diagnosis under various torque conditions | Sang Kyung Lee, Hyeongmin Kim, Minseok Chae, Hye Jun Oh, Heonjun Yoon, Byeng D. Youn | 2024 | Knowledge-Based Systems (Elsevier) | 미확인 (2024년 3월로 표기됨) | 미확인 | V2 | https://scholarworks.bwise.kr/ssu/handle/2018.sw.ssu/49461 | K, J |
| B2-12 | A synchronization-induced cross-modal contrastive learning strategy for fault diagnosis of electromechanical systems under semi-supervised learning with current signal | Qinyuan Luo, Jinglong Chen, Yanyang Zi, Jingsong Xie | 2024 | Expert Systems with Applications (Elsevier) | Vol.249, 123801 | 미확인 | V2 | https://scholar.xjtu.edu.cn/en/publications/a-synchronization-induced-cross-modal-contrastive-learning-strate/ | K, O |
| B2-13 | Parameter Estimation of Power Electronic Converters with Physics-Informed Machine Learning | Shuai Zhao, Huai Wang | 2022 | IEEE Transactions on Power Electronics | 미확인 | 미확인 | V2 | https://vbn.aau.dk/files/519289832/Parameter_Estimation_of_Power_Electronic_Converters_With_Physics_Informed_Machine_Learning.pdf | J (보조: 물리정보 기반 강건성) |
| B2-14 | Hierarchical temporal memory-based predictive maintenance of DC-link capacitors in power electronic converters | **저자 미확인** | 2026 | Measurement: Energy (Elsevier) | Vol.10 (2026년 6월로 표기됨) | 미확인 | **X** (저자 미확인) | https://www.sciencedirect.com/science/article/pii/S2950345026000138 ; https://www.synapsesocial.com/papers/69d892886c1944d70ce03ef1 | L |
| B2-15 | Fault detection method for power conversion circuits using thermal image and convolutional autoencoder | 저자 미확인 | 2025 (arXiv) | arXiv 프리프린트 (게재처 미확인) | – | 미확인 | X | https://www.arxiv.org/abs/2505.08150 | L, O |
| B2-16 | Hypergraph Contrastive Sensor Fusion for Multimodal Fault Diagnosis in Induction Motors | Usman Ali, Ali Zia, Waqas Ali, Umer Ramzan, Abdul Rehman, Muhammad Tayyab Chaudhry, Wei Xiang | 2025 (arXiv) | arXiv 프리프린트 (저널/학회 미확인) | – | 미확인 | X (게재처 미확인) | https://arxiv.org/abs/2510.15547v1 | O, K |
| B2-17 | Domain-collaborative multimodal transformer (DCMT) for fault diagnosis of rotating machines (정확한 제목은 검색결과에서 잘림) | 저자 미확인 (Kumoh National Institute of Technology) | 미확인 | 미확인 | – | 미확인 | X | https://pure.seoultech.ac.kr/en/publications/domain-collaborative-multimodal-transformer-for-fault-diagnosis-o/ | O |
| B2-18 | Applications of Unsupervised Deep Transfer Learning to Intelligent Fault Diagnosis: A Survey and Comparative Study | 저자 미확인 | 미확인 | arXiv:1912.12528 (게재처 미확인) | – | 미확인 | X | https://arxiv.org/pdf/1912.12528 | J (리뷰) |
| B2-19 | A multi-source domain generalization network (MDGN) for rotating machinery fault diagnosis under unseen operating conditions (제목 일부만 확인) | 저자 미확인 | 미확인 | 미확인 | – | 미확인 | X | https://scholar.hit.edu.cn/en/publications/a-multi-source-domain-generalization-network-for-rotating-machine/ | J |
| B2-20 | Transfer learning 기반 DC-link capacitance 추정 (시뮬레이션 학습 후 실험 데이터로 분류기만 재학습) | 저자 미확인 | 미확인 | 포스터 (게재처 미확인) | – | 미확인 | X | https://expo.pwr.edu.pl/Event_files/posters/Poster_Japonia_SO_v3.pdf | J |
| B2-21 | Fault diagnosis of three-phase inverter based on GAF-CNN | 저자 미확인 | 2025 | Journal of Measurement Science and Instrumentation (추정, URL 기준) | 미확인 | 10.62756/jmsi.1674-8042.2025044 (URL에 포함) | X (저자 미확인) | https://journal.hep.com.cn/jmsi/EN/10.62756/jmsi.1674-8042.2025044 | D |

후보는 21편이다(V1 3편, V2 10편, X 8편). 핵심 논문은 V1/V2에서만 골랐다.

---

## 2) 핵심 논문 상세 (8편)

선정 기준: (a) 운전조건 또는 도메인이 바뀌어도 진단이 유지되는가(J), (b) 3-Level NPC 또는 3상 인버터를 직접 다루는가, (c) 라벨 부족 상황(자기지도/부분 전이)을 다루는가, (d) 설명가능성.
J(운전조건/도메인 일반화) 분야는 B2-04, B2-06, B2-07, B2-01에 B2-11(K+J)을 더해 5편이다.

### [핵심 1] B2-04 — 시뮬레이션→HIL 전이학습 기반 IGBT 개방고장 진단
| 항목 | 내용 |
|---|---|
| 논문 제목 | A Transferable Deep Learning Network for IGBT Open-circuit Fault Diagnosis in Three-phase Inverters |
| 저자 | Yongjie Liu, Ariya Sangwongwanich, Yibin Zhang, Shuyu Ou, Huai Wang (Aalborg University) |
| 연도 / 학회 | 2024 / IEEE APEC 2024 |
| DOI | 미확인 (V2) |
| 진단 대상 | 3상 인버터 IGBT open-circuit fault |
| 입력 신호 | "original current signals" (스니펫). 상전류로 보이나 정확한 측정 지점은 논문에서 확인하지 못함 |
| AI 모델 | lightweight CNN. 특징 추출과 함께 "operation condition identification"도 수행한다고 기술됨 |
| 학습 방식 | source domain(시뮬레이션 모델) 데이터로 사전학습한 뒤, target domain(real-time HIL)의 소량 샘플로 fine-tuning (지도 전이학습) |
| 데이터 규모 | 논문에서 확인되지 않음 (초록 수준) |
| 운전조건 | 논문에서 확인되지 않음 (초록 수준) |
| 성능 지표 | 진단 정확도: 시뮬레이션 99.52%, HIL 98.30% |
| 일반화 시험 여부 | 시스템 간 도메인 이동(sim→HIL)을 시험함. 학습에 없던 운전조건(부하, 주파수)으로 시험했는지는 확인하지 못함. split 방식도 확인하지 못함 |
| 실험 vs 시뮬레이션 | 시뮬레이션과 HIL. 실제 전력 하드웨어 실험 여부는 확인하지 못함 |
| fault severity | 해당 없음 (개방고장 유무/위치 분류로 보임, 초록 수준) |
| Edge 적용 | "lightweight" CNN이라고만 언급됨. MCU 구현 여부는 확인하지 못함 |
| 연구실과의 관련성 | 높음. 커패시터 노화 데이터는 실측으로 많이 얻기 어려우므로, C/ESR을 바꾼 시뮬레이션으로 사전학습하고 실험 소량으로 fine-tuning하는 구조를 그대로 옮겨 쓸 수 있다. 저자들은 문제 정의에서 기존 방법의 한계로 "한 시스템에서 학습한 모델을 다른 시스템에 적용할 수 없음"과 "fault 데이터 확보가 어려움"을 들었는데, 이는 연구실의 일반화 이슈와 같다 |
| 한계 | 학회 논문이다. target 라벨이 필요하다(소량이라도). 운전조건별 일반화 정량 결과는 초록에서 확인되지 않음 |

### [핵심 2] B2-06 — 가중 부분 전이(partial transfer) 기반 VSI 고장진단
| 항목 | 내용 |
|---|---|
| 논문 제목 | A New Weighted Mechanism-Based Partial Transfer Fault Diagnosis Method for Voltage Source Inverter |
| 저자 | Jun Zhu, Yuanfan Wang, Hao Yan, Siliang Lu, Weilin Li |
| 연도 / 저널 | 2025 / IEEE Transactions on Transportation Electrification, 11(3), 7588–7598 |
| DOI | 미확인 (V2) |
| 진단 대상 | 3상 PMSM 구동용 VSI의 open-circuit fault |
| 입력 신호 | 논문에서 확인되지 않음 (초록 수준) |
| AI 모델 | transferable recognition network (구조 세부는 확인하지 못함) |
| 학습 방식 | 비지도 도메인 적응의 변형인 partial transfer. 가중치를 준 source 데이터와 target 데이터 사이의 Wasserstein distance를 최소화한다. source의 outlier에는 작은 가중치를 준다. source에는 weighted cross-entropy를, target에는 conditional entropy loss를 쓴다. 가중치와 네트워크 파라미터를 번갈아 최적화한다 |
| 데이터 규모 | 논문에서 확인되지 않음 (초록 수준) |
| 운전조건 | 논문에서 확인되지 않음 (초록 수준) |
| 성능 지표 | 논문에서 확인되지 않음 (초록 수준) |
| 일반화 시험 여부 | source에서 target으로의 전이 시나리오를 시험함. target 클래스가 source 클래스의 부분집합인 경우(partial)다. 구체적 조건은 확인하지 못함 |
| 실험 vs 시뮬레이션 | 논문에서 확인되지 않음 |
| fault severity | 해당 없음 (개방고장 분류) |
| Edge 적용 | 확인되지 않음 |
| 연구실과의 관련성 | 높음. 현장(target)에서 새 운전조건의 데이터는 대부분 "정상"뿐이고 노화 라벨은 없다. 이는 target 클래스가 source의 부분집합인 partial transfer 상황과 구조가 같다(해석). target 라벨 없이 적응하는 방식이라 연구실 시나리오에 가깝다 |
| 한계 | 입력 신호, 데이터 규모, 성능을 초록 수준에서 확인하지 못함. target 비라벨 데이터가 학습 시점에 있어야 한다(UDA의 일반적 전제) |

### [핵심 3] B2-07 — 다중 운전조건 lifelong learning 기반 컨버터 개방고장 진단
| 항목 | 내용 |
|---|---|
| 논문 제목 | Lifelong Learning-Enabled Fractional Order-Convolutional Encoder Model for Open-Circuit Fault Diagnosis of Power Converters Under Multi-Conditions |
| 저자 | Tao Li, Enyu Wang, Jun Yang |
| 연도 / 저널 | 2025 / Sensors, 25(6), 1884 |
| DOI | 10.3390/s25061884 (V1) |
| 진단 대상 | 모터 구동 시스템 전력변환기의 open-circuit fault |
| 입력 신호 | "fault signal". 구체적 신호 종류는 초록 수준에서 확인하지 못함 |
| AI 모델 | convolutional module과 encoder module의 조합(Fractional Order-Convolutional Encoder) |
| 학습 방식 | 과거 gradient 정보를 쓰는 fractional order learning으로 최적화하고, 다단계(multilevel) lifelong learning framework로 새 운전조건의 fault 특징을 연속 학습하면서 catastrophic forgetting을 억제한다 |
| 데이터 규모 | 논문에서 확인되지 않음 (초록 수준) |
| 운전조건 | "multi-conditions". 구체적 조건(부하, 속도 등)은 확인하지 못함 |
| 성능 지표 | 논문에서 확인되지 않음 (초록 수준) |
| 일반화 시험 여부 | 문제 정의 자체가 "운전조건이 바뀌면 기존 모델이 새 fault 특징을 인식하지 못해 정확도가 떨어진다"는 것이다. 조건을 순차적으로 추가하며 평가한 것으로 보이나 split 방식은 확인하지 못함 |
| 실험 vs 시뮬레이션 | 논문에서 확인되지 않음 |
| fault severity | 해당 없음 |
| Edge 적용 | 확인되지 않음 |
| 연구실과의 관련성 | 중~높음. 운전조건(f0, fsw, 부하)을 하나씩 추가해 가며 모델을 갱신하는 운영 시나리오에 대응한다. 다만 처음 보는 조건에서 zero-shot으로 일반화하는 것과는 다른 접근이다 |
| 한계 | 새 조건의 라벨 데이터가 필요할 가능성이 높다(확인하지 못함). 오픈액세스(MDPI/PMC)이므로 본문 검토로 세부 확인이 가능하다 |

### [핵심 4] B2-11 — 토크 조건 불변 특징을 위한 자기지도 학습 (NFA-MSSL)
| 항목 | 내용 |
|---|---|
| 논문 제목 | Self-supervised feature learning for motor fault diagnosis under various torque conditions |
| 저자 | Sang Kyung Lee, Hyeongmin Kim, Minseok Chae, Hye Jun Oh, Heonjun Yoon, Byeng D. Youn |
| 연도 / 저널 | 2024 / Knowledge-Based Systems |
| DOI | 미확인 (V2) |
| 진단 대상 | 전동기 고장 (유도전동기, PMSM 데이터셋) |
| 입력 신호 | stator current. 전처리로 instantaneous amplitude를 추출함 |
| AI 모델 | multi-channel self-supervised learning (백본 구조는 확인하지 못함) |
| 학습 방식 | 자기지도 학습(NFA-MSSL). notch filter augmentation으로 torque-invariant하면서 fault와 관련된 특징을 추출하도록 설계함 |
| 데이터 규모 | 논문에서 확인되지 않음 (초록 수준) |
| 운전조건 | "various torque conditions" (토크/부하 변화) |
| 성능 지표 | 논문에서 확인되지 않음 (초록 수준) |
| 일반화 시험 여부 | 토크 조건 간 분포 차이를 핵심 문제로 다룸. split 방식은 확인하지 못함 |
| 실험 vs 시뮬레이션 | open-source 유도전동기 데이터셋과 PMSM 데이터셋으로 검증함(실측 데이터셋으로 보이나 세부는 확인하지 못함) |
| fault severity | 확인되지 않음 |
| Edge 적용 | 확인되지 않음 |
| 연구실과의 관련성 | 높음. (1) 라벨 부족과 (2) 운전조건별 분포 차이라는 두 문제를 동시에 다룬다. 운전조건 성분(f0, fsw 고조파)을 notch로 지워 조건 불변 특징을 학습한다는 발상은 리플 파형에도 그대로 적용해 볼 만하다(해석) |
| 한계 | 전력전자 부품 노화가 아니라 전동기 고장이 대상이다. 성능 수치를 확인하지 못함 |

### [핵심 5] B2-08 — 3-Level NPC 인버터 CNN 고장검출의 Grad-CAM 설명
| 항목 | 내용 |
|---|---|
| 논문 제목 | Explainable Deep Learning Fault Detection Method for Multilevel Inverters |
| 저자 | Hasan Ali Gamal Al-Kaf, Samer Saleh Hakami, Kyo-Beum Lee |
| 연도 / 저널 | 2026 / IEEE Transactions on Industrial Informatics, 22(1), 579–590 |
| DOI | 미확인 (V2) |
| 진단 대상 | 멀티레벨 인버터(3-Level NPC)의 fault detection과 fault type 분류. 구체적 고장 종류는 초록에서 확인하지 못함. 같은 저자의 선행 연구 B2-09는 open fault를 다룸 |
| 입력 신호 | 논문에서 확인되지 않음 (초록 수준) |
| AI 모델 | CNN과 Grad-CAM (gradient weighted class activation map) |
| 학습 방식 | 지도학습 분류에 사후(post-hoc) 시각적 설명을 붙임 |
| 데이터 규모 | 논문에서 확인되지 않음 (초록 수준) |
| 운전조건 | 논문에서 확인되지 않음 (초록 수준) |
| 성능 지표 | "high classification accuracy" (수치는 확인하지 못함) |
| 일반화 시험 여부 | 확인되지 않음 |
| 실험 vs 시뮬레이션 | 둘 다 수행 (3L-NPC) |
| fault severity | 확인되지 않음 |
| Edge 적용 | 확인되지 않음 |
| 연구실과의 관련성 | 높음. 대상 토폴로지(3L-NPC)와 모델(CNN)이 같다. 리플 window 안에서 CNN이 어느 구간과 주파수에 반응하는지 보면, 노화와 관련된 성분 대신 운전조건 특이 성분(예: f0 위상, fsw 리플 포락선)을 근거로 쓰는 shortcut learning이 있는지 점검할 수 있다(해석) |
| 한계 | Grad-CAM은 정성적 사후 설명이다. 설명의 신뢰도(faithfulness)를 정량 평가했는지는 확인하지 못함 |

### [핵심 6] B2-01 — DANN (도메인 적대 학습 원전)
| 항목 | 내용 |
|---|---|
| 논문 제목 | Domain-Adversarial Training of Neural Networks |
| 저자 | Y. Ganin, E. Ustinova, H. Ajakan, P. Germain, H. Larochelle, F. Laviolette, M. Marchand, V. Lempitsky |
| 연도 / 저널 | 2016 / JMLR, 17(59), 1–35 |
| DOI | 미확인 (V2). arXiv:1505.07818 확인 |
| 진단 대상 | 해당 없음 (일반 도메인 적응 방법론) |
| 입력 신호 | 해당 없음 |
| AI 모델 | feed-forward 네트워크에 feature extractor, label predictor, domain classifier를 두고 **gradient reversal layer**를 추가함 |
| 학습 방식 | 라벨 있는 source와 라벨 없는 target으로 학습한다. source와 target을 구별할 수 없는(domain-invariant) 특징으로 예측하도록 학습하며, 일반 backpropagation/SGD로 구현한다 |
| 데이터 규모 / 운전조건 / 성능 | 해당 없음 (방법론 논문, 세부 벤치마크는 확인하지 못함) |
| 일반화 시험 여부 | 도메인 적응 실험(세부 확인하지 못함) |
| 실험 vs 시뮬레이션 | 해당 없음 |
| fault severity / Edge | 해당 없음 / 추론 시에는 domain classifier를 떼어내므로 추론 비용이 늘지 않는다(구조상 추론) |
| 연구실과의 관련성 | 높음 (방법론 기준선). 운전조건(f0, fsw, Vout, 부하)을 domain label로 두면 DANN 계열(single-source DA, multi-source DG 변형)의 직접적인 출발점이 된다. 전력전자 DA 논문(B2-06 등) 대부분이 이 계열의 분포 정렬 사상을 공유한다 |
| 한계 | target 비라벨 데이터가 학습 시점에 필요하다. 클래스 조건부 분포까지 정렬해 주지는 않는다(후속 연구의 동기, 일반론) |

### [핵심 7] B2-02 — 전력전자 고장진단 데이터마이닝/ML/DL 체계적 리뷰
| 항목 | 내용 |
|---|---|
| 논문 제목 | Data Mining Applications to Fault Diagnosis in Power Electronic Systems: A Systematic Review |
| 저자 | Arash Moradzadeh, Behnam Mohammadi-Ivatloo, Kazem Pourhossein, Amjad Anvari-Moghaddam |
| 연도 / 저널 | 2022 / IEEE TPEL, 37(5), 6026–6050 |
| DOI | 10.1109/TPEL.2021.3131293 (V1) |
| 진단 대상 | 전력전자 시스템(PES) 고장 전반 |
| 입력 신호 / 모델 | ANN, ML, DL 기반 data-mining 기법을 리뷰함 |
| 학습 방식 | 리뷰 |
| 데이터 규모 / 운전조건 / 성능 | 해당 없음 (리뷰) |
| 주요 결론(스니펫) | 측정 신호에서 특징을 스스로 추출하는 DL 기반 기법이 다른 방법보다 "significantly more effective"하며, 향후 전력전자 산업의 이상적인 도구로 제시됨 |
| 일반화 시험 여부 | 리뷰 대상 논문들의 split/일반화 관행은 확인하지 못함 |
| 실험 vs 시뮬레이션 / severity / Edge | 확인되지 않음 |
| 연구실과의 관련성 | 중. 서론과 관련연구에서 DL 우위를 인용하는 근거로 쓸 수 있다. 연구실이 다루는 "운전조건 일반화"와 "노화(점진 열화)"가 리뷰의 주된 범주였는지는 확인하지 못함 |
| 한계 | 2021년까지의 문헌이다. DA/DG, 자기지도, XAI 같은 최근 흐름은 포함되지 않았을 가능성이 있다(확인하지 못함) |

### [핵심 8] B2-12 — 동기화 기반 교차모달(진동-전류) contrastive learning
| 항목 | 내용 |
|---|---|
| 논문 제목 | A synchronization-induced cross-modal contrastive learning strategy for fault diagnosis of electromechanical systems under semi-supervised learning with current signal |
| 저자 | Qinyuan Luo, Jinglong Chen, Yanyang Zi, Jingsong Xie |
| 연도 / 저널 | 2024 / Expert Systems with Applications, 249, 123801 |
| DOI | 미확인 (V2) |
| 진단 대상 | 전기기계 시스템 고장 |
| 입력 신호 | 진동 + 전류. 전류는 Clarke transformation으로 전처리함 |
| AI 모델 | CVC (contrastive vibration-current) framework. 진동 모델에는 noise-resistant augment Mean Teacher를 씀 |
| 학습 방식 | 반지도(semi-supervised)에 동기화 기반 교차모달 contrastive learning(SICMCL)을 더함. 동시에 측정한 진동/전류 특징을 정렬해, 운용 시에는 전류만으로 진단하는 모델을 강화한다 |
| 데이터 규모 / 운전조건 / 성능 | 논문에서 확인되지 않음 (초록 수준) |
| 주요 결론(스니펫) | 전류 모델에는 SICMCL이 true label보다 더 도움이 되었다고 보고됨 |
| 일반화 시험 여부 | 확인되지 않음 |
| 실험 vs 시뮬레이션 | 확인되지 않음 |
| fault severity / Edge | 확인되지 않음 |
| 연구실과의 관련성 | 중~높음. 실험실에서는 정밀 센서(예: 커패시터 전류 프로브, 온도, LCR로 측정한 C/ESR)를 함께 수집하고 현장에서는 값싼 센서(DC-link 전압 리플이나 상전류)만 쓰는 "학습 시 멀티모달, 추론 시 단일모달" 설계의 근거가 된다(해석) |
| 한계 | 전력전자 소자 노화가 아니라 전기기계(회전기) 대상이다 |

---

## 3) 분야별 동향 요약

### D. 인버터/컨버터 고장진단 DL (CNN/LSTM/Transformer/AE)
- 리뷰(B2-02, B2-03)에 따르면 전력전자 고장진단은 ANN/ML에서 측정 신호를 직접 입력하는 DL로 옮겨가고 있고, DL의 우위가 반복해서 보고된다(B2-02 결론).
- 대상은 대부분 **IGBT/스위치 open-circuit fault**다(B2-03, B2-04, B2-05, B2-06, B2-07, B2-21). 고장은 이산적이고 급격한 사건이다.
- 입력은 상전류 원신호를 lightweight CNN에 넣는 방식이 많고(B2-04, B2-05), 2D 영상 변환(GAF-CNN, B2-21 X)도 있다.
- 최근에는 정확도 경쟁에서 **강건성(운전조건, 부품 파라미터 편차, 측정오차)**으로 초점이 옮겨가고 있다(B2-05 스니펫: "diverse operation conditions and circuit parameter variances").
- 3L-NPC를 직접 다룬 DL 연구는 XAI와 결합된 사례(B2-08, B2-09, 아주대 Kyo-Beum Lee 그룹)가 확인되었다.
- 커패시터 노화처럼 **점진 열화(연속 severity)**를 DL로 분류하는 연구는 이번 탐색 범위(D)에서는 거의 확인되지 않았다(B2-14 X, B2-20 X 정도만 보임).
- **연구실 적용**: OC fault 연구의 lightweight CNN과 원신호 입력 구조는 리플 window(2048점) 분류에 그대로 쓸 수 있다. 다만 노화는 경계가 흐린 연속 열화이므로, 이진분류 외에 C/ESR 회귀나 순서형(ordinal) 등급 분류로 확장하는 것이 차별점이 된다.

### J. 운전조건 변화 대응: Transfer learning / Domain adaptation / Domain generalization
- 방법론 원전은 DANN(B2-01)이다. gradient reversal로 source와 target을 구별할 수 없는 특징을 학습하는 방식이며, 이후 진단 분야 DA 연구의 기반이 된다.
- 전력전자 적용은 크게 세 갈래다. ① **sim→실측(HIL) fine-tuning**(B2-04, B2-20 X), ② **비지도/부분 도메인 적응**(Wasserstein 거리 정렬과 source 가중치, B2-06), ③ **조건 순차 추가 lifelong learning**(B2-07).
- 회전기 진단 쪽에서는 target 데이터 없이 처음 보는 조건에 대응하는 **multi-source domain generalization**(B2-19 X)이 활발하다. 전력전자에서는 아직 드물다(이번 검색 범위 기준).
- 물리 모델을 학습에 결합해 데이터 부족과 강건성 문제를 완화하는 PIML(B2-13)도 같은 Aalborg 그룹에서 나왔다.
- 대부분 초록 수준에서는 **split 방식(무작위 vs 조건별 분할)**과 **학습에 없던 조건에서의 정량 성능**이 명시되지 않았다.
- **연구실 적용**: (1) 평가를 leave-one-condition-out으로 바꿔 미지 조건 성능을 먼저 정량화한다. (2) 운전조건(f0, fsw, Vout, 부하)을 domain label로 둔 DANN/DG 계열을 기준선으로 쓴다. (3) 현장 target에는 정상 데이터만 있는 경우가 많으므로 B2-06식 partial DA, 또는 C/ESR을 바꾼 시뮬레이션으로 사전학습하고 실험 소량으로 fine-tuning하는 B2-04식 방법이 현실적이다.

### K. 자기지도 / contrastive learning
- 라벨 부족과 운전조건 분포 차이를 함께 다루는 방향으로 발전하고 있다(B2-11: 토크 조건 불변 특징).
- 증강(augmentation)을 "보존해야 할 정보(고장)는 남기고 바뀌어도 되는 정보(운전조건)는 지우는" 방향으로 설계하는 것이 핵심이다(B2-11의 notch filter augmentation).
- 교차모달 contrastive(B2-12)는 동기 측정된 두 센서의 특징을 정렬해 약한 모달(전류)의 표현을 강화한다. 반지도 학습과 결합된다.
- 전력전자(인버터/컨버터) 부품 노화에 SSL을 직접 적용한 연구는 이번 검색에서 확인되지 않았다(연구 공백 후보, 단 검색 한도 때문에 탐색이 불완전함).
- **연구실 적용**: 여러 운전조건에서 얻은 비라벨 리플 window로 SSL 사전학습을 한다. 양성쌍은 같은 커패시터 상태의 다른 window, 또는 f0/fsw 성분을 notch로 제거한 증강본으로 둔다. 이렇게 조건 불변 표현을 만든 뒤 소량 라벨로 노화를 분류한다.

### L. 비라벨 데이터 이상탐지 (AE, one-class, 정상 데이터만으로 학습)
- 정상 데이터만으로 학습한 convolutional AE로 재구성 오차를 보는 방식이 전력변환 회로에 적용된 사례가 있다(열화상, B2-15 X: 부하전류를 무작위로 바꿔 가며 정상 열화상으로 학습).
- DC-link 커패시터 노화를 **운전조건이 바뀌는 상황에서 비라벨 ripple-voltage**로 온라인 탐지하는 HTM 기반 연구가 2026년에 보고되었다(B2-14). 스니펫 기준 탐지 정확도 95% 이상, false alarm 4% 미만이며 비지도 기준선 5종과 비교했다. 다만 **저자를 확인하지 못해 X 등급**이고 서지 보완이 최우선이다.
- 전력전자 시스템용 비지도 이상탐지 Transformer(DDformer)도 검색 스니펫에서 언급되었으나 서지를 확인하지 못해 표에 넣지 않았다.
- 공통 쟁점은 **운전조건 변화로 생기는 정상 분포 이동과 노화로 생기는 이동을 구분하는 것**이다(B2-14 문제 정의).
- **연구실 적용**: 현장에서는 노화 라벨이 거의 없으므로, 설치 초기(정상) 데이터로 조건부(f0, fsw, 부하를 입력으로 주는) AE나 one-class 모델을 학습하고 이탈도를 노화 지표로 쓰는 구조가 이진분류보다 실용적이다. 조건별 임계값 보정이 필요하다.

### N. 설명가능성 (Grad-CAM, SHAP, LIME, LRP)
- 3L-NPC 인버터에 대해 ML+SHAP/LIME(시뮬레이션, B2-09, 2023)에서 CNN+Grad-CAM(시뮬레이션+실험, TII 2026, B2-08)으로 이어지는 같은 그룹의 연속 연구가 확인되었다.
- 에너지/전력시스템 XAI 리뷰(B2-10)는 이 분야가 높은 accountability를 요구하므로 black-box ML의 설명이 필요하다고 정리한다.
- 대부분 **사후(post-hoc) 정성 설명**이다. 설명의 정량 검증(faithfulness, 물리량과의 대응)은 초록 수준에서 확인되지 않았다.
- LRP를 전력전자 진단에 적용한 사례는 이번 검색에서 확인하지 못했다.
- **연구실 적용**: 1D CNN의 Grad-CAM으로 리플 window의 시간축 기여를 보고, FFT 대역별 occlusion이나 SHAP으로 주파수 기여를 본다. 이렇게 하면 모델이 fsw 측대역이나 2f0 같은 노화 관련 성분을 쓰는지, 아니면 조건 특이 성분을 쓰는지 판별할 수 있다. 미지 조건에서 성능이 떨어지는 원인을 진단하는 도구로 쓴다.

### O. 멀티모달 센서 퓨전 (예지보전)
- 전기기계 분야에서 진동+전류 퓨전이 주류다(B2-12, B2-16 X, B2-17 X). 시간-주파수 이중 경로 Transformer(B2-17)나 hypergraph contrastive fusion(B2-16) 같은 구조가 등장했다.
- "학습 시 멀티모달, 추론 시 단일모달"(B2-12)은 센서 비용 제약이 있는 현장 진단에 맞는 설계다.
- 전력전자에서 전기+열(+진동) 퓨전 사례로는 열화상 기반 이상탐지(B2-15 X) 정도만 확인했다. 검색 한도 소진으로 전력전자 직접 사례를 충분히 확보하지 못했다.
- **연구실 적용**: 커패시터의 ESR은 온도 의존성이 크므로, 리플 파형에 케이스/주변 온도를 보조 입력으로 융합하면 온도에 따른 ESR 변화와 노화에 따른 ESR 증가를 분리하는 데 도움이 될 수 있다(해석). 실험실에서는 iC 전류 프로브나 LCR 측정치를 보조 모달로 쓰고 contrastive 정렬을 하면, 현장 단일 센서 모델의 성능을 높일 수 있다.

---

## 4) 공통 한계

1. **고장 유형 편중**: 인버터 DL 진단의 주류는 이산적인 스위치 open-circuit fault다. 커패시터 노화 같은 연속·점진 열화(fault severity)를 다룬 DL 일반화 연구는 드물다(B2-14 X, B2-20 X를 빼면 이번 범위에서 확인하지 못함).
2. **평가 프로토콜 불투명**: 대부분의 초록에서 random split인지 운전조건별 split인지, 학습에 없던 조건에서 시험했는지가 명시되지 않는다. 한 기록에서 잘라낸 겹치는 window가 train과 test에 섞이면 정확도가 과대평가될 수 있다. 이는 일반론적 추론이며 각 논문에서 확인한 것은 아니다.
3. **도메인 이동의 정의가 좁음**: sim→HIL(B2-04), 부하/토크 변화(B2-11) 등 한두 축만 다룬다. f0, fsw, 변조지수(출력전압), 부하가 동시에 바뀌는 다축 조건 일반화는 확인되지 않았다.
4. **target 데이터 전제**: DA(B2-01, B2-06)와 fine-tuning(B2-04)은 target 데이터(비라벨 또는 소량 라벨)가 있어야 한다. target 없이 대응하는 DG는 전력전자에서 아직 적다.
5. **XAI의 정성성**: Grad-CAM/SHAP 결과가 물리적 근거(고조파 성분, ESR/C 변화)와 맞는지 정량 검증한 사례는 확인되지 않았다.
6. **Edge 검증 부족**: "lightweight"라는 주장은 있으나 MCU 실구현, 추론 시간, 메모리를 보고한 사례는 초록 수준에서 확인하지 못했다.
7. **재현성**: 데이터셋 비공개가 일반적이고, 성능 수치는 대부분 초록에만 나온다.
8. **본 탐색의 한계**: 모든 정보가 검색 스니펫과 요약 수준이다. 본문을 읽지 않았고 WebSearch 한도 소진으로 DOI, 권호 보완과 O/L 분야 추가 탐색을 끝내지 못했다. 다음 우선 확인 대상은 다음과 같다. ① B2-14(HTM, 커패시터 노화 비지도) 저자와 DOI, ② B2-04/05/06/08/11/12/13의 DOI, ③ B2-07(오픈액세스) 본문의 split 방식과 운전조건 표.
