from fastapi import APIRouter
from app.crud.put.controller import update_user_controller
from app.models import UserInput, User

router = APIRouter()

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_input: UserInput):
    return update_user_controller(user_id, user_input)
