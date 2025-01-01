import React from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import { Phone, BarChart2, FileText, LogOut } from 'lucide-react';
import './Navbar.css';

const Navbar = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('kam_id');
    navigate('/');
    window.location.reload();
  };

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <div className="navbar-brand">
          <span>Dashboard</span>
        </div>
        <div className="navbar-links">
          <NavLink 
            to="/callplans" 
            className={({ isActive }) => 
              `nav-link ${isActive ? 'active' : ''}`
            }
          >
            <Phone className="icon" />
            <span>Call Plans</span>
          </NavLink>
          
          <NavLink 
            to="/performance" 
            className={({ isActive }) => 
              `nav-link ${isActive ? 'active' : ''}`
            }
          >
            <BarChart2 className="icon" />
            <span>Performance</span>
          </NavLink>
          
          <NavLink 
            to="/form" 
            className={({ isActive }) => 
              `nav-link ${isActive ? 'active' : ''}`
            }
          >
            <FileText className="icon" />
            <span>Form</span>
          </NavLink>
          
          <button className="nav-link logout" onClick={handleLogout}>
            <LogOut className="icon" />
            <span>Logout</span>
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
