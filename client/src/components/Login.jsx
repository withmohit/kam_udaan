import React, { useState } from "react";
import axios from "axios";
import OrderForm from "./OrderForm";
function Login({ onLogin }) {
    const [formData, setFormData] = useState({ kam_id: "", password: "" });
    const [error, setError] = useState("");

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://127.0.0.1:8000/login", formData);
            if (response.status === 200) {
                localStorage.setItem("kam_id", formData.kam_id); // Save kam_id in local storage
                onLogin(formData.kam_id); // Notify parent of successful login
            } else {
                setError("Login failed. Please try again.");
            }
        } catch (err) {
            setError(err.response?.data?.detail || "ID or password is incorrect.");
        }
    };

    return (
        <>
            <OrderForm />
            <div style={{ textAlign: "center", marginTop: "50px" }}>
                <h2>Login (For KAM)</h2>
                {error && <p style={{ color: "red" }}>{error}</p>}
                <form onSubmit={handleSubmit} style={{ display: "inline-block", textAlign: "left" }}>
                    <div>
                        <label>KAM ID:</label>
                        <input
                            type="number"
                            name="kam_id"
                            value={formData.kam_id}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div>
                        <label>Password:</label>
                        <input
                            type="password"
                            name="password"
                            value={formData.password}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <button type="submit">Login</button>
                </form>
            </div>
        </>
    );
}

export default Login;
