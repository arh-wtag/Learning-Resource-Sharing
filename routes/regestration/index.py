from config.db import connection
from fastapi import FastAPI, APIRouter
from schema.user import User, LoginUser
from models.user import users

cursor = connection.cursor()
user = APIRouter()

@user.get("/")
def create_user():
    cursor.execute(users)
    connection.commit()


@user.post("/regestration")
async def regestration(user: User):
   

    sql = """INSERT INTO users (username, email, password, created_at)
             VALUES (%s, %s, %s, %s)"""
    created = user.created_at.isoformat()
    
    cursor.execute(sql, (user.username, user.email, user.password, created))
    connection.commit()
    return {"msg": "kaj kore vai!!!"}

@user.post("/login")
async def login(loginUser: LoginUser):
    query = "SELECT username, password FROM users"
    cursor.execute(query)

    # Fetch all rows from the result
    users = cursor.fetchall()

    for row in users:
        username, password = row
        if (loginUser.username == username and loginUser.password == password):
            return {"msg" : "login hoise re!"}
   
    return {"msg": "vul hoise thik koren!"}

        

