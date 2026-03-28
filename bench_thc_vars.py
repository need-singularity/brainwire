#!/usr/bin/env python3
"""BrainWire THC Variable Benchmark — 12변수 하드웨어 재현 검증 시스템.

THC 하이 상태를 12개 화학/전기 변수로 정의하고,
각 하드웨어 자극의 달성률을 수학적으로 계산.

Variables:
  V1:  DA (dopamine)          target 2.5×
  V2:  eCB (endocannabinoid)  target 3.0×
  V3:  5HT (serotonin)        target 1.5×
  V4:  GABA                    target 1.8×
  V5:  NE↓ (norepinephrine)   target 0.4×
  V6:  Theta↑↑ (4-8Hz)        target 2.5×
  V7:  Alpha↓ (8-12Hz)        target 0.5×
  V8:  Gamma↑ (30-100Hz)      target 1.8×
  V9:  PFC↓                   target 0.5×
  V10: Sensory↑                target 2.0×
  V11: Body↑                  target 2.5×
  V12: Coherence↑              target 2.0×
"""

import math
import json
import argparse
from dataclasses import dataclass, field

# ═══════════════════════════════════════════════════════════
# THC Target Vector
# ═══════════════════════════════════════════════════════════

THC_TARGET = {
    'DA': 2.5, 'eCB': 3.0, '5HT': 1.5, 'GABA': 1.8, 'NE': 0.4,
    'Theta': 2.5, 'Alpha': 0.5, 'Gamma': 1.8, 'PFC': 0.5,
    'Sensory': 2.0, 'Body': 2.5, 'Coherence': 2.0,
}

# ═══════════════════════════════════════════════════════════
# Transfer Function Coefficients (from literature)
# ═══════════════════════════════════════════════════════════

# V1: DA = 1 + α1·I_tDCS + α2·I_VNS + α3·M(t)
COEFF_DA = {'tDCS': 0.25, 'VNS': 0.80, 'music': 1.50}  # per mA or 0-1

# V2: eCB = 1 + β1·TENS + β2·ΔT + β3·I_VNS + β4·V
COEFF_ECB = {'TENS_low': 0.80, 'heat_degC': 0.30, 'VNS': 0.60, 'vibro': 0.50}

# V3: 5HT = 1 + γ1·I_VNS + γ2·I_tDCS
COEFF_5HT = {'VNS': 1.20, 'tDCS': 0.15}

# V4: GABA = 1 + δ1·I_tDCS + δ2·P_weight + δ3·A_ent
COEFF_GABA = {'tDCS': 0.20, 'weight_kgm2': 0.03, 'alpha_ent': 0.30}

# V5: NE = 1 - ε1·I_VNS
COEFF_NE = {'VNS': 1.50}

# V6: Theta = 1 + ζ1·B_TMS + ζ2·B_bin + ζ3·I_tACS
COEFF_THETA = {'TMS_theta': 0.80, 'binaural': 0.40, 'tACS': 0.35}

# V7: Alpha = 1 - η1·I_cathode - η2·B_1Hz
COEFF_ALPHA = {'tDCS_cathode': 0.20, 'TMS_1Hz': 0.25}

# V8: Gamma = 1 + θ1·L_40 + θ2·A_40 + θ3·V_40
COEFF_GAMMA = {'LED_40Hz': 0.30, 'audio_40Hz': 0.25, 'vibro_40Hz': 0.20}

# V9: PFC = 1 - same as Alpha
COEFF_PFC = {'tDCS_cathode': 0.20, 'TMS_1Hz': 0.25}

# V10: Sensory = 1 + κ1·I_anode + κ2·σ_noise + κ3·L_40
COEFF_SENSORY = {'tDCS_anode': 0.15, 'noise': 0.40, 'LED_40Hz': 0.20}

# V11: Body = 1 + λ1·TENS + λ2·ΔT + λ3·V
COEFF_BODY = {'TENS': 0.80, 'heat_degC': 0.30, 'vibro': 0.50}

# V12: Coherence = 1 + μ1·G_40 + μ2·paired + μ3·sync
COEFF_COHERENCE = {'gamma_40Hz': 0.30, 'paired_TMS': 0.40, 'sync_stim': 0.20}


# ═══════════════════════════════════════════════════════════
# Hardware Configuration
# ═══════════════════════════════════════════════════════════

