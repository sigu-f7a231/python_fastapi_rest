from app.crud.user.post.service import create_user_service
from app.models import User, UserInput

def create_user_controller(user_input: UserInput) -> User:
    # バリデーションや例外処理はここで
    return create_user_service(user_input)
