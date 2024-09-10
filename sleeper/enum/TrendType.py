from enum import Enum, unique


@unique
class TrendType(Enum):
    ADD = "ADD"
    DROP = "DROP"
