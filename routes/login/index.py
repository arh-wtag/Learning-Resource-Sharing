from config.db import connection
from fastapi import APIRouter, Depends, HTTPException, status, Form
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
import os
from schema.user import User, Token, TokenData, UserDict

from datetime import datetime, timedelta, timezone

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

cursor = connection.cursor()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

log = APIRouter()



# database connection pull 
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(username: str):
    query = """SELECT * FROM users"""
    cursor.execute(query)
    # Fetch all rows from the result
    users = cursor.fetchall()
    for row in users:
        #print(row)
        user_id, username1, email, password, created_at = row
        # username1 = row
        # print(username)
        # print(username1)
        if (username1 == username):
            # user_id, username, password, created_at = row
            user_dict = {'user_id': user_id, 'username': username1, 'email': email, 'password': password}
            #print("arafat = ", user_dict)
            # print(user_dict)
            
            return UserDict(**user_dict)
    
def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if (password != user.password):
        return False
    #print("user = ", user)
    return user

def create_access_token(data: dict):
    #print("type = " , type(data), "\n\n\n\n")
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    #print("\n\n\n\nto_encode = ", to_encode, "\n\n\n\n")
    encoded_jwt = jwt.encode(to_encode, b"7caed3dfc8ed0335575bf68010c01f3da141b249c73c26115c17456e017c0325", algorithm='HS256')
    #print("\n\n\n\n\n\nencoded_jwt = ", encoded_jwt, "\n\n\n\n\\n")
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    #print("\n\n\n\ntoken data = ", token, "\n\n\n\n")
    try:
        payload = jwt.decode(token, b"7caed3dfc8ed0335575bf68010c01f3da141b249c73c26115c17456e017c0325", algorithms=[ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Annotated[UserDict, Depends(get_current_user)],
):
    #print('\n\n\n\n', current_user, '\n\n\n\n')
    
          
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@log.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data = {'user_id': user.user_id, 'username': user.username, 'email': user.email}
    )
    return Token(access_token=access_token, token_type="bearer")




@log.get("/users/me/")
async def read_users_me(current_user: Annotated[UserDict, Depends(get_current_active_user)], ):
    return current_user


@log.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[UserDict, Depends(get_current_active_user)],
):
    #print("\n\n\n\ncurr: ", current_user, "\n\n\n\n")
    return [{"item_id": "Foo", "owner": current_user.username}]