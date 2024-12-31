import React from 'react';
import './Dashboard.css';
// import OrderForm from "./OrderForm";
import CallPlans from "./CallPlans";
import PerformanceList from "./PerformanceList";
function Dashboard() {
    return (
        <div className="dashboard">
            <center><h1>Dashboard</h1></center>
            <CallPlans/>
            <PerformanceList/>
        </div>
    );
}

export default Dashboard;
