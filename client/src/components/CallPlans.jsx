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
        const config = {
          headers: {
              'Kam-Id': localStorage.getItem('kam_id') || 'default_kam_id', // Replace with your logic for retrieving Kam-Id
          },
      };
        const response = await axios.get('http://127.0.0.1:8000/leads/call-plan',config);
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
    <div className='boxx'>
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
                <a href={`http://127.0.0.1:8000/leads/${plan.lead_id}/contacts`} target="_blank" rel="noopener noreferrer">View Contacts</a>
                <a href={`http://127.0.0.1:8000/leads/${plan.lead_id}/interactions/`} target="_blank" rel="noopener noreferrer">All Interactions</a>
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
              <a href={`http://127.0.0.1:8000/leads/${plan.lead_id}/contacts`} target="_blank" rel="noopener noreferrer">View Contacts</a>
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
