from pydantic import BaseModel


class QInfoModel(BaseModel):
    animal: str


__all__ = ["QInfoModel"]
