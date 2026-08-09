"""
backend/models/risk.py — Risk assessment models (§11.2).
"""
from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel


class EvidenceItem(BaseModel):
    evidence_id: str
    source: str
    description: str
    value: float | None = None
    unit: str | None = None
    weight: float = 1.0
    ts: datetime
    metadata: dict[str, Any] = {}


class HistoricalMatch(BaseModel):
    match_id: str
    collection: str
    similarity_score: float
    description: str
    occurred_at: datetime | None = None
    outcome: str | None = None
    metadata: dict[str, Any] = {}


class RiskAssessment(BaseModel):
    assessment_id: str
    case_id: str
    zone_id: str
    compound_score: float
    tier: Literal["low", "medium", "high", "critical"]
    evidence: list[EvidenceItem] = []
    historical_matches: list[HistoricalMatch] = []
    reasoning_summary: str = ""
    assessed_at: datetime
