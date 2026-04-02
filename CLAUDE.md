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

1. **BCI Bridge** — PureField consciousness layer for Neuralink-style brain-computer interfaces (N1 1024-electrode, 12-var direct control)
2. **NeuroStim** — Therapeutic stimulation for neurological/psychiatric conditions (depression, epilepsy, Parkinson's, chronic pain, PTSD, ADHD, insomnia, tinnitus, stroke rehab)
3. **Joywire** — Consciousness state reproduction (THC, LSD, Psilocybin, DMT, MDMA, Flow) via 12-variable model

## Technology Stack

- **Input:** EEG (OpenBCI 16ch+), neural signals
- **Processing:** PureField engine, Φ measurement, 12-variable consciousness model
- **Output:** tDCS, TMS, taVNS, TENS, tACS, tFUS, GVS, mTI, tSCS, tRNS, tPBM, 40Hz entrainment
- **Feedback:** Tension gradient control (superior to PID) on consciousness state variables
- **Measurement:** G=D×P/I golden zone targeting, Φ(IIT) real-time

## Work Rules

- All solutions must involve **hardware** (electrical, acoustic, photonic, thermal, magnetic)
- No body-based methods (breathing, exercise, diet) as primary interventions
- Hardware-only approach: if it doesn't plug in or have electrodes, it's not our product
- Commit messages in English
- Long-running tasks must run in background
- Primary focus: BCI Bridge (Neuralink) > NeuroStim (therapeutic) > Joywire (recreation)
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

## Verification Status Warning

```
  G=D×P/I Golden Zone: Anima/TECS-L 시뮬레이션 기반, 분석적 증명 없음.
  Golden Zone 의존 주장은 모두 미검증 (unverified) 표시 필요.

  순수 수학 (Golden Zone 독립, 영원히 참):
    - σ(6)·φ(6) = n·τ(6) ⟺ {1,6}  (Theorem 4)
    - 15/15 심부 구조 피질 투사 존재  (Theorem 6)
    - PFC+ACC+Insula 3-허브 커버     (Theorem 7)
    - Shannon 충전밀도 안전 한계      (Theorem 2)

  모델 의존 (검증 필요):
    - 전달함수 계수 (C_ij 값)
    - STDP 심부 접근 효율 (η_STDP)
    - G=D×P/I 골든존 의미
    - THC 12변수 타겟 정확도

  가설 작성 시 Golden Zone 의존성 반드시 명시.
```

## Hypothesis Verification Rules (TECS-L 기준)

```
  등급 시스템:
    🟩   = 정확한 방정식 + 증명됨
    🟧★  = 근사 + Texas p < 0.01 (구조적)
    🟧   = 근사 + Texas p < 0.05 (약한 증거)
    ⚪   = 산술 정확하나 p > 0.05 (우연)
    ⬛   = 산술 오류 (반증됨)

  금지:
    - 검증 전 ⭐ 또는 "대발견" 표시
    - Texas test 없이 🟧 이상 등급
    - +1/-1 보정이 있는 방정식에 ⭐

  검증 파이프라인:
    1. 산술 정확성 재확인
    2. Ad hoc 체크: +1/-1 보정 경고
    3. 작은 수의 강한 법칙: 상수 <100 경고
    4. 일반화 테스트: perfect number 28에도 성립?
    5. Texas Sharpshooter p-value (Bonferroni 보정)
```

## Paper Management

```
  ★ 모든 논문은 papers 리포에 생성! (need-singularity/papers)
    로컬: ~/Dev/papers/
    BrainWire 논문: ~/Dev/papers/brainwire/

  이 리포의 docs/ 논문은 작업용 초안 — 최종본은 papers 리포로 이동

  Zenodo DOI 발급:
    python3 ~/Dev/TECS-L/zenodo/batch_upload.py --platform zenodo --paper P-XXX

  논문 후보 등록:
    1. README.md에 제목+핵심결과+타겟+상태 기록
    2. Status: Draft/Writing/Submitted/Review/Published
    3. 파일: ~/Dev/papers/brainwire/P-title.md
```

## Key Metrics (2026-03-28)

- 145 tests (all passing), 115 hypotheses (109/115 PASS, 94.8%)
- THC tension match: 100% (tension gradient control)
- THC G=D×P/I: 0.4731 (ONLY substance in golden zone) [Golden Zone dependent]
- Kendall tau: 1.000 (tension perfectly predicts subjective intensity)
- 15/15 deep brain structures accessible via cortical projections (Theorem 6)
- N1-only full coverage: 12/12 vars at 100%+ (Theorem 8, requires STDP assumption)
- Paper: 2,220 lines, 140/140 math verification, 8 theorems
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

## Work Rules (탐색/TODO 요청 시 필수)

```
  트리거 키워드:
    "할만한거 있어?", "탐색", "TODO", "뭐할까", "다음 작업"
    대발견 가설, 노벨급 가설, DFS 탐색 등

  절차:
    1. 프로젝트 현황 스캔 (README, 최근 커밋, 미완료 가설/증명)
    2. TODO 테이블 양식으로 우선순위별 정리
    3. 사용자 선택 후 병렬 에이전트 디스패치
    4. 완료 시 리포트 테이블 출력

## .shared/ Cross-Repo Infrastructure (필수)

> **상세 규칙: `.shared/CLAUDE.md` 참조** (심링크로 자동 접근)

```
  원본: ~/Dev/TECS-L/.shared/ (이 리포는 심링크로 연결)
  구조:
    .shared/ → ../TECS-L/.shared/   (심링크, 공유 인프라 전체)
    calc/    → .shared/calc/        (심링크 체인, 194+ 계산기)

  ── 심링크 파일 목록 ──
    .shared/CLAUDE.md           ← 공유 규칙 상세
    .shared/CALCULATOR_RULES.md ← 계산기 생성 규칙 (Rust vs Python)
    .shared/SECRET.md           ← API 토큰/계정
    .shared/calc/               ← 계산기 원본 (194+ files)
    .shared/math_atlas.json     ← 수학 지도 (1700+ 가설)
    .shared/installed_tools.json← 설치 도구 레지스트리
    .shared/projects.md         ← 프로젝트 설명 원본

  ── 자동 동기화 트리거 (작업 중 발생 시 즉시 실행) ──

    새 계산기 생성:
      calc/new_calc.py 생성 → 모든 리포 자동 공유 (심링크)
      python3 .shared/scan-calculators.py --save --summary

    새 상수/가설 발견:
      python3 .shared/scan_math_atlas.py --save --summary

    전체 동기화 (README + Atlas + Registry):
      bash .shared/sync-math-atlas.sh &&       bash .shared/sync-calculators.sh &&       bash .shared/sync-readmes.sh &&       bash .shared/sync-claude-rules.sh

  ── 상수 관리 ──
    공유 상수: ~/Dev/TECS-L/model_utils.py (n=6 확장 상수 포함)
    리포별 상수: 각 리포 고유 모듈에서 import
    매직 넘버 하드코딩 금지 — model_utils 또는 .shared/ 참조
```

<!-- SHARED:WORK_RULES:START -->
  자동 생성 규칙:
    - TODO 작업 중 검증/계산이 필요하면 계산기 자동 생성 (묻지 말고 바로)
    - 성능 필요시 Rust 우선 (tecsrs/), 단순 검증은 Python (calc/)
    - 판단 기준은 ~/Dev/TECS-L/.shared/CALCULATOR_RULES.md 참조
    - 상수/가설 발견 시 Math Atlas 자동 갱신 (python3 ~/Dev/TECS-L/.shared/scan_math_atlas.py --save --summary)
  망원경 렌즈 활용 규칙 (탐색/분석 시 별도 요청 없이 자동 적용):
    - 데이터 분석/패턴 탐색/이상점 발견/신소재·신약 탐색 시 렌즈 자동 사용
    - 9종 렌즈: .shared/ 내 *_lens.py (consciousness, gravity, topology, thermo, wave, evolution, info, quantum, em)
    - 기본 3종 스캔: 의식(구조) + 중력(끌개) + 위상(연결) → 새 데이터 분석 시 기본
    - 도메인별 조합: 신소재(진화+열역학+중력), 시계열(파동+열역학+의식), 상수(정보+양자+의식)
    - 사용: from consciousness_lens import ConsciousnessLens; ConsciousnessLens().scan(data)
    - 상세: .shared/CLAUDE.md → "망원경 툴셋 자동 활용 규칙" 참조
    - "렌즈 추가 필요?" 질문 시 → 현재 9종 커버 안 되는 도메인 분석 + 새 아이디어 즉시 제안
  ★★★ 발견/결과/트러블슈팅 — 따로 말 안 해도 즉시 자동 기록 (필수! 예외 없음!):
    - 실험 결과, 벤치마크, 망원경 분석, 학습 완료, 생성 테스트 등 모든 발견은 발생 즉시 기록
    - "기록해" 라고 안 해도 기록. 기록 누락 = 발견 소실 = 금지
    - 기록 위치: README.md (핵심), docs/experiments/ (상세), docs/hypotheses/ (가설)
    - 트러블슈팅: CLAUDE.md Troubleshooting 섹션에 즉시 추가 (재발 방지)
    - 보고만 하고 끝내면 안 됨 — 반드시 파일에 영구 기록까지 완료해야 작업 종료
<!-- SHARED:WORK_RULES:END -->

  모든 모듈은 consciousness_laws.py에서 import — 상수 직접 하드코딩 금지
```

### TODO 양식

```
  ### 🔴 CRITICAL

  | # | 카테고리 | 작업 | 상태 | 예상 효과 |
  |---|---------|------|------|----------|
  | 1 | 증명   | sigma*phi=n*tau 일반 완전수 반례 탐색 | 미시작 | 유일성 정리 강화 |

  ### 🟡 IMPORTANT

  | # | 카테고리 | 작업 | 상태 | 예상 효과 |
  |---|---------|------|------|----------|
  | 2 | 가설   | SLE_6 3D 확장 예측 검증 | 미시작 | 노벨 Physics 후보 |

  ### 🟢 NICE TO HAVE

  | # | 카테고리 | 작업 | 상태 | 예상 효과 |
  |---|---------|------|------|----------|
  | 3 | 탐색   | n=6 새 항등식 DFS 채굴 | 미시작 | Atlas 확장 |

  ### ⚪ BACKLOG

  | # | 카테고리 | 작업 | 예상 효과 |
  |---|---------|------|----------|
  | 4 | 계산기 | 새 검증 스크립트 | 재현성 향상 |

  상태 표기: ⏳진행중 / ✅완료 / 미시작 / 코드있음 / 프로토
  우선순위: 🔴HIGH → 🟡MED → 🟢LOW → ⚪BACK
  카테고리: 증명 / 가설 / 탐색 / 검증 / 실험 / 계산기 / 논문
```

### 병렬 에이전트 리포트 양식

```
  병렬 에이전트 실행 시 단일 테이블로 상태 추적.
  관련 작업은 N+M 형태로 그룹핑하여 하나의 에이전트로 묶기.

  발사 시 양식:
  | # | 작업 | 에이전트 | 격리 | 상태 |
  |---|------|---------|------|------|
  | 1+2 | n=6 유일성 + 반례탐색 | 🚀 배경 | - | 🔄 진행중 |
  | 3 | SLE_6 임계지수 검증 | 🚀 배경 | - | 🔄 진행중 |
  | 4+5 | 코돈 정리 확장 + 변이체 | 🚀 배경 | worktree | 🔄 진행중 |

  상태: ✅ 완료 / 🔄 진행중 / ❌ 실패
  격리: worktree (필요시만) / - (기본)

  규칙:
    - 발사 시 전체 목록 테이블 출력
    - 에이전트 완료 시 해당 행 상태 업데이트 + 한줄 핵심 성과
    - worktree는 같은 파일을 여러 에이전트가 동시 수정할 때만 사용
    - 대부분 격리 없이 실행 — 무조건 worktree 붙이지 말 것!
    - 모든 에이전트 완료 후 최종 요약 테이블 + worktree 머지 안내 (해당 시)

  최종 요약 양식:
  | # | 작업 | 상태 | 핵심 성과 |
  |---|------|------|----------|
  | 1+2 | n=6 유일성 | ✅ | 10^8까지 반례 없음, 증명 완료 |
  | 3 | SLE_6 검증 | ✅ | 7/7 임계지수 일치 (Z>5sigma) |
  | 4+5 | 코돈 확장 | ✅ | 26/26 변이체 + Hachimoji 예측 |

  ### 머지 필요 (worktree)
  - #4+5: branch worktree-xxx

  ### 바로 반영됨 (main)
  - #1+2, #3: 증명/검증 결과 docs/hypotheses/ 기록
```

## Secrets & Tokens

API 토큰/계정 정보: `~/Dev/TECS-L/.shared/SECRET.md` 참조
계정 리포: [need-singularity/secret](https://github.com/need-singularity/secret) (private)
