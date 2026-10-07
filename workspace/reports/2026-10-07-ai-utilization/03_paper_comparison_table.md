# 03. 핵심 선행논문 비교표 (Table 2)

- 작성일: 2026-10-07
- 선정: 외부 후보 84편(중복 포함) 중 V1/V2 등급이면서 연구실 연구(커패시터·소자 진단, 아크, 운전조건 일반화, Edge AI)와 직접 관련된 **외부 16편 + 연구실 선행 2편([L1], [L2]) = 18편**. 연구실 논문은 비교 기준선으로만 넣었고 "연구실" 표시를 붙였다.
- 번호는 `06_reference_verification.md`의 최종 참고문헌 번호와 같다.
- **약어**: NC = 논문에서 확인되지 않음(초록·스니펫 수준). 이번 조사는 본문을 읽지 못했으므로 NC는 "그 논문이 하지 않았다"는 뜻이 아니다.
- 등급: V1(DOI까지 확인), V2(서지 확인, DOI 미확인).

---

## 1. 요약 비교표

| # | 논문 (제1저자, 연도, 게재처) | 등급 | 진단 대상 | 입력 신호 | AI 모델 | 일반화 시험 | 실험/시뮬 | Edge | 연구실 관련성 |
|---|---|---|---|---|---|---|---|---|---|
| [1] | Zhao S., 2021, IEEE TPEL | V1 | 리뷰(전력전자 AI 전반) | — | 전문가시스템·퍼지·메타휴리스틱·ML 분류 | — | — | NC | 서론·위치 설정 |
| [2] | Moradzadeh, 2022, IEEE TPEL | V1 | 리뷰(전력전자 고장진단) | — | ANN/ML/DL 데이터 마이닝 | — | — | NC | DL 진단 동향 근거 |
| [L1] | Park H.-J., 2022, JPE (연구실) | V1 | 단상 DC/AC 입력 커패시터 C·ESR | 커패시터 v·i FFT(2f, fsw) | DNN 회귀 | NC | 실험 | NC | 연구실 선행(회귀 계열) |
| [L2] | Park H.-J., 2023, JEET (연구실) | V1 | 3상 DC/AC DC 커패시터 C·ESR | 주파수 대역별 입력 | DNN·CNN·Simple RNN·LSTM 비교 | NC | NC | NC | 연구실 선행(모델 비교 계열) |
| [5] | Örüklü K., 2024/25, IEEE TIE | V2 | AC/DC/AC DC-link 커패시터 | DC-link 리플 기반(이전 조사: PSD) | ML(이전 조사: GPR) | NC(이전 조사에서 다중 조건 기록, 미재확인) | NC | NC | 리플 기반 ML CM 직접 비교 대상 |
| [6] | Zhao S., 2022, IEEE TPEL | V1 | Buck 컨버터 부품 파라미터 | NC | DNN + 동적 모델(PIML) | NC | NC | NC | 물리 결합 학습 방법론 |
| [7] | Chen W., 2020, IEEE TPEL | V1 | SiC MOSFET 고장 예지 | 소자 전압·전류·온도 추세 | 비지도 학습 | NC | NC | online 목표(구현 NC) | 소자 열화 AI |
| [8] | Kahraman C. L., 2024, IEEE Access | V1 | power MOSFET SoH·RUL | 열화(저항) 궤적 | RF 분류 + Bayesian Ridge 회귀 | NC | 가속 stress test(20개) | 계산 효율 주장 | 분류→조건부 회귀 2단계 |
| [10] | Liu Y., 2024, IEEE APEC | V2 | 3상 인버터 IGBT 개방고장 | 원 전류 신호 | 경량 CNN + 전이학습 | sim → HIL 시스템 이동 | 시뮬+HIL | "lightweight"(MCU NC) | sim 사전학습→실측 미세조정 |
| [12] | Li T., 2025, Sensors | V1 | 전력변환기 개방고장(다중 조건) | NC | Fractional order-conv encoder + lifelong | 조건 순차 추가 | NC | NC | 운전조건 추가 갱신 |
| [15] | Al-Kaf H. A. G., 2026, IEEE TII | V2 | 3L-NPC 인버터 고장 검출 | NC | CNN + Grad-CAM | NC | 시뮬+실험 | NC | NPC + CNN + XAI |
| [14] | Lee S. K., 2024, KBS | V2 | 전동기 고장(토크 변화) | 고정자 전류 | 자기지도(notch filter 증강) | 토크 조건 간 분포 차이 | 데이터셋(세부 NC) | NC | 조건 불변 표현 학습 |
| [18] | Jiang R., 2023, IEEE Sensors J. | V1 | AC series arc | 전류(진동 성분 단순화) | 1D-CNN | **미관측 부하 9종** | 학습: RLC 아크 모델 합성 | NC | 부하 범용 아크 |
| [19] | Jiang R., 2023, IEEE TII | V1 | series arc(AC 추정) | 전류 시간·주파수 coupling 특징 | ML 분류기(종류 NC) | **단일 부하 학습→미관측 다중부하** | 실험 | NC | 도메인 특징 기반 일반화 |
| [20] | Mao Y., 2025, IEEE Access | V1 | DC series arc | NC(저샘플링) | AI vs rule-based 비교 | 조건 변화 적응성 비교 | 문헌+실험 | 저자원 장치 목표 | "왜 AI인가" 근거 |
| [21] | Sung Y., 2022, IEEE Access | V1 | PV 저에너지 DC series arc | 센싱 전류 | 1-layer LSTM + 경량 1D-CNN, 전이학습 | NC | NC | **SBC 실시간** | 경량 DC 아크 |
| [25] | Paul K. C., 2025, IEEE TPEL | V2 | PV DC arc + 차단기 | NC | KD 경량 CNN(5.04k 파라미터, 90 kB) | 여러 PV 운전 상황 | 하드웨어 프로토타입 | **STM32H743, 19 ms(5-cycle 확인 95 ms)** | MCU 실구현 기준 |
| [27] | Ma G., 2025, IEEE TIE | V1 | ANPC 인버터 다중 개방고장 | NC | 경량 Edge 2D-CNN | NC | NC | Edge 배포(장치 NC) | NPC 계열 Edge 진단 |

