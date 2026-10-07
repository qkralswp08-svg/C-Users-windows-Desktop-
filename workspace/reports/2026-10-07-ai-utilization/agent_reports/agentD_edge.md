# Agent D — Literature Researcher 3: Edge AI / TinyML / MCU 진단 / 모델 경량화

작성일: 2026-10-07 · 검색 수단: WebSearch 만 사용(WebFetch/curl 미사용, 우회 없음)

## 0. 검색 범위와 한계 (먼저 읽을 것)

- 검색 질의 약 35회 후 **세션 공유 WebSearch 한도(200회/turn, 전 Agent 공유)가 소진**되어 추가 검색을 하지 못했다. 그래서 일부 항목(D-08 Sensors DOI 독립 재확인, D-14 의 Edge 장치 종류, D-16 의 수치 세부)은 확인하지 못한 상태로 남았다. 필요하면 후속 요청으로 이어서 검증할 수 있다.
- 등급 기준: **V1** = 제목+제1저자+venue+연도 일치이고, DOI 또는 arXiv ID 문자열이 검색결과(결과 URL 또는 결과 본문)에 직접 나타남 / **V2** = 서지는 일치하나 DOI 미확인 / **X** = 서지 확인 실패(핵심 선정 금지).
- 질의문에 DOI·arXiv ID 를 넣어 검색한 경우, 결과 **URL 자체에 같은 ID 가 나온 경우만** V1 근거로 인정했다(응답 요약이 질의를 되풀이한 것은 근거로 보지 않음). 예외는 각 행에 적었다.
- 논문 세부(MCU 종류, 메모리, 지연, 정확도)는 **검색 스니펫/초록 요약에 나온 것만** 적었다. 없는 것은 "확인되지 않음(초록 수준)"으로 표시했다.
- 검색 중 발견한 **서지 오류 사례**: 한 검색 요약이 D-16(Thota et al.)을 "CVPR 2025, pp. 2704–2713"이라고 했는데, 이 쪽수는 D-01(Jacob et al., CVPR 2018)의 쪽수다. 요약이 잘못 섞인 것으로 판단해 버리고, dblp 스니펫(ACM GLSVLSI 2025: 911–915)과 ACM DOI URL 을 채택했다.
- 로컬 작업공간(`/home/user/C-Users-windows-Desktop-`)에서 `tflite`/`TFLiteConverter` 문자열을 Grep 했으나 **찾지 못했다**. 연구실 Keras→TFLite export 코드는 이 작업공간에서 확인하지 못했다(다른 Agent 확인 사항).

---

## 1) 후보 표

### 1-A. 주 후보 16편

