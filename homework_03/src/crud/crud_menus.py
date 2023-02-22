from pydantic import BaseModel

from ..schemas import Menus, MenusCreate, MenusUpdate


class MenusStorage(BaseModel):
    counter: int = 0
    mstore: dict[str, Menus] = {}  # mstore --> menus_store: keeps menu's dict by id

    @property
    def next_id(self) -> int:
        self.counter += 1
        return self.counter


s = MenusStorage()  # s --> store: MenusStorage class instance


def get_menus_storage() -> list[dict[str, Menus]]:
    return list(map(lambda key: {key: s.mstore[key]}, s.mstore.keys()))


def create_menus(m_in: MenusCreate) -> Menus:
    menu = Menus(**m_in.dict())
    s.mstore[str(s.next_id)] = menu
    return menu


def update_menus(m_id: str, m_in: MenusUpdate):
    menus = s.mstore.get(m_id).dict()
    update = m_in.dict()
    for key in menus:
        if key in update and update[key]:
            menus[key] = update[key]
    s.mstore[m_id] = Menus(**menus)
    return menus


def get_menus_by_id(m_id: str) -> Menus or None:
    return s.mstore.get(m_id)


def delete_menus(m_id: str) -> None:
    s.mstore.pop(m_id, None)