---

## 2. 논문별 상세 비교 (사용자 요청 16개 항목)

### [1] An Overview of Artificial Intelligence Applications for Power Electronics
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 | Shuai Zhao, Frede Blaabjerg, Huai Wang / 2021 / IEEE Trans. Power Electron. 36(4):4633–4658 |
| DOI | 10.1109/TPEL.2020.3024914 |
| 진단 대상·입력·모델 | 리뷰: 설계·제어·유지보수 단계의 AI(전문가시스템, 퍼지, 메타휴리스틱, ML) |
| 학습 방식·데이터·운전조건 | 500편 이상 문헌 분류(초록) |
| 성능·일반화·실험·severity·Edge | 해당 없음 / NC |
| 연구실 관련성 | 연구실의 정상/노화 분류는 "유지보수 × 분류" 범주(해석) |
| 한계 | 2020년까지 문헌. 진단 세부 비교·일반화 쟁점 포함 여부 NC |

### [2] Data Mining Applications to Fault Diagnosis in Power Electronic Systems: A Systematic Review
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 | A. Moradzadeh, B. Mohammadi-Ivatloo, K. Pourhossein, A. Anvari-Moghaddam / 2022 / IEEE TPEL 37(5):6026–6050 |
| DOI | 10.1109/TPEL.2021.3131293 |
| 내용 | ANN·ML·DL 기반 데이터 마이닝 고장진단 리뷰. DL이 특징을 스스로 추출해 더 효과적이라는 결론(스니펫) |
| 일반화·split 관행 | NC |
| 연구실 관련성 | 서론의 동향 근거. 단 "DL이 우수"는 리뷰의 결론이며 연구실 데이터에서 그대로 성립한다는 근거는 아님 |
| 한계 | 2021년까지 문헌, DA/DG·XAI 포함 여부 NC |

