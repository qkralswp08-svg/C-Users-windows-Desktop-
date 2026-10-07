# 06. 참고문헌 실재성 검증 기록

- 작성일: 2026-10-07
- 목적: 보고서에 인용한 모든 논문의 실재 여부, 서지 정확성, DOI 확인 수준을 기록하고, 확인하지 못한 항목을 명시한다.

---

## 1. 검증 방법과 한계

| 항목 | 내용 |
|---|---|
| 사용 도구 | WebSearch(검색결과 제목·URL·스니펫). 다섯 개 문헌 에이전트(A, B1, B2, C, D)가 분담 |
| 사용 불가 | Crossref API, doi.org, IEEE Xplore, MDPI, ScienceDirect, Springer, OpenAlex, dblp, Semantic Scholar API — 컨테이너 egress 정책으로 **WebFetch·curl 모두 차단**(Lead가 직접 시험해 403/EGRESS_BLOCKED 확인). KIPRIS도 확인 불가 |
| 검색 한도 | 세션 공유 WebSearch 한도(200회)가 탐색 중 소진됨. 이후 추가 검증 불가 |
| 결과의 의미 | **V1이라도 doi.org로 해석(resolve)해 본 것이 아니다.** DOI 문자열이 검색결과의 URL·스니펫에 나타난 것을 확인한 수준이다. 최종 제출 전 doi.org에서 재확인을 권고한다 |
| 본문 확인 | 0편. 모든 내용 요약은 초록·스니펫 수준 |

### 등급 정의
| 등급 | 기준 | 보고서 사용 |
|---|---|---|
| V1 | 제목·제1저자·게재처·연도 일치 + DOI(또는 arXiv ID) 문자열을 검색결과 URL/스니펫에서 직접 확인 | 참고문헌 사용 |
| V1* | 제목·DOI는 출판사 URL로 확인, 저널은 DOI prefix로 판정, 저자·연도 일부 미확인 | 연구실 논문 목록에만 사용 |
| V2 | 제목·저자·게재처·연도 일치, DOI 미확인 | 참고문헌 사용(DOI "미확인" 표기) |
| P | 이전 조사(2026-09-29, 같은 저장소 `papers/index.md`)에서 검색 색인 URL과 함께 기록, 이번 세션 미재검증 | 배경 설명에만 제한적으로 사용 |
| X | 제1저자·게재처·연도 중 하나 이상 미확인 | **사용하지 않음** |

---

## 2. 최종 참고문헌 목록 (외부 논문)

