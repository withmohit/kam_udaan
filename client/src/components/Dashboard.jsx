import React from 'react';
import AddLeadForm from './AddLeadForm';
import UpdateCallPlanForm from './UpdateCallPlanForm';
import AddPocForm from './AddPocForm';
import AddInteractionForm from './AddInteractionForm';

function Dashboard() {
    return (
        <div>
            <h1>Dashboard</h1>
            <AddLeadForm />
            <UpdateCallPlanForm />
            <AddPocForm />
            <AddInteractionForm />
        </div>
    );
}

export default Dashboard;
