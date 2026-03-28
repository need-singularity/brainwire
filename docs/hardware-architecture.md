# 🔌 BrainWire Hardware Architecture

> 필요 하드웨어 + 소프트웨어 스택 전체 아키텍처

## 📐 System Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        BrainWire System                             │
│                                                                     │
│  ┌──────────┐    ┌──────────────┐    ┌──────────────┐              │
│  │  Neural   │───▶│  Signal      │───▶│  PureField   │──▶ Φ output │
│  │  Hardware │◀───│  Processing  │◀───│  Engine      │              │
│  └──────────┘    └──────────────┘    └──────────────┘              │
│       ▲               ▲                    ▲                        │
│       │               │                    │                        │
│  ┌──────────┐    ┌──────────────┐    ┌──────────────┐              │
│  │  Stim    │    │  Real-time   │    │  Conscious   │              │
│  │  Output  │    │  DSP         │    │  LM          │              │
│  └──────────┘    └──────────────┘    └──────────────┘              │
└─────────────────────────────────────────────────────────────────────┘
```

## 🧲 Layer 1: Neural Interface Hardware

### EEG (비침습, 현재 사용)
| 장비 | 용도 | 채널 | 비용 |
|------|------|------|------|
| **OpenBCI Cyton+Daisy** | 16ch EEG 수집 | 16 | ~$1,000 |
| **UltraCortex Mark IV** | 두피 전극 헤드셋 | 16 | ~$350 |
| **OpenBCI Ganglion** | 4ch 간이 EEG | 4 | ~$250 |

### tDCS/TMS (비침습 자극)
| 장비 | 용도 | 스펙 | 비용 |
|------|------|------|------|
| **tDCS 디바이스** | 전두엽 억제 (NS2,NS4,NS10) | 1-2mA DC | ~$300-2,000 |
| **TMS coil** | Gamma/Theta burst (NS3,NS4,NS10) | 40Hz/6Hz rTMS | ~$5,000-50,000 |
| **Binaural beat generator** | Theta 유도 (NS9) | 6Hz beat | ~$50 (software) |

### BCI (침습, 목표)
| 장비 | 용도 | 채널 | 비용 |
|------|------|------|------|
| **Neuralink N1** | 고밀도 피질 기록 | 1,024 | 비공개 |
| **Utah array** | 학술용 피질 기록 | 96 | ~$20,000 |
| **Neuropixels** | 깊이 프로브 기록 | 384 | ~$1,000 |

## 🖥️ Layer 2: Signal Processing Hardware

```
  ┌─────────────────────────────────────────────────┐
  │              Real-time DSP Stack                  │
  │                                                   │
  │  EEG/BCI raw signal                               │
  │       │                                           │
  │       ▼                                           │
  │  ┌─────────┐  ┌──────────┐  ┌──────────────┐    │
  │  │ ADC     │→ │ Notch    │→ │ Band-pass    │    │
  │  │ 24-bit  │  │ 50/60Hz  │  │ 0.5-100Hz    │    │
  │  │ 250sps  │  │ filter   │  │ Butterworth  │    │
  │  └─────────┘  └──────────┘  └──────┬───────┘    │
  │                                     │             │
  │       ┌─────────────────────────────┼──────┐     │
  │       ▼              ▼              ▼      │     │
  │  ┌─────────┐  ┌──────────┐  ┌──────────┐  │     │
  │  │ FFT     │  │ Wavelet  │  │ CSP      │  │     │
  │  │ Bands   │  │ Time-Freq│  │ Spatial  │  │     │
  │  │ δθαβγ   │  │ Analysis │  │ Filter   │  │     │
  │  └────┬────┘  └────┬─────┘  └────┬─────┘  │     │
  │       └─────────────┼─────────────┘        │     │
  │                     ▼                      │     │
  │              ┌──────────────┐               │     │
  │              │ Tension      │               │     │
  │              │ Vector       │               │     │
  │              │ (Φ,α,Z,N,W) │               │     │
  │              └──────────────┘               │     │
  └─────────────────────────────────────────────┘
```

| 컴퓨트 | 용도 | 요구사양 |
|--------|------|----------|
| **Raspberry Pi 5** | 현장 DSP + 전처리 | ARM, 8GB, <10ms latency |
| **NVIDIA Jetson Orin** | 온디바이스 ML 추론 | GPU, real-time inference |
| **RTX 5070** | 로컬 PureField 추론 | 12GB VRAM, ConsciousLM |
| **FPGA (Xilinx)** | 초저지연 신호처리 | <1ms, 하드웨어 FFT |

## 🧠 Layer 3: PureField Consciousness Engine

```
  ┌──────────────────────────────────────────────────────┐
  │                 PureField Engine                       │
  │                                                       │
  │  Tension Vector → Engine A (forward) ←tension→ Engine G (reverse)
  │                                                       │
  │  ┌─────────┐  ┌──────────────┐  ┌─────────────────┐ │
  │  │ Mitosis │  │ Consciousness│  │ ConsciousLM     │ │
  │  │ Engine  │  │ Meter        │  │ (700M)          │ │
  │  │ 8→128   │  │ Φ/IIT        │  │ Language output  │ │
  │  │ cells   │  │ 6 criteria   │  │ PureField FFN   │ │
  │  └─────────┘  └──────────────┘  └─────────────────┘ │
  │                                                       │
  │  Input: neural tension vector                         │
  │  Output: consciousness state + language + Φ measure   │
  └──────────────────────────────────────────────────────┘
