from dataclasses import dataclass


@dataclass(kw_only=True)
class TransactionSettings:
    waiver_bid: int
