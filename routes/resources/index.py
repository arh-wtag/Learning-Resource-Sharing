from fastapi import APIRouter, Depends, HTTPException, status, Form
from config.db import connection
from schema.resource import ResourceDetails, Resources
from models.resource import resource_details, resources
from routes.login.index import get_current_active_user
from typing import Annotated
from schema.user import User, UserDict
from psycopg2 import Error
cursor = connection.cursor()
res = APIRouter()

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
def insert_resource(resourse : Resources, resource_details: ResourceDetails):
    query = """Select * from """


@res.get("/read/{id}")
def read_id(id: int):
    return {"msg" : "read bt id"}