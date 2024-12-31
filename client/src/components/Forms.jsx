import React from 'react';
import './Dashboard.css';
import AddLeadForm from './AddLeadForm';
import AddPocForm from './AddPocForm';
import AddInteractionForm from './AddInteractionForm';
function AllForms() {
    return (
        <div className="dashboard">
            <center><h1>Forms</h1></center>
            <AddLeadForm />
            <AddPocForm />
            <AddInteractionForm />
        </div>
    );
}

export default AllForms;