### [L1] Deep learning-based estimation technique for capacitance and ESR of input capacitors in single-phase DC/AC converters (연구실)
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 / DOI | Hye-Jin Park, Jae-Chang Kim, Sangshin Kwak / 2022 / J. Power Electron. 22(3):513–521 / 10.1007/s43236-021-00366-x |
| 진단 대상 | 단상 DC/AC 컨버터 입력 커패시터 C, ESR(연속값) |
| 입력 신호 | 실험 커패시터 전압·전류의 FFT 성분(2배 기본파, 스위칭 주파수 성분 우세), 입력 조합 11종 |
| AI 모델 / 학습 | DNN / 지도 회귀 |
| 데이터 규모 / 운전조건 | NC / NC |
| 성능 | 정량 NC. C는 중간주파 성분을 함께 쓸 때, ESR은 중간주파의 전압·전류를 모두 쓸 때 우수(스니펫) |
| 일반화 시험 | NC |
| 실험/시뮬 | 실험 데이터 |
| severity | 연속값 추정이므로 노화 정도를 다룸(해석) |
| Edge | NC |
| 관련성 / 한계 | 현재 분류 코드와 같은 연구실의 회귀 계열 선행. 커패시터 전류 측정이 필요한 구성으로 보임(해석) |

### [L2] DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter Using Deep Learning Methods with Different Frequency Band Inputs (연구실)
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 / DOI | H.-J. Park, Sangshin Kwak / 2023 / J. Electr. Eng. Technol. 18(3):1841–1850 / 10.1007/s42835-023-01424-z |
| 진단 대상 | 3상 DC/AC DC 커패시터 C, ESR |
| 입력 신호 | 서로 다른 주파수 대역 입력(저주파 → C, 중간주파 → ESR 지배) |
| AI 모델 | DNN, CNN, Simple RNN, LSTM 비교 |
| 성능 | 특정 성분 입력 → DNN 우수, 넓은 대역 입력 → CNN 최고(스니펫) |
| 데이터·운전조건·일반화·실험 여부·Edge | NC |
| 관련성 | 현재 코드의 4모델 비교와 같은 구조. "입력 표현이 모델 우열을 바꾼다"는 연구실 자체 근거 |
| 한계 | 고전 ML(RF 등) 비교 NC, 일반화 NC |

### [5] Machine learning-based condition monitoring for dc-link capacitors in ac/dc/ac converters
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 / DOI | K. Örüklü, Ş. Ağalar / 2024(참고문헌 표기; 권호는 2025년 권) / IEEE Trans. Ind. Electron. 72(4):4227–4237 / 미확인 |
| 진단 대상 | AC/DC/AC 컨버터 DC-link 커패시터 |
| 입력·모델 | 이전 조사(2026-09-29) 기록: DC-link 리플 PSD + GPR. **이번 세션 미재확인** |
| 운전조건·일반화 | 이전 조사 기록: 다중 운전조건 실험. 이번 세션 미재확인 → 본 보고서에서는 NC로 취급 |
| 관련성 | DC-link 리플 기반 ML CM의 가장 가까운 외부 비교 대상(서지 보완 필요) |
| 한계 | DOI·세부 미확인 |

### [6] Parameter Estimation of Power Electronic Converters With Physics-Informed Machine Learning
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 / DOI | Shuai Zhao, Yingzhou Peng, Yi Zhang, Huai Wang / 2022 / IEEE TPEL 37(10):11567–11578 / 10.1109/TPEL.2022.3176468 |
| 진단 대상 | 컨버터 부품 파라미터(사례: Buck) |
| 모델·학습 | DNN + 컨버터 동적 모델 결합 PIML |
| 데이터·운전조건·성능·일반화·실험 | NC. 순수 데이터 기반 방법의 데이터·정확도·강건성 문제를 완화한다고 주장 |
| 관련성 | DC-link 리플 물리식(ESR·i_C + ∫i_C/C)을 손실·구조에 넣는 연구의 방법론 근거 |
| 한계 | Buck 사례, 인버터 DC-link 적용 NC |

