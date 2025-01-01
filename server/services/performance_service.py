from database import get_db_connection


def leads_performance(kam_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    performance = cursor.execute("""
    SELECT
    call_plan.lead_id,
    COALESCE(SUM(order_amount), 0) AS total_amount,
    COALESCE(COUNT(orders.id), 0) AS total_order_count,
    (call_plan.frequency * 0.3 + COALESCE(SUM(order_amount), 0) * 0.4 + COALESCE(COUNT(orders.id), 0) * 0.3) AS performance_score
    FROM call_plan
    LEFT JOIN orders ON call_plan.lead_id = orders.lead_id
    JOIN leads ON leads.id = call_plan.lead_id AND leads.kam_id = ?
    GROUP BY call_plan.lead_id, call_plan.frequency
    ORDER BY performance_score DESC;

    """,(kam_id,)).fetchall()
    # print(performance)
    conn.close()
    return performance
    # where leads.kam_id = ?