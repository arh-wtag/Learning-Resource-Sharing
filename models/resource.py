resources = """CREATE TABLE IF NOT EXISTS resources (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(100)
);"""

resource_details = """Create Table IF NOT EXISTS resource_details (
    id SERIAL PRIMARY KEY,
    resource_id INTEGER,
    resource_link VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id),
    FOREIGN KEY (resource_id) 
        REFERENCES resources(id);
);"""
