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
        FOREIGN KEY (lead_id) REFERENCES leads (id) ON UPDATE CASCADE
    );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS call_plan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lead_id INTEGER NOT NULL,
        frequency INTEGER NOT NULL,
        last_date DATE NULL,
        next_date DATE NULL,
        FOREIGN KEY (lead_id) REFERENCES leads (id) ON UPDATE CASCADE
    );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lead_id INTEGER NOT NULL,
        interaction_date DATETIME NOT NULL,
        type TEXT CHECK (type IN ('Call', 'Visit', 'Order')) NOT NULL,
        notes TEXT,
        FOREIGN KEY (lead_id) REFERENCES leads (id) ON UPDATE CASCADE
    );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lead_id INTEGER NOT NULL,
        order_date DATETIME NOT NULL,
        order_amount REAL NOT NULL, -- Total value of the order
        FOREIGN KEY (lead_id) REFERENCES leads (id) ON UPDATE CASCADE
    );
    """)
    conn.commit()
    conn.close()


# Initialize tables
create_tables()
