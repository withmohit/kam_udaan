from database import get_db_connection

def add_lead(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO leads (restaurant_name, address, current_status, frequency, order_count, assigned_kam)
        VALUES (?, ?, ?, ?, ?, ?);          
    """, (data.restaurant_name, data.address, data.current_status, data.frequency, 0, data.assigned_kam))
    conn.commit()
    conn.close()
    return {"message": "Lead added successfully!"}

def get_all_leads():
    conn = get_db_connection()
    cursor = conn.cursor()
    leads = cursor.execute("SELECT * FROM leads").fetchall()
    conn.close()
    return leads
