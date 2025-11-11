from app.data_store.get_repository.get_user_repository import get_all_users, get_user_by_id
from app.models import User
from typing import Optional

def get_all_users_service() -> list[User]:
    return get_all_users()

def get_user_by_id_service(user_id: int) -> Optional[User]:
    return get_user_by_id(user_id)
