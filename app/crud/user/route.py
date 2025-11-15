from fastapi import APIRouter
from .get.route import router as get_router
from .post.route import router as post_router
from .put.route import router as put_router
from .delete.route import router as delete_router

router = APIRouter(prefix="/users", tags=["Users"])

# メソッドごとの router を統合
router.include_router(get_router)
router.include_router(post_router)
router.include_router(put_router)
router.include_router(delete_router)
