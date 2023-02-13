from typing import Optional

from pydantic import BaseModel, constr


class MenusBase(BaseModel):
    title: constr(min_length=3, max_length=32)
    description: constr(min_length=3, max_length=128)


class MenusCreate(MenusBase):
    pass


class MenusUpdate(MenusBase):
    title: Optional[str] = None
    description: Optional[str] = None


class Menus(MenusBase):
    pass
