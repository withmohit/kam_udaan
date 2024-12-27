import sqlite3

def get_db_connection():
    conn = sqlite3.connect("db.sqlite")
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            restaurant_name TEXT NOT NULL,
            address TEXT NOT NULL,
            current_status TEXT NOT NULL,
            frequency INTEGER NOT NULL,
            order_count INTEGER NOT NULL,
            assigned_kam TEXT NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lead_id INTEGER NOT NULL,
        person_name TEXT NOT NULL,
        role TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        email TEXT,
        FOREIGN KEY (lead_id) REFERENCES leads (id) ON DELETE CASCADE
    );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS call_plan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lead_id INTEGER NOT NULL,
        last_date DATE NOT NULL,
        next_date DATE NOT NULL,
        FOREIGN KEY (lead_id) REFERENCES leads (id) ON DELETE CASCADE
    );
    """)
    conn.commit()
    conn.close()


# Initialize tables
create_tables()
