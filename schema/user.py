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