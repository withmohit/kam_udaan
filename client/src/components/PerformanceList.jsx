import React, { useState, useEffect } from 'react';
import axios from 'axios';

function PerformanceList() {
    const [data, setData] = useState([]);

    useEffect(() => {
        // Fetch performance data using axios
        const config = {
            headers: {
                'Kam-Id': localStorage.getItem('kam_id') || 'default_kam_id', // Replace with your logic for retrieving Kam-Id
            },
        };
        axios.get('http://127.0.0.1:8000/leads/performance',config) // Replace with your API endpoint
            .then((response) => setData(response.data))
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
                            width: '200%',
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
