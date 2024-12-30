from database import get_db_connection

def update_this(lead_id,last_date,data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE call_plan SET 
    last_date = ?, -- Replace with your input date
    next_date = DATE(?, '+' || frequency || ' days') WHERE id = ?;
    """, (last_date, last_date, lead_id))
    cursor.execute("""
        INSERT INTO interactions (lead_id, interaction_date, type, notes)
        VALUES (?, ?, 'Call', ?);
        """, (lead_id,last_date, data.notes))
    conn.commit()
    conn.close()
    return {"message": "Call plan updated successfully!"}

def pending_calls():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT restaurant_name,last_date,next_date FROM call_plan
        join leads on leads.id = call_plan.lead_id
        WHERE next_date <= date('now') or next_date is null;
    """)
    call_plan = cursor.fetchall()
    conn.close()
    return call_plan
    