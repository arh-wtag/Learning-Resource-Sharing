from fastapi import APIRouter, Depends, HTTPException, status, Form
from config.db import connection
from schema.resource import ResourceDetails, Resources
from models.resource import resource_details, resources
from routes.login.index import get_current_active_user
from typing import Annotated
from schema.user import User, UserDict
from psycopg2 import Error
from config.redis import REDIS_URL
import redis
import json
cursor = connection.cursor()
res = APIRouter()

REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 0


r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


@res.get("/resources")
def create_table_resources(current_user: Annotated[UserDict, Depends(get_current_active_user)], ):
    cursor.execute(resources)
    connection.commit()
    cursor.execute(resource_details)
    connection.commit()

@res.post("/insert")
def insert_resource(resource : Resources,
                    current_user: Annotated[UserDict, Depends(get_current_active_user)], ):
    user_id = current_user.user_id
    # if user_id is not found in user then return a exception
    # but it can't happen because of current_user is always authorized
    insert_query = """INSERT INTO resources (title, user_id, created_at) 
                VALUES (%s, %s, %s)"""
    
    try:
        created = resource.created_at.isoformat()
        cursor = connection.cursor()
        cursor.execute(insert_query, (resource.title, user_id, created))
        connection.commit()
        return {"msg": "insert resource successfully"}
    except (Exception, Error) as error:
        return {"msg kaj kore na": error, "msg": "kan kaj kore na"}

@res.post("/insert/{resourse_id}")
def insert_resource_datails (resource_id: int, resourse_details : ResourceDetails,
                    current_user: Annotated[UserDict, Depends(get_current_active_user)], ):
    # print("\n\n\n\nres = ", resource_id)
    # first e amake check kora lagbe ei je ami resource id paisi eita ei user_id er kina
    
    query = """SELECT user_id FROM resources WHERE id = %s"""
    cursor = connection.cursor()
    cursor.execute(query, (resource_id, ))
    row = cursor.fetchone()
    user_id = row[0]
    # return {"msg: user is": user_id}
    if(user_id == current_user.user_id):
        # try to make operatins
        try:
            query = """INSERT INTO resource_details 
            (resource_id, resource_link, created_at) 
            VALUES (%s, %s, %s)"""
            created = resourse_details.created_at.isoformat()
            cursor.execute(query, 
                        (resource_id, resourse_details.resource_link, created))
            connection.commit()
            return {"msg": "user details inserted successfully"}
        except:
            return {"msg": "jhamela hoise!!"}
    else:
        return {"msg": "user is not authorized for change this resources"}


    

    

@res.delete("/delete")
def insert_resource(resourse : Resources, resource_details: ResourceDetails):

    query = """"""



@res.put("/update")
def insert_resource(resourse : Resources, resource_details: ResourceDetails):
    query = """"""


@res.get("/read")
def insert_resource(current_user: Annotated[UserDict, Depends(get_current_active_user)],):

    query = """Select * from resources"""
    cursor.execute(query)
    row = cursor.fetchall()
    return row
    


@res.get("/read/{id}")
def read_id(id: int,  current_user: Annotated[UserDict, Depends(get_current_active_user)]):
    key = f"resource:{id}"
    value = r.get(key)
    
    if value:
        # Data found in Redis, return it
        resource_data = json.loads(value)
        return {"data": resource_data, "source": "redis"}
    else:
        # Data not found in Redis, fetch from PostgreSQL
        try:
            # Fetch data from PostgreSQL
            query = """SELECT * FROM resources WHERE id = %s"""
            cursor.execute(query, (id,))
            row = cursor.fetchone()

            if row:
                # Convert row to dictionary
                resource_dict = {
                    "id": row[0],
                    "title": row[1],
                    "user_id": row[2],
                    "created_at": row[3].isoformat()
                }
                # Insert data into Redis
                r.set(key, json.dumps(resource_dict))
                return resource_dict
            else:
                raise HTTPException(status_code=404, detail="Resource not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))