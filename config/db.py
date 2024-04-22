import psycopg2
import os
connection = psycopg2.connect(
    dbname = os.environ.get('DATABASE_NAME'),
    user = os.environ.get('DATABASE_USER'),
    password = os.environ.get('DATABASE_PASSWORD'),
    host = 'localhost',
    port = '5432'
)

if(connection):
    print("kaj kore!!")
else: 
    print("kaj kore na!!")
cursor = connection.cursor()
