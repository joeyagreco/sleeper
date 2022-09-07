from __future__ import annotations

from enum import unique

from sleeper.enum.ModelEnum import ModelEnum


@unique
class PlayoffRoundType(ModelEnum):
    ONE_WEEK_PER_ROUND = "ONE_WEEK_PER_ROUND"  # each round of playoffs is one week
    TWO_WEEK_CHAMPIONSHIP_ROUND = "TWO_WEEK_CHAMPIONSHIP_ROUND"  # each round of playoffs is one week, while the championship spans two weeks
    TWO_WEEKS_PER_ROUND = "TWO_WEEKS_PER_ROUND"  # each round of playoffs spans two weeks

    @classmethod
    def from_int(cls, val: int) -> PlayoffRoundType:
        if val == 0:
            return PlayoffRoundType.ONE_WEEK_PER_ROUND
        elif val == 1:
            return PlayoffRoundType.TWO_WEEK_CHAMPIONSHIP_ROUND
        elif val == 2:
            return PlayoffRoundType.TWO_WEEKS_PER_ROUND
        else:
            cls._handle_unknown_value(PlayoffRoundType, str(val))
