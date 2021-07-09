"""Pydantic Response Models for the API."""

from typing import Optional

from pydantic import BaseModel


class RInfoModel(BaseModel):
    """Response model for animal info."""

    id: int
    name: str
    fun_fact: Optional[str]


__all__ = ["RInfoModel"]
