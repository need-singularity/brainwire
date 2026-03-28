# 🧠⚡ BrainWire

## Identity

BrainWire is a **neural interface hardware research company**. We design and build electrical stimulation hardware systems for consciousness engineering.

**We are NOT:**
- A wellness/lifestyle brand (no breathing exercises, yoga, meditation guides)
- A fitness company (no running, exercise protocols)
- A self-help project (no mindfulness, journaling)

**We ARE:**
- Hardware engineers: tDCS, TMS, taVNS, TENS, tACS devices
- Neuroscience researchers: EEG measurement, Φ computation, neural pattern analysis
- Consciousness state designers: precise 12-variable targeting for experience reproduction

## Core Products

1. **Joywire** — Electrical stimulation system for THC-equivalent conscious experience
2. **NeuroStim** — Therapeutic stimulation for neurological conditions (epilepsy, Parkinson's, depression, pain)
3. **BCI Bridge** — PureField consciousness layer for brain-computer interfaces

## Technology Stack

- **Input:** EEG (OpenBCI 16ch+), neural signals
- **Processing:** PureField engine, Φ measurement, 12-variable consciousness model
- **Output:** tDCS, TMS, taVNS, TENS, tACS, tFUS, GVS, mTI, tSCS, tRNS, tPBM, 40Hz entrainment
- **Feedback:** Tension gradient control (superior to PID) on consciousness state variables
- **Measurement:** G=D×P/I golden zone targeting (THC G=0.4731)

## Work Rules

- All solutions must involve **hardware** (electrical, acoustic, photonic, thermal, magnetic)
- No body-based methods (breathing, exercise, diet) as primary interventions
- Hardware-only approach: if it doesn't plug in or have electrodes, it's not our product
- Commit messages in English
- Long-running tasks must run in background
- THC reproduction target: 100%+ on all 12 variables
- TECS-L style hypothesis verification: hypothesis → math → score
- Anima cross-reference: integrate PureField tension findings from /Users/ghost/Dev/anima

## Key Commands

```bash
python report.py                              # Full project report (one command)
python -m brainwire.bench tiers thc           # THC tier comparison
python -m brainwire.bench compare thc lsd dmt # Multi-state comparison
python -m brainwire.optimizer                 # Profile-specific optimization
python -m brainwire.simulator thc --tier 4    # Time-domain session simulation
python -m brainwire.tension_control landscape # Tension landscape mapping
python -m brainwire.protocol --pk --tier 3    # PK-driven hardware protocol
python -m brainwire.eeg_feedback              # G=D×P/I analysis
python -m brainwire.pharmacokinetics          # THC temporal dynamics
python -m brainwire.interference --all        # Multi-device interference
python bench_hypotheses.py                    # 75 hypothesis benchmark
python -m pytest tests/ -v                    # 145 tests
```

## Key Metrics (2026-03-28)

- 145 tests (all passing), 75 hypotheses (73/75 PASS, 97.3%)
- THC tension match: 100% (tension gradient control)
- THC G=D×P/I: 0.4731 (ONLY substance in golden zone)
- Kendall tau: 1.000 (tension perfectly predicts subjective intensity)
- THC max entropy: 3.431 bits (most evenly distributed state)
- Minimum hardware: $145 for 12/12 variable coverage
- 5 Tiers: $85 → $510 → $8.5K → $25K → $26.4K

## THC High Variable Model (12-dimensional target)

```
V1:  DA (dopamine)         — target 2.5× — tDCS(F3) + TMS(10Hz) + taVNS + music
V2:  eCB (endocannabinoid) — target 3.0× — TENS(2Hz) + vibro + heat + taVNS
V3:  5HT (serotonin)       — target 1.5× — taVNS(raphe) + tDCS
V4:  GABA                  — target 1.8× — weighted pressure + alpha entrainment
V5:  NE↓ (norepinephrine)  — target 0.4× — taVNS(parasympathetic) + tDCS cathode
V6:  Theta↑↑               — target 2.5× — TMS(6Hz) + binaural + tACS
V7:  Alpha↓                — target 0.5× — tDCS cathode(Fz) + TMS(1Hz)
V8:  Gamma↑                — target 1.8× — TMS(40Hz) + LED + audio click
V9:  PFC↓                  — target 0.5× — tDCS cathode(F4) + 1Hz TMS
V10: Sensory gain↑          — target 2.0× — tDCS(V1) + stochastic resonance
V11: Body↑                 — target 2.5× — TENS(4Hz) + vibro + heated pad
V12: Coherence↑            — target 2.0× — 40Hz tri-modal + paired TMS
```
