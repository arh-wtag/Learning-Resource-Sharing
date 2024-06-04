from config.db import connection
from fastapi import APIRouter
from schema.user import User
from models.user import users
# from main import REQUESTS_COUNT
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST, start_http_server
cursor = connection.cursor()
user = APIRouter()
REQUESTS_COUNT_TABLE = Counter('create_table_request_total', 'Total Table Request',['app_name', 'endpoint'])
@user.get("/create_table")
def create_user():
    REQUESTS_COUNT_TABLE.labels('Learning Resource Sharing Algorithm', '/create_table').inc()
    cursor.execute(users)
    connection.commit()
    return {"msg": "table created succesfully" }

@user.get("/userpass")
def get_all_user():
    sql = """select * from users"""
    cursor.execute(sql)
    row = cursor.fetchall()
    return row
    

@user.post("/regestration")
async def regestration(user: User):
    sql = """INSERT INTO users (username, email, password, created_at)
             VALUES (%s, %s, %s, %s)"""
    created = user.created_at.isoformat()
    
    cursor.execute(sql, (user.username, user.email, user.password, created))
    connection.commit()
    return {"msg": "kaj kore vai!!!"}

