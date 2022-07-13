from __future__ import annotations

from enum import unique, Enum


@unique
class Status(Enum):
    COMPLETE: "COMPLETE"
    DRAFTING: "DRAFTING"
    IN_SEASON: "IN_SEASON"
    PRE_DRAFT: "PRE_DRAFT"
