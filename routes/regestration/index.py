from config.db import connection
from fastapi import APIRouter
from schema.user import User
from models.user import users, generate_token

cursor = connection.cursor()
user = APIRouter()

@user.get("/")
def create_user():
    cursor.execute(users)
    connection.commit()
    return {"msg": "table created succesfully" }


@user.post("/regestration")
async def regestration(user: User):
    sql = """INSERT INTO users (username, email, password, created_at)
             VALUES (%s, %s, %s, %s)"""
    created = user.created_at.isoformat()
    
    cursor.execute(sql, (user.username, user.email, user.password, created))
    connection.commit()
    return {"msg": "kaj kore vai!!!"}