| ID | 제목 | 저자 | 연도 | venue | 권호/쪽 | DOI / arXiv | 등급 | 근거 URL | 범주 |
|---|---|---|---|---|---|---|---|---|---|
| D-01 | Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference | Benoit Jacob, Skirmantas Kligys, Bo Chen, Menglong Zhu, Matthew Tang, Andrew Howard, Hartwig Adam, Dmitry Kalenichenko | 2018 | Proc. IEEE/CVF CVPR | pp. 2704–2713 | 10.1109/CVPR.2018.00286 / arXiv:1712.05877 | **V1** | https://openaccess.thecvf.com/content_cvpr_2018/html/Jacob_Quantization_and_Training_CVPR_2018_paper.html , https://arxiv.org/abs/1712.05877v1 | 양자화 (원전) |
| D-02 | Distilling the Knowledge in a Neural Network | Geoffrey Hinton, Oriol Vinyals, Jeff Dean | 2015 | arXiv (Google) | — | arXiv:1503.02531 | **V1** | https://arxiv.org/abs/1503.02531 , https://research.google/pubs/pub44873/ | KD (원전) |
| D-03 | Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding | Song Han, Huizi Mao, William J. Dally | 2016 | ICLR 2016 | — | arXiv:1510.00149 | **V1** | https://arxiv.org/abs/1510.00149 , https://mlanthology.org/iclr/2016/han2016iclr-deep/ | 프루닝+양자화 (원전) |
| D-04 | Learning both Weights and Connections for Efficient Neural Networks | Song Han, Jeff Pool, John Tran, William J. Dally | 2015 | NeurIPS (NIPS) 2015 | — | arXiv:1506.02626 | **V1** | https://arxiv.org/abs/1506.02626v1 , https://mlanthology.org/neurips/2015/han2015neurips-learning | 프루닝 (원전) |
| D-05 | TensorFlow Lite Micro: Embedded Machine Learning for TinyML Systems (arXiv v3 제목: "...on TinyML Systems") | Robert David, Jared Duke, Advait Jain, Vijay Janapa Reddi, Nat Jeffries, Jian Li, Nick Kreeger, Ian Nappier, Meghna Natraj, Tiezhen Wang, Pete Warden, Rocky Rhodes | 2021 | Proc. MLSys 3 (MLSys 2021) | — | arXiv:2010.08678 | **V1** | https://proceedings.mlsys.org/paper_files/paper/2021/hash/6c44dc73014d66ba49b28d483a8f8b0d-Abstract.html , https://arxiv.org/abs/2010.08678v3 | TinyML (프레임워크 원전) |
| D-06 | MLPerf Tiny Benchmark | Colby Banbury 외 (50개 이상 기관 공동; 전체 저자 목록 미확인) | 2021 | NeurIPS 2021 Datasets and Benchmarks Track | — | arXiv:2106.07597 | **V1** | https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/da4fb5c6e93e74d3df8527599fa62642-Abstract-round1.html , https://arxiv.org/pdf/2106.07597 | TinyML (벤치마크 원전) |
| D-07 | CMSIS-NN: Efficient Neural Network Kernels for Arm Cortex-M CPUs | Liangzhen Lai, Naveen Suda, Vikas Chandra | 2018 | arXiv (Arm) | — | arXiv:1801.06601 | **V1** | https://arxiv.org/pdf/1801.06601 | TinyML (MCU 커널) |
| D-08 | Quantization and Deployment of Deep Neural Networks on Microcontrollers | Pierre-Emmanuel Novac, Ghouthi Boukli Hacene, Alain Pegatoquet, Benoît Miramond, Vincent Gripon | 2021 | Sensors (MDPI) | vol. 21, art. 2984 | 10.3390/s21092984 (※질의에 포함, 결과 URL 미노출) / arXiv:2105.13331 (결과 URL 확인) | **V1** (arXiv ID 기준; 저널 DOI 는 독립 재확인 못함) | https://arxiv.org/pdf/2105.13331 | 양자화 / MCU 배포 |
| D-09 | Machine Learning for Microcontroller-Class Hardware: A Review | Swapnil Sayan Saha, Sandeep Singh Sandha, Mani Srivastava | 2022 | IEEE Sensors Journal | vol. 22, no. 22, pp. 21362–21390 | 10.1109/JSEN.2022.3210773 / arXiv:2205.14550 | **V1** | https://arxiv.org/pdf/2205.14550 , https://par.nsf.gov/biblio/10411935 | TinyML 리뷰 (IEEE) |
| D-10 | A review on TinyML: State-of-the-art and prospects | Partha Pratim Ray | 2022 | Journal of King Saud University – Computer and Information Sciences (Elsevier) | vol. 34, no. 4, pp. 1595–1623 | 10.1016/j.jksuci.2021.11.019 | **V1** | https://ouci.dntb.gov.ua/works/45Go8xv9 | TinyML 리뷰 (Elsevier) |
| D-11 | LArcNet: Lightweight Neural Network for Real-Time Series AC Arc Fault Detection | Kamal Chandra Paul, Chen Chen, Yao Wang, Tiefu Zhao | 2025 | IEEE Open Journal of Industry Applications | vol. 6, pp. 79–92 | DOI 미확인 | **V2** | https://ieeexplore.ieee.org/document/10816166 , https://engage.ieee.org/rs/756-GPH-899/images/ES_TA_1017_2025_10_IAS_Publications_NL_October_ES_TA_1017_IEEE_IAS_Pubs_Newsletter.html?version=0 | MCU 사례 (아크) + KD |
| D-12 | PV Arc Fault Circuit Interrupter with Knowledge Distillation-Based Lightweight Convolutional Neural Network and SSCB Integration | Kamal Chandra Paul, Jiale Zhou, Shen-En Chen, Tiefu Zhao | 2025 | IEEE Transactions on Power Electronics | vol. 40, no. 12, pp. 18189–18201 (Dec. 2025) | DOI 미확인 | **V2** | https://ieeexplore.ieee.org/document/11078896/ , https://coefs.charlotte.edu/tzhao5/home/publications/ | MCU 사례 (PV DC 아크) + KD |
| D-13 | Real Time Bearing Fault Diagnosis Based on Convolutional Neural Network and STM32 Microcontroller | Wenhao Liao (공저자 유무 확인 못함) | 2023 | arXiv | — | arXiv:2304.09100 | **V1** (arXiv) | https://arxiv.org/pdf/2304.09100 | MCU 사례 (베어링) |
| D-14 | Real-Time Diagnosis of Multiple Open-Circuit Faults in ANPC Inverters Based on Lightweight Deployment of Edge 2D-CNN | G. Ma, C. Yao, S. Xu, G. Ren, Z. Sun, S. Wu | 2025 | IEEE Transactions on Industrial Electronics (early access; 최종 권호 미확인) | — | 10.1109/TIE.2025.3549086 | **V1** (DOI 가 검색결과 URL `api.openalex.org/works/doi:10.1109%2FTIE.2025.3549086` 에 노출; 해당 페이지는 열지 않음) | https://api.openalex.org/works/doi:10.1109%2FTIE.2025.3549086 (검색결과 링크로만 확인) | Edge 사례 (전력전자, NPC 계열) |
| D-15 | ArcNet: Series AC Arc Fault Detection Based on Raw Current and Convolutional Neural Network | Yao Wang, Linming Hou, Kamal Chandra Paul, Yunsheng Ban, Chen Chen, Tiefu Zhao | 2022 | IEEE Transactions on Industrial Informatics | vol. 18, no. 1, pp. 77–86 | DOI 미확인 | **V2** | https://www.researchgate.net/publication/350536091_ArcNet_Series_AC_Arc_Fault_Detection_Based_on_Raw_Current_and_Convolutional_Neural_Network , https://coefs.charlotte.edu/tzhao5/home/publications/ | Edge 사례 (아크, 임베디드 보드) |
| D-16 | TinyML Enabled Real-Time Bearing Fault Classification in Motors Using Vibration Signals | Yogeswar Reddy Thota, Mojtaba Afshar, Samantha Boden, Brendan Dunlap, Bilal Akin, Tooraj Nikoubin | 2025 | Proc. ACM Great Lakes Symposium on VLSI (GLSVLSI 2025) | pp. 911–915 | 10.1145/3716368.3735272 | **V1** | https://dl.acm.org/doi/10.1145/3716368.3735272 , https://dblp.uni-trier.de/pid/19/8271.html | MCU 사례 (모터 베어링, TinyML) |