### [7] Data-Driven Approach for Fault Prognosis of SiC MOSFETs
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 / DOI | Weiqiang Chen, Lingyi Zhang, Krishna Pattipati, Ali M. Bazzi, Shailesh Joshi, Ercan M. Dede / 2020 / IEEE TPEL 35(4) / 10.1109/TPEL.2019.2936850 |
| 진단 대상 / 입력 | SiC MOSFET 고장 예지 / 소자 전기·열 특성 추세 |
| 모델·학습 | 비지도 학습(알고리즘 NC) |
| 성능·데이터·운전조건·일반화 | NC |
| Edge | online 구현 목표(실구현 NC) |
| 관련성 | 연구실 SiC 열화 연구[L10][L11]의 AI 확장 참고. 라벨 부족 상황의 비지도 접근 |
| 한계 | 세부 대부분 NC |

### [8] Machine Learning Pipeline for Power Electronics State of Health Assessment and Remaining Useful Life Prediction
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 / DOI | C. L. Kahraman, D. Roman, L. Kirschbaum, D. Flynn, J. Swingler / 2024 / IEEE Access 12:136727–136746 / 10.1109/ACCESS.2024.3460177 |
| 진단 대상 / 입력 | power MOSFET SoH(healthy/pre-failure)·RUL / 열화 궤적 |
| 모델·학습 | RF 분류 → pre-failure일 때만 Bayesian Ridge 회귀 |
| 데이터 | power MOSFET 20개 stress test |
| 성능 | 분류 평균 정확도 80%, RUL RMSPE 1.25% |
| 일반화 | 소자 단위 split 여부 NC |
| severity | healthy/pre-failure + RUL |
| Edge | "computationally efficient" 주장, 구현 NC |
| 관련성 | 이진 분류 → 노화 정도 추정 확장 설계 참고. 표본(개체) 수가 결론 단위라는 점의 예 |
| 한계 | 단품 시험, 표본 20개 |

### [10] A Transferable Deep Learning Network for IGBT Open-circuit Fault Diagnosis in Three-phase Inverters
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 / DOI | Yongjie Liu, Ariya Sangwongwanich, Yibin Zhang, Shuyu Ou, Huai Wang / 2024 / IEEE APEC 2024 / 미확인 |
| 진단 대상 / 입력 | 3상 인버터 IGBT 개방고장 / 원 전류 신호 |
| 모델·학습 | 경량 CNN, 시뮬레이션 사전학습 → HIL 소량 미세조정 |
| 성능 | 시뮬레이션 99.52%, HIL 98.30% |
| 일반화 | 시스템 간 이동(sim→HIL) 시험. 미관측 운전조건 시험·split 방식 NC |
| 실험/시뮬 | 시뮬레이션 + HIL(실 전력 하드웨어 NC) |
| Edge | "lightweight"(MCU NC) |
| 관련성 | C/ESR을 스윕한 시뮬레이션으로 사전학습 후 실측 소량으로 미세조정하는 경로 |
| 한계 | 학회 논문, target 라벨 필요 |

### [12] Lifelong Learning-Enabled Fractional Order-Convolutional Encoder Model for Open-Circuit Fault Diagnosis of Power Converters Under Multi-Conditions
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 / DOI | Tao Li, Enyu Wang, Jun Yang / 2025 / Sensors 25(6):1884 / 10.3390/s25061884 |
| 진단 대상 | 모터 구동 전력변환기 개방고장(다중 운전조건) |
| 모델·학습 | 합성곱 + 인코더, fractional order 학습, 다단계 lifelong learning(catastrophic forgetting 억제) |
| 데이터·성능·split | NC(오픈액세스라 본문 확인 가능) |
| 일반화 | "운전조건이 바뀌면 정확도가 떨어진다"는 문제 정의, 조건 순차 추가 평가로 보임(NC) |
| 관련성 | 현장에서 운전조건이 추가될 때의 모델 갱신 시나리오 |
| 한계 | zero-shot 일반화와는 다른 접근, 새 조건 라벨 필요 가능성 |

