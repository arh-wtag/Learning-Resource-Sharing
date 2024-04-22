resources = """CREATE TABLE IF NOT EXISTS resources (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    user_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"""

resource_details = """Create Table IF NOT EXISTS resource_details (
    id SERIAL PRIMARY KEY,
    resource_id INTEGER REFERENCES resources(id),
    resource_link VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"""
