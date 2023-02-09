from typing import Optional

from pydantic import BaseModel


class DishesBase(BaseModel):
    title: str
    description: str
    price: str


class DishesCreate(DishesBase):
    pass


class DishesUpdate(DishesBase):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None
