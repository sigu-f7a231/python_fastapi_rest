from app.data_store.memory_db import USERS
from app.models import UserInput, User

def update_user(user_id: int, user_input: UserInput) -> User | None:
    for user in USERS:
        if user.id == user_id:
            user.name = user_input.name
            return user
    return None
