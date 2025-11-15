from app.crud.user.get.service import get_all_users_service, get_user_by_id_service
from app.models import User
from typing import Optional

def get_all_users_controller() -> list[User]:
    return get_all_users_service()

def get_user_by_id_controller(user_id: int) -> Optional[User]:
    return get_user_by_id_service(user_id)
