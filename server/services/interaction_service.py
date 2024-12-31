from datetime import datetime
from database import get_db_connection

current_date = datetime.now().strftime('%Y-%m-%d')

def add_interaction_query(lead_id, data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE call_plan SET 
    last_date = ?, -- Replace with your input date
    next_date = DATE(?, '+' || frequency || ' days') WHERE id = ?;
    """, (current_date, current_date, lead_id))
    
    cursor.execute("""
        INSERT INTO interactions (lead_id, interaction_date, type, notes)
        VALUES (?, ?, ?, ?);
        """, (lead_id,current_date,data.type ,data.notes))
    conn.commit()
    conn.close()
    return {"message": "Interaction added successfully!"}