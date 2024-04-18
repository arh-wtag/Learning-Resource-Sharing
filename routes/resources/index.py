from fastapi import APIRouter
from config.db import connection
from schema.resource import ResourceDetails, Resources
from models.resource import resource_details, resources

cursor = connection.cursor()

res = APIRouter()

@res.get("/")
def create_table():
    cursor.execute(resources)
    cursor.commit()
    cursor.execute(resource_details)
    cursor.commit()

@res.put("/insert")
def insert_resource(resourse : Resources, resource_details: ResourceDetails):
    query = """"""