### 1-B. 보조 후보 (핵심 선정 대상 아님, 체크리스트·배경 근거로만 사용)

| ID | 제목 | 저자 | 연도 | venue | 권호/쪽 | DOI / arXiv | 등급 | 근거 URL | 범주 |
|---|---|---|---|---|---|---|---|---|---|
| D-17 | MCUNet: Tiny Deep Learning on IoT Devices | Ji Lin, Wei-Ming Chen, Yujun Lin, John Cohn, Chuang Gan, Song Han | 2020 | NeurIPS 2020 | — | arXiv:2007.10319 | V1 | https://papers.nips.cc/paper/2020/hash/86c51678350f656dcc7f490a43946ee5-Abstract.html , https://arxiv.org/abs/2007.10319v2 | TinyML (NAS+엔진) |
| D-18 | A Comprehensive Survey on TinyML | Youssef Abadade 외 | 2023 | IEEE Access | 권호 미확인 | 10.1109/ACCESS.2023.3294111 | V1 | https://www.researchgate.net/publication/372235897_A_Comprehensive_Survey_on_TinyML | TinyML 리뷰 |
| D-19 | A Machine Learning-oriented Survey on Tiny Machine Learning | Capogrosso 외 (제1저자 성만 확인, 이름·공저자 미확인) | 2024 | IEEE Access | vol. 12, pp. 23406–23426 | 10.1109/ACCESS.2024.3365349 / arXiv:2309.11932 | V1 | https://arxiv.org/pdf/2309.11932 , https://iris.polito.it/handle/11583/2986085 | TinyML 리뷰 |
| D-20 | Neural Network Quantization for Microcontrollers: A Comprehensive Survey of Methods, Platforms, and Applications | Hamza A. Abushahla, Dara Varam, Ariel J. N. Panopio, Mohamed I. AlHajri | 2025 | arXiv | — | arXiv:2508.15008 | V1 (arXiv) | https://arxiv.org/abs/2508.15008v4 | 양자화 리뷰 (MCU) |
| D-21 | Arc_EffNet: A Novel Series Arc Fault Detection Method Based on Lightweight Neural Network | Xin Ning, Dejie Sheng, Jiawang Zhou, Yuying Liu, Yao Wang, Hua Zhang, Xiao Lei | 2023 | Electronics (MDPI) | vol. 12, no. 22, art. 4617 | 10.3390/electronics12224617 | V1 | https://doi.org/10.3390/electronics12224617 (결과 URL), https://www.mdpi.com/2079-9292/12/22/4617 | Edge 사례 (아크, Raspberry Pi) |
| D-22 | Ultra-Low-Energy Open-Circuit Fault Diagnosis for Three-Phase Inverters | Xiaoyi Lei, Fanfu Wu, Yunting Liu | 2026 | arXiv | — | arXiv:2607.25037 | V1 (arXiv) | https://arxiv.org/pdf/2607.25037 | 저에너지 진단 (SNN, 인버터) |
| D-23 | Microcontroller-based real-time motor bearing fault detection and diagnosis using 1D convolutional neural networks | Sertac Kilickaya | 2022 | M.S. thesis, Izmir University of Economics (스니펫 기준) | — | 없음 | V2 (학위논문) | https://www.researchgate.net/publication/382996936_Microcontroller-based_real-time_motor_bearing_fault_detection_and_diagnosis_using_1D_convolutional_neural_networks | MCU 사례 (베어링) |
| D-24 | Deep transfer learning strategy for efficient domain generalisation in machine fault diagnosis | Supriya Asutkar, Siddharth Tallur | 2023 | Scientific Reports | 권호 미확인 | 10.1038/s41598-023-33887-5 | V1 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10125977/ | 도메인 일반화 (진단) |

### 1-C. 등급 X (채택하지 않음)

| 항목 | 사유 |
|---|---|
| "TinyML-enabled edge implementation of transfer learning framework for domain generalization in machine fault diagnosis" (ResearchGate 364634937) | 제목만 확인. 저자·venue·연도·DOI 를 검색결과에서 확인하지 못함 → X |
| D-16 을 "CVPR 2025, pp. 2704–2713" 으로 적은 검색 요약 | D-01 의 쪽수와 섞인 오류로 판단, 버림 |
| TI TMS320F28P55x (C2000 + NPU) 아크/베어링 고장 검출 | 제조사 보도자료(electronicspecifier 등)로 논문이 아님. "5–10배 지연 감소, >99% 검출" 은 **벤더 주장**이다. 산업 동향 참고로만 쓴다 |

---

## 2) 핵심 논문 상세 (8편: 방법론 원전 4 + 전기/산업 진단 Edge·MCU 적용 4)

> 표기: [사실] = 검색 스니펫/초록 요약에서 확인 · [해석] = 내 판단 · "확인되지 않음(초록 수준)" = 스니펫에 없음

