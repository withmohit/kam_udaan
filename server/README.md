# FastAPI API Documentation

This document provides a comprehensive overview of the available API endpoints, their parameters, request/response formats, and usage examples.

## General Information

- **Title**: FastAPI
- **Version**: 0.1.0
- **OpenAPI Version**: 3.1.0

---

## Endpoints

### 1. `/leads/`

#### **POST**: Add Lead Endpoint

- **Summary**: Create a new lead.
- **Headers**:
  - `kam-id` (Optional, Integer): Key Account Manager ID.
- **Request Body**:
  ```json
  {
    "restaurant_name": "string",
    "address": "string",
    "frequency": 1
  }
  ```
- **Responses**:
  - **200**: Successful Response
  - **422**: Validation Error

#### **GET**: Get Leads Endpoint

- **Summary**: Retrieve a list of leads.
- **Headers**:
  - `kam-id` (Optional, Integer): Key Account Manager ID.
- **Responses**:
  - **200**: Successful Response
  - **422**: Validation Error

---

### 2. `/leads/call-plan/`

#### **GET**: Get Pending Calls

- **Summary**: Retrieve pending call plans.
- **Headers**:
  - `kam-id` (Optional, Integer): Key Account Manager ID.
- **Responses**:
  - **200**: Successful Response
  - **422**: Validation Error

---

### 3. `/leads/{lead_id}/contacts/`

#### **POST**: Add Lead POCs

- **Summary**: Add a new Point of Contact (POC) for a lead.
- **Path Parameters**:
  - `lead_id` (Required, Integer): ID of the lead.
- **Request Body**:
  ```json
  {
    "person_name": "string",
    "role": "string",
    "phone_number": "string",
    "email": "string",
    "lead_id": 1
  }
  ```
- **Responses**:
  - **200**: Successful Response
  - **422**: Validation Error

#### **GET**: Get Lead POCs

- **Summary**: Retrieve Points of Contact (POCs) for a lead.
- **Path Parameters**:
  - `lead_id` (Required, Integer): ID of the lead.
- **Responses**:
  - **200**: Successful Response
  - **422**: Validation Error

---

### 4. `/leads/{lead_id}/interactions/`

#### **POST**: Interaction

- **Summary**: Record a new interaction for a lead.
- **Path Parameters**:
  - `lead_id` (Required, Integer): ID of the lead.
- **Request Body**:
  ```json
  {
    "notes": "string",
    "type": "string"
  }
  ```
- **Responses**:
  - **200**: Successful Response
  - **422**: Validation Error

#### **GET**: Interactions

- **Summary**: Retrieve interactions for a lead.
- **Path Parameters**:
  - `lead_id` (Required, Integer): ID of the lead.
- **Responses**:
  - **200**: Successful Response
  - **422**: Validation Error

---

### 5. `/leads/{lead_id}/orders/`

#### **POST**: Create Order

- **Summary**: Create a new order for a lead.
- **Path Parameters**:
  - `lead_id` (Required, Integer): ID of the lead.
- **Request Body**:
  ```json
  {
    "order_amount": 100.0
  }
  ```
- **Responses**:
  - **200**: Successful Response
  - **422**: Validation Error

#### **GET**: View Order

- **Summary**: Retrieve orders for a lead.
- **Path Parameters**:
  - `lead_id` (Required, Integer): ID of the lead.
- **Responses**:
  - **200**: Successful Response
  - **422**: Validation Error

---

### 6. `/leads/orders/`

#### **GET**: All Orders

- **Summary**: Retrieve all orders.
- **Responses**:
  - **200**: Successful Response

---

### 7. `/leads/performance/`

#### **GET**: Performance

- **Summary**: Retrieve performance data.
- **Headers**:
  - `kam-id` (Optional, Integer): Key Account Manager ID.
- **Responses**:
  - **200**: Successful Response
  - **422**: Validation Error

---

### 8. `/leads/performance/{lead_id}/pattern`

#### **GET**: Performance Pattern

- **Summary**: Retrieve performance pattern for a lead.
- **Path Parameters**:
  - `lead_id` (Required, Integer): ID of the lead.
- **Responses**:
  - **200**: Successful Response
  - **422**: Validation Error

---

### 9. `/login/`

#### **POST**: Login

- **Summary**: Authenticate a user.
- **Request Body**:
  ```json
  {
    "kam_id": "string",
    "password": "string"
  }
  ```
- **Responses**:
  - **200**: Successful Response
  - **422**: Validation Error

---

### 10. `/`

#### **GET**: Root

- **Summary**: Retrieve API root information.
- **Responses**:
  - **200**: Successful Response

---

## Components

### Lead Schema

```json
{
  "restaurant_name": "string",
  "address": "string",
  "frequency": 1
}
```

### Contact Schema

```json
{
  "person_name": "string",
  "role": "string",
  "phone_number": "string",
  "email": "string",
  "lead_id": 1
}
```

### Interaction Schema

```json
{
  "notes": "string",
  "type": "string"
}
```

### Order Schema

```json
{
  "order_amount": 100.0
}
```

### Login Schema

```json
{
  "kam_id": "string",
  "password": "string"
}
```
