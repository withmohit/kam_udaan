from database import get_db_connection

def add_lead(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO leads (restaurant_name, address, contact_number, current_status, assigned_kam)
        VALUES (?, ?, ?, ?, ?);
    """, (data.restaurant_name, data.address, data.contact_number, data.current_status, data.assigned_kam))
    conn.commit()
    conn.close()
    return {"message": "Lead added successfully!"}

def get_all_leads():
    conn = get_db_connection()
    cursor = conn.cursor()
    leads = cursor.execute("SELECT * FROM leads").fetchall()
    conn.close()
    return leads

def add_pocs(lead_id,data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO contacts (lead_id, name, role, phone_number, email)
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