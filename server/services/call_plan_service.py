from datetime import datetime
from database import get_db_connection

current_date = datetime.now().strftime('%Y-%m-%d')

def pending_calls(kam_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT lead_id,restaurant_name,last_date,next_date FROM call_plan
        join leads on leads.id = call_plan.lead_id
        WHERE (next_date) <= ? and kam_id = ?;
    """, (current_date,kam_id))
    call_plan = cursor.fetchall()
    conn.close()
    return call_plan
    