| # | 서지 | DOI / ID | 등급 | 근거 URL(검색결과) |
|---|---|---|---|---|
| [1] | S. Zhao, F. Blaabjerg, H. Wang, "An Overview of Artificial Intelligence Applications for Power Electronics," *IEEE Trans. Power Electron.*, 36(4):4633–4658, 2021 | 10.1109/TPEL.2020.3024914 | V1 | vbn.aau.dk/ws/files/431659513/... |
| [2] | A. Moradzadeh, B. Mohammadi-Ivatloo, K. Pourhossein, A. Anvari-Moghaddam, "Data Mining Applications to Fault Diagnosis in Power Electronic Systems: A Systematic Review," *IEEE Trans. Power Electron.*, 37(5):6026–6050, 2022 | 10.1109/TPEL.2021.3131293 | V1 | vbn.aau.dk/da/publications/data-mining-applications-to-fault-diagnosis-in-power-electronic-s |
| [3] | H. Wang, F. Blaabjerg, "Reliability of Capacitors for DC-Link Applications in Power Electronic Converters—An Overview," *IEEE Trans. Ind. Appl.*, 50(5), 2014 | 10.1109/TIA.2014.2308357 | P | ieeexplore.ieee.org/document/6748007 (이전 조사 기록) |
| [4] | Z. Zhao, P. Davari, W. Lu, H. Wang, F. Blaabjerg, "An Overview of Condition Monitoring Techniques for Capacitors in DC-Link Applications," *IEEE Trans. Power Electron.*, 36(4), 2021 | 10.1109/TPEL.2020.3023469 | P | ieeexplore.ieee.org/document/9195018 (이전 조사 기록) |
| [5] | K. Örüklü, Ş. Ağalar, "Machine learning-based condition monitoring for dc-link capacitors in ac/dc/ac converters," *IEEE Trans. Ind. Electron.*, 72(4):4227–4237 (참고문헌 표기 연도 2024) | 미확인 | V2 | arxiv.org/pdf/2609.00218 의 참고문헌 목록 |
| [6] | S. Zhao, Y. Peng, Y. Zhang, H. Wang, "Parameter Estimation of Power Electronic Converters With Physics-Informed Machine Learning," *IEEE Trans. Power Electron.*, 37(10):11567–11578, 2022 | 10.1109/TPEL.2022.3176468 | V1 | research.polyu.edu.hk/en/publications/parameter-estimation-of-power-electronic-converters-with-physics- |
| [7] | W. Chen, L. Zhang, K. Pattipati, A. M. Bazzi, S. Joshi, E. M. Dede, "Data-Driven Approach for Fault Prognosis of SiC MOSFETs," *IEEE Trans. Power Electron.*, 35(4), 2020 | 10.1109/TPEL.2019.2936850 | V1 | scholarworks.aub.edu.lb/items/754c3e2e-... |
| [8] | C. L. Kahraman, D. Roman, L. Kirschbaum, D. Flynn, J. Swingler, "Machine Learning Pipeline for Power Electronics State of Health Assessment and Remaining Useful Life Prediction," *IEEE Access*, 12:136727–136746, 2024 | 10.1109/ACCESS.2024.3460177 | V1 | researchportal.hw.ac.uk; doaj.org/article/10811e92f8b043028aec1f6d967d21f6 |
| [9] | T. Mamee, Z. Lou, K. Hata, M. Takamiya, T. Sakurai, S.-I. Nishizawa, W. Saito, "Estimating of IGBT Bond Wire Lift-Off Trend Using Convolutional Neural Network (CNN)," *IEEE Access*, 12:96936–96945, 2024 | 미확인 | V2 | doaj.org/article/56cc239cec64451d8dbdeb6da0aa6792 |
| [10] | Y. Liu, A. Sangwongwanich, Y. Zhang, S. Ou, H. Wang, "A Transferable Deep Learning Network for IGBT Open-circuit Fault Diagnosis in Three-phase Inverters," *IEEE APEC*, 2024 | 미확인 | V2 | research.polyu.edu.hk/en/publications/a-transferable-deep-learning-network-for-igbt-open-circuit-fault- |
| [11] | J. Zhu, Y. Wang, H. Yan, S. Lu, W. Li, "A New Weighted Mechanism-Based Partial Transfer Fault Diagnosis Method for Voltage Source Inverter," *IEEE Trans. Transp. Electrific.*, 11(3):7588–7598, 2025 | 미확인 | V2 | pure.nwpu.edu.cn/en/publications/a-new-weighted-mechanism-based-partial-transfer-fault-diagnosis-m |
| [12] | T. Li, E. Wang, J. Yang, "Lifelong Learning-Enabled Fractional Order-Convolutional Encoder Model for Open-Circuit Fault Diagnosis of Power Converters Under Multi-Conditions," *Sensors*, 25(6):1884, 2025 | 10.3390/s25061884 | V1 | ncbi.nlm.nih.gov/pmc/articles/PMC11945422 |
| [13] | Y. Ganin, E. Ustinova, H. Ajakan, P. Germain, H. Larochelle, F. Laviolette, M. Marchand, V. Lempitsky, "Domain-Adversarial Training of Neural Networks," *J. Mach. Learn. Res.*, 17(59):1–35, 2016 | arXiv:1505.07818 (저널 DOI 없음/미확인) | V2 | jmlr.org/papers/v17/15-239.html |
| [14] | S. K. Lee, H. Kim, M. Chae, H. J. Oh, H. Yoon, B. D. Youn, "Self-supervised feature learning for motor fault diagnosis under various torque conditions," *Knowledge-Based Systems*, 2024 | 미확인 | V2 | scholarworks.bwise.kr/ssu/handle/2018.sw.ssu/49461 |
| [15] | H. A. G. Al-Kaf, S. S. Hakami, K.-B. Lee, "Explainable Deep Learning Fault Detection Method for Multilevel Inverters," *IEEE Trans. Ind. Informat.*, 22(1):579–590, 2026 | 미확인 | V2 | pure.kfupm.edu.sa/en/publications/explainable-deep-learning-fault-detection-method-for-multilevel-i |
| [16] | R. Machlev, L. Heistrene, M. Perl, K. Y. Levy, J. Belikov, S. Mannor, Y. Levron, "Explainable Artificial Intelligence (XAI) techniques for energy and power systems: Review, challenges and opportunities," *Energy and AI*, 9:100169, 2022 | 10.1016/j.egyai.2022.100169 | V1 | doaj.org/article/6984422d40a64f4497b21db3cfbb1370 |
| [17] | Q. Luo, J. Chen, Y. Zi, J. Xie, "A synchronization-induced cross-modal contrastive learning strategy for fault diagnosis of electromechanical systems under semi-supervised learning with current signal," *Expert Syst. Appl.*, 249:123801, 2024 | 미확인 | V2 | scholar.xjtu.edu.cn/en/publications/a-synchronization-induced-cross-modal-contrastive-learning-strate |
| [18] | R. Jiang, Y. Wang, X. Gao, G. Bao, Q. Hong, C. Booth, "AC series arc fault detection based on RLC arc model and convolutional neural network," *IEEE Sensors J.*, 23(13):14618–14627, 2023 | 10.1109/JSEN.2023.3280009 | V1 | strathprints.strath.ac.uk/86091 |
| [19] | R. Jiang, G. Bao, Q. Hong, C. Booth, "Machine learning approach to detect arc faults based on regular coupling features," *IEEE Trans. Ind. Informat.*, 19(3):2761–2771, 2023 | 10.1109/TII.2022.3153333 | V1 | strathprints.strath.ac.uk/79813 |
| [20] | Y. Mao, S. Safa, G. Smith, L. Wurth, R. Weiss, J. Hagemeyer, "Why AI: A Comparative Study for Detection Methods in DC Series Arc Fault," *IEEE Access*, 2025 | 10.1109/ACCESS.2025.3548309 | V1 | cris.fau.de/publications/337993174 |
| [21] | Y. Sung, G. Yoon, J.-H. Bae, S. Chae, "TL–LEDarcNet: Transfer Learning Method for Low-Energy Series DC Arc-Fault Detection in Photovoltaic Systems," *IEEE Access*, 10:100725–100735, 2022 | 10.1109/ACCESS.2022.3208115 | V1 | doaj.org/article/f8acb1683e4f4f9e9af687863463b566 |
| [22] | Y. Wang, L. Hou, K. C. Paul, Y. Ban, C. Chen, T. Zhao, "ArcNet: Series AC Arc Fault Detection Based on Raw Current and Convolutional Neural Network," *IEEE Trans. Ind. Informat.*, 18(1):77–86, 2022 | 미확인 | V2 | researchgate.net/publication/350536091; dblp.org/pid/303/5658 |
| [23] | Choi 외, "Series-arc-fault diagnosis using feature fusion-based deep learning model," *ETRI J.*, 46(6):1061–1074, 2024 (제1저자 이름·공저자 미확인) | 10.4218/etrij.2023-0457 | V1(저자 일부) | onlinelibrary.wiley.com/doi/10.4218/etrij.2023-0457 |
| [24] | K. C. Paul 외, "Artificial Intelligence for DC Arc Fault Detection in Photovoltaic Systems," *IEEE Access*, 2025 (공저자 순서 재확인 필요) | 10.1109/ACCESS.2025.3572521 | V1(저자 일부) | doaj.org/article/9e9435d5f93840fa82ee38a532eb8da7 |
| [25] | K. C. Paul, J. Zhou, S.-E. Chen, T. Zhao, "PV Arc Fault Circuit Interrupter with Knowledge Distillation-Based Lightweight Convolutional Neural Network and SSCB Integration," *IEEE Trans. Power Electron.*, 40(12):18189–18201, 2025 | 미확인 | V2 | ieeexplore.ieee.org/document/11078896 (검색결과 URL) |
| [26] | K. C. Paul, C. Chen, Y. Wang, T. Zhao, "LArcNet: Lightweight Neural Network for Real-Time Series AC Arc Fault Detection," *IEEE Open J. Ind. Appl.*, 6:79–92, 2025 | 미확인 | V2 | ieeexplore.ieee.org/document/10816166 (검색결과 URL) |
| [27] | G. Ma, C. Yao, S. Xu, G. Ren, Z. Sun, S. Wu, "Real-Time Diagnosis of Multiple Open-Circuit Faults in ANPC Inverters Based on Lightweight Deployment of Edge 2D-CNN," *IEEE Trans. Ind. Electron.*, 2025 (early access) | 10.1109/TIE.2025.3549086 | V1(DOI는 검색결과 URL에만 노출) | api.openalex.org/works/doi:10.1109%2FTIE.2025.3549086 (링크로만 확인) |
| [28] | B. Jacob, S. Kligys, B. Chen, M. Zhu, M. Tang, A. Howard, H. Adam, D. Kalenichenko, "Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference," *Proc. IEEE/CVF CVPR*, pp. 2704–2713, 2018 | 10.1109/CVPR.2018.00286 | V1 | openaccess.thecvf.com/content_cvpr_2018/html/Jacob_... |
| [29] | G. Hinton, O. Vinyals, J. Dean, "Distilling the Knowledge in a Neural Network," arXiv, 2015 | arXiv:1503.02531 | V1 | arxiv.org/abs/1503.02531 |
| [30] | S. Han, H. Mao, W. J. Dally, "Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding," *ICLR*, 2016 | arXiv:1510.00149 | V1 | arxiv.org/abs/1510.00149 |
| [31] | S. Han, J. Pool, J. Tran, W. J. Dally, "Learning both Weights and Connections for Efficient Neural Networks," *NeurIPS*, 2015 | arXiv:1506.02626 | V1 | arxiv.org/abs/1506.02626 |
| [32] | R. David et al., "TensorFlow Lite Micro: Embedded Machine Learning for TinyML Systems," *Proc. MLSys*, 2021 | arXiv:2010.08678 | V1 | proceedings.mlsys.org/paper_files/paper/2021/hash/6c44dc73... |
| [33] | C. Banbury et al., "MLPerf Tiny Benchmark," *NeurIPS Datasets and Benchmarks Track*, 2021 | arXiv:2106.07597 | V1 | datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/da4fb5c6... |
| [34] | L. Lai, N. Suda, V. Chandra, "CMSIS-NN: Efficient Neural Network Kernels for Arm Cortex-M CPUs," arXiv, 2018 | arXiv:1801.06601 | V1 | arxiv.org/pdf/1801.06601 |
| [35] | S. S. Saha, S. S. Sandha, M. Srivastava, "Machine Learning for Microcontroller-Class Hardware: A Review," *IEEE Sensors J.*, 22(22):21362–21390, 2022 | 10.1109/JSEN.2022.3210773 | V1 | arxiv.org/pdf/2205.14550; par.nsf.gov/biblio/10411935 |
| [36] | P.-E. Novac, G. Boukli Hacene, A. Pegatoquet, B. Miramond, V. Gripon, "Quantization and Deployment of Deep Neural Networks on Microcontrollers," *Sensors*, 21:2984, 2021 | arXiv:2105.13331 (저널 DOI 독립 재확인 못함) | V1(arXiv) | arxiv.org/pdf/2105.13331 |
| [37] | W. Liao, "Real Time Bearing Fault Diagnosis Based on Convolutional Neural Network and STM32 Microcontroller," arXiv, 2023 | arXiv:2304.09100 | V1(arXiv, 동료심사 미확인) | arxiv.org/pdf/2304.09100 |

