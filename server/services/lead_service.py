from database import get_db_connection

def add_lead(data,kam_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO leads (restaurant_name, address, current_status, kam_id)
        VALUES (?, ?, 'Active', ?);          
    """, (data.restaurant_name, data.address, kam_id))
    lead_id = cursor.lastrowid
    cursor.execute("""
                   INSERT INTO call_plan (lead_id,frequency ,last_date, next_date)
        VALUES (?, ?, ?, ?);
    """, (lead_id,data.frequency,"",""))
    conn.commit()
    conn.close()
    return {"message": "Lead added successfully!"}

def get_all_leads(kam_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    leads = cursor.execute("SELECT * FROM leads where kam_id=?",(kam_id,)).fetchall()
    conn.close()
    return leads