### 2.1 D-01 Jacob et al., CVPR 2018 — int8 정수 전용 추론 (양자화 원전)
| 항목 | 내용 |
|---|---|
| 제목/저자/연도/venue/DOI | Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference / Jacob, B. 외 7인 / 2018 / CVPR, pp. 2704–2713 / 10.1109/CVPR.2018.00286 |
| 진단 대상 | 해당 없음 (범용 방법론) |
| 입력 | 이미지 (ImageNet 분류, COCO 검출) [사실] |
| 모델 | MobileNet 계열 등 CNN. 세부 확인되지 않음(초록 수준) |
| 학습·경량화 방식 | [사실] 정수 전용 연산 추론을 위한 양자화 방식과, 이와 함께 설계한 학습 절차(quantization-aware training)를 제안. 가중치와 활성값을 모두 8-bit 정수로 양자화 |
| 성능 | [사실] float32 대비 메모리 약 4배 감소, 정확도는 float 추론에 근접, ARM CPU 에서 지연-정확도 trade-off 개선 |
| Edge 적용 | ARM 모바일 CPU (MCU 아님) [사실] |
| 연구실 관련성 | [해석] TFLite 의 int8 양자화(scale/zero-point affine 방식)의 이론적 근거다. Keras→.tflite int8 변환 시 "PTQ 로 충분한가, QAT 가 필요한가"를 판단하는 기준 문헌이다 |
| 한계 | 대상이 이미지 CNN 이다. 1D 전류 FFT 특징처럼 동적 범위가 넓은 입력(기본파 대비 매우 작은 고조파)에서 int8 이 해상도를 충분히 유지하는지는 이 논문으로는 알 수 없다 [해석] |

### 2.2 D-02 Hinton, Vinyals, Dean, 2015 — Knowledge Distillation (원전)
| 항목 | 내용 |
|---|---|
| 서지 | Distilling the Knowledge in a Neural Network / arXiv:1503.02531 (2015) |
| 진단 대상/입력 | 해당 없음 (범용) |
| 방법 | [사실] softmax 의 temperature 를 높여 큰 모델(또는 앙상블)이 만든 soft target 으로 작은 모델을 학습시켜, 앙상블의 지식을 배포하기 쉬운 단일 모델로 압축 |
| 성능/데이터 | 확인되지 않음(초록 수준) |
| Edge 적용 | 논문 자체에는 MCU 구현이 없음 [사실 범위 내 판단] |
| 연구실 관련성 | [해석] D-11, D-12 (아크 진단)가 KD 로 STM32 용 학생 모델을 만든 직접 선례다. 커패시터 진단에서도 큰 CNN/LSTM(teacher) → 작은 1D-CNN/MLP(student)로 옮기는 근거가 된다 |
| 한계 | 회귀(C/ESR 추정) 문제에는 soft target 개념을 그대로 쓸 수 없고 변형(특징 증류, 출력 회귀 증류)이 필요하다 [해석] |

### 2.3 D-03 Han, Mao, Dally, ICLR 2016 — Deep Compression (프루닝+양자화 원전)
| 항목 | 내용 |
|---|---|
| 서지 | Deep Compression... / ICLR 2016 / arXiv:1510.00149 |
| 방법 | [사실] 3단계: (1) pruning(중요 연결만 남김) → (2) trained quantization(weight sharing) → (3) Huffman coding. (1)(2) 뒤 재학습으로 남은 연결과 양자화 중심값을 미세조정 |
| 성능 | [사실] 저장공간 35–49배 감소, 정확도 손실 없음. AlexNet 240 MB→6.9 MB(35배), VGG-16 552 MB→11.3 MB(49배), ImageNet |
| Edge 적용 | MCU 구현은 확인되지 않음(초록 수준) |
| 연구실 관련성 | [해석] Flash 가 부족할 때 쓸 수 있는 압축 방법의 기준점이다. 다만 TFLM 은 비정형(unstructured) sparsity 를 실행 속도 이득으로 바꾸지 못하므로, MCU 에서는 **구조적 프루닝(채널 제거) + int8** 조합이 현실적이다 (일반적 공학 판단) |
| 한계 | 대규모 이미지 모델 기준이다. 수 kB~수십 kB 규모의 1D 진단 모델에서는 압축률 이득이 작다 [해석] |
| 관련 | D-04 (Han et al., NeurIPS 2015): train→prune→retrain 3단계, AlexNet 파라미터 9배(61M→6.7M), VGG-16 13배(138M→10.3M) 감소, 정확도 손실 없음 [사실] — 프루닝 단독 원전 |

### 2.4 D-05 David et al., MLSys 2021 — TensorFlow Lite Micro (TinyML 프레임워크 원전)
| 항목 | 내용 |
|---|---|
| 서지 | TensorFlow Lite Micro: Embedded Machine Learning for TinyML Systems / Proc. MLSys 3 (2021) / arXiv:2010.08678 |
| 내용 | [사실] 임베디드 시스템에서 딥러닝 모델을 실행하는 오픈소스 추론 프레임워크. 임베디드 자원 제약에 따른 효율 요구와, 플랫폼 간 상호운용을 어렵게 하는 단편화(fragmentation) 문제를 다룸. 인터프리터 기반 구조로 유연성을 확보 |
| 성능 수치 | 확인되지 않음(초록 수준) |
| 연구실 관련성 | [해석] 연구실의 `.tflite` export 가 MCU 로 가는 공식 경로다. Keras 모델 → `.tflite`(flatbuffer) → TFLM 인터프리터 + tensor arena(정적 메모리)로 실행된다. LSTM 등 일부 연산자의 TFLM 지원 여부는 별도로 확인해야 한다 (논문 스니펫에서는 확인 못함) |
| 한계 | 인터프리터 오버헤드가 있다. 벤더 툴(STM32Cube.AI 등)과의 성능 비교는 D-08, D-23 참고 |

