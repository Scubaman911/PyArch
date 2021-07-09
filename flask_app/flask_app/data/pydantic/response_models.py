"""Pydantic Response Models for the API."""

from typing import Optional

from pydantic import BaseModel


class RInfoModel(BaseModel):
    id: str
    name: str
    fact: Optional[str]
