from fastapi import APIRouter
from .create.controller import router as create_router
from .get.controller import router as get_router
from .put.controller import router as update_router
from .delete.controller import router as delete_router

router = APIRouter()
router.include_router(create_router)
router.include_router(get_router)
router.include_router(update_router)
router.include_router(delete_router)
