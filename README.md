# Udaan Lead Management System 🚀

## Introduction

Udaan, a leading B2B e-commerce platform, requires a comprehensive Lead Management System for Key Account Managers (KAMs). This system is designed to help KAMs manage relationships with large restaurant accounts efficiently. It provides tools to track and manage leads, monitor interactions, and evaluate account performance effectively.

---

## Requirements

### Core Features

#### Lead Management
- Add new restaurant leads and store their basic information.
- Track the status of each lead.

#### Contact Management
- Manage multiple Points of Contact (POCs) for each restaurant.
- Store detailed contact information, including name, role, and contact details.
- Support different roles for POCs.

#### Interaction Tracking
- Record all interactions, including calls and orders.
- Maintain detailed logs with dates and interaction descriptions.

#### Call Planning
- Set custom call frequencies for leads.
- Display leads that require a call today.
- Track the last call made for each lead.

#### Performance Tracking
- Monitor high-performing accounts based on metrics.
- Analyze ordering patterns and frequency.
- Identify underperforming accounts for targeted action.

---

### Technical Requirements

#### Data Models
- Design efficient database schemas for entity relationship management.
- Ensure robust querying capabilities for real-time data access.

#### API Design
- Provide RESTful APIs for all operations.
- Implement comprehensive error handling mechanisms.
- Ensure secure authentication and authorization processes.

#### Business Logic
- Automate call scheduling based on lead requirements.
- Provide tools to calculate and display account performance metrics.
- Handle lead status transitions seamlessly.

---

## Key Functionalities

1. **Lead Management**:
   Manage a centralized database of restaurant leads.

2. **Contact Management**:
   Maintain detailed contact information for efficient communication.

3. **Call Planning**:
   Automate call scheduling and track daily tasks for KAMs.

4. **Performance Analysis**:
   Deliver insights on account performance to inform strategic decisions.

---

This system ensures streamlined workflows for KAMs, enhancing their ability to maintain strong client relationships and drive business growth effectively.

## 1. System Requirements 🖥️

To run this Lead Management System, ensure the following versions are installed:
- **Node.js**: v22.12.0
- **Python**: 3.12.3

---

## 2. Installation Instructions 🛠️

1. Clone this repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```bash
   cd "kam_udaan"
   ```

### For the Client:
3. Navigate to the client folder:
   ```bash
   cd client
   ```

4. Install the required dependencies:
   ```bash
   npm install
   ```

### For the Server:
5. Navigate to the server folder:
   ```bash
   cd server
   ```

6. Create and activate a virtual environment (refer to the [Python venv documentation](https://docs.python.org/3/library/venv.html)):
   ```bash
   python3 -m venv env
   source env/bin/activate   # For Linux/MacOS
   env\Scripts\activate    # For Windows
   ```

7. Install the required Python dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

### Running the System

- **Client Side**:
  ```bash
  npm run dev
  ```

- **Server Side**:
  ```bash
  fastapi dev main.py
  ```

---

## 3. API Documentation 📄

Refer to the [API Documentation](https://github.com/withmohit/kam_udaan/tree/master/server#readme) for detailed information about the available endpoints and their usage.

---

## 4. Sample Usage Examples

Examples of how to use this system can be found in the respective sections of the API documentation or by following these steps.

---