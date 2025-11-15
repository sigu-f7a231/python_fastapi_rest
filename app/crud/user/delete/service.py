from app.data_store.delete_repository.delete_user_repository import delete_user

def delete_user_service(user_id: int) -> bool:
    return delete_user(user_id)
