import React from 'react';
import './Dashboard.css';
import AddLeadForm from './AddLeadForm';
import AddPocForm from './AddPocForm';
function AllForms() {
    return (
        <div className="dashboard">
            <center><h1>Forms</h1></center>
            <AddLeadForm />
            <AddPocForm />
        </div>
    );
}

export default AllForms;
