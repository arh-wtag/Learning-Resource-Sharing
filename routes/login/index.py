from config.db import connection
from fastapi import APIRouter
from schema.user import LoginUser

cursor = connection.cursor()
log = APIRouter()

@log.post("/login")
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
