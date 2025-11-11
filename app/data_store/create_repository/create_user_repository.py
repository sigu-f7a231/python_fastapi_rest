from app.data_store.memory_db import USERS, NEXT_ID
from app.models import User, UserInput

def add_user(user_input: UserInput) -> User:
    global NEXT_ID
    user = User(id=NEXT_ID, name=user_input.name)
    USERS.append(user)
    NEXT_ID += 1
    return user
