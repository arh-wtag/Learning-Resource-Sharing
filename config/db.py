import psycopg2

connection = psycopg2.connect( # need to change all the things for security
    dbname = "resources",
    user = "postgres",
    password = "12345678",
    host = "localhost",
    port = "5432"
)

if(connection):
    print("kaj kore!!")
else: 
    print("kaj kore na!!")
cursor = connection.cursor()



