from app.data_store.memory_db import USERS
from app.models import User
from typing import Optional

def get_all_users() -> list[User]:
    return USERS

def get_user_by_id(user_id: int) -> Optional[User]:
    for user in USERS:
        if user.id == user_id:
            return user
    return None
