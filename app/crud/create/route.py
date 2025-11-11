from fastapi import APIRouter
from app.crud.create.controller import create_user_controller
from app.models import User, UserInput

router = APIRouter()

@router.post("/users", response_model=User)
def create_user(user_input: UserInput):
    return create_user_controller(user_input)