## 3. 연구실 논문 (계획서 13–14쪽 29편 중 보고서 인용분)

| # | 서지 | DOI | 등급 | 근거 |
|---|---|---|---|---|
| [L1] | H.-J. Park, J.-C. Kim, S. Kwak, "Deep learning-based estimation technique for capacitance and ESR of input capacitors in single-phase DC/AC converters," *J. Power Electron.*, 22(3):513–521, 2022 | 10.1007/s43236-021-00366-x | V1 | scholarworks.bwise.kr/cau/handle/2019.sw.cau/52713 |
| [L2] | H.-J. Park, S. Kwak, "DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs," *J. Electr. Eng. Technol.*, 18(3):1841–1850, 2023 | 10.1007/s42835-023-01424-z | V1 (Agent B1; Agent A는 DOI 미발견 → B1 결과 채택) | scholarworks.bwise.kr/cau/handle/2019.sw.cau/66390 |
| [L3] | H.-L. Dang, H.-J. Park, S. Kwak, S. Choi, "Evaluation of Single-Phase DC-AC Converters with Condition Monitoring Algorithm of Aluminum Electrolytic Capacitors using Artificial Learnings with Various Circuit Signals and Filtering Combinations," *J. Electr. Eng. Technol.*, 18(4):3021–3032, 2023 | 10.1007/s42835-023-01426-x | V1 | link.springer.com/10.1007/s42835-023-01426-x |
| [L4] | H.-L. Dang, S. Kwak, "Review of Health Monitoring Techniques for Capacitors Used in Power Electronics Converters," *Sensors*, 20(13):3740, 2020 | 10.3390/s20133740 | V1 | ncbi.nlm.nih.gov/pmc/articles/PMC7374397 |
| [L5] | H.-L. Dang, J. Kim, S. Kwak, S. Choi, "Series DC Arc Fault Detection Using Machine Learning Algorithms," *IEEE Access*, 9:133346–133364, 2021 | 10.1109/ACCESS.2021.3115512 | V1 | doaj.org/article/95a58cf5410746469291043df98e0483 |
| [L6] | J.-Y. Jeong, J.-C. Kim, S. Kwak, "DC Series Arc Diagnosis based on Deep-learning Algorithm with Frequency-domain Characteristics," *J. Power Electron.*, 21(12):1900–1909, 2021 | 10.1007/s43236-021-00332-7 | V1 | link.springer.com/article/10.1007/s43236-021-00332-7 |
| [L7] | H.-L. Dang, S. Kwak, S. Choi, "Identifying DC Series and Parallel Arcs based on Deep Learning Algorithms," *IEEE Access*, 10:76386–76400, 2022 | 10.1109/ACCESS.2022.3192517 | V1 | doaj.org/article/081d4b6a84fc4ebcbe5f1cbeaac4b5fc |
| [L8] | H.-L. Dang, S. Kwak, S. Choi, "DC Series Arc Failure Diagnosis using Artificial Machine Learning with Switching Frequency Component Elimination Technique," *IEEE Access*, 11:119584–119595, 2023 | 10.1109/ACCESS.2023.3327465 | V1 | doaj.org/article/e642b659cab94f02bc6358a3492c30c2 |
| [L9] | H.-L. Dang, S. Kwak, S. Choi, "Intelligence Detection of DC Parallel Arc Failure with Featuring from Different Domains," *IEEE Access*, 12:56062–56076, 2024 | 10.1109/ACCESS.2024.3389031 | V1 | scholarworks.bwise.kr/cau/handle/2019.sw.cau/73695 |
| [L10] | J.-Y. Jeong, S. Kwak, "Investigation of Loss Characteristics in SiC-MOSFET Based Three-Phase Converters Subject to Power Cycling and Short Circuit Aging," *J. Electr. Eng. Technol.*, 18(4):3049–3059, 2023 | 10.1007/s42835-023-01537-5 | V1 | scholarworks.bwise.kr/cau/handle/2019.sw.cau/67216 |
| [L11] | J. Kim, S. Kwak, S. Choi, "Impacts of SiC-MOSFET Gate Oxide Degradation on Three-Phase Voltage and Current Source Inverters," *Machines*, 10(12), 2022 | 미확인(URL 패턴상 10.3390/machines10121194로 보이나 유추) | V2 | mdpi.com/2075-1702/10/12/1194 |

