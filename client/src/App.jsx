import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import AllForms from "./components/Forms";
import Dashboard from "./components/Dashboard";

function App() {
  return (
    <div className="App">
      <Router>
            <Routes>
                <Route path="/forms" element={<AllForms/>} />
                <Route path="/" element={<Dashboard/>} />
                {/* <Route path="/forms" element={<Forms />} />
                <Route path="/call-plan" element={<CallPlans />} />
                <Route path="/performance" element={<PerformanceList/>} /> */}
            </Routes>
        </Router>
      
    </div>
  );
}

export default App;
