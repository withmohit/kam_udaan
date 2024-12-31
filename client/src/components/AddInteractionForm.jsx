import React, { useState } from 'react';
import axios from 'axios';
import './form.css';
function AddInteractionForm() {
    const [formData, setFormData] = useState({
        lead_id: '',
        type: 'Call', // Default value for the dropdown
        notes: ''
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const { lead_id, ...interactionData } = formData; // Extract lead_id
            
            const response = await axios.post(
                `http://127.0.0.1:8000/leads/${lead_id}/interactions/`, 
                interactionData
            );
            alert(response.data.message || 'Interaction added successfully!');
        } catch (error) {
            console.error('Error adding interaction:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h3>Add Interaction</h3>
            <input
                type="number"
                name="lead_id"
                placeholder="Lead ID"
                value={formData.lead_id}
                onChange={handleChange}
                required
            />
            <select
                name="type"
                value={formData.type}
                onChange={handleChange}
                required
            >
                <option value="Call">Call</option>
                <option value="Visit">Visit</option>
                <option value="Order">Order</option>
            </select>
            <textarea
                name="notes"
                placeholder="Interaction Notes"
                value={formData.notes}
                onChange={handleChange}
                required
            />
            <button type="submit">Add Interaction</button>
        </form>
    );
}

export default AddInteractionForm;
