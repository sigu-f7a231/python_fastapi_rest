from fastapi import APIRouter
from app.crud.user.route import router as user_crud_router

router = APIRouter()

router.include_router(user_crud_router)
