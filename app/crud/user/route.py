from fastapi import APIRouter
from app.crud.user.get.route import router as get_router
from app.crud.user.post.route import router as post_router
from app.crud.user.put.route import router as put_router
from app.crud.user.delete.route import router as delete_router

router = APIRouter(prefix="/users", tags=["Users"])

router.include_router(get_router)
router.include_router(post_router)
router.include_router(put_router)
router.include_router(delete_router)