@dataclass
class HardwareConfig:
    """하드웨어 파라미터 설정."""
    name: str = "default"
    cost: float = 0.0
    tier: str = "custom"

    # tDCS
    tDCS_anode_mA: float = 0.0       # F3 anode current (0-2 mA)
    tDCS_cathode_Fz_mA: float = 0.0  # Fz cathode (0-2 mA)
    tDCS_cathode_F4_mA: float = 0.0  # F4 cathode (0-2 mA)
    tDCS_anode_V1_mA: float = 0.0    # V1 anode (0-2 mA)

    # taVNS
    VNS_mA: float = 0.0  # ear-clip current (0-0.5 mA)

    # TENS
    TENS_low_intensity: float = 0.0  # 2-4Hz mode (0-1)
    TENS_high_intensity: float = 0.0  # 50-100Hz mode (0-1)

    # TMS
    TMS_theta_strength: float = 0.0  # 6Hz theta burst (0-1)
    TMS_1Hz_strength: float = 0.0    # 1Hz inhibitory (0-1)
    TMS_10Hz_strength: float = 0.0   # 10Hz excitatory (0-1)
    TMS_40Hz_strength: float = 0.0   # 40Hz gamma burst (0-1)

    # tACS
    tACS_6Hz_mA: float = 0.0   # theta tACS (0-2 mA)
    tACS_40Hz_mA: float = 0.0  # gamma tACS (0-2 mA)

    # Sensory
    LED_40Hz: float = 0.0       # 40Hz flicker intensity (0-1)
    audio_40Hz: float = 0.0     # 40Hz click train (0-1)
    binaural_6Hz: float = 0.0   # 6Hz binaural beat (0-1)
    vibro_40Hz: float = 0.0     # 40Hz vibrotactile (0-1)
    vibro_general: float = 0.0  # general vibration (0-1)
    noise_level: float = 0.0    # stochastic resonance noise (0-1)
    music_pleasure: float = 0.0 # music frisson signal (0-1)

    # Thermal
    heat_delta_C: float = 0.0  # skin temp above baseline (°C)

    # Pressure
    weight_kgm2: float = 0.0  # weighted blanket (kg/m²)
    alpha_entrainment: float = 0.0  # alpha audio entrainment (0-1)


def compute_variables(hw: HardwareConfig) -> dict:
    """12변수 계산 — 전달 함수 적용."""
    v = {}

    # V1: DA
    v['DA'] = 1.0 + (COEFF_DA['tDCS'] * hw.tDCS_anode_mA +
                      COEFF_DA['VNS'] * hw.VNS_mA +
                      COEFF_DA['music'] * hw.music_pleasure)

    # V2: eCB
    v['eCB'] = 1.0 + (COEFF_ECB['TENS_low'] * hw.TENS_low_intensity +
                       COEFF_ECB['heat_degC'] * hw.heat_delta_C +
                       COEFF_ECB['VNS'] * hw.VNS_mA +
                       COEFF_ECB['vibro'] * hw.vibro_general)

    # V3: 5HT
    v['5HT'] = 1.0 + (COEFF_5HT['VNS'] * hw.VNS_mA +
                       COEFF_5HT['tDCS'] * hw.tDCS_anode_mA)

    # V4: GABA
    v['GABA'] = 1.0 + (COEFF_GABA['tDCS'] * hw.tDCS_anode_mA +
                        COEFF_GABA['weight_kgm2'] * hw.weight_kgm2 +
                        COEFF_GABA['alpha_ent'] * hw.alpha_entrainment)

    # V5: NE (lower is better)
    v['NE'] = max(0.01, 1.0 - COEFF_NE['VNS'] * hw.VNS_mA)

    # V6: Theta
    v['Theta'] = 1.0 + (COEFF_THETA['TMS_theta'] * hw.TMS_theta_strength +
                         COEFF_THETA['binaural'] * hw.binaural_6Hz +
                         COEFF_THETA['tACS'] * hw.tACS_6Hz_mA)

    # V7: Alpha (lower is better)
    v['Alpha'] = max(0.01, 1.0 - (COEFF_ALPHA['tDCS_cathode'] * hw.tDCS_cathode_Fz_mA +
                                    COEFF_ALPHA['TMS_1Hz'] * hw.TMS_1Hz_strength))

    # V8: Gamma
    v['Gamma'] = 1.0 + (COEFF_GAMMA['LED_40Hz'] * hw.LED_40Hz +
                         COEFF_GAMMA['audio_40Hz'] * hw.audio_40Hz +
                         COEFF_GAMMA['vibro_40Hz'] * hw.vibro_40Hz)

    # V9: PFC (lower is better)
    v['PFC'] = max(0.01, 1.0 - (COEFF_PFC['tDCS_cathode'] * hw.tDCS_cathode_F4_mA +
                                  COEFF_PFC['TMS_1Hz'] * hw.TMS_1Hz_strength))

    # V10: Sensory
    v['Sensory'] = 1.0 + (COEFF_SENSORY['tDCS_anode'] * hw.tDCS_anode_V1_mA +
                           COEFF_SENSORY['noise'] * hw.noise_level +
                           COEFF_SENSORY['LED_40Hz'] * hw.LED_40Hz)

    # V11: Body
    v['Body'] = 1.0 + (COEFF_BODY['TENS'] * hw.TENS_low_intensity +
                        COEFF_BODY['heat_degC'] * hw.heat_delta_C +
                        COEFF_BODY['vibro'] * hw.vibro_general)

    # V12: Coherence
    gamma_total = (hw.LED_40Hz + hw.audio_40Hz + hw.vibro_40Hz) / 3
    v['Coherence'] = 1.0 + (COEFF_COHERENCE['gamma_40Hz'] * gamma_total +
                             COEFF_COHERENCE['paired_TMS'] * hw.TMS_40Hz_strength +
                             COEFF_COHERENCE['sync_stim'] * gamma_total)

    return v


