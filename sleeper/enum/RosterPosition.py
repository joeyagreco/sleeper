from __future__ import annotations

from enum import unique, Enum


@unique
class RosterPosition(Enum):
    BN: "BN"
    DEF: "DEF"
    FLEX: "FLEX"
    K: "K"
    QB: "QB"
    RB: "RB"
    TE: "TE"
    WR: "WR"