### [15] Explainable Deep Learning Fault Detection Method for Multilevel Inverters
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 / DOI | Hasan Ali Gamal Al-Kaf, Samer Saleh Hakami, Kyo-Beum Lee / 2026 / IEEE Trans. Ind. Informat. 22(1):579–590 / 미확인 |
| 진단 대상 | 3L-NPC 인버터 고장 검출·유형 분류 |
| 모델 | CNN + Grad-CAM(사후 설명) |
| 실험/시뮬 | 시뮬레이션 + 실험 |
| 입력·데이터·운전조건·성능·일반화 | NC("high classification accuracy") |
| 관련성 | 토폴로지(NPC)·모델(CNN) 동일. 리플 CNN의 shortcut 점검 도구로 Grad-CAM 활용 근거 |
| 한계 | 정성적 설명, faithfulness 정량 평가 NC |

### [14] Self-supervised feature learning for motor fault diagnosis under various torque conditions
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 / DOI | Sang Kyung Lee, Hyeongmin Kim, Minseok Chae, Hye Jun Oh, Heonjun Yoon, Byeng D. Youn / 2024 / Knowledge-Based Systems / 미확인 |
| 진단 대상 / 입력 | 전동기 고장(유도전동기, PMSM 데이터셋) / 고정자 전류(순시 진폭) |
| 모델·학습 | 다채널 자기지도 학습, notch filter 증강으로 토크 불변 특징 |
| 운전조건 | 다양한 토크 조건 |
| 성능·split | NC |
| 관련성 | f0·fsw 성분을 notch로 지우는 증강 → 리플의 조건 불변 표현 학습에 응용 가능(해석) |
| 한계 | 전력전자 부품 노화가 아님 |

### [18] AC series arc fault detection based on RLC arc model and convolutional neural network
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 / DOI | Run Jiang, Yilong Wang, Xiaoqing Gao, Guanghai Bao, Qiteng Hong, Campbell Booth / 2023 / IEEE Sensors J. 23(13):14618–14627 / 10.1109/JSEN.2023.3280009 |
| 진단 대상 / 입력 | AC series arc / 전류(진동 신호 유형으로 단순화) |
| 모델·학습 | 1D-CNN, 고주파 RLC 아크 모델로 학습 데이터 생성(부하 유형·위상각 등 조절) |
| 운전조건·일반화 | **미관측 부하 9종 시험** |
| 성능 | 평균 검출 정확도 99.33% |
| 실험/시뮬 | 학습: 모델 합성. 시험 데이터 실측 여부 NC |
| Edge·severity | NC |
| 관련성 | 물리 모델 기반 합성 + DL로 부하 일반화 — 연구실 MATLAB 시뮬레이션 역량과 결합 가능 |
| 한계 | AC series 한정, sim-to-real 정량 분석 NC |

### [19] Machine learning approach to detect arc faults based on regular coupling features
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 / DOI | Run Jiang, Guanghai Bao, Qiteng Hong, Campbell Booth / 2023 / IEEE TII 19(3):2761–2771 / 10.1109/TII.2022.3153333 |
| 입력 | 전류의 regular coupling features(시간영역 IFA·CMA, 주파수영역 MFA) |
| 모델 | ML 분류기(종류 NC) |
| 학습·일반화 | **단일 부하 회로로 학습 → 미관측 다중부하 회로 시험** |
| 성능 | 일반화·정확도가 크게 향상(수치 NC) |
| 실험/시뮬 | 실험 |
| 관련성 | 도메인 지식 특징이 일반화를 이끈 사례 — 연구실 시간·주파수 하이브리드 특징 연구와 비교 기준 |
| 한계 | 수치·분류기 NC, DC 적용 NC |

### [20] Why AI: A Comparative Study for Detection Methods in DC Series Arc Fault
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 / DOI | Y. Mao, S. Safa, G. Smith, L. Wurth, R. Weiss, J. Hagemeyer / 2025 / IEEE Access / 10.1109/ACCESS.2025.3548309 |
| 진단 대상 | DC series arc |
| 내용 | AI 기반 vs rule-based 검출 비교. AI가 변화 조건에 더 적응적이며, 도메인 지식 기반 특징추출과 결합 시 성능 향상(초록) |
| 운전조건 | "varying conditions"(세부 NC) |
| Edge | 저샘플링·저연산 장치 대상 |
| 관련성 | Q1("AI가 임계값 방식보다 무엇이 나은가")의 외부 근거 |
| 한계 | 모델·데이터·수치 NC, AC 미포함 |