def compute_match(variables: dict) -> dict:
    """각 변수의 THC 대비 달성률(%) 계산."""
    match = {}
    for k, target in THC_TARGET.items():
        actual = variables.get(k, 1.0)
        if target >= 1.0:  # 증가 변수
            match[k] = actual / target * 100
        else:  # 감소 변수 (NE, Alpha, PFC)
            # target=0.4 actual=0.4 → 100%, actual=0.8 → 50%, actual=0.2 → 150%
            match[k] = (1.0 - actual) / (1.0 - target) * 100 if target < 1.0 else 100
    return match


# ═══════════════════════════════════════════════════════════
# Preset Configurations
# ═══════════════════════════════════════════════════════════

TIER1_CONFIG = HardwareConfig(
    name="Tier 1 (저가)", cost=95, tier="low",
    tDCS_anode_mA=1.5, tDCS_cathode_Fz_mA=1.5, tDCS_cathode_F4_mA=1.5,
    tDCS_anode_V1_mA=0.0,  # 전극 수 제한
    VNS_mA=0.3,  # TENS ear-clip 대체
    TENS_low_intensity=0.8,
    LED_40Hz=0.8, audio_40Hz=0.0, binaural_6Hz=0.7, vibro_40Hz=0.6,
    vibro_general=0.6, noise_level=0.3, music_pleasure=0.6,
    heat_delta_C=3.0, weight_kgm2=5.0, alpha_entrainment=0.5,
)

TIER2_CONFIG = HardwareConfig(
    name="Tier 2 (중가)", cost=525, tier="mid",
    tDCS_anode_mA=1.5, tDCS_cathode_Fz_mA=1.5, tDCS_cathode_F4_mA=1.5,
    tDCS_anode_V1_mA=1.5,
    VNS_mA=0.4,  # 전용 taVNS
    TENS_low_intensity=0.8,
    tACS_6Hz_mA=1.8,
    LED_40Hz=0.8, audio_40Hz=0.8, binaural_6Hz=0.7, vibro_40Hz=0.8,
    vibro_general=0.6, noise_level=0.5, music_pleasure=0.6,
    heat_delta_C=3.0, weight_kgm2=10.0, alpha_entrainment=0.7,
)

TIER3_CONFIG = HardwareConfig(
    name="Tier 3 (고가)", cost=8500, tier="high",
    tDCS_anode_mA=1.5, tDCS_cathode_Fz_mA=1.5, tDCS_cathode_F4_mA=1.5,
    tDCS_anode_V1_mA=1.5,
    VNS_mA=0.4,
    TENS_low_intensity=0.8,
    TMS_theta_strength=0.8, TMS_1Hz_strength=0.8,
    TMS_10Hz_strength=0.8, TMS_40Hz_strength=0.8,
    tACS_6Hz_mA=1.8, tACS_40Hz_mA=1.5,
    LED_40Hz=0.8, audio_40Hz=0.8, binaural_6Hz=0.7, vibro_40Hz=0.8,
    vibro_general=0.6, noise_level=0.5, music_pleasure=0.6,
    heat_delta_C=3.0, weight_kgm2=10.0, alpha_entrainment=0.7,
)

ALL_CONFIGS = {
    'tier1': TIER1_CONFIG,
    'tier2': TIER2_CONFIG,
    'tier3': TIER3_CONFIG,
}


