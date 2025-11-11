from app.data_store.memory_db import USERS

def delete_user(user_id: int) -> bool:
    for i, user in enumerate(USERS):
        if user.id == user_id:
            USERS.pop(i)
            return True
    return False
