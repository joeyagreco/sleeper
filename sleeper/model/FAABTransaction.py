from dataclasses import dataclass


@dataclass(kw_only=True)
class FAABTransaction:
    sender: int
    receiver: int
    amount: int
