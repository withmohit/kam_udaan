from database import get_db_connection


def leads_performance(kam_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    performance = cursor.execute("""
    SELECT
    leads.restaurant_name,
    call_plan.lead_id,
    COALESCE(SUM(order_amount), 0) AS total_amount,
    COALESCE(COUNT(orders.id), 0) AS total_order_count,
    (call_plan.frequency * 0.3 + COALESCE(SUM(order_amount), 0) * 0.4 + COALESCE(COUNT(orders.id), 0) * 0.3) AS performance_score
    FROM call_plan
    LEFT JOIN orders ON call_plan.lead_id = orders.lead_id
    JOIN leads ON leads.id = call_plan.lead_id AND leads.kam_id = ?
    GROUP BY call_plan.lead_id
    ORDER BY performance_score DESC;

    """,(kam_id,)).fetchall()
    conn.close()
    return performance

def leads_performance_pattern(lead_id):
    conn=get_db_connection()
    cursor=conn.cursor()

    performance_pattern = cursor.execute("""
   WITH ordered_data AS (
    SELECT 
        lead_id, 
        julianday(order_date) - julianday(LAG(order_date) OVER (PARTITION BY lead_id ORDER BY order_date)) AS order_gap,
        order_amount
    FROM 
        orders
    WHERE 
        lead_id = ?
        )
    SELECT 
        lead_id,
        COUNT(*) AS total_orders,
        AVG(order_gap) AS avg_order_gap,
        SUM(order_amount) AS total_revenue
    FROM 
        ordered_data
    GROUP BY 
        lead_id;

    """, (lead_id,)).fetchall()
    conn.close()
    return performance_pattern