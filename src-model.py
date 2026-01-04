from dataclasses import dataclass
from typing import List, Optional


@dataclass
class MeasureProfile:
    """
    Research-oriented representation of a regulatory measure for GATS analysis.

    NOTE: This is a conceptual model for structured legal reasoning.
    It does not automate legal advice and is not a substitute for doctrinal analysis.
    """
    name: str

    # Trade structure (high-level)
    affects_supply_modes: List[str]  # e.g., ["Mode 1", "Mode 3"]

    # Prima facie flags (simplified proxies)
    market_access_restriction: bool  # proxy for potential Art. XVI concerns
    national_treatment_concern: bool  # proxy for potential Art. XVII concerns

    # Art. XIV elements (simplified)
    legitimate_objective: Optional[str] = None  # e.g., "privacy", "security", "innovation"

    # Necessity / proportionality proxies
    less_trade_restrictive_alternatives_available: Optional[bool] = None
    contribution_to_objective_clear: Optional[bool] = None

    # Chapeau-style / non-discrimination proxy
    applied_non_arbitrarily: Optional[bool] = None