from pydantic import BaseModel, Field


class QInfoModel(BaseModel):
    """Query model for animal info."""
    animal: str = Field("kangaroo", description="The name of an animal, of course!")


__all__ = ["QInfoModel"]