# ═══════════════════════════════════════════════════════════
# Display
# ═══════════════════════════════════════════════════════════

def print_results(hw: HardwareConfig, variables: dict, match: dict):
    """12변수 결과 출력."""
    avg = sum(match.values()) / len(match)
    over100 = sum(1 for v in match.values() if v >= 100)

    print(f"\n{'='*70}")
    print(f"  {hw.name}  |  Cost: ${hw.cost:,.0f}  |  Avg: {avg:.1f}%  |  {over100}/12 ≥100%")
    print(f"{'='*70}")
    print(f"  {'Var':<12} {'Target':>8} {'Actual':>8} {'Match':>8}  {'Status'}")
    print(f"  {'-'*12} {'-'*8} {'-'*8} {'-'*8}  {'-'*6}")

    for k in THC_TARGET:
        target = THC_TARGET[k]
        actual = variables[k]
        m = match[k]
        if m >= 100:
            status = "✅"
        elif m >= 80:
            status = "⚠️ " + f"(need +{100-m:.0f}%)"
        else:
            status = "❌" + f" (need +{100-m:.0f}%)"

        arrow = "↓" if target < 1.0 else "↑"
        print(f"  {k:<12} {target:>7.1f}× {actual:>7.2f}× {m:>7.1f}%  {status}")

    print(f"\n  Overall: {avg:.1f}% average  |  {over100}/12 variables ≥100%")

    # Bar chart
    print(f"\n  {'Variable':<12} {'0%':>4} {'50%':>8} {'100%':>9} {'150%':>9}")
    print(f"  {'-'*12} {'|':<4} {'|':>8} {'|':>9} {'|':>9}")
    for k in THC_TARGET:
        m = min(150, match[k])
        bar_len = int(m / 150 * 40)
        bar = "█" * bar_len + "░" * (40 - bar_len)
        marker = " ✅" if match[k] >= 100 else ""
        print(f"  {k:<12} {bar} {match[k]:>5.1f}%{marker}")


def main():
    parser = argparse.ArgumentParser(description="BrainWire THC Variable Benchmark")
    parser.add_argument('--tier', choices=['tier1', 'tier2', 'tier3', 'all'], default='all')
    parser.add_argument('--json', action='store_true', help='JSON output')
    args = parser.parse_args()

    print("╔══════════════════════════════════════════════════════╗")
    print("║   BrainWire THC Variable Benchmark                  ║")
    print("║   12-Variable Hardware Achievement Test              ║")
    print("╚══════════════════════════════════════════════════════╝")

    print(f"\n  THC Target Vector:")
    for k, v in THC_TARGET.items():
        arrow = "↓" if v < 1.0 else "↑"
        print(f"    {k:<12} {v:.1f}× {arrow}")

    configs = ALL_CONFIGS if args.tier == 'all' else {args.tier: ALL_CONFIGS[args.tier]}
    all_results = {}

    for name, hw in configs.items():
        variables = compute_variables(hw)
        match = compute_match(variables)
        print_results(hw, variables, match)
        all_results[name] = {'variables': variables, 'match': match}

    # Summary comparison
    if len(configs) > 1:
        print(f"\n{'='*70}")
        print(f"  TIER COMPARISON SUMMARY")
        print(f"{'='*70}")
        print(f"  {'Var':<12}", end="")
        for name in configs:
            print(f" {configs[name].name:>20}", end="")
        print()
        print(f"  {'-'*12}", end="")
        for _ in configs:
            print(f" {'-'*20}", end="")
        print()
        for k in THC_TARGET:
            print(f"  {k:<12}", end="")
            for name in configs:
                m = all_results[name]['match'][k]
                status = "✅" if m >= 100 else "⚠️"
                print(f" {m:>15.1f}% {status}", end="")
            print()

        print(f"\n  {'AVERAGE':<12}", end="")
        for name in configs:
            avg = sum(all_results[name]['match'].values()) / 12
            print(f" {avg:>17.1f}%  ", end="")
        print()
        print(f"  {'≥100%':<12}", end="")
        for name in configs:
            over = sum(1 for v in all_results[name]['match'].values() if v >= 100)
            print(f" {over:>15}/12   ", end="")
        print()
        print(f"  {'COST':<12}", end="")
        for name in configs:
            print(f" {'$'+str(int(configs[name].cost)):>18}  ", end="")
        print()

    if args.json:
        print(f"\n{json.dumps(all_results, indent=2)}")


if __name__ == '__main__':
    main()
