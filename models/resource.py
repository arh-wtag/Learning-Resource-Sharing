from config.db import connection

cursor = connection.cursor()

resources = """CREATE TABLE IF NOT EXISTS resources (
    id serial PRIMARY KEY,
    title VARCHAR(100),
    created_at VARCHAR(100)
);"""

cursor.execute(resources)


resource_details = """Create Table IF NOT EXISTS resource_details (
    id SERIAL PRIMARY KEY,
    resource_id INTEGER,
    resource_link VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id),
    FOREIGN KEY (resource_id) 
        REFERENCES resources(id);
);"""

cursor.execute(resource_details)

connection.close()
cursor.close()