### [21] TL–LEDarcNet: Transfer Learning Method for Low-Energy Series DC Arc-Fault Detection in Photovoltaic Systems
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 / DOI | Yoondong Sung, Gihwan Yoon, Ji-Hoon Bae, Suyong Chae / 2022 / IEEE Access 10:100725–100735 / 10.1109/ACCESS.2022.3208115 |
| 진단 대상 / 입력 | PV 저에너지 series DC arc / 센싱 전류 |
| 모델·학습 | 1-layer LSTM + 경량 1D-CNN, 전이학습 기반 2단계 학습 |
| 성능 | 정확도 95.8% |
| 일반화 | NC |
| Edge | single-board computer 실시간 동작 |
| 관련성 | 국내 외부 그룹의 경량 DC 아크 사례 |
| 한계 | SBC는 MCU보다 자원이 큼, 부하 일반화 NC |

### [25] PV Arc Fault Circuit Interrupter with Knowledge Distillation-Based Lightweight Convolutional Neural Network and SSCB Integration
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 / DOI | Kamal Chandra Paul, Jiale Zhou, Shen-En Chen, Tiefu Zhao / 2025 / IEEE TPEL 40(12):18189–18201 / 미확인 |
| 진단 대상 | PV DC arc 검출 + 고체 차단기 차단 |
| 모델·학습 | KD 기반 경량 CNN(PArcNet), 파라미터 5.04k, 메모리 90 kB |
| 운전조건 | 인버터 기동, 음영, 부하 변동 등 |
| 성능 | 정확도 98% 이상 |
| Edge | **STM32H743ZI2, 검출+차단 최소 19 ms, 5-cycle 확인 시 95 ms** |
| 실험/시뮬 | 하드웨어 프로토타입 |
| 관련성 | 연구실 "저가 MCU 온보드 AI"의 외부 기준점. 연속 N회 확인 판정 로직의 근거 |
| 한계 | DOI 미확인, 미관측 부하 split 방식 NC |

### [27] Real-Time Diagnosis of Multiple Open-Circuit Faults in ANPC Inverters Based on Lightweight Deployment of Edge 2D-CNN
| 항목 | 내용 |
|---|---|
| 저자 / 연도 / 게재처 / DOI | G. Ma, C. Yao, S. Xu, G. Ren, Z. Sun, S. Wu / 2025 / IEEE TIE(early access) / 10.1109/TIE.2025.3549086 |
| 진단 대상 | ANPC 인버터 다중 개방고장 |
| 모델 | 경량 Edge 2D-CNN |
| 입력·장치·지연·메모리·일반화 | NC — **인용 전 원문 확인 필요** |
| 관련성 | NPC 계열 토폴로지 Edge CNN 진단의 최신 사례 |
| 한계 | 세부 미확인 |

---

## 3. 비교에서 도출되는 관찰 (근거 중심)

1. **평가 프로토콜이 공개되지 않은 고정확도 보고가 많다.** 99% 이상을 보고한 논문 중 미관측 부하/조건 시험이 초록에 명시된 것은 [18]뿐이다. 따라서 연구실 결과를 이 수치들과 단순 비교하는 것은 근거가 약하다.
2. **일반화에 성공한 사례는 하이브리드다.** [18](물리 모델 합성), [19](도메인 특징), [20](도메인 특징 결합 시 향상).
3. **커패시터 AI 논문은 회귀가 주류**([L1], [L2], [5])이며, 연구실 현재 코드(이진 분류)는 노화 정도 정보를 쓰지 않는다.
4. **Edge 실구현 보고는 아크 쪽에 집중**([25], [21])되어 있고, 커패시터 노화의 MCU 구현은 이번 범위에서 확인되지 않았다.
5. **NPC 계열 AI 진단은 개방고장(이산 사건)이 대상**([15], [27])이며, NPC DC-link 커패시터 노화 AI는 이번 범위에서 확인되지 않았다.
