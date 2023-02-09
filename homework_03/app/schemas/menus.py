from typing import Optional

from pydantic import BaseModel


class MenusBase(BaseModel):
    title: str
    description: str


class MenusCreate(MenusBase):
    pass


class MenusUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
