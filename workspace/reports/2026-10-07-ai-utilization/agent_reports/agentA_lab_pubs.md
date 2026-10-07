# Agent A — 연구실 논문·특허 실재성 검증 (중앙대 전력전자연구실, 곽상신 교수)

- 원자료: 창업계획서 PDF 12~15쪽 (특허 11건, Best Paper Award 1건, 논문 29편). 개인정보(연락처·학생 정보)는 옮기지 않음.
- 검증 방법: WebSearch 결과(제목/URL/스니펫)만 사용. Crossref·doi.org·IEEE Xplore 등은 egress 정책으로 직접 열람 불가.
- **제약(중요)**: 검증 도중 WebSearch 턴 한도(200회, 모든 에이전트가 공유)가 소진되었다. 그래서 X 등급 6편은 1~3회만 검색했고 특허는 외부 검색을 하지 못했다. 사용자가 후속 요청을 보내면 남은 항목을 이어서 검색할 수 있다.
- 작성일: 2026-10-07

## 등급 기준
| 등급 | 의미 |
|---|---|
| V1 | 출판사·색인 페이지(scholarworks.bwise.kr = 중앙대 기관 리포지토리, doaj, mdpi, springer, PMC, citedrive 등)의 스니펫·URL에서 제목, 저널, 연도가 일치하고 DOI 문자열도 확인됨 |
| V1* | 출판사 URL(link.springer.com/article/10.1007/…)에서 **제목과 DOI는 확인**됨. 그러나 저널명은 DOI prefix로만 판정했고(s42835 = J. Electr. Eng. Technol.(JEET), s43236 = J. Power Electron.(JPE). 같은 prefix를 가진 다른 논문들이 각각 JEET·JPE로 확인되어 판정 근거로 씀), 연도는 스니펫에 직접 나오지 않은 경우가 있음. V1과 V2 사이로 본다 |
| V2 | 제목, 저널, 연도는 확인했으나 DOI 문자열은 확인하지 못함 |
| V3 | 일부만 일치(제목 유사, 연도 상이 등) |
| X | 찾지 못함 |

---

## (a) 논문 29편 검증표

※ 저자는 스니펫에 나온 것만 적었다. 진단대상, 입력신호, AI 모델, 데이터 칸도 스니펫에 있는 내용만 적었고, 스니펫에 없으면 "확인되지 않음"으로 표기했다.
※ PDF의 "SCIE" 표기는 외부에서 검증하지 않았다(범위 밖).

