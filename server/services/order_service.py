from database import get_db_connection

def add_order(lead_id,data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO orders (lead_id, order_date, order_amount, order_status)
        VALUES (?, date('now'), ?, 'Completed');
    """, (lead_id, data.order_amount))
    conn.commit()
    conn.close()
    return {"message": "Order added successfully!"}

def get_orders_summary():
    conn=get_db_connection()
    cursor=conn.cursor()
    orders=cursor.execute("""
        SELECT restaurant_name,count(orders.id) as order_count,sum(order_amount) as total_order_amount
        join leads on leads.id = orders.lead_id;
        group by lead_id
    """).fetchall()
    conn.close()
    return orders

def get_orders_summary_by_id(lead_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    orders = cursor.execute("SELECT * FROM orders WHERE lead_id = ?", (lead_id,)).fetchall()
    conn.close()
    return orders