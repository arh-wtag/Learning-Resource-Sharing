import psycopg2
import os
# print("+++++++",os.environ['DB_HOST'])
connection = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        port=os.environ.get('DB_PORT', '5432'),
        dbname=os.environ.get('DB_NAME', 'resources'),
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('POSTGRES_PASSWORD', '12345678')
    )

if(connection):
    print("kaj kore!!")
else: 
    print("kaj kore na!!")
cursor = connection.cursor()
