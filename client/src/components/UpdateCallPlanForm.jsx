import React, { useState } from 'react';
import axios from 'axios'; // Ensure Axios is imported

function UpdateCallPlanForm() {
    const [formData, setFormData] = useState({
        lead_id: 0, // Field for lead ID
        notes:"",    // Call frequency in days
    });

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!formData.lead_id) {
            alert('Please provide a Lead ID!');
            return;
        }

        try {
            const url = `http://127.0.0.1:8000/leads/${formData.lead_id}/call_plan/`;
            const data = {
                freq: formData.freq,
                notes:formData.notes, // Ensure freq is an integer
            };

            const response = await axios.patch(url, data, {
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            alert(response.data.message || 'Call plan updated successfully!');
        } catch (error) {
            console.error('Error updating call plan:', error);
            alert(error.response?.data?.detail || 'An error occurred while updating the call plan.');
        }
    };

    return (
        <div>
            <h3>Update Call Plan</h3>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Lead ID:</label>
                    <input
                        type="number"
                        placeholder="Enter Lead ID"
                        value={formData.lead_id}
                        onChange={(e) => setFormData({ ...formData, lead_id: parseInt(e.target.value, 10) })}
                        required
                    />
                </div>
                <div>
                    <label>Notes:</label>
                    <input
                        type="text"
                        placeholder="Notes"
                        value={formData.notes}
                        onChange={(e) => setFormData({ ...formData, notes:e.target.value })}
                        required
                    />
                </div>
                <button type="submit">Update Call Plan</button>
            </form>
        </div>
    );
}

export default UpdateCallPlanForm;
