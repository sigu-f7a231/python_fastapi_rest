from pydantic import BaseModel

# 入力用
class UserInput(BaseModel):
    name: str

# 出力用
class User(UserInput):
    id: int
