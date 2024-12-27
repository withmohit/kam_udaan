from database import get_db_connection

def update_first(lead_id,last_date,next_date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO call_plan (lead_id, last_date, next_date)
        VALUES (?, ?, ?);
    """, (lead_id, last_date, next_date))
    conn.commit()
    conn.close()
    return {"message": "Call plan added successfully!"}

def update_this(lead_id,last_date,next_date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE call_plan SET last_date = ?, next_date = ? WHERE lead_id = ?;
    """, (last_date, next_date, lead_id))
    conn.commit()
    conn.close()
    return {"message": "Call plan updated successfully!"}