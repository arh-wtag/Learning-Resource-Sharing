from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    created_at: datetime

class LoginUser(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str or None = None
