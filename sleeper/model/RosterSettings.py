from dataclasses import dataclass


@dataclass(kw_only=True)
class RosterSettings:
    wins: int
    waiver_position: int
    waiver_budget_used: int
    total_moves: int
    ties: int
    losses: int
    fpts: int
    fpts_decimal: int
    fpts_against: int
    fpts_against_decimal: int
