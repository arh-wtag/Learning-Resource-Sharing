from config.db import connection
from fastapi import APIRouter
from schema.user import LoginUser
from models.user import generate_token
cursor = connection.cursor()
log = APIRouter()

@log.post("/login")
async def login(loginUser: LoginUser):
    query = "SELECT id, username, password FROM users"
    cursor.execute(query)

    # Fetch all rows from the result
    users = cursor.fetchall()

    for row in users:
        user_id, username, password = row
        if (loginUser.username == username and loginUser.password == password):
            token = generate_token(user_id)
            return {"token": token}
        
    return {"msg": "vul hoise thik koren!"}
