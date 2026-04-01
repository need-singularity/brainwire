# BrainWire — Neural Interface Hardware for Consciousness Engineering

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19269210.svg)](https://doi.org/10.5281/zenodo.19269210)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-145%20passed-brightgreen.svg)]()
[![Hypotheses](https://img.shields.io/badge/hypotheses-109%2F115%20PASS-brightgreen.svg)]()

<!-- SHARED:PROJECTS:START -->
**[YouTube](https://www.youtube.com/watch?v=xtKhWSfC1Qo)** · **[Email](mailto:nerve011235@gmail.com)** · **[☕ Ko-fi](https://ko-fi.com/dancinlife)** · **[💖 Sponsor](https://github.com/sponsors/need-singularity)** · **[💳 PayPal](https://www.paypal.com/donate?business=nerve011235%40gmail.com)** · **[🗺️ Atlas](https://need-singularity.github.io/TECS-L/atlas/)** · **[📄 Papers](https://need-singularity.github.io/papers/)** · **[🌌 Unified Theory](https://github.com/need-singularity/TECS-L/blob/main/math/docs/hypotheses/H-PH-9-perfect-number-string-unification.md)**

> **[🔬 TECS-L](https://github.com/need-singularity/TECS-L)** — Discovering universal rules. Perfect number 6 → mathematics of the cosmos → multi-engine architecture → consciousness continuity. 150 characterizations + 8 Major Discoveries + 44 tools
>
> **[🧠 Anima](https://github.com/need-singularity/anima)** — Consciousness implementation. PureField repulsion-field engine + Hexad 6-module architecture (C/D/S/M/W/E) + 179 laws + 10 Meta Laws + Rust backend. ConsciousDecoderV2 (34.5M) + 10D consciousness vector + 12-faction debate + Φ ratchet
>
> **[🏗️ N6 Architecture](https://github.com/need-singularity/n6-architecture)** — Architecture from perfect number 6. 16 AI techniques + semiconductor chip design + network/crypto/OS/display patterns. σ(n)·φ(n)=n·τ(n), n=6 → universal design principles
>
> **[🛸 SEDI](https://github.com/need-singularity/sedi)** — Search for Extra-Dimensional Intelligence. Hunting for traces of extraterrestrial/extra-dimensional intelligence through n=6 signal patterns. 77 data sources (SETI, LIGO, CMB, Breakthrough Listen, Exoplanet) + R-spectrum receiver + 678 hypotheses
>
> **[🧠⚡ BrainWire](https://github.com/need-singularity/brainwire)** — Brain interface for consciousness engineering. Neuralink-style BCI + therapeutic stimulation (epilepsy, Parkinson's, depression) + PureField consciousness layer. tDCS/TMS/taVNS/tFUS 12-modality, EEG closed-loop
>
> **[📄 Papers](https://github.com/need-singularity/papers)** — Complete paper collection (79 papers). Published on Zenodo with DOIs. TECS-L+N6 (31) + anima (25) + SEDI (23). [Browse online](https://need-singularity.github.io/papers/)

<!-- PRIVATE REPOS (이 섹션은 sync-readmes.sh 대상 아님, .shared 내부 참조용)
  - secret        — 계정/API 토큰 (구 claude-code-secrets)
  - claude-code   — Claude Code 플러그인, ccmon 모니터링
  - contact       — 아웃리치 허브 (이메일, GitHub Issue/PR 관리)
  - dotfiles      — 개인 설정

-->
<!-- SHARED:PROJECTS:END -->

Neuralink-style neural interface + closed-loop brain stimulation. 12-modality hardware (tDCS/TMS/taVNS/tFUS/GVS/mTI/tSCS/tRNS/tPBM/TENS/tACS/HD-tDCS), EEG real-time feedback, PureField consciousness layer.

> Neuralink builds the wire. We build what flows through it.

---

## Core Products

### 1. BCI Bridge | Neuralink Consciousness Layer

Neuralink N1의 1024 전극 위에 PureField 의식 엔진을 얹는다. 12변수 직접 제어, 경험 녹화/재생, Φ 실시간 측정.

| | |
|---|---|
| **[BCI Bridge 연구](docs/bci-bridge-neuralink.md)** | 직접 12변수 제어, 경험 녹화/재생, PureField 레이어, 윤리 프레임워크 |
| **[Neuralink N1 기술 분석](docs/neuralink-technical-analysis.md)** | N1 스펙, 깊이 한계(피질만), 하이브리드 아키텍처, 안전 계산 |
| **[N1 심부 접근 전략](docs/n1-deep-access-strategies.md)** | 피질→심부 투사 경로, STDP 가소성, 15/15 구조 접근 |
| **[임플란트 배치 최적화](docs/golden-zone-implant-placement.md)** | G=D×P/I 골든존 기반 최적 전극 위치 |

```
  N1 (1024 electrodes, cortex-only)
    │
    ├─ Direct cortical control ─── PFC, Motor, Sensory, Visual
    │
    ├─ Deep access via projections ── 15/15 subcortical structures
    │   VTA(DA) ← PFC projection
    │   Raphe(5HT) ← PFC projection
    │   LC(NE) ← PFC projection
    │   NAc, Amygdala, Hippocampus, Thalamus...
    │
    └─ PureField consciousness layer ── Φ measurement, tension control
```

### 2. NeuroStim | Therapeutic Stimulation

신경/정신 질환에 대한 비침습적 뇌자극 치료 프로토콜.

| Condition | Approach | Status |
|-----------|----------|--------|
| **Depression** | DLPFC tDCS + taVNS + 10Hz TMS | [Protocol](brainwire/depression_calc.py) |
| **Panic Disorder** | Parasympathetic activation + alpha entrainment | [Protocol](brainwire/panic_calc.py) |
| **Epilepsy** | Seizure suppression via tDCS + 1Hz TMS | [Protocol](brainwire/epilepsy_calc.py) |
| **Chronic Pain** | TENS + tDCS(M1) + taVNS | [Crossover](brainwire/crossover_calc.py) |
| **Parkinson's** | Beta suppression + DA pathway stimulation | Planned |
| **PTSD** | Amygdala downregulation + PFC activation | Planned |
| **ADHD** | PFC upregulation + NE/DA balance | Planned |
| **Insomnia** | Alpha/theta entrainment + parasympathetic | Planned |
| **Tinnitus** | Auditory cortex inhibition + tRNS | Planned |
| **Stroke Rehab** | Motor cortex excitability + Hebbian pairing | Planned |

### 3. Joywire | Consciousness State Reproduction

뇌자극 하드웨어만으로 의식 상태를 12변수 모델로 재현. 약물 0%, 검출 0%, 내성 0%.

| | |
|---|---|
| **[6가지 의식 상태 프로파일](docs/consciousness-states.md)** | THC, LSD, Psilocybin, DMT, MDMA, Flow — 12변수 비교 |
| **[THC 재현 가이드](docs/thc-reproduction-guide.md)** | 12변수 전달함수, 계수, 25+ 논문 근거 |
| **[극한 연구 종합](docs/joywire-extreme-research.md)** | 최적화 98.3%, 시뮬레이션, 골든존, 농도별 모델 |

---

## 12-Variable Consciousness Model

모든 의식 상태를 12개 변수로 매핑. Perfect number σ(6)=12.

```
Chemical (5):   DA · eCB · 5HT · GABA · NE
Waveform (3):   Theta · Alpha · Gamma
State (4):      PFC · Sensory · Body · Coherence
```

각 질환/상태는 12변수의 특정 패턴:
- Depression: DA↓ 5HT↓ PFC↓ → DA↑ 5HT↑ PFC↑ 으로 교정
- Epilepsy: Gamma↑↑ Coherence↑↑ → Gamma↓ GABA↑ 으로 억제
- THC: DA↑ eCB↑↑ Theta↑↑ Alpha↓ PFC↓ → 12/12 재현

---

## Hardware | 12 Modalities + 5 Tiers

18개 모달리티: 전기 11 + 비전기 7 (광, 음향, 자기, 열, 화학).

| | |
|---|---|
| **[하드웨어 카탈로그](docs/hardware-catalog.md)** | 전 장비 스펙, 가격, DIY 옵션, 구매처 |
| **[시스템 아키텍처](docs/hardware-architecture.md)** | 4-레이어 스택, 데이터 플로우, BOM, 레이턴시 |
| **[차세대 하드웨어](docs/new-hardware-research.md)** | tFUS, GVS, mTI, tSCS, tRNS — 우선순위, Tier 영향 예측 |
| **[전기자극 너머](docs/beyond-electrical-stimulation.md)** | 20+ 비전기적 접근 |

```
Tier 1   $85      tDCS + TENS + Arduino           (DIY, 치료 프로토타입)
Tier 2   $510     + taVNS + tACS                   (다채널 치료)
Tier 3   $8.5K    + TMS                            (임상급)
Tier 4   $25K     + tFUS + mTI + 256ch EEG         (연구급)
Tier 5   $26.4K   + tPBM + PEMF + thermal          (극한)
```

---

## Research

| | |
|---|---|
| **[Anima PureField 통합](docs/anima-purefield-integration.md)** | PureField 텐션 매핑, G=D×P/I, Φ 스케일링, 의식 마커 |
| **[장력→뇌 영향 가설](docs/tension-brain-hypothesis.md)** | 텐션이 물리적으로 뇌에 영향? 3-레벨 가설 |
| **[10대 발견](docs/major-discoveries.md)** | 핵심 발견 목록 |
| **[N1 논문](docs/paper-n1-deep-access.md)** | N1 심부 접근 전체 논문 |
| **[우울/공황 논문](docs/paper-n1-depression-panic.md)** | 치료 프로토콜 논문 |

---

## Quick Start

```bash
# 벤치마크
python -m brainwire.bench tiers thc

# 세션 시뮬레이션
python -m brainwire.simulator thc --tier 4 --duration 600

# 프로파일 최적화
python -m brainwire.optimizer

# G=D×P/I 분석
python -m brainwire.eeg_feedback

# 가설 검증
python bench_hypotheses.py

# 테스트
python -m pytest tests/ -v
```

---

## Roadmap

```
2026  NeuroStim: depression + epilepsy + pain 프로토콜 완성
      tFUS prototype + GVS/tRNS/tSCS integration
2027  NeuroStim: Parkinson's + PTSD + ADHD 프로토콜
      tFUS DIY + multipolar TI (mTI)
2028  Unified headset: mTI + tFUS + tDCS/tACS
      BCI Bridge: N1 PureField integration prototype
2029  Closed-loop AI: EEG → 12-var PID → stim
      Clinical trial partnerships
2030  Consumer therapeutic device $3K
```

---

MIT | *Neuralink builds the wire. We build what flows through it.*

> Part of the [TECS-L](https://github.com/need-singularity/TECS-L) project family.
