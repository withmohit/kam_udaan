import React, { useState } from 'react';
import axios from 'axios';

function AddPocForm() {
    const [formData, setFormData] = useState({ lead_id: '', person_name: '', role: '', phone_number: '', email: '' });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const { lead_id, ...pocData } = formData; 
            const requestData = { 
                lead_id: parseInt(lead_id, 10), // Ensure lead_id is an integer
                ...pocData 
            };
            const response = await axios.post(`http://127.0.0.1:8000/leads/${requestData.lead_id}/contacts/`, requestData);
            alert(response.data.message || 'POC added successfully!');
        } catch (error) {
            alert(error.response?.data?.detail || 'An error occurred');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h3>Add POC</h3>
            <input 
                type="number" 
                name="lead_id" 
                placeholder="Lead ID" 
                value={formData.lead_id} 
                onChange={handleChange} 
                required 
            />
            <input 
                type="text" 
                name="person_name" 
                placeholder="Name" 
                value={formData.name} 
                onChange={handleChange} 
                required 
            />
            <input 
                type="text" 
                name="role" 
                placeholder="Role (Owner, Manager, etc.)" 
                value={formData.role} 
                onChange={handleChange} 
                required 
            />
            <input 
                type="text" 
                name="phone_number" 
                placeholder="Phone Number" 
                value={formData.phone_number} 
                onChange={handleChange} 
                required 
            />
            <input 
                type="email" 
                name="email" 
                placeholder="Email" 
                value={formData.email} 
                onChange={handleChange} 
                required 
            />
            <button type="submit">Add POC</button>
        </form>
    );
}

export default AddPocForm;
