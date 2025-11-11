from app.data_store.put_repository.update_user_repository import update_user
from app.models import UserInput, User
from typing import Optional

def update_user_service(user_id: int, user_input: UserInput) -> Optional[User]:
    return update_user(user_id, user_input)