### 2.5 D-11 Paul, Chen, Wang, Zhao, IEEE OJIA 2025 — LArcNet (아크 진단 MCU 사례)
| 항목 | 내용 |
|---|---|
| 서지 | LArcNet: Lightweight Neural Network for Real-Time Series AC Arc Fault Detection / IEEE Open J. Ind. Appl., vol. 6, pp. 79–92, 2025 / DOI 미확인 (V2) |
| 진단 대상 | 직렬 AC 아크 고장 [사실] |
| 입력 | 확인되지 않음(초록 수준). 같은 그룹의 D-15(ArcNet)는 raw current 를 입력으로 썼음 [사실, D-15 제목] |
| 모델 | [사실] teacher–student KD + 효율적 CNN 구조 |
| 학습·경량화 | [사실] KD 로 경량화한 뒤 TensorFlow Lite 형식으로 변환해 크기와 지연을 줄임. 양자화 비트수는 확인되지 않음(초록 수준) |
| 데이터/운전조건 | 확인되지 않음(초록 수준) |
| 성능 | [사실] 검출 정확도 99.31% |
| 일반화 시험 | 확인되지 않음(초록 수준) |
| 실험 vs 시뮬 | 실측 하드웨어 배포 (아래 참조). 데이터 수집 방식은 확인되지 않음 |
| Edge 적용 | [사실] Raspberry Pi 4B 추론 0.20 ms, **STM32H743ZI2 추론 3 ms** (Cortex-M7 계열, 메모리 수치는 확인되지 않음) |
| 연구실 관련성 | [해석] "아크 진단 + 설비 진단 MCU 통합" 목표에서 아크 쪽 기준점이다. **Keras→KD→TFLite→STM32** 경로가 연구실의 Keras→TFLite 경로와 같다 |
| 한계 | DOI 미확인(V2). 입력 window 길이와 int8 여부가 스니펫에 없어 커패시터 진단의 2048점 window 와 직접 비교할 수 없음 |

### 2.6 D-12 Paul, Zhou, Chen, Zhao, IEEE TPEL 2025 — PArcNet + SSCB (전력전자 저널, MCU 실시간 차단)
| 항목 | 내용 |
|---|---|
| 서지 | PV Arc Fault Circuit Interrupter with Knowledge Distillation-Based Lightweight CNN and SSCB Integration / IEEE Trans. Power Electron., vol. 40, no. 12, pp. 18189–18201, Dec. 2025 / DOI 미확인 (V2) |
| 진단 대상 | PV 시스템 DC 아크 고장 [사실] |
| 모델 | [사실] PArcNet: KD 로 최적화한 경량 CNN, **파라미터 5.04 k, 메모리 footprint 90 kB** |
| 성능 | [사실] 검출 정확도 98% 이상 |
| 운전조건/일반화 | [사실] 인버터 기동, 음영(shadow occlusion), 부하 변동 등 여러 PV 운전 상황에서 신뢰성 유지 |
| Edge 적용 | [사실] **STM32H743ZI2** 에 구현, 고체 차단기(SSCB)와 통합. 아크 검출+차단 최소 **19 ms**. 과도 외란에 따른 오검출을 줄이려고 **5-cycle 확인 전략**을 써서 총 응답시간 **95 ms** |
| 실험 vs 시뮬 | 실 하드웨어 프로토타입 [사실] |
| 연구실 관련성 | [해석] (1) 전력전자 최상위 저널에 실린 저가 MCU 실구현 사례로, 창업계획서의 "저가형 MCU 온보드 AI" 근거로 인용하기 좋다. (2) **5-cycle 확인 = 연속 스트리밍 판정 로직(다수결/연속 N회)**의 직접 근거이며, 지연과 오경보 사이의 trade-off 를 수치(19 ms → 95 ms)로 보여준다. (3) 같은 그룹의 학위논문 스니펫에는 STM32 + SiC MOSFET SSCB, 정확도 98.14%, 차단 19 ms 로 나온다 (UNCC 학위논문, 별도 서지 미검증) |
| 한계 | DOI 미확인. 입력 샘플링률과 양자화 방식은 확인되지 않음(초록 수준) |

