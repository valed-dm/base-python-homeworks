from fastapi import APIRouter, HTTPException, status

from ..crud import crud_menus
from ..schemas import Menus, MenusCreate, MenusUpdate

router = APIRouter(prefix='/menus', tags=['Menus'])


@router.get('', response_model=list[dict[str, Menus]])
def read_menus_storage() -> list[dict[str, Menus]]:
    return crud_menus.get_menus_storage()


@router.post('', response_model=Menus)
def create_menus_entry(menus_in: MenusCreate) -> Menus:
    return crud_menus.create_menus(menus_in)


@router.patch('/{menus_id}', response_model=Menus)
def update_menus_entry(menus_id: str, menus_in: MenusUpdate) -> Menus:
    menus = crud_menus.get_menus_by_id(menus_id)
    if menus:
        return crud_menus.update_menus(menus_id, menus_in)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Menus #{menus_id} does not exist'
    )


@router.get('/{menus_id}', response_model=Menus)
def read_menus_entry(menus_id: str) -> Menus:
    menus = crud_menus.get_menus_by_id(menus_id)
    if menus:
        return menus

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Menus #{menus_id} does not exist'
    )


@router.delete('/{menus_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_menus_entry(menus_id: str) -> None:
    return crud_menus.delete_menus(menus_id)
