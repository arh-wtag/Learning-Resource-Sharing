import psycopg2
import os
# print("+++++++",os.environ['DB_HOST'])
connection = psycopg2.connect(
    host = os.environ.get('DB_HOST'),
    port = os.environ.get('DB_PORT'),
    dbname = os.environ.get('DB_NAME'),
    user = os.environ.get('DB_USER'),
    password = os.environ.get('DB_PASSWORD')
)

if(connection):
    print("kaj kore!!")
else: 
    print("kaj kore na!!")
cursor = connection.cursor()
