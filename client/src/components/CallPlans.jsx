import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './CallPlans.css';

const CallPlans = () => {
  const [callPlans, setCallPlans] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch the call plans data from API
  useEffect(() => {
    const fetchCallPlans = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/leads/call-plan');
        setCallPlans(response.data); // Assuming the response returns the correct array of call plans
        setLoading(false);
      } catch (err) {
        setError('Failed to fetch call plans.');
        setLoading(false);
      }
    };
    fetchCallPlans();
  }, []);

  // Separate the call plans into "pending calls" and "no interaction"
  const pendingCalls = callPlans.filter(plan => plan.next_date !== "");
  const noInteraction = callPlans.filter(plan => plan.next_date === "");

  return (
    <div>
      <h2>Pending Call Section</h2>
      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p>{error}</p>
      ) : (
        <div className="call-section">
          {pendingCalls.length > 0 ? (
            pendingCalls.map((plan, index) => (
              <div key={index} className="call-plan">
                <h3>{plan.restaurant_name}</h3>
                <p><strong>Lead ID:</strong> {plan.lead_id}</p>
                <p><strong>Last Interaction:</strong> {plan.last_date || 'No interaction'}</p>
                <p><strong>Next Call:</strong> {plan.next_date || 'No interaction'}</p>
              </div>
            ))
          ) : (
            <p>No pending calls.</p>
          )}
        </div>
      )}

      <h2>No Interaction Done</h2>
      <div className="no-interaction-section">
        {noInteraction.length > 0 ? (
          noInteraction.map((plan, index) => (
            <div key={index} className="call-plan">
              <h3>{plan.restaurant_name}</h3>
              <p><strong>Lead ID:</strong> {plan.lead_id}</p>
              <p><strong>Last Interaction:</strong> No interaction done.</p>
              <p><strong>Next Call:</strong> No interaction done.</p>
            </div>
          ))
        ) : (
          <p>No records available.</p>
        )}
      </div>
    </div>
  );
};

export default CallPlans;