### 2.7 D-13 Liao, arXiv 2023 — CNN 베어링 진단 on STM32H743VI
| 항목 | 내용 |
|---|---|
| 서지 | Real Time Bearing Fault Diagnosis Based on Convolutional Neural Network and STM32 Microcontroller / arXiv:2304.09100 (2023) / V1 (arXiv) |
| 진단 대상 | 베어링 고장 [사실] |
| 입력/데이터 | 확인되지 않음(초록 수준). 공개 데이터셋 사용 여부도 미확인 |
| 모델 | CNN (최적화 모델) [사실] |
| 성능 | [사실] 최적화 모델의 고장 식별 정확도 98.9% |
| Edge 적용 | [사실] **STM32H743VI** 에 배포, **진단 1회 19 ms**. PC↔STM32 시리얼 통신으로 데이터를 보내고 TFT-LCD 에 결과 표시 |
| 실험 vs 시뮬 | MCU 실구현이지만, 데이터를 PC 에서 시리얼로 보내는 구조라 **센서·ADC 를 MCU 가 직접 받는 end-to-end 실측 경로는 아닌 것으로 보임** [해석] |
| 연구실 관련성 | [해석] Cortex-M7 급 MCU 에서 1D 신호 CNN 1회 추론에 수십 ms 가 든다는 기준값이다. 2048점@100 kHz window(20.48 ms)와 **같은 크기 범위**이므로, 50% 겹침 슬라이딩(hop 10.24 ms)을 하려면 모델을 더 줄이거나 판정 주기를 늦춰야 한다 |
| 한계 | 저자 1인 arXiv(동료심사 미확인). 양자화 여부, RAM/Flash 사용량 확인되지 않음 |

### 2.8 D-14 Ma et al., IEEE TIE 2025 — ANPC 인버터 다중 개방고장 Edge 2D-CNN
| 항목 | 내용 |
|---|---|
| 서지 | Real-Time Diagnosis of Multiple Open-Circuit Faults in ANPC Inverters Based on Lightweight Deployment of Edge 2D-CNN / IEEE Trans. Ind. Electron., 2025 (early access) / 10.1109/TIE.2025.3549086 (V1) |
| 진단 대상 | ANPC(Active NPC) 인버터의 다중 개방회로 고장 [사실, 제목] |
| 입력/모델 | 2D-CNN 경량 모델 [사실, 제목]. 입력 신호 종류는 확인되지 않음(초록 수준) |
| Edge 적용 | "edge 경량 배포"로 실시간 진단 [사실, 제목]. **장치 종류(MCU/DSP/ARM-A/FPGA), 지연, 메모리는 검색 한도 소진으로 확인하지 못함** |
| 연구실 관련성 | [해석] 3-Level NPC 계열 토폴로지에서 CNN 을 edge 에 올린 최신 IEEE TIE 사례로, 연구실의 NPC DC-Link 진단과 토폴로지가 가장 가깝다. 스위칭 소자 고장 진단과 커패시터 노화 진단을 한 장치에 통합하는 근거로 쓸 수 있다 |
| 한계 | 세부를 확인하지 못했으므로 **인용 전 원문 확인이 반드시 필요**하다. edge 장치가 MCU 가 아니면 "저가 MCU" 주장의 근거로는 약하다 |

> 핵심에서 뺀 이유: D-15(ArcNet)과 D-21(Arc_EffNet)은 Raspberry Pi(ARM-A, Linux)로, MCU 가 아니다. D-16(Thota)은 서지는 V1 이지만 MCU 종류와 수치를 확인하지 못했다. D-23 은 학위논문, D-22 는 arXiv 프리프린트이고 SNN 이라 TFLite 경로와 다르다.

---

## 3) Cloud AI vs Edge AI 비교표 (진단 디바이스 관점)

| 항목 | Cloud AI (원시/특징 데이터 전송 → 서버 추론) | Edge AI (MCU 온보드 추론) | 근거 |
|---|---|---|---|
| 지연 | 네트워크 왕복과 큐잉이 더해져 지연이 가변적이다. ms 단위 보호 동작(아크 차단)에는 쓰기 어렵다 | 센서→판정이 장치 안에서 끝난다. STM32H7 급에서 추론 3 ms(D-11), 19 ms(D-13), 검출+차단 19 ms(D-12) | Edge 수치: D-11, D-12, D-13 / Cloud 쪽: 일반적 공학 판단 |
| 통신 의존 | 통신이 끊기면 진단도 멈춘다. 대역폭 요구가 크다(100 kHz 원시 전류 연속 전송은 비현실적) | 판정 결과·이벤트·요약 통계만 보내면 된다. 오프라인에서도 동작한다 | 일반적 공학 판단 (100 kHz×16 bit ≈ 1.6 Mbit/s/채널 계산) |
| 프라이버시·보안 | 설비 운전 데이터가 밖으로 나간다. 전송 구간과 서버 보안이 필요하다 | 원시 데이터가 장치 안에 남는다. 대신 펌웨어·모델 변조 방지(서명, secure boot)가 필요하다 | 일반적 공학 판단 |
| 연산·메모리 | 사실상 제약이 없다. 대형 CNN/LSTM, 앙상블, 재학습이 가능하다 | KB~수백 KB RAM/Flash. 모델을 int8 양자화(메모리 약 1/4, D-01)·KD(D-02, D-12: 5.04 k 파라미터, 90 kB)·프루닝(D-03, D-04)으로 줄여야 한다. MCU 메모리는 모바일 기기보다 2–3 자릿수 작다(D-17) | D-01, D-02, D-03, D-04, D-12, D-17 |
| 정확도 | float32 원 모델 그대로 쓸 수 있다 | 양자화·경량화에 따른 정확도 저하를 다시 검증해야 한다. 적절한 방법을 쓰면 float 에 근접한다(D-01) | D-01, D-08 |
| 모델 업데이트 | 서버에서 즉시 교체·A/B 시험이 가능하다 | OTA 펌웨어/모델 갱신 체계가 필요하다. TFLM 은 인터프리터 구조라 모델(flatbuffer) 교체에 유연하다(D-05) | D-05 (인터프리터 구조) + 일반적 공학 판단 (OTA) |
| 전력·에너지 | 장치 쪽 통신 전력과 서버 전력을 계속 쓴다 | 추론당 에너지가 작다. CMSIS-NN 은 에너지 효율 4.9배 개선(D-07), SNN 진단은 11 μJ/회(D-22). MLPerf Tiny 는 정확도·지연·에너지를 함께 측정한다(D-06) | D-06, D-07, D-22 |
| 비용 | 장치는 싸지만 통신모듈·서버 운영비가 반복해서 든다 | MCU 단가 외에 반복 비용이 거의 없다. 저가 MCU 실시간 배포 가능(D-12 초록 문구 "low-cost microcontrollers") | D-12 + 일반적 공학 판단 |
| 산업 동향 | — | MCU 안에 NPU 를 넣는 흐름(TI C2000 F28P55x, 아크·베어링 고장 검출 대상; 벤더 주장) | 비논문, 1-C 참고 |

