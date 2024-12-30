from database import get_db_connection

def add_interaction_query(lead_id, data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO interactions (lead_id, interaction_date, type, notes)
        VALUES (?, date('now'), ?, ?);
    """, (lead_id, data.type, data.notes))
    conn.commit()
    conn.close()
    return {"message": "Interaction added successfully!"}