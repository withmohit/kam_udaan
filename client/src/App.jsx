import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './components/Login';
import Navbar from './components/Navbar';
import CallPlans from './components/CallPlans';
import PerformanceList from './components/PerformanceList';
import AllForms from './components/Forms';
import AddInteractionForm from './components/AddInteractionForm';
function App() {
  const [isAuthenticated, setIsAuthenticated] = React.useState(!!localStorage.getItem('kam_id'));

  const handleLogin = (id) => {
    setIsAuthenticated(true);
  };

  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        {isAuthenticated && <Navbar />}
        <div className="container mx-auto px-4 py-8">
          <Routes>
            <Route 
              path="/" 
              element={
                !isAuthenticated ? (
                  <Login onLogin={handleLogin} />
                ) : (
                  <Navigate to="/callplans" replace />
                )
              } 
            />
            <Route 
              path="/callplans" 
              element={
                isAuthenticated ? (
                  <>
                  <CallPlans />
                  <AddInteractionForm />
                  </>  
                ) : (
                  <Navigate to="/" replace />
                )
              } 
            />
            <Route 
              path="/performance" 
              element={
                isAuthenticated ? (
                  <PerformanceList />
                ) : (
                  <Navigate to="/" replace />
                )
              } 
            />
            <Route 
              path="/form" 
              element={
                isAuthenticated ? (
                  <AllForms/>
                ) : (
                  <Navigate to="/" replace />
                )
              } 
            />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;