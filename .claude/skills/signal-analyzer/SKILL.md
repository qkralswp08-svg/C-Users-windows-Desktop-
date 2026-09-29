---
name: signal-analyzer
description: FFT, 고조파(harmonic) 분석, 스펙트럼/파형/리플 해석, 창 함수·분해능·누설 같은 신호처리 방법론을 담당한다. Use when the request is about FFT, harmonics, spectrum, ripple, THD, sampling/windowing, or interpreting a waveform or spectrum (language-independent; pairs with matlab-analyzer or python-analyzer for the code).
keywords: [fft, 고조파, harmonic, 하모닉, 스펙트럼, spectrum, 주파수 성분, 주파수, frequency, 신호처리, signal processing, 파형, waveform, 필터, filter, 리플, ripple, thd, 창 함수, window, 샘플링, sampling, 분해능, resolution, 누설, leakage, 2n, 짝수 고조파, even harmonic, 홀수 고조파, 측대파, sideband, 스위칭 주파수 성분, stft, wavelet, 웨이블릿, rms, 실효값, 위상, phase]
order: 40
combine-with: [matlab-analyzer, python-analyzer, npc-inverter-expert, capacitor-aging-expert]
---

# signal-analyzer

## 목적
전류/전압 파형의 스펙트럼을 올바르게 구하고 해석하는 방법을 제공한다. 어떤 고조파가 크고 왜 그런지 판단할 때, 계산이 신뢰할 만한지(분해능·누설·스케일) 먼저 확인한다.

## 언제 사용하는가
- "iSa2 의 FFT 에서 주요 고조파 확인", "2n 고조파가 큰 이유", "리플 성분 분리"
- FFT/STFT/wavelet 구현 검토, 창 함수·구간 선택
- 스펙트럼 결과를 CNN 특징으로 만들 때 어떤 성분을 쓸지 판단

## 확인해야 할 핵심 정보
- `fs`, `N`, 분석 구간 길이 `T = N/fs`, 주파수 분해능 `Δf = fs/N`
- 기본파 `f1` 과 `fsw`: `f1` 의 정수배 주기를 잘라 썼는지 (아니면 누설 발생)
- 창 함수 (rectangular / Hann / flat-top) 와 진폭 보정 계수
- 단측 스펙트럼 스케일: `|X(k)|·2/N` (DC 와 Nyquist 는 1/N), 진폭 vs RMS
- 고조파 차수 정의: `h = f/f1`. 스위칭 성분은 `m·fsw ± n·f1` 형태로 표기
- 정상상태 진입 여부, DC offset 제거 여부, 신호 방향(부호) 규약

## 절차
1. 설정값 표를 만들고 `Δf` 가 관심 성분(예: 2f1, 3f1, fsw±f1)을 분리하기에 충분한지 확인한다.
2. 파형을 먼저 시간영역에서 이해한다: 대칭성(반파 대칭이면 짝수 고조파 없음, 반파 정류형이면 DC + 기본파 + 짝수 고조파), 주기, 펄스형 여부.
3. 스펙트럼에서 상위 성분을 크기 순으로 나열하고 차수(`h`)와 절대/상대(기본파 또는 DC 대비) 크기를 표로 만든다. 저주파(기본파 배수)와 스위칭 주파수 대역을 분리해 본다.
4. 각 성분의 발생 원인을 "파형 대칭성 / 스위칭 동작 / 부하 / 계산 아티팩트(누설, 창)" 로 분류한다. 아티팩트 가능성은 구간 길이나 창을 바꿔 재계산해 확인하도록 안내한다.
5. 결론에서 "코드/데이터로 확인한 사실" 과 "물리적 추론" 을 분리한다.

## 출력 형식
- **설정 표** (fs, N, Δf, f1, fsw, 창, 구간)
- **주요 성분 표**: 순위 | f [Hz] | 차수 h | 크기 | 상대 크기 | 추정 원인 | 근거 유형(사실/추론)
- **해석**: 왜 그 성분이 큰지, 노화/상태 정보와 어떻게 연결되는지 (도메인 Skill 과 함께)
- **검증 제안**: 구간/창 변경, 이론 파형과의 비교, 다른 상(phase)과의 대칭 확인

## 주의사항
- "2n 고조파가 지배적" 같은 결론은 실제 스펙트럼 값과 파형 대칭성 근거 없이 단정하지 않는다.
- 스펙트럼 크기 단위(피크/RMS/dB)를 반드시 명시한다.
- MATLAB `fft` 와 numpy `fft` 의 스케일/정규화 차이를 코드에서 확인한다.

## 다른 Skill과의 조합
- `matlab-analyzer` / `python-analyzer`: 실제 계산 코드 확인
- `npc-inverter-expert`: 스위칭 상태에 따른 성분의 물리적 원인
- `capacitor-aging-expert`: 어떤 성분이 ESR/C 변화에 민감한지
