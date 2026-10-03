from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class RecommendationMode(StrEnum):
    SHADOW = "SHADOW"
    HUMAN_APPROVAL = "HUMAN_APPROVAL"
    CONTROLLED_EXECUTION = "CONTROLLED_EXECUTION"


@dataclass(frozen=True, slots=True)
class Recommendation:
    recommendation_id: str
    tenant_id: str
    site_id: str
    mode: RecommendationMode = RecommendationMode.SHADOW
    evidence_refs: tuple[str, ...] = field(default_factory=tuple)

    def requires_human_or_safety_path(self) -> bool:
        return self.mode is not RecommendationMode.SHADOW
