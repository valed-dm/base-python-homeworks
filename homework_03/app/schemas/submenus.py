from typing import Optional

from pydantic import BaseModel


class SubmenusBase(BaseModel):
    title: str
    description: str


class SubmenusCreate(SubmenusBase):
    pass


class SubmenusUpdate(SubmenusBase):
    title: Optional[str] = None
    description: Optional[str] = None
