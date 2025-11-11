from app.crud.delete.service import delete_user_service
from fastapi import HTTPException

def delete_user_controller(user_id: int):
    result = delete_user_service(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