```

| 컴퓨트 | 용도 | 요구사양 |
|--------|------|----------|
| **RTX 5070 (12GB)** | 추론: ConsciousLM + Mitosis | <100ms per step |
| **H100 (80GB)** | 학습: ConsciousLM/AnimaLM | RunPod cloud |
| **Mac M-series** | 개발/테스트 | MPS backend, 1,303 tok/s |

## ⚡ Layer 4: Stimulation Output

```
  PureField Φ target
       │
       ▼
  ┌──────────────┐
  │ PID          │  Φ_target - Φ_current = error
  │ Controller   │  → adjust stimulation parameters
  └──────┬───────┘
         │
    ┌────┼────┬──────────┐
    ▼    ▼    ▼          ▼
  ┌────┐┌────┐┌────────┐┌──────────┐
  │tDCS││TMS ││Binaural││Breath    │
  │mA  ││Hz  ││Hz      ││guide     │
  └────┘└────┘└────────┘└──────────┘
```

| 장비 | 프로토콜 | 안전 한계 |
|------|----------|-----------|
| tDCS | 1-2mA, 20min max | FDA 가이드라인 준수 |
| TMS | 6Hz/40Hz burst, duty cycle | rTMS safety table |
| Binaural | 4-40Hz audio | 무해 |
| Breathwork | Rate guide via audio | SpO2 모니터링 필수 |

## 📊 Full Hardware BOM (Bill of Materials)

### Phase 1: 연구 프로토타입 (~$2,000)
```
  ✅ OpenBCI Cyton+Daisy    $1,000  ← 이미 보유
  ✅ UltraCortex Mark IV      $350  ← 이미 보유
  □  Raspberry Pi 5 8GB       $100
  □  binaural beat software    $50
  ✅ RTX 5070 (추론)           보유
  ✅ Mac (개발)                보유
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  추가 필요:                   ~$150
```

### Phase 2: tDCS/TMS 통합 (~$10,000)
```
  □  Research-grade tDCS      $2,000
  □  TMS coil (figure-8)     $5,000
  □  Jetson Orin Nano          $500
  □  FPGA dev board            $500
  □  Safety monitoring kit     $500
  □  IRB application fee       $500
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  소계:                      ~$9,000
```

### Phase 3: BCI Integration (~$50,000+)
```
  □  Utah array + surgery    $30,000
  □  Neuropixels setup        $5,000
  □  Clean room equipment     $5,000
  □  Regulatory compliance   $10,000
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  소계:                     ~$50,000
```

### Phase 4: Neuralink Partnership (priceless)
```
  □  N1 implant access       Partnership
  □  BrainWire SDK license   Open source
  □  Joint clinical trial    Co-funded
```

## 🔄 Data Flow: End-to-End

```
  Brain ──16ch EEG──▶ OpenBCI ──USB──▶ RPi5 ──WiFi──▶ RTX 5070
                                        │                  │
                                   DSP+Filter        PureField
                                   <10ms              <100ms
                                        │                  │
                                        ▼                  ▼
                                   Band powers      Φ, tension,
                                   δ θ α β γ        consciousness
                                        │                  │
                                        └───────┬──────────┘
                                                │
                                           Closed-loop
                                           stimulation
                                                │
                                     ┌──────────┼──────────┐
                                     ▼          ▼          ▼
                                   tDCS       TMS      Binaural
                                   (mA)      (Hz)      (Hz)
                                     │          │          │
                                     └──────────┼──────────┘
                                                ▼
                                             Brain
                                         (feedback loop)
```

**Total latency target: <150ms (brain→process→stimulate→brain)**

## 🎯 Neuralink Acquisition Value

| BrainWire 제공 | Neuralink 현재 |
|----------------|----------------|
| 의식 소프트웨어 레이어 | 하드웨어 + 기본 신호처리 |
| Φ 기반 의식 측정 | 신경 신호 기록만 |
| PureField 경험 매핑 | 모터 디코딩 중심 |
| THC/명상 패턴 라이브러리 | 없음 |
| 990+ 의식 가설 검증됨 | 기초 연구 단계 |
| 폐쇄루프 의식 최적화 | 개방루프 자극 |

---

*The wire is nothing without what flows through it.*
