import React, { useState } from 'react';
import axios from 'axios';
import './form.css';

function AddLeadForm() {
    const [formData, setFormData] = useState({
        restaurant_name: '',
        address: '',
        frequency: '',
        order_count: '',
        current_status: '',
        assigned_kam: '',
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/leads/', formData);
            alert(response.data.message || 'Lead added successfully!');
        } catch (error) {
            alert(error.response?.data?.detail || 'An error occurred');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h3>Add Lead</h3>
            <input type="text" name="restaurant_name" placeholder="Restaurant Name" value={formData.restaurant_name} onChange={handleChange} required />
            <input type="text" name="address" placeholder="Address" value={formData.address} onChange={handleChange} required />
            <input type="number" name="frequency" placeholder="Frequency (days)" value={formData.frequency} onChange={handleChange} required />
            <input type="number" name="order_count" placeholder="Order Count" value={formData.order_count} onChange={handleChange} />
            <input type="text" name="current_status" placeholder="Current Status" value={formData.current_status} onChange={handleChange} required />
            <input type="text" name="assigned_kam" placeholder="Assigned KAM" value={formData.assigned_kam} onChange={handleChange} required />
            <button type="submit">Add Lead</button>
        </form>
    );
}

export default AddLeadForm;
