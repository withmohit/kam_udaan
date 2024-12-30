from database import get_db_connection


def add_pocs(lead_id,data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO contacts (lead_id, person_name, role, phone_number, email)
        VALUES (?, ?, ?, ?, ?);
    """, (lead_id, data.person_name, data.role, data.phone_number, data.email))
    conn.commit()
    conn.close()
    return {"message": "Contact added successfully!"}

def get_pocs(lead_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    pocs = cursor.execute("SELECT * FROM contacts WHERE lead_id = ?", (lead_id,)).fetchall()
    conn.close()
    return pocs