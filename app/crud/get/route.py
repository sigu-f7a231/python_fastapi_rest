from fastapi import APIRouter, HTTPException
from app.crud.get.controller import get_all_users_controller, get_user_by_id_controller
from app.models import User

router = APIRouter()

@router.get("/users", response_model=list[User])
def get_users():
    return get_all_users_controller()

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = get_user_by_id_controller(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