### 3.1 연구실 논문 29편 전체 검증 결과 요약 (Agent A)

| 등급 | 편수 | 계획서 번호 |
|---|---:|---|
| V1 | 18 | 3, 4, 5, 6, 7, 8, 12, 13, 15, 16, 18, 20, 21, 22, 23(Agent B1이 DOI 확인해 상향), 26, 27, 29 |
| V1* | 4 | 1, 9, 14, 19 (제목·DOI는 Springer URL로 확인, 저자 미확인) |
| V2 | 1 | 25 |
| X | 6 | 2, 10, 11, 17, 24, 28 — **검색 2–3회로 찾지 못함. 부존재를 뜻하지 않음** |

### 3.2 계획서 기재와 검색결과의 차이

| 항목 | 계획서 | 검색결과 | 비고 |
|---|---|---|---|
| #21 게재월 | 2023.05 | JEET 18(4), 2023년 7월 | 온라인 선공개일 가능성 |
| #9, #14 연도 | 2023.05, 2022.03 | DOI가 각각 2022, 2021 부여 패턴 | 실제 게재 연월 미확인 |
| Best Paper Award 논문 제목 | "DC series arc diagnosis **on** deep learning algorithm with frequency domain characteristics" | #18의 실제 제목 "…**based on deep-learning** algorithm with **frequency-domain** characteristics" | 같은 논문으로 보임(추론). 수상 사실은 외부 미확인 |
| #10과 #13 | IEEE Access 2022.06 / 2022.07, 주제 유사 | #13만 확인 | 이중 기재 가능성(추론, 미확인) |
| SCIE 표기 | 29편 모두 SCIE | 외부 검증하지 않음 | — |

