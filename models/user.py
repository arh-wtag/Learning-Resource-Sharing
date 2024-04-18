import bcrypt
import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from os.path import join, dirname

users = """CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(255),
    password VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"""

def hashed_password(self, password: str):
    self.hashed_password = bcrypt.hashpw(password.encode('utf-8'),
                                        bcrypt.gensalt().decode('utf-8'))

def verify_password(self, password: str):
    return bcrypt.checkpw(password.encode('utf-8'), self.hashed_password('utf-8')) 

load_dotenv()


def generate_token(user_id: int):
    expiration = datetime.utcnow() + timedelta(hours=24)
    payload = {
        "user_id" : str(user_id),
        "exp" : expiration
    }
    return jwt.encode(payload, os.environ.get("SECRET_KEY"), algorithm="HS256")