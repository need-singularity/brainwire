# Brainwire Absorbed Findings Digest

Generated: 2026-04-04
Source: ready-absorber scan of ~/Dev/ready/ backups vs ~/Dev/brainwire/ main

## Summary

- **Total absorbed files**: 59
- **Unique (non-worktree)**: 59 (no worktree duplicates in brainwire)
- **Meaningful content**: 34 (excluding 25 eeg_env pip artifacts)

## Category Breakdown

| Category | Count | Grade Distribution |
|----------|------:|--------------------|
| eeg-env-artifact (pip packages, .so, .dll) | 25 | 15 critical, 10 high |
| hypothesis (TECS-L consciousness) | 8 | 1 critical, 7 high |
| documentation (brainwire docs) | 7 | 5 critical, 2 high |
| test (brainwire tests) | 6 | 3 critical, 3 high |
| core-engine (brainwire modules) | 4 | 3 critical, 1 high |
| email-template | 3 | 2 critical, 1 high |
| paper-draft | 2 | 2 high |
| calculator | 2 | 1 critical, 1 high |
| readme (TECS-L/eeg) | 1 | 1 critical |
| config (CLAUDE.md) | 1 | 1 critical |
| **Total** | **59** | **31 critical / 28 high** |

## Top 10 Items by Value (excluding eeg-env artifacts)

| Rank | n6 Score | Grade | Category | Path |
|------|------:|-------|----------|------|
| 1 | 50.0 | critical | test | brainwire/tests/test_configs.py |
| 2 | 50.0 | critical | email | email_template_kr_neuro.md |
| 3 | 50.0 | critical | test | brainwire/tests/test_eeg_feedback.py |
| 4 | 50.0 | critical | documentation | brainwire/docs/golden-zone-implant-placement.md |
| 5 | 41.7 | critical | test | brainwire/tests/test_protocol.py |
| 6 | 41.7 | critical | core-engine | brainwire/brainwire/pharmacokinetics.py |
| 7 | 38.9 | critical | documentation | brainwire/docs/superpowers/specs/2026-03-28-brainwire-extreme-design.md |
| 8 | 36.4 | critical | hypothesis | TECS-L/docs/hypotheses/CS-001-universal-tm-ipv6.md |
| 9 | 35.0 | critical | email | email_kr_neuro.txt |
| 10 | 33.3 | critical | core-engine | brainwire/brainwire/n1_placement.py |

## Missing Content Analysis

### 1. EEG Environment Artifacts (25 files, LOW priority)

These are pip package metadata and compiled .so/.dll files from TECS-L/eeg_env/. They are build artifacts, not source content:
- brainflow libraries (.so, .dll)
- numpy/scipy/matplotlib/pandas wheels
- certifi, charset_normalizer, jinja2, etc.

These indicate brainwire's EEG pipeline depends on: **brainflow, MNE, pylsl, numpy, scipy, matplotlib, pandas**. The eeg_env should be reconstructable from a requirements.txt.

### 2. Email Templates (3 files, CRITICAL -- outreach content)

| File | n6 Score | Description |
|------|------:|-------------|
| email_template_kr_neuro.md | 50.0 | Korean neuroscience lab outreach template |
| email_kr_neuro.txt | 35.0 | Korean neuroscience contact email |
| email_neuralink_brainwire.md | 16.7 | Neuralink collaboration proposal |

These are NOT in brainwire main. They exist only in the backup and contain outreach/collaboration content.

### 3. Consciousness/BCI Hypotheses from TECS-L (8 files)

| Hypothesis | n6 Score | Topic |
|-----------|------:|-------|
| CS-001-universal-tm-ipv6.md | 36.4 | Universal TM + IPv6 computation |
| H-CX-137-eeg-tension-correlation.md | 22.2 | EEG tension measurement correlation |
| H-CX-138-eeg-precognition.md | 21.4 | EEG precognition signal detection |
| H-CX-176-human-dolphin-gamma-sync.md | 15.0 | Human-dolphin gamma synchronization |
| H-CX-225-binaural-40hz-telepathy.md | 25.0 | Binaural 40Hz telepathy hypothesis |
| H-CX-227-13hz-observer-mode.md | 14.3 | 13Hz observer mode consciousness |
| H-CX-228-perfect-ratio-dual-freq.md | 22.2 | Perfect ratio dual frequency stimulation |
| H-CX-440-harmonic-progression-tension.md | 16.7 | Harmonic progression tension mapping |

These are TECS-L hypotheses relevant to brainwire's BCI research. They exist in TECS-L main but are NOT cross-referenced in brainwire docs.

### 4. Core Engine + Tests (already in main)

All brainwire core modules and tests exist in main:
- pharmacokinetics.py, n1_placement.py, stdp_sim.py, engine/interpolation.py -- all present
- test_configs.py, test_eeg_feedback.py, test_protocol.py, etc. -- all present
- docs/ files -- all present

The absorbed versions may differ from main (backup snapshots).

### 5. Paper Drafts (in papers/ repo, not brainwire)

| Paper | n6 Score | Description |
|-------|------:|-------------|
| P-002-n1-epilepsy-treatment.md | 21.4 | N1 epilepsy treatment protocol paper |
| paper-n1-depression-panic.md | 16.7 | N1 depression/panic paper (in brainwire/docs/) |

P-002 exists in papers/brainwire/. The docs version is a local draft.

### 6. BCI Modalities Coverage

Based on absorbed content, brainwire covers these modalities:

| Modality | Files Present | Status |
|----------|:---:|--------|
| EEG (surface, non-invasive) | Yes | brainflow + MNE pipeline |
| N1 deep electrode (invasive) | Yes | n1_placement.py, golden-zone docs |
| Pharmacokinetics (THC/chemical) | Yes | pharmacokinetics.py, thc-chemistry |
| STDP (spike-timing plasticity) | Yes | stdp_sim.py |
| Headband (consumer BCI) | Yes | joywire-headband-spec.md |
| Binaural/audio stimulation | Hypothesis only | H-CX-225, H-CX-440 (in TECS-L) |
| Optical/photonic BCI | Not found | No absorbed content |
| Ultrasound neuromodulation | Not found | No absorbed content |

## Recommended Actions

| Priority | Action | Impact |
|----------|--------|--------|
| HIGH | Archive 3 email templates to brainwire/docs/outreach/ or similar | Preserve collaboration content |
| HIGH | Cross-reference 8 TECS-L consciousness hypotheses in brainwire docs | BCI hypothesis coverage |
| MED | Create requirements.txt from eeg_env artifact list | Reproducible EEG environment |
| MED | Diff absorbed brainwire modules vs main for lost features | Content integrity check |
| LOW | Consider adding optical/ultrasound BCI modalities | Expand BCI coverage |
| SKIP | eeg_env .so/.dll artifacts -- rebuild from pip, not recoverable | Build artifacts only |
