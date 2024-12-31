import React, { useState } from 'react';
import axios from 'axios';

const OrderForm = () => {
  const [leadId, setLeadId] = useState('');
  const [orderAmount, setOrderAmount] = useState('');

  // Handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault(); // Prevent form from refreshing the page

    // Ensure leadId is treated as a number
    const parsedLeadId = parseInt(leadId, 10);

    // Validate if leadId is a valid number
    if (isNaN(parsedLeadId)) {
      console.error('Lead ID must be a valid number');
      return; // Prevent submission if lead_id is not valid
    }

    const url = `http://127.0.0.1:8000/leads/${parsedLeadId}/orders`;

    const orderData = {
      order_amount: orderAmount
    };

    try {
      const response = await axios.post(url, orderData, {
        headers: {
          'Content-Type': 'application/json'
        }
      });

      alert(response.data.message || 'Order placed successfully!');
    } catch (error) {
      alert(error.response?.data?.detail || 'An error occurred while placing the order');
    }
  };

  return (
    <div>
      <h2>Make Order</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="lead_id">Lead ID:</label>
          <input
            type="text"
            id="lead_id"
            value={leadId}
            onChange={(e) => setLeadId(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="order_amount">Order Amount:</label>
          <input
            type="number"
            id="order_amount"
            value={orderAmount}
            onChange={(e) => setOrderAmount(e.target.value)}
            required
          />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default OrderForm;
