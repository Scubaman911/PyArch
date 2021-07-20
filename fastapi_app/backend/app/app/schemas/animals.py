from typing import Optional

from pydantic import BaseModel


class AnimalFactModel(BaseModel):
    """Response model for animal info."""

    id: int
    name: str
    fun_fact: Optional[str]
