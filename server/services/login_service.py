from database import get_db_connection

def login_check(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    user = cursor.execute("SELECT * FROM kam WHERE id = ? AND password = ?", (data.kam_id, data.password)).fetchone()
    conn.close()
    if user:
        return True
    else:
        return False