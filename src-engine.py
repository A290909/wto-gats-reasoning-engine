from typing import Any, Dict, List
from .model import MeasureProfile


def _risk_level(score: int) -> str:
    if score >= 6:
        return "High"
    if score >= 3:
        return "Medium"
    return "Low"


def assess_gats(profile: MeasureProfile) -> Dict[str, Any]:
    """
    A transparent, rule-based reasoning sequence:
    (1) Prima facie (Art. XVI / XVII)
    (2) Art. XIV (legitimate objective)
    (3) Necessity / proportionality (structured proxies)
    (4) Chapeau-style check (non-arbitrary application proxy)

    Output is explainable and intended for research structuring only.
    """
    steps: List[str] = []
    missing: List[str] = []
    score = 0

    # (1) Prima facie concerns
    prima_facie = False

    if profile.market_access_restriction:
        prima_facie = True
        steps.append("Step 1 — Prima facie: Potential concern under GATS Art. XVI (market access).")
        score += 2

    if profile.national_treatment_concern:
        prima_facie = True
        steps.append("Step 1 — Prima facie: Potential concern under GATS Art. XVII (national treatment).")
        score += 2

    if not prima_facie:
        steps.append("Step 1 — Prima facie: No indicated Art. XVI / XVII concerns on provided inputs.")
        return {"risk": "Low", "steps": steps, "missing_info": missing}

    # (2) Art. XIV justification
    if not profile.legitimate_objective:
        missing.append("Art. XIV: Specify the legitimate objective (e.g., privacy, security, innovation).")
        steps.append("Step 2 — Art. XIV: Legitimate objective not provided; cannot structure justification.")
        score += 3
        return {"risk": _risk_level(score), "steps": steps, "missing_info": missing}

    steps.append(f"Step 2 — Art. XIV: Legitimate objective stated as '{profile.legitimate_objective}'.")
    score += 1

    # (3) Necessity / proportionality proxies
    if profile.contribution_to_objective_clear is None:
        missing.append("Necessity: Is the measure's contribution to the objective demonstrably clear?")
        score += 1
    elif profile.contribution_to_objective_clear is False:
        steps.append("Step 3 — Necessity: Contribution to objective appears unclear/weak (risk factor).")
        score += 2
    else:
        steps.append("Step 3 — Necessity: Contribution to objective appears plausibly supported.")
        score += 0

    if profile.less_trade_restrictive_alternatives_available is None:
        missing.append("Necessity: Are reasonably available, less trade-restrictive alternatives present?")
        score += 1
    elif profile.less_trade_restrictive_alternatives_available is True:
        steps.append("Step 3 — Necessity: Less trade-restrictive alternatives appear available (risk factor).")
        score += 2
    else:
        steps.append("Step 3 — Necessity: No clear less trade-restrictive alternatives indicated.")
        score += 0

    # (4) Chapeau-style proxy (non-arbitrary application)
    if profile.applied_non_arbitrarily is None:
        missing.append("Chapeau-style: Is the measure applied in a non-arbitrary / non-discriminatory manner?")
        score += 1
    elif profile.applied_non_arbitrarily is False:
        steps.append("Step 4 — Chapeau-style: Application appears arbitrary/discriminatory (high risk factor).")
        score += 3
    else:
        steps.append("Step 4 — Chapeau-style: Application appears non-arbitrary/non-discriminatory.")
        score += 0

    return {"risk": _risk_level(score), "steps": steps, "missing_info": missing}