## 4. 특허 (계획서 12–13쪽)

11건(등록 3: 10-2906080, 10-2933289, 10-2659878 / 출원 8: 모두 2026년) — **모두 외부 미확인**(KIPRIS 접근 불가, 검색 한도 소진). 보고서에서는 "계획서 기재"로만 표기했다. 상세 목록은 `01_lab_research_analysis.md`와 scratchpad의 Agent A 결과에 있다.

## 5. 보류·제외 항목 (보고서 참고문헌에 넣지 않음)

| 항목 | 사유 |
|---|---|
| "Generative Physics-Informed Machine Learning Method for DC-Link Capacitance …", T. Qie et al., IEEE TIE 72(5):5461–5471, 2025 | **제목 후반부 미확인**(scholars.cityu.edu.hk 페이지에서 앞부분만 확인). 정확한 서지가 아니므로 본문에서 "검색된 후보"로만 언급 |
| "Hierarchical temporal memory-based predictive maintenance of DC-link capacitors in power electronic converters," Measurement: Energy, 2026 | 저자 미확인(X). 주제 관련성은 가장 높음 — 서지 보완 1순위 |
| "A Highly Accurate Generative Learning-Based DC-Link Capacitance Estimation Approach for Electrified Railway Traction Systems," IET Power Electron. (DOI 10.1049/pel2.70151) | 연도 미확인(V1†) — 인용 보류 |
| 커패시터 RUL: CNN-LSTM(Electronics 2025), LSTM(Proc. IMechE Part O 2023) | 이번 세션 미재검증(X) |
| Efficient-ArcNet, Chen 2024 adaptive arc, LTCNN-ADA, DA-DCGAN(DOI 미확인 V2지만 핵심 미선정) | 서지 미완 |
| Vu Le & X. Yao 2019 ensemble DC arc | 게재처 미확인(X) |
| 직렬 아크 관련 Sensors/Sci. Rep. 논문 다수(PMC 링크로만 확인) | 저자 미확인(X) |
| TI C2000 NPU 아크 검출 | 제조사 보도자료(논문 아님) |
| Kolar & Round 계열 DC-link 전류 실효값 근사식 | Agent G가 정성 비교에 사용했으나 원문 미확인 → 최종 보고서에서는 수식 인용 없이 "가정값 기반 정성 비교"로만 서술 |

