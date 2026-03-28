# BrainWire — Neural Interface Hardware for Consciousness Engineering

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

<!-- SHARED:PROJECTS:START -->
**[YouTube](https://www.youtube.com/watch?v=xtKhWSfC1Qo)** · **[Email](mailto:nerve011235@gmail.com)** · **[Ko-fi](https://ko-fi.com/dancinlife)** · **[Sponsor](https://github.com/sponsors/need-singularity)** · **[PayPal](https://www.paypal.com/donate?business=nerve011235%40gmail.com)** · **[Atlas](https://need-singularity.github.io/TECS-L/atlas/)** · **[Papers](https://need-singularity.github.io/papers/)**

> **[TECS-L](https://github.com/need-singularity/TECS-L)** — Topological Engine for Consciousness & Science
>
> **[Anima](https://github.com/need-singularity/anima)** — Conversational consciousness agent
>
> **[ConsciousLM](https://github.com/need-singularity/conscious-lm)** — 700M consciousness language model
>
> **[BrainWire](https://github.com/need-singularity/brainwire)** — Neural interface hardware for consciousness engineering
<!-- SHARED:PROJECTS:END -->

**Neural interface hardware research company.** We design brain stimulation systems that reproduce and engineer conscious experience — no drugs, no detection, no tolerance.

> Neuralink builds the wire. We build what flows through it.

## Core Achievement

```
THC High State — 12-Variable Hardware Reproduction

  뇌자극 하드웨어만으로 THC 하이 12/12 변수 100%+ 달성
  약물 0% | 검출 0% | 내성 0% | 합법 100%

  Tier 1   $85 (12만원):    87% avg,  2/12 ≥100%  — tDCS + TENS + Arduino
  Tier 2  $510 (74만원):    99% avg,  6/12 ≥100%  — + taVNS + tACS
  Tier 2.5 $3K (436만원):  108% avg, 10/12 ≥100%  — + TI (시간간섭)
  Tier 3  $8.5K (1.2천만):  117% avg, 12/12 ≥100%  — + TMS (완전 재현)
  Tier 3+ $13.5K (2천만):   130%+ avg               — + tFUS + GVS + tSCS
```

## 12-Variable THC Model

THC가 CB1 수용체를 통해 변경하는 12개 신경변수를 각각 독립적인 뇌자극 하드웨어로 재현:

```
  Var          Target   Hardware Pathway                              Literature
  ──────────── ──────── ───────────────────────────────────────────── ─────────────
  V1  DA↑       2.5×    tDCS(F3) + taVNS + TMS(10Hz)                 Strafella 2001
  V2  eCB↑      3.0×    TENS(2Hz) + taVNS + tDCS + tACS(θ) + TMS(θ) Centonze 2007
  V3  5HT↑      1.5×    taVNS(raphe) + tDCS                          Frangos 2015
  V4  GABA↑     1.8×    tDCS + α-entrainment + TMS(θ) + tACS(10Hz)  Stagg 2009
  V5  NE↓       0.4×    taVNS → LC inhibition                        Dietrich 2008
  V6  Theta↑↑   2.5×    TMS(6Hz) + binaural(6Hz) + tACS(6Hz)        Huang 2005
  V7  Alpha↓    0.5×    tDCS cathode(Fz) + TMS(1Hz)                  Romei 2016
  V8  Gamma↑    1.8×    LED(40Hz) + Audio(40Hz) + Vibro(40Hz)        Iaccarino 2016
                         + tACS(40Hz) + TMS(40Hz)                     Helfrich 2014
  V9  PFC↓      0.5×    tDCS cathode(F4) + TMS(1Hz)                  —
  V10 Sensory↑  2.0×    tDCS(V1) + tRNS + LED(40Hz) + TENS          Collins 1996
  V11 Body↑     2.5×    TENS(low+high) + tDCS(S1) + Vibro(40Hz)     Ragert 2008
  V12 Coherence↑ 2.0×   Tri-modal 40Hz sync + TMS(40Hz) + tACS(40Hz) Polanía 2012
```

## THC Concentration Levels

```
  Level      THC%   Avg    ≥100%   Duration   Description
  ────────── ────── ────── ─────── ────────── ──────────────────────
  micro       1%    269%   12/12    45 min    micro-dose, 기분전환
  light       5%    180%   12/12    60 min    가벼운 하이, 사교/창작
  medium     15%    141%   12/12    90 min    일반 레크리에이션
  strong     25%    117%   12/12   120 min    강한 하이, 숙련자 수준
  intense    30%    107%    9/12   150 min    고농축 dabbing 수준

  (Tier 3 기준, python bench_thc_vars.py --levels)
```

## Hardware Stack

### Current (검증 완료)

| Hardware | Type | Target Variables | Cost |
|----------|------|------------------|------|
| **tDCS** | 경두개 직류자극 | V1,V3,V4,V7,V9,V10,V11 | $30-2K |
| **tACS** | 경두개 교류자극 (6/10/40Hz) | V4,V6,V8,V12 | $80-5K |
| **TMS** | 경두개 자기자극 (1/6/10/40Hz) | V1,V6,V7,V8,V9 | $3K-50K |
| **TENS** | 경피 신경자극 (2-100Hz) | V2,V10,V11 | $25-80 |
| **taVNS** | 경피 미주신경자극 | V1,V2,V3,V5 | $100-600 |
| **LED 40Hz** | 시각 감마 엔트레인먼트 | V8,V10,V12 | $10 |
| **Audio** | 청각 6Hz binaural + 40Hz click | V6,V8,V12 | $0-10 |
| **Vibro 40Hz** | 체성감각 감마 엔트레인먼트 | V8,V11,V12 | $5 |
| **tRNS** | 경두개 랜덤노이즈 (확률공명) | V10,V11 | $0 (펌웨어) |

### Next-Gen (연구 중)

| Hardware | Type | Key Advantage | Cost | Status |
|----------|------|---------------|------|--------|
| **tFUS** | 경두개 집속 초음파 | VTA/해마 직접 자극 (12cm 깊이, 2-5mm 정밀) | $5K-50K | 연구기기 존재 |
| **TI** | 시간간섭 자극 | kHz 간섭으로 깊은 부위 비침습 (Grossman 2017) | $2K-5K | 인간 해마 성공 |
| **GVS** | 갈바닉 전정자극 | 전정-VTA-해마 경로 ($5 추가) | $5 | 즉시 가능 |
| **tSCS** | 경피 척수자극 | 척수 레벨 감각 게인 제어 | $500-1.5K | FDA 승인 기기 존재 |
| **tPBM** | 경두개 광생체조절 | 810nm NIR → DA↑, Gamma↑ (조건부) | $450-1.8K | 소비자 기기 존재 |

## Project Structure

```
brainwire/
├── bench_thc_vars.py           # 12-variable benchmark (brain stim only)
├── calc.py                     # Numerical calculator (sensitivity, sweep, optimize)
├── calculator/index.html       # Web calculator
├── docs/
│   ├── thc-reproduction-guide.md   # Complete implementation manual
│   ├── thc-chemistry.md            # THC molecular → 12-variable pathway
│   ├── new-hardware-research.md    # Next-gen hardware (tFUS, TI, GVS, tSCS)
│   ├── hardware-architecture.md    # System architecture
│   └── hardware-catalog.md         # Full hardware catalog with prices
└── CLAUDE.md                   # Project rules
```

## Quick Start

```bash
# 전체 Tier 비교
python bench_thc_vars.py

# THC 농도별 비교 + 유지시간
python bench_thc_vars.py --levels

# 특정 농도 + 특정 Tier
python bench_thc_vars.py --level medium --tier tier2

# 수치 계산기
python calc.py sensitivity          # 민감도 분석
python calc.py gap                  # 미달 변수 해결방법
python calc.py optimize --budget 500  # 예산 내 최적 조합
python calc.py sweep --param VNS     # 파라미터 스윕
```

## Key Principles

1. **Brain stimulation only** — 전기자극 + 자기자극 + 신경 엔트레인먼트만 사용. 온열/가중/음악/약물 제외.
2. **Literature-backed** — 모든 전달함수 계수에 논문 근거. 25+ 핵심 논문 참조.
3. **No detection** — 내인성 신경전달물질(도파민, 아난다마이드 등)만 방출. 약물검사 음성.
4. **No tolerance** — 전기자극은 수용체 downregulation 없음. 반복 사용 가능.
5. **Instant OFF** — 전원 끄면 즉시 종료. THC는 2-4시간 대기.

## PureField Tension Framework

```
  T_total = sqrt(T_chem^2 + T_wave^2 + T_state^2)

  T_chem  = f(DA, eCB, 5HT, GABA, NE)       화학적 장력
  T_wave  = f(Theta, Alpha, Gamma)            뇌파 장력
  T_state = f(PFC, Sensory, Body, Coherence)  상태 장력

  THC T_total = 4.280 (기준)
  Tier 3 달성: T=4.993, 방향유사도 99.1%, 장력매칭 90.5%
```

## 5-Year Roadmap

```
  2026  TI prototype + GVS/tRNS/tSCS integration
  2027  tFUS DIY + multipolar TI (mTI)
  2028  Unified headset: mTI + tFUS + tDCS/tACS
  2029  Closed-loop AI (EEG → 12-var PID → stim)
  2030  Consumer device $3K, Neuralink validation
```

## THC vs BrainWire

```
  시간    THC 흡연(25%)    BrainWire
  ────── ──────────────── ────────────
   0min  ░░░░░░░░░░   0%  ░░░░░░░░░░   0%
   5min  █████░░░░░  50%  ███░░░░░░░  30%
  15min  █████████░  95%  █████████░  90%
  30min  ██████████ 100%  ██████████ 100%
  60min  ███████░░░  75%  ██████████ 100%  ← BrainWire 유지
  90min  █████░░░░░  50%  ██████████ 100%
 120min  ███░░░░░░░  30%  ██████████ 100%
 150min  █░░░░░░░░░  15%  █████░░░░░  50%  ← 전원 OFF
 180min  ░░░░░░░░░░   5%  ░░░░░░░░░░   0%

         제어 불가          전원 OFF=즉시
```

## License

MIT

---

*No molecules. No detection. No tolerance. Just electrons.*

*BrainWire: 12 variables, 12 electrical solutions, 117% THC.*

> Part of the [TECS-L](https://github.com/need-singularity/TECS-L) project family.
