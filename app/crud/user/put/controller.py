from app.crud.user.put.service import update_user_service
from app.models import UserInput, User
from typing import Optional
from fastapi import HTTPException

def update_user_controller(user_id: int, user_input: UserInput) -> User:
    user = update_user_service(user_id, user_input)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
