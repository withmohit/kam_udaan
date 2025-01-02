# Udaan Lead Management System 🚀

## Project Overview

The Lead Management System for Udaan is a tool designed to help Key Account Managers (KAMs) efficiently manage relationships with large restaurant accounts. It offers:

- **Lead Management**: Add and track restaurant leads.
- **Contact Management**: Manage multiple Points of Contact (POCs) with roles and details.
- **Interaction Tracking**: Record calls, orders, and maintain interaction logs.
- **Call Planning**: Schedule and track calls with customizable frequencies.
- **Performance Tracking**: Monitor account performance, ordering patterns, and identify underperforming accounts.

### Technical Highlights
- Efficient database schemas and real-time querying.
- RESTful APIs with secure authentication and error handling.
- Automated call scheduling and performance metric calculations.

This system ensures streamlined workflows, improved client relationships, and better account performance tracking for KAMs.

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