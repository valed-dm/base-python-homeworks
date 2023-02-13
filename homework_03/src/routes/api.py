from fastapi import APIRouter

from ..views import menus_router, test_router

router = APIRouter()
router.include_router(test_router)
router.include_router(menus_router)