[해석] 결론: **아크 보호(ms 단위, 차단 동작)**는 Edge 가 필수다. **커패시터 노화(일~월 단위로 진행)**는 지연 요구가 느슨해서, Edge 에서 판정하고 결과/추세만 Cloud 로 보내는 **하이브리드**가 합리적이다. 통합 디바이스에서는 두 작업의 실시간 요구가 다르므로 스케줄링 우선순위를 나눠야 한다(아크 = hard real-time, 커패시터 = 저우선 배경 작업).

---

## 4) "실험실 Keras 모델 → MCU Edge AI" 이전 시 추가 검증 체크리스트 (15항목)

| # | 검증 항목 | 구체적 방법 / 합격 기준(제안) | 근거 |
|---|---|---|---|
| 1 | **int8 양자화 후 정확도·혼동행렬 재평가** | float32 Keras / float `.tflite` / int8 `.tflite` 세 가지를 **같은 test set** 으로 평가한다. 전체 정확도뿐 아니라 **클래스별 recall, 노화 경계 클래스(예: 정상↔경미) 혼동**, 회귀라면 C·ESR 오차 분포를 비교한다. 저하 허용치를 사전에 정한다(예: ≤1%p) | D-01, D-08, D-20 |
| 2 | **PTQ calibration(대표) 데이터셋 선택** | 활성값 범위가 모든 운전조건을 덮도록 고른다(부하, 변조지수, 역률, DC 전압, 노화 전 구간). 한 조건만 쓰면 다른 조건에서 포화·클리핑이 생긴다. 100–500 window 규모로 층화추출(stratified)한다 | D-01 (활성값 양자화 범위) + 일반적 공학 판단 |
| 3 | **PTQ 로 부족할 때 QAT / KD 적용** | int8 저하가 허용치를 넘으면 QAT(D-01)를 쓴다. 모델이 RAM/Flash 를 넘으면 KD 학생 모델(D-02)을 만든다. 아크 진단에서 KD 학생 모델을 STM32 에 올린 선례가 있다(D-11, D-12) | D-01, D-02, D-11, D-12 |
| 4 | **전처리의 펌웨어 재현 일치성** | z-score 의 mean/std 상수, 리샘플링·필터 계수, FFT 창함수·정규화(1/N, 단측 스펙트럼 ×2), bin 선택을 Python 과 **같은 상수**로 펌웨어에 넣는다. 고정 test vector 를 넣고 Python 출력과 MCU 출력을 원소 단위로 비교한다(허용오차 명시). float vs 고정소수점(CMSIS-DSP q15) 차이도 확인한다 | 일반적 공학 판단 (D-08: MCU 에서 fixed-point 8/16-bit 실행 비교) |
| 5 | **입력 텐서 양자화 파라미터 정합** | int8 입력 모델이면 펌웨어에서 `q = round(x/scale) + zero_point` 를 적용해야 한다. z-score 이후 값의 분포가 scale 범위를 넘지 않는지(고조파 특징의 작은 값이 0 으로 뭉개지지 않는지) 확인한다. 특징의 동적 범위가 넓으면 log 스케일 특징을 검토한다 | D-01 + 일반적 공학 판단 |
| 6 | **ADC 분해능·샘플링 지터·anti-aliasing** | 시뮬레이션 입력(이상적 float)과 실제 ADC(12/16 bit, 유효비트 ENOB, 지터, AAF 대역)의 차이를 시뮬 데이터에 **양자화 노이즈·지터를 주입**해 민감도를 평가한다. 관심 고조파의 진폭이 ADC LSB 보다 충분히 큰지 계산한다 | 일반적 공학 판단 (논문 근거 미확보) |
| 7 | **추론 지연 vs window 길이 (실시간 조건)** | window = 2048점@100 kHz = **20.48 ms**. 겹침 없으면 (ADC 수집 DMA 와 병렬) 전처리+FFT+추론 < 20.48 ms, 50% 겹침이면 < 10.24 ms 여야 한다. 참고로 STM32H7 급 CNN 추론이 3 ms(D-11)~19 ms(D-13)이다. 최악 실행시간(WCET)을 DWT 사이클 카운터로 측정한다. CMSIS-NN 커널 사용 여부도 비교한다(D-07, 4.6배 throughput 차이 보고) | D-07, D-11, D-13 |
| 8 | **판정 주기 설계 (작업 성격 구분)** | 커패시터 노화는 느리므로 매 window 판정이 필요 없다. N 분마다 M 개 window 를 처리하는 duty-cycled 방식으로 아크 진단(ms 단위 hard real-time)과 CPU 를 나눠 쓴다. 우선순위·인터럽트 지연이 아크 판정을 늦추지 않는지 시험한다 | D-12 (아크 응답 19–95 ms 요구) + 일반적 공학 판단 |
| 9 | **RAM / Flash 예산** | Flash = 모델(int8 가중치) + TFLM 런타임 + 아크 모델 + 펌웨어. RAM = tensor arena(TFLM 이 보고하는 사용량) + ADC 이중버퍼(2048×2 B×2 = 8 KB/채널) + FFT 작업버퍼(2048 float = 8 KB, 복소면 더 큼) + 아크 모델 arena. **두 모델이 동시에 상주하는 경우**를 기준으로 측정한다. 참고: PArcNet 90 kB(D-12) | D-05, D-12, D-17 |
| 10 | **연산자 지원·변환 호환성** | Keras LSTM/GRU, 일부 activation, 동적 shape 는 TFLM 커널 지원이 제한될 수 있다. 변환한 `.tflite` 의 op 목록을 확인하고 MCU 빌드에서 OpResolver 에 등록되는지 확인한다. 지원이 안 되면 1D-CNN/MLP 로 교체한다 | D-05 + 일반적 공학 판단 (op 지원 목록은 공식 문서로 확인 필요) |
| 11 | **연속 스트리밍 판정 로직** | 단일 window 판정은 과도 상태에 흔들리므로 **연속 N회 확인 / 다수결 / 히스테리시스(진입·해제 임계 분리) / 이동평균 확률**을 적용한다. N 과 지연·오경보의 trade-off 를 정량화한다. 선례: 5-cycle 확인으로 총 응답 19 ms→95 ms, 과도 외란 오검출 감소(D-12) | D-12 |
| 12 | **운전 과도·외란 강건성** | 기동, 부하 계단, 변조지수 변화, DC 전압 변동, 불평형 부하에서 오경보가 나지 않는지 시험한다. 측정 노이즈 주입 시험도 한다 | D-12 (인버터 기동·음영·부하변동), D-22 (불평형 부하·전류 진폭 계단·측정 노이즈) |
| 13 | **온도 영향 분리** | 전해 커패시터 C/ESR 은 온도에 따라 변하므로 "노화"와 "온도"를 혼동하지 않는지 확인한다. 온도 센서 입력을 함께 쓰거나 온도 보상 후 판정하고, 온도 sweep 시험을 한다. MCU·센서 오프셋의 온도 드리프트도 확인한다 | 일반적 공학 판단 (커패시터 온도 의존성은 capacitor-aging 문헌 담당 Agent 근거 참조) |
| 14 | **시뮬레이션→실측 도메인 시프트** | 시뮬레이션 데이터로 학습한 모델을 실측 데이터로 시험한다(최소한 holdout 실측 세트). 필요하면 하위 conv 층 fine-tuning 같은 전이학습을 쓴다 | D-24 (conv 층 fine-tune + dense 층 전이로 도메인 일반화) + 일반적 공학 판단 |
| 15 | **장시간 오경보율·에너지 보고** | 정상 운전 장시간(예: ≥24–72 h) 연속 실행으로 **시간당/일당 오경보 횟수**와 놓침률을 측정한다. 추론당 에너지(mJ)·평균 전력과 함께 **정확도·지연·에너지를 같은 형식으로 보고**한다(MLPerf Tiny 형식) | D-06 (정확도·지연·에너지 동시 측정), D-07, D-08 + 일반적 공학 판단 (FAR 장시간 시험) |

