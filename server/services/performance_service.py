from database import get_db_connection


def leads_performance():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    leads_performance = cursor.execute("""
    SELECT
    call_plan.lead_id,
    COALESCE(SUM(order_amount), 0) AS total_amount,
    COALESCE(COUNT(orders.id), 0) AS total_order_count,
    (call_plan.frequency * 0.3 + COALESCE(SUM(order_amount), 0) * 0.4 + COALESCE(COUNT(orders.id), 0) * 0.3) AS performance_score
    FROM call_plan
    LEFT JOIN orders ON call_plan.lead_id = orders.lead_id
    GROUP BY call_plan.lead_id, call_plan.frequency
    ORDER BY performance_score DESC;

    """).fetchall()
    conn.close()
    return leads_performance