## 6. 에이전트 간 교차검증에서 바로잡은 사항

| 항목 | 내용 | 조치 |
|---|---|---|
| PIML 논문 저자 | B2는 "Shuai Zhao, Huai Wang"(2인)으로, B1은 4인(Zhao, Peng, Zhang, Wang) + 권호·DOI로 기록 | B1의 V1 서지 채택([6]) |
| ArcNet 중복 | Agent C(C-01)와 Agent D(D-15)가 같은 논문 | [22] 하나로 통합 |
| 연구실 논문 판정 | Agent C는 L-02, L-03을 "연구실 추정"으로 표시 | Agent A가 저자(Dang, Kwak, Choi) 확인 → 연구실 논문으로 확정 |
| 잘못된 쪽수 | 한 검색 요약이 TinyML 베어링 논문을 "CVPR 2025 pp. 2704–2713"으로 표시 — Jacob et al.(CVPR 2018)의 쪽수가 섞인 오류 | Agent D가 감지해 폐기. 해당 논문은 보고서에 인용하지 않음 |
| 이전 조사 "(확인 필요)" | D6(→[L2]) 저자·DOI 확인, D3(→[5]) 저자 확인, D10 저자·DOI 확인(연도 미확인) | `papers/index.md` 갱신 대상 |

## 7. 제출 전 권장 확인 목록

