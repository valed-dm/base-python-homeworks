from fastapi import APIRouter

router = APIRouter(prefix='/ping', tags=['TestAPI'])


@router.get('/', status_code=200)
def test_menus_api():
    return {"message": "pong"}
