"""Universal transfer function engine — maps device parameters to 12 consciousness variables."""

from brainwire.variables import VAR_NAMES

# ---------------------------------------------------------------------------
# Coefficient tables
# Each entry: (device, param) -> coefficient
# ---------------------------------------------------------------------------
_C: dict[str, dict[tuple[str, str], float]] = {}

# V1: DA — tDCS(F3) + taVNS + TMS(10Hz) + tFUS(VTA) + GVS
_C['DA'] = {
    ('tDCS', 'anode_mA'): 0.25,
    ('taVNS', 'VNS_mA'): 0.80,
    ('TMS', '10Hz'): 0.80,
    ('tFUS', 'VTA_intensity'): 1.20,
    ('GVS', 'current_mA'): 0.30,
}

# V2: eCB
_C['eCB'] = {
    ('TENS', 'low'): 0.80,
    ('taVNS', 'VNS_mA'): 0.60,
    ('tDCS', 'anode_mA'): 0.20,
    ('tACS', '6Hz_mA'): 0.15,
    ('TMS', 'theta'): 0.20,
    ('tFUS', 'hippo_intensity'): 1.00,
}

# V3: 5HT
_C['5HT'] = {
    ('taVNS', 'VNS_mA'): 1.20,
    ('tDCS', 'anode_mA'): 0.15,
    ('tFUS', 'raphe_intensity'): 1.50,
}

# V4: GABA
_C['GABA'] = {
    ('tDCS', 'anode_mA'): 0.20,
    ('entrainment', 'alpha_ent'): 0.30,
    ('TMS', 'theta'): 0.25,
    ('tACS', '10Hz_mA'): 0.15,
    ('mTI', 'thalamus_intensity'): 0.40,
}

# V5: NE — SUPPRESSED (result = max(0.01, 1.0 - total))
_C['NE'] = {
    ('taVNS', 'VNS_mA'): 1.50,
    ('mTI', 'LC_intensity'): 0.80,
    ('tFUS', 'LC_intensity'): 0.60,
}

# V6: Theta
_C['Theta'] = {
    ('TMS', 'theta'): 0.80,
    ('entrainment', 'binaural_6Hz'): 0.40,
    ('tACS', '6Hz_mA'): 0.35,
    ('tFUS', 'hippo_intensity'): 0.70,
}

# V7: Alpha — SUPPRESSED
_C['Alpha'] = {
    ('tDCS', 'cathode_Fz_mA'): 0.20,
    ('TMS', '1Hz'): 0.25,
    ('HD-tDCS', 'cathode_mA'): 0.15,
}

# V8: Gamma
_C['Gamma'] = {
    ('entrainment', 'LED_40Hz'): 0.30,
    ('entrainment', 'audio_40Hz'): 0.25,
    ('entrainment', 'vibro_40Hz'): 0.20,
    ('tACS', '40Hz_mA'): 0.15,
    ('TMS', '40Hz'): 0.10,
    ('tFUS', '40Hz_intensity'): 0.25,
}

# V9: PFC — SUPPRESSED
_C['PFC'] = {
    ('tDCS', 'cathode_F4_mA'): 0.20,
    ('TMS', '1Hz'): 0.25,
    ('mTI', 'dlPFC_intensity'): 0.40,
}

# V10: Sensory
_C['Sensory'] = {
    ('tDCS', 'anode_V1_mA'): 0.15,
    ('entrainment', 'noise'): 0.40,
    ('entrainment', 'LED_40Hz'): 0.20,
    ('TENS', 'low'): 0.15,
    ('tACS', '40Hz_mA'): 0.10,
    ('tSCS', 'intensity'): 0.50,
    ('tRNS', 'intensity'): 0.35,
    ('tFUS', 'V1_intensity'): 0.40,
}

# V11: Body
_C['Body'] = {
    ('TENS', 'low'): 0.80,
    ('TENS', 'high'): 0.30,
    ('tDCS', 'anode_S1_mA'): 0.20,
    ('entrainment', 'vibro_40Hz'): 0.15,
    ('tSCS', 'intensity'): 0.60,
    ('GVS', 'current_mA'): 0.40,
}

# V12: Coherence
_C['Coherence'] = {
    ('entrainment', 'gamma_avg'): 0.30,   # avg of LED+audio+vibro 40Hz
    ('TMS', '40Hz'): 0.40,
    ('entrainment', 'sync_avg'): 0.20,    # same as gamma_avg
    ('tACS', '40Hz_mA'): 0.15,
    ('tRNS', 'intensity'): 0.20,
}

COEFFICIENTS = _C
SUPPRESSED_VARS = {'NE', 'Alpha', 'PFC'}

# ---------------------------------------------------------------------------
# Param key helpers
# ---------------------------------------------------------------------------

def _make_key(device: str, param: str) -> str:
    """Canonical flat key: device_param."""
    return f"{device}_{param}"


def _resolve_param(params: dict[str, float], device: str, param: str) -> float:
    """Look up a param value, trying device_param then bare param as fallback."""
    key = _make_key(device, param)
    if key in params:
        return params[key]
    # Fallback: bare param name (no device prefix)
    if param in params:
        return params[param]
    return 0.0


def _gamma_avg(params: dict[str, float]) -> float:
    """Compute average of LED_40Hz, audio_40Hz, vibro_40Hz entrainment params."""
    led = _resolve_param(params, 'entrainment', 'LED_40Hz')
    audio = _resolve_param(params, 'entrainment', 'audio_40Hz')
    vibro = _resolve_param(params, 'entrainment', 'vibro_40Hz')
    return (led + audio + vibro) / 3.0


# ---------------------------------------------------------------------------
# TransferEngine
# ---------------------------------------------------------------------------

class TransferEngine:
    """Maps flat hardware parameter dict to 12 consciousness variables."""

    def compute(self, params: dict[str, float]) -> dict[str, float]:
        """Compute all 12 consciousness variables from device parameters.

        Args:
            params: Flat dict of param values, keys formatted as
                    ``{device}_{param}``, e.g. ``tDCS_anode_mA``.

        Returns:
            Dict mapping each variable name to its computed multiplier.
            Normal vars: 1.0 + Σ(coeff * param_value).
            Suppressed vars: max(0.01, 1.0 - Σ(coeff * param_value)).
        """
        # Pre-compute derived aggregate params
        gamma_avg_val = _gamma_avg(params)
        derived: dict[str, float] = {
            'gamma_avg': gamma_avg_val,
            'sync_avg': gamma_avg_val,
        }

        result: dict[str, float] = {}

        for var in VAR_NAMES:
            coeffs = COEFFICIENTS.get(var, {})
            total = 0.0

            for (device, param), coeff in coeffs.items():
                # Check derived first (device == 'entrainment', special params)
                if device == 'entrainment' and param in derived:
                    value = derived[param]
                else:
                    value = _resolve_param(params, device, param)
                total += coeff * value

            if var in SUPPRESSED_VARS:
                result[var] = max(0.01, 1.0 - total)
            else:
                result[var] = 1.0 + total

        return result