1. V2 항목([5], [9], [10], [11], [13], [14], [15], [17], [22], [25], [26], [L11])의 DOI를 doi.org/출판사에서 확인.
2. [23], [24]의 전체 저자 목록 확인.
3. [27]은 DOI만 검색 링크로 확인 — 원문(장치·지연·메모리)을 읽은 뒤 인용 문장 재확인.
4. 연구실 X 6편(#2, #10, #11, #17, #24, #28)과 특허 11건을 연구실 내부 자료로 확인.
5. 보고서의 모든 "(초록)" 수준 서술은 본문 확인 후 수정 가능성 있음.

## 8. Red Team(Agent H) 검토 반영 기록

Agent H가 01–07을 원본 코드·계획서 PDF·에이전트 원보고서와 대조해 38건(Critical 1, Major 8, Minor 29)을 보고했다(`agent_reports/agentH_redteam.md`). 대조 결과 DOI/arXiv ID 37개, 코드 행 번호 35개 이상 범위, 파일 수·1-NN·파라미터 수·합성 실험 수치는 모두 일치했다. 반영 내용:

| 구분 | 내용 | 반영 위치 |
|---|---|---|
| Critical | 검증 대상 `train80.py`는 연구실 주 모델이 아니라 "첨부 CNN"(미제공)에서 PI·PI 보조 손실·I1/부하 임피던스 계산을 뺀 비교 스크립트(코드 17–24, 86, 1466, 3253행) → 결론 범위 명시, PIML 신규성 하향 | 07 요약·§3.5·§6, 04 머리말, 01 §7, 02 G2, 05 #3·TOP5 |
| Major | Q4 근거를 internal VALIDATION 수치에서 unseen 기준 비교로 교체 | 07 §7.4·Q4, 04 C5 |
| Major | 합성 데이터 설계(2-level, 블록 효과 없음, 노화=진폭 약 2배)가 진폭·RF raw에 유리함을 07에 명시 | 07 §7 머리말 |
| Major | 물리 해석 가정(2-level, Vdc 400 V, R 32 Ω, 미확인 근사식)과 NPC 반쪽 전압 측정 시 영향 명시 | 07 §7.6 |
| Major | 연구실 목록 밖 논문(필름 커패시터 AI, 데이터 vs 모델 기반 ESR 비교) 언급 | 07 §2.3·Q1, 01 §4 |
| Major | 주제상 가장 가까운 X 등급 후보(HTM, 2026) 언급 | 07 요약·Q6·TOP1, 05 TOP1 |
| Major | HIL을 실측으로 표기한 부분 정정 | 07 §3.6·§5, 02, 03 |
| Major | "성공 사례는 모두 하이브리드" 일반화 완화 | 07 Q1·Figure 4 표, 02, 03 |
| Major | 에이전트 원보고서의 경로 속 Windows 사용자명 마스킹 | agent_reports/agentE_code_audit.md |
| Minor | 집계·쪽번호(p.18→p.4)·연도(2021–2024)·등급(V1 18/V2 1)·CI 병기·LOCO fold 구조·이득 민감도 인과 완화·MLP 크기·부분 파일 판정(N/A)·참고문헌 미인용([9][24][L4] 본문 인용) 등 | 01–07 해당 위치 |