| # | PDF 기재 제목 | PDF 기재 저널/연월 | 확인된 저자 | 확인된 저널·권호·연도 | DOI | 등급 | 근거 URL | 진단대상 | 입력신호 | AI 모델 | 실험/시뮬 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Dual-Band-Based Moving Z-Score Algorithm for Detecting Series AC Arc Faults | J. Electrical Engineering & Technology / 2025.03 | 확인되지 않음 | (JEET, prefix로 판정) 2025년 3월 게재로 스니펫에 표기. 권호 미확인 | 10.1007/s42835-025-02203-8 (URL) | V1* | https://link.springer.com/article/10.1007/s42835-025-02203-8 | Series AC arc | FFT dual band 성분에서 계산한 moving Z-score (신호명 미기재) | 스니펫상 AI 언급 없음. 통계 기반 임계값 방식("simplifies the process of setting the threshold value") | 실험: 8종 masking load(저항, 형광등, 할로겐, 압축기, SMPS, 드릴, 청소기, 디머) × 4개 회로 구성 = 32개 실험 조건 |
| 2 | DC Arc Failure Detection based on Division of Time and Frequency Components using Intelligence Models | J. Electrical Engineering & Technology / 2025.01 | — | — | 미확인 | X | — (3회 검색, 유사 주제인 #6만 검색됨) | 확인되지 않음 | 확인되지 않음 | 확인되지 않음 | 확인되지 않음 |
| 3 | Intelligence Detection of DC Parallel Arc Failure with Featuring from Different Domains | IEEE Access / 2024.04 | Hoang-Long Dang, Sangshin Kwak, Seungdeog Choi | IEEE Access, Vol.12, pp.56062–56076, 2024 | 10.1109/ACCESS.2024.3389031 | V1 | https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/73695 , https://doaj.org/article/0f112960604045da8446d835933f1a7e | DC parallel arc | Source current 신호를 여러 domain에서 분석해 얻은 특징 | "artificial learning models"(종류 미기재) | 확인되지 않음 |
| 4 | Various Feature-Based Series Direct Current Arc Fault Detection Methods Using Intelligence Learning Models and Diverse Domain Exclusion Techniques | Machines / 2024.04 | Hoang-Long Dang, Sangshin Kwak, Seungdeog Choi | Machines, Vol.12, No.4, 235, 2024년 4월 | 10.3390/machines12040235 | V1 | https://www.citedrive.com/en/discovery/various-feature-based-series-direct-current-arc-fault-detection-methods-using-intelligence-learning-models-and-diverse-domain-exclusion-techniques/ , https://doaj.org/article/d4d0b700ac0f4134910e761f3f74e1cf | DC series arc | 특징: square average, average, median, RMS, peak-to-peak, variance. 원신호명은 확인되지 않음 | "intelligence learning models"(종류 미기재) | 확인되지 않음 |
| 5 | Advanced Learning Technique Based on Feature Differences of Moving Intervals for Detecting DC Series Arc Failures | Machines / 2024.02 | Hoang-Long Dang, Sangshin Kwak, Seungdeog Choi | Machines, Vol.12, No.3, 167, 2024년 2월 | 10.3390/machines12030167 | V1 | https://www2.mdpi.com/2075-1702/12/3/167 , https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/73304 | DC series arc (DC microgrid) | Moving interval 간 특징 차분(원신호명은 확인되지 않음) | "advanced learning techniques (ALTs)"(종류 미기재) | 확인되지 않음 |
| 6 | DC Series Arc Fault Diagnosis Scheme Based on Hybrid Time and Frequency Features Using Artificial Learning Models | Machines / 2024.02 | Hoang-Long Dang, Sangshin Kwak, Seungdeog Choi | Machines, Vol.12, No.2, 102, 2024-02-01 게재 | 10.3390/machines12020102 | V1 | https://www.mdpi.com/2075-1702/12/2/102 , https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/72999 | DC series arc | 전원측(power supply-side) 신호의 시간·주파수 특징. 시간영역 Three-Sigma Rule 필터링과 주파수영역 스위칭 노이즈 제거 후 추출 | "artificial learning models"(종류 미기재) | 확인되지 않음 |
| 7 | DC Series Arc Failure Diagnosis using Artificial Machine Learning with Switching Frequency Component Elimination Technique | IEEE Access / 2023.11 | Hoang-Long Dang, Sangshin Kwak, Seungdeog Choi | IEEE Access, Vol.11, pp.119584–119595, 2023 | 10.1109/ACCESS.2023.3327465 | V1 | https://doaj.org/article/e642b659cab94f02bc6358a3492c30c2 | DC series arc | 스위칭 노이즈를 제거한 전처리 신호(원신호명은 확인되지 않음). 모든 스위칭 주파수 범위에서 유효하다고 기술 | "artificial machine learning algorithms"(종류 미기재) | 확인되지 않음 |
| 8 | Empirical Filtering based Artificial Intelligence Learning Diagnosis of Series DC Arc Faults in Time Domains | Machines / 2023.10 | Hoang-Long Dang, Sangshin Kwak, Seungdeog Choi | Machines, Vol.11, No.10, 968, 2023년 10월 | 10.3390/machines11100968 | V1 | https://www.mdpi.com/2075-1702/11/10/968 , https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/68691 | DC series arc | 전류 센서 신호 하나만 사용. empirical rule 기반 전류 필터링 | "intelligent machine learning techniques"(종류 미기재) | 확인되지 않음 |
| 9 | Analysis and Diagnosis Scheme of Parallel Arc Failure in DC Power Lines | J. Electrical Engineering & Technology / 2023.05 | 확인되지 않음 | (JEET, prefix로 판정) 연도·권호는 스니펫에 없음 | 10.1007/s42835-022-01273-2 (URL) | V1* | https://link.springer.com/article/10.1007/s42835-022-01273-2 | DC parallel arc(제목 기준) | 확인되지 않음 | 확인되지 않음 | 확인되지 않음 |
| 10 | Detection and Identification Technique for Series and Parallel DC Arc Faults | IEEE Access / 2022.06 | — | — | 미확인 | X | — (3회 검색에서 #12, #13만 검색됨) | 확인되지 않음 | 확인되지 않음 | 확인되지 않음 | 확인되지 않음 |
| 11 | Standard Deviation Based Series DC Arc Detection Method for Voltage Source Converters | J. Power Electronics / 2022.07 | — | — | 미확인 | X | — (2회 검색) | 확인되지 않음 | 확인되지 않음 | 확인되지 않음 | 확인되지 않음 |
| 12 | Parallel DC Arc Failure Detecting Methods based on Artificial Intelligent Techniques | IEEE Access / 2022.03 | Hoang-Long Dang, Sangshin Kwak, Seungdeog Choi | IEEE Access, Vol.10, pp.26058–26067, 2022 | 10.1109/access.2022.3157298 | V1 | https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/55667 , https://doaj.org/article/1198775d2d124d26bea31da8b78b4976 | DC parallel arc | 전류의 시간·주파수 영역 분석, Fourier 분석으로 추출한 특징 | "eight learning techniques"(종류 미기재) | 확인되지 않음 |
| 13 | Identifying DC Series and Parallel Arcs based on Deep Learning Algorithms | IEEE Access / 2022.07 | Hoang-Long Dang, Sangshin Kwak, Seungdeog Choi | IEEE Access, Vol.10, pp.76386–76400, 2022 | 10.1109/ACCESS.2022.3192517 | V1 | https://doaj.org/article/081d4b6a84fc4ebcbe5f1cbeaac4b5fc | DC series + parallel arc 구분 | 부하 전류와 전압(load current and voltage)의 시간·주파수 영역 데이터 | "eight learning techniques"(종류 미기재. 제목상 deep learning) | 확인되지 않음 |
| 14 | Detection Algorithms of Parallel Arc Fault on AC Power Lines Based on Deep Learning Techniques | J. Electrical Engineering & Technology / 2022.03 | 확인되지 않음 | (JEET, prefix로 판정) 연도·권호는 스니펫에 없음 | 10.1007/s42835-021-00976-2 (URL) | V1* | https://link.springer.com/article/10.1007/s42835-021-00976-2 | Parallel AC arc | 요약 스니펫에 "frequency- and time-domain current characteristics"가 나오나 **이 논문의 것인지 불확실** | 요약 스니펫에 "neural networks 비교"가 나오나 귀속 불확실 | 확인되지 않음 |
| 15 | Different Domains based Machine and Deep Learning Diagnosis for DC Series Arc Failure | IEEE Access / 2021.12 | Hoang-Long Dang, Sangshin Kwak, Seungdeog Choi | IEEE Access, Vol.9, pp.166249–166261, 2021 | 10.1109/ACCESS.2021.3135526 | V1 | https://doaj.org/article/fbc77fdeb5a94f7cb3793853f284a81f | DC series arc | 시간·주파수 영역 특징 6종(feature parameters)의 조합 | "various AI algorithms"(제목상 ML+DL, 세부 종류 미기재) | 확인되지 않음 |
| 16 | Series DC Arc Fault Detection Using Machine Learning Algorithms | IEEE Access / 2021.09 | Hoang-Long Dang, Jaechang Kim, Sangshin Kwak, Seungdeog Choi | IEEE Access, Vol.9, pp.133346–133364, 2021년 9월 | 10.1109/ACCESS.2021.3115512 | V1 | https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/50141 , https://doaj.org/article/95a58cf5410746469291043df98e0483 | DC series arc (전력전자 부하 포함 여러 부하) | 전류의 시간영역 파라미터 5종: average, median, variance, RMS, max–min distance | "various machine learning algorithms" 비교(종류 미기재) | 확인되지 않음 |
| 17 | DC Series Arc Detection Algorithm Based on Adaptive Moving Average Technique | IEEE Access / 2021.07 | — | — | 미확인 | X | — (3회 검색) | 확인되지 않음 | 확인되지 않음 | 확인되지 않음 | 확인되지 않음 |
| 18 | DC Series Arc Diagnosis based on Deep-learning Algorithm with Frequency-domain Characteristics | J. Power Electronics / 2021.12 | Jae-Yoon Jeong, Jae-Chang Kim, Sangshin Kwak | J. Power Electronics, Vol.21, No.12, pp.1900–1909, 2021년 12월 | 10.1007/s43236-021-00332-7 | V1 | https://link.springer.com/article/10.1007/s43236-021-00332-7 , https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/51657 | DC series arc (부하: 3상 PWM 인버터, 3상 MPC 인버터) | 전류 FFT 결과의 전 주파수 대역 | DNN | 요약 스니펫에 "Experimental results … 99.63%"가 있으나 이 논문에 귀속되는지는 불확실. 전류 크기와 스위칭 주파수를 바꿔가며 시험했다고 기술 |
| 19 | Deep Learning-based Series AC Arc Detection Algorithms | J. Power Electronics / 2021.10 | 확인되지 않음 | J. Power Electronics(스니펫 표기, prefix s43236과 일치). 연도·권호는 스니펫에 없음 | 10.1007/s43236-021-00299-5 (URL) | V1* | https://link.springer.com/article/10.1007/s43236-021-00299-5 | Series AC arc | 아크 전압과 전류의 주파수·시간 영역 특징: zero-crossing period, frequency average, instantaneous frequency, entropy, FFT 조합 | 여러 artificial neural networks 비교. 학습 샘플 수에 따른 검출률 변화도 분석 | 확인되지 않음 |
| 20 | Frequency-Domain Characteristics of Series DC Arcs in Photovoltaic Systems with Voltage-Source Inverters | Applied Sciences / 2020.11 | Jae-Chang Kim, Sang-Shin Kwak | Applied Sciences, Vol.10, No.22, 8042, 2020년 11월 | 10.3390/app10228042 | V1 | https://www.mdpi.com/2076-3417/10/22/8042 , https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/48036 | PV 시스템(VSI)의 series DC arc 주파수 특성 분석 | 아크 전류의 주파수 성분. 아크 발생 후 5–40 kHz 성분 증가 | 스니펫상 AI 언급 없음(특성 분석 논문) | 확인되지 않음 |
| 21 | Investigation of Loss Characteristics in SiC-MOSFET Based Three-Phase Converters Subject to Power Cycling and Short Circuit Aging | J. Electrical Engineering & Technology / 2023.05 | Jae-Yoon Jeong, Sangshin Kwak | JEET, Vol.18, No.4, pp.3049–3059, 2023년 7월 | 10.1007/s42835-023-01537-5 | V1 (월 상이) | https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/67216 | SiC-MOSFET 노화(Power Cycling, Short Circuit)가 3상 컨버터 손실·효율에 주는 영향 | DPT로 측정한 손실 모델 | 스니펫상 AI 언급 없음 | DPT 측정(실험). 손실 모델을 3상 계통연계 컨버터에 적용한 방식(실험/시뮬)은 확인되지 않음 |
| 22 | Evaluation of Single-Phase DC-AC Converters with Condition Monitoring Algorithm of Aluminum Electrolytic Capacitors using Artificial Learnings with Various Circuit Signals and Filtering Combinations | J. Electrical Engineering & Technology / 2023.07 | H.-L. Dang, H.-J. Park, Sang Shin Kwak, S. Choi | JEET, Vol.18, No.4, pp.3021–3032, 2023년 7월 | 10.1007/s42835-023-01426-x | V1 | https://link.springer.com/10.1007/s42835-023-01426-x , https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/66391 | 단상 인버터 알루미늄 전해 커패시터 파라미터(ESR, C) 추정 | 부하 전압·전류, 커패시터 전압·전류. DWT와 FFT+각종 필터 조합 | "six AI algorithms"(종류 미기재) | 확인되지 않음 |
| 23 | DC Capacitor Parameter Estimation Technique for Three-Phase DC/AC Converter using Deep Learning Methods with Different Frequency Band Inputs | J. Electrical Engineering & Technology / 2023.05 | H.-J. Park, Sangshin Kwak | JEET, Vol.18, No.3, pp.1841–1850, 2023년 5월 | 미확인 | V2 | https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/66390 | 3상 DC/AC 컨버터의 DC 커패시터 C와 ESR 추정 | 서로 다른 주파수 대역 성분(C 추정에는 저주파, ESR 추정에는 중간주파가 우세). 원신호명은 확인되지 않음 | DNN, CNN, Simple RNN, LSTM. 특정 성분만 넣으면 DNN, 넓은 대역을 넣으면 CNN이 우수 | 확인되지 않음 |
| 24 | DC-Link Electrolytic Capacitors Monitoring Techniques based on Advanced Learning Intelligence Techniques for Three-Phase Inverters | Machines / 2022.12 | — | — | 미확인 | X | — (2회 검색, 아래 (d) 참고) | 확인되지 않음 | 확인되지 않음 | 확인되지 않음 | 확인되지 않음 |
| 25 | Impacts of SiC-MOSFET Gate Oxide Degradation on Three-Phase Voltage and Current Source Inverters | Machines / 2022.12 | Jaechang Kim, Sangshin Kwak, Seungdeog Choi | Machines, 2022년 12월. URL 경로상 Vol.10, No.12, 1194 | 미확인. URL 패턴으로 10.3390/machines10121194를 **유추**했을 뿐 직접 확인하지 못함 | V2 | https://www.mdpi.com/2075-1702/10/12/1194 , https://doaj.org/article/10297b5b78514fc79b328c8cf143a97d | SiC-MOSFET gate oxide 열화가 VSI·CSI 성능에 주는 영향 | Turn-on/off delay 변화에 따른 duty error | 스니펫상 AI 언급 없음 | 확인되지 않음 |
| 26 | Deep Learning-based Estimation Technique for Capacitance and ESR of Input Capacitors in Single-phase DC/AC Converters | J. Power Electronics / 2022.03 | Hye-Jin Park, Jae-Chang Kim, Sangshin Kwak | J. Power Electronics, Vol.22, No.3, pp.513–521, 2022년 3월 | 10.1007/s43236-021-00366-x | V1 | https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/52713 | 단상 DC/AC 컨버터 입력 커패시터 C와 ESR 추정 | 실험으로 수집한 전압·전류의 FFT 성분. 기본파의 2배 주파수와 스위칭 주파수 성분이 우세. 입력 변수 조합 11종 | DNN | 실험 데이터("collected experimental voltage and current") |
| 27 | Review of Health Monitoring Techniques for Capacitors Used in Power Electronics Converters | Sensors / 2020.07 | Hoang-Long Dang, Sangshin Kwak | Sensors, 2020-07-03 게재 | 10.3390/s20133740 | V1 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7374397/ , https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/49064 | 커패시터 health monitoring 리뷰(ESR, C 지표) | 해당 없음(리뷰) | 해당 없음(리뷰) | 해당 없음(리뷰) |
| 28 | Open-Circuit Switch-Fault Tolerant Control of a Modified Boost DC-DC Converter for Alternative Energy Systems | IEEE Access / 2019.05 | — | — | 미확인 | X | — (2회 검색) | 확인되지 않음 | 확인되지 않음 | 확인되지 않음 | 확인되지 않음 |
| 29 | Fault Diagnosis Algorithm Based on Switching Function for Boost Converters | International Journal of Electronics / 2015.07 | H.-K. Cho, S.-S. Kwak, S.-H. Lee | Int. J. Electronics, Vol.102, No.7, pp.1229–1243, 2015년 7월 | 10.1080/00207217.2014.966780 | V1 | https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/9354 | Boost 컨버터 스위치의 open/short-circuit 고장 | 인덕터 전압과 스위칭 함수 비교 | AI 사용하지 않음(아날로그 회로 기반 판정) | 확인되지 않음 |

### Best Paper Award (PDF 13쪽)
- PDF 기재: "DC series arc diagnosis on deep learning algorithm with frequency domain characteristics", Journal of Power Electronics (SCIE), 수상일 23.12.01.
- 이 제목은 #18의 실제 서지 제목 "DC series arc diagnosis **based on deep-learning** algorithm with **frequency-domain** characteristics"(JPE 21(12), 2021, DOI 10.1007/s43236-021-00332-7)과 단어 몇 개만 다르다. **추론**: 같은 논문으로 보인다.
- 수상 사실(수상일, 수여기관)은 외부에서 확인하지 못했다.

---

## (b) 특허 표 (PDF 12~13쪽 전사)

KIPRIS 직접 조회는 egress 정책으로 차단되어 있었고, WebSearch 한도도 소진되어 **11건 모두 외부 검색으로 확인하지 못했다**. 발명자는 PDF의 "창업팀 구성원(발명자 中)" 칸 기재값이다.

| # | 구분 | 상태 | 명칭 (PDF 원문) | 등록(출원)년도 | 등록(출원)번호 | 등록(출원)인 | 발명자(PDF) | 비고 | 검증 |
|---|---|---|---|---|---|---|---|---|---|
| P1 | 국내 | 등록 | 인공 기계 학습을 이용한 직류 아크 결함 진단 장치 | 2025 | 10-2906080 | 중앙대학교 산학협력단 | 곽상신 | 핵심특허 | PDF 기재 내용(외부 미확인) |
| P2 | 국내 | 출원 | 인공지능을 이용한 3상 인버터 전력 반도체 소자의 노화 진단 및 위치 진단 장치 및 방법 | 2026 | 10-2026-0066701 | 중앙대학교 산학협력단 | 곽상신 | 핵심특허 | PDF 기재 내용(외부 미확인) |
| P3 | 국내 | 출원 | 전력변환기에 구비된 커패시터의 노화를 진단하기 위한 커패시터 노화 진단 장치 및 방법 | 2026 | 10-2026-0030907 | 중앙대학교 산학협력단 | 곽상신 | 핵심특허 | PDF 기재 내용(외부 미확인) |
| P4 | 국내 | 출원 | 인공지능을 이용한 전력변환 장치용 커패시터의 온라인 상태 진단 장치 | 2026 | 10-2026-0006795 | 중앙대학교 산학협력단 | 곽상신 | 핵심특허 | PDF 기재 내용(외부 미확인) |
| P5 | 국내 | 출원 | 인공지능을 이용한 3상 인버터 전력 반도체 소자의 소프트 고장 발생 여부 및 고장 위치 진단 장치 및 방법 | 2026 | 10-2026-0006796 | 중앙대학교 산학협력단 | 곽상신 | 핵심특허 | PDF 기재 내용(외부 미확인) |
| P6 | 국내 | 출원 | 인공지능을 이용한 3상 인버터의 전력 스위칭 소자 및 DC 커패시터 노화 진단 장치 및 방법 | 2026 | 10-2026-0006794 | 중앙대학교 산학협력단 | 곽상신 | 핵심특허 | PDF 기재 내용(외부 미확인) |
| P7 | 국내 | 등록 | 아크 검출 장치 및 방법 | 2026 | 10-2933289 | 중앙대학교 산학협력단, 한국전력공사 | 곽상신 | 핵심특허 | PDF 기재 내용(외부 미확인) |
| P8 | 국내 | 등록 | 이동평균을 이용한 아크 검출장치 및 방법 | 2024 | 10-2659878 | 중앙대학교 산학협력단 | 곽상신 | 핵심특허 | PDF 기재 내용(외부 미확인) |
| P9 | 국내 | 출원 | 인공지능 기반 노화 감속 제어모델을 구비한 직류-직류 컨버터 스위칭 제어 장치 및 그에 의한 제어 방법 | 2026 | 10-2026-0065938 | 중앙대학교 산학협력단 | 곽상신 | 핵심특허 | PDF 기재 내용(외부 미확인) |
| P10 | 국내 | 출원 | 인공지능 기반 노화 감속 제어모델을 구비한 3상 인버터 스위칭 제어 장치 및 방법 | 2026 | 10-2026-0044528 | 중앙대학교 산학협력단 | 곽상신 | 핵심특허 | PDF 기재 내용(외부 미확인) |
| P11 | 국내 | 출원 | 아크 결함 검출 장치 및 방법 | 2026 | 10-2026-0012400 | 중앙대학교 산학협력단 | 곽상신 | 핵심특허 | PDF 기재 내용(외부 미확인) |

PDF 기재 기준 집계: 등록 3건(P1, P7, P8), 출원 8건(모두 2026년).
- 아크 관련 4건: P1, P7, P8, P11
- 커패시터 노화 진단 3건: P3, P4, P6(스위치 노화와 겸함)
- 전력반도체 소자 노화·고장 진단 3건: P2, P5, P6(커패시터와 겸함)
- AI 기반 노화 감속 제어 2건: P9, P10

---

## (c) 주제별 요약 분석

분류는 PDF 제목과 확인된 스니펫을 기준으로 했다. X 등급 논문은 **제목만 보고** 분류했으므로 내용은 확인되지 않은 상태다.

| 주제 | 편수 | 논문 번호 | AI 사용 (스니펫으로 확인된 것) | AI 확인 안 됨 / 비AI |
|---|---|---|---|---|
| DC series arc | 12 | 2(X), 4, 5, 6, 7, 8, 11(X), 15, 16, 17(X), 18, 20 | 7편: #4, #5, #6, #7, #8, #15, #16은 "learning models/ML"로만 서술(종류 미기재), #18은 DNN | #20은 주파수 특성 분석이고 AI 언급 없음. #11(표준편차), #17(adaptive moving average)은 미검색(X). 제목상 비AI 통계 기법으로 보이나 **추론**. #2(X)는 제목에 "Intelligence Models"가 있음 |
| DC parallel arc | 3 | 3, 9(V1*), 12 | 2편: #3 artificial learning models, #12 eight learning techniques | #9는 내용 미확인 |
| DC series+parallel 구분 | 2 | 10(X), 13 | 1편: #13 eight learning techniques(제목상 DL) | #10 미확인 |
| AC arc (series/parallel) | 3 | 1(V1*), 14(V1*), 19(V1*) | 1편: #19 여러 ANN. #14는 제목상 DL이나 스니펫 귀속이 불확실 | #1은 moving Z-score 통계·임계값 방식이며 스니펫상 AI 언급 없음 |
| 커패시터 C/ESR 추정·상태감시 | 5 | 22, 23, 24(X), 26, 27(리뷰) | 3편: #22 AI 6종, #23 DNN/CNN/Simple RNN/LSTM, #26 DNN | #24 미확인(제목상 learning intelligence). #27은 리뷰 |
| SiC MOSFET·소자 열화 | 2 | 21, 25 | 0편 | #21(손실 특성, DPT), #25(gate oxide 열화 영향) 모두 AI 언급 없음 |
| 컨버터 고장진단·내고장제어 | 2 | 28(X), 29 | 0편 | #29는 아날로그 회로 기반 스위칭 함수 비교. #28 미확인 |
| **합계** | **29** | | AI 확인 14편 (#14는 미포함) | |

### 해석
- **AI 적용이 확인된 영역**
  - DC arc(series, parallel, 구분) 다수. 2021~2024년 Hoang-Long Dang, Sangshin Kwak, Seungdeog Choi 공저 시리즈다.
  - AC series arc(#19, ANN).
  - 커패시터 C/ESR 추정(#22, #23, #26). DNN, CNN, RNN, LSTM이 명시된 것은 #18(DNN), #23(DNN/CNN/Simple RNN/LSTM), #26(DNN)뿐이다. 나머지는 "learning models", "eight learning techniques"처럼 묶어서만 서술되어 있어, 세부 알고리즘(SVM, RF, KNN 등)은 스니펫으로 확인하지 못했다.
- **AI 사용이 확인되지 않은 영역**
  - SiC-MOSFET 노화 영향 분석(#21, #25): 물리·특성 분석 논문으로 보인다.
  - 컨버터 스위치 고장진단(#29 아날로그, #28 미확인).
  - AC series arc의 통계 기반 검출(#1 moving Z-score).
  - PV DC arc 주파수 특성 분석(#20).
- **PDF 사업 내용과의 대응(추론)**: 창업계획서는 "AI 기반 전력반도체 소자 상태진단"을 핵심기술로 내세운다. 그런데 소자 열화 관련 논문 2편(#21, #25)에서는 AI가 확인되지 않았다. 이 영역의 AI 근거는 2026년 출원 특허(P2, P5, P6)에만 기재되어 있다. 반면 아크 AI 진단과 커패시터 AI 추정은 논문 근거가 충분하다.
- **현재 프로젝트(NPC DC-link 커패시터 노화진단)와의 접점(스니펫에서 확인된 사실)**
  - #26: 단상 DC/AC에서 "기본파의 2배 주파수와 스위칭 주파수 성분이 우세"하며, 이를 DNN 입력으로 썼다.
  - #23: 3상 DC/AC에서 "C 추정에는 저주파, ESR 추정에는 중간주파가 우세"하며, 넓은 대역을 입력하면 CNN이 우수했다.
  - 두 논문 모두 본 프로젝트의 주파수 대역 기반 CNN 입력 설계와 직접 관련된다. 단, 3-level NPC를 대상으로 한 논문은 목록에 없다.

---

## (d) PDF와 검색결과의 차이 및 주의점

1. **#21 게재 월**: PDF는 2023.05, 검색결과는 JEET Vol.18 No.4, 2023년 7월. 온라인 선공개일일 가능성이 있으나 확인하지 못했다.
2. **#9 연도**: PDF는 2023.05인데 DOI가 s42835-**022**-01273-2(2022년 부여 패턴)다. 실제 게재 연월은 확인하지 못했다.
3. **#14 연도**: PDF는 2022.03인데 DOI가 s42835-**021**-00976-2(2021년 부여 패턴)다. 실제 게재 연월은 확인하지 못했다.
4. **Best Paper Award 제목**: PDF의 "…diagnosis **on** deep learning algorithm with frequency domain…"과 실제 #18 제목 "…diagnosis **based on deep-learning** algorithm with **frequency-domain**…"의 표기가 다르다. 수상 사실 자체는 외부에서 확인하지 못했다.
5. **#8 표기 차이(경미)**: PDF는 "Empirical Filtering based", 검색결과는 "Empirical Filtering-**Based**".
6. **#10과 #13의 중복 가능성(추론, 미확인)**: 둘 다 IEEE Access 2022(06월, 07월)이고 주제(series+parallel DC arc 검출·식별)가 겹친다. 검색에서는 #13만 확인되었다. 한 검색 요약문에 "detection and identification techniques for series and parallel DC arc faults"라는 문구가 나왔지만 독립된 서지(제목/DOI)로는 확인하지 못했다. 이중 기재인지 별개 논문인지 추가 확인이 필요하다.
7. **X 6편(#2, #10, #11, #17, #24, #28)**: 검색 한도 소진 전까지 2~3회씩 검색했으나 찾지 못했다. **존재하지 않는다는 뜻이 아니다.**
   - #17(adaptive moving average)은 특허 P8(이동평균을 이용한 아크 검출장치)과 주제가 대응한다.
   - #24 관련: 한 검색 요약에 "Dang, Kwak, Kim의 3상 AC-DC 컨버터 커패시터 상태감시(DWT, RMS·variance·average·median 특징, AI, 정확도 약 99.85%)"가 나왔으나 제목이 보이지 않아 #24와 같은 논문인지 판단할 수 없다.
8. **#25 DOI**: MDPI URL 경로(2075-1702/10/12/1194)로 10.3390/machines10121194를 유추했을 뿐 직접 확인하지 못했다. 그래서 V2로 두었다.
9. **#23 DOI**: 미확인이다. 저널, 권호, 쪽, 연도는 일치한다.
10. **V1* 4편(#1, #9, #14, #19)**: 저자는 스니펫에 나오지 않아 곽상신 교수 포함 여부를 확인하지 못했다. 제목과 DOI는 Springer URL로 확인했다.
11. **PDF 목록 밖의 연구실 논문**: 검색 중 다음이 중앙대 리포지토리에서 노출되었다. 모두 서지 세부는 미검증이다.
    - "Metalized Polymer-Film Capacitors Health Estimation for Three-Phase DC to AC Converters with Artificial Intelligences" (scholarworks cau 67782)
    - 「데이터 기반 방식과 모델 기반 방식을 이용한 DC/AC 컨버터의 입력 커패시터 ESR 추정 비교 연구」 (cau 72859)
    - 「고전계 노화 SiC-MOSFET 소자를 가지는 양방향 DC-DC 컨버터 특성 분석 연구」 (cau 59011)
12. **리포지토리 중복 등재**: #16은 중앙대 scholarworks에 handle 두 개(50141, 72863)로 올라 있다. 서지 오류는 아니다.
13. **SCIE 등재 여부**: 29편 모두 외부에서 검증하지 않았다.

## 등급별 집계
| 등급 | 편수 | 번호 |
|---|---|---|
| V1 | 17 | 3, 4, 5, 6, 7, 8, 12, 13, 15, 16, 18, 20, 21, 22, 26, 27, 29 |
| V1* | 4 | 1, 9, 14, 19 |
| V2 | 2 | 23, 25 |
| V3 | 0 | (#21은 월만 달라 V1로 두고 (d)에 기록) |
| X | 6 | 2, 10, 11, 17, 24, 28 |