---

## 5) 요약 판단 [해석]

1. 방법론 원전(D-01 양자화, D-02 KD, D-03/D-04 프루닝, D-05 TFLM, D-06 MLPerf Tiny)은 모두 V1 로 확인했다.
2. 전기설비 진단을 MCU 에 실구현한 사례 중 가장 강한 근거는 **같은 그룹(UNC Charlotte, T. Zhao)의 아크 진단 연작**이다: D-15(TII 2022) → D-11(OJIA 2025, STM32H743ZI2 3 ms) → D-12(TPEL 2025, 5.04 k 파라미터/90 kB, 19 ms 차단, 5-cycle 확인). 다만 D-11, D-12 는 DOI 미확인(V2)이므로 인용 전에 DOI 를 확인해야 한다.
3. **DC-Link 커패시터 노화를 MCU 온보드 신경망으로 진단한 논문은 이번 검색에서 찾지 못했다.** ANN 을 DSP 에 통합했다는 서술은 검색 요약에 있었으나 서지를 특정하지 못했다(미채택). 이 분야의 **연구 공백(Research Gap)**일 가능성이 있으나, 검색 한도로 충분히 탐색하지 못했으므로 단정하지 않는다.
4. 연구실 이전 경로(Keras→TFLite→MCU)는 D-11/D-12 의 경로(KD→TFLite→STM32H7)와 같다. 연구실 window(20.48 ms)는 문헌의 STM32H7 추론 지연(3–19 ms)과 같은 크기 범위이므로 **지연 예산 검증(체크리스트 7, 8)**이 가장 먼저 해야 할 일이다.
