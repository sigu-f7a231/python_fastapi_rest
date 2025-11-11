from fastapi import APIRouter
from app.crud.delete.controller import delete_user_controller

router = APIRouter()

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    return delete_user_controller(user_id)
