from app.data_store.create_repository.create_user_repository import add_user
from app.models import UserInput, User

def create_user_service(user_input: UserInput) -> User:
    return add_user(user_input)
