import React, { useState, useEffect } from 'react';

function PerformanceList() {
    const [data, setData] = useState([]);

    useEffect(() => {
        // Simulate API call
        fetch('http://127.0.0.1:8000/leads/performance') // Replace with your API endpoint
            .then((response) => response.json())
            .then((data) => setData(data))
            .catch((error) => console.error('Error fetching performance data:', error));
    }, []);

    return (
        <div style={{ padding: '60px', fontFamily: 'Arial, sans-serif' }}>
            <h2>Lead Performance Data</h2>
            <ul style={{ listStyleType: 'none', padding: 0 }}>
                {data.map((item) => (
                    <li 
                        key={item.lead_id} 
                        style={{
                            border: '1px solid #ccc',
                            borderRadius: '8px',
                            padding: '10px',
                            marginBottom: '10px',
                            display: 'flex',
                            justifyContent: 'space-between',
                            alignItems: 'center',
                        }}
                    >
                        <div>
                            <strong>Lead ID:</strong> {item.lead_id} <br />
                            <strong>Total Amount:</strong> ₹{item.total_amount} <br />
                            <strong>Total Orders:</strong> {item.total_order_count}
                        </div>
                        <div 
                            style={{
                                fontSize: '12px',
                                fontWeight: 'bold',
                                color: 'white',
                                textAlign: 'right',
                            }}
                        >
                            Performance Score:
                            <div style={{ fontSize: '10px', color: 'white' }}>
                                {item.performance_score.toFixed(1)}
                            </div>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default PerformanceList;
