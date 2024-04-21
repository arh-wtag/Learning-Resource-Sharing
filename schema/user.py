from pydantic import BaseModel, EmailStr
from datetime import datetime

# class User(BaseModel):
#     username: str
#     email: EmailStr
#     password: str
#     created_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: EmailStr | None = None
    created_at: datetime | None = None
    # hashed_password: str 
    disabled: bool | None = None

# class UserInDB(User):
    