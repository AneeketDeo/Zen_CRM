# ZenCRM Complete API Documentation

## Base URL
```
http://localhost:8000
```

---

## 🔐 Authentication Endpoints

### 1. Register User
**POST** `/register`

**Headers:**
```
Content-Type: application/json
```

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123",
  "full_name": "John Doe",
  "role": "user"
}
```

**Parameters:**
- `email` (string, required): Valid email address
- `password` (string, required): 6-72 characters
- `full_name` (string, required): User's full name
- `role` (string, optional): "admin" or "user" (default: "user")

**Success Response (201):**
```json
{
  "id": 1,
  "email": "user@example.com",
  "full_name": "John Doe",
  "role": "user",
  "is_active": true,
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

**Error Response (400):**
```json
{
  "detail": "Email already registered"
}
```

**Validation Error (422):**
```json
{
  "detail": [
    {
      "loc": ["body", "password"],
      "msg": "Password must be at least 6 characters long",
      "type": "value_error"
    }
  ]
}
```

---

### 2. Login
**POST** `/token`

**Headers:**
```
Content-Type: application/x-www-form-urlencoded
```

**Request Body (Form Data):**
```
username: user@example.com
password: password123
```

**Parameters:**
- `username` (string, required): Email address
- `password` (string, required): User password

**Success Response (200):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Error Response (401):**
```json
{
  "detail": "Incorrect email or password"
}
```

---

### 3. Get Current User
**GET** `/users/me`

**Headers:**
```
Authorization: Bearer <jwt_token>
```

**Success Response (200):**
```json
{
  "id": 1,
  "email": "user@example.com",
  "full_name": "John Doe",
  "role": "user",
  "is_active": true,
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

**Error Response (401):**
```json
{
  "detail": "Could not validate credentials"
}
```

---

### 4. Get All Users
**GET** `/users`

**Headers:**
```
Authorization: Bearer <jwt_token>
```

**Query Parameters:**
- `skip` (integer, optional): Number of records to skip (default: 0)
- `limit` (integer, optional): Maximum records to return (default: 100)

**Success Response (200):**
```json
[
  {
    "id": 1,
    "email": "user@example.com",
    "full_name": "John Doe",
    "role": "user",
    "is_active": true,
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
  },
  {
    "id": 2,
    "email": "admin@example.com",
    "full_name": "Admin User",
    "role": "admin",
    "is_active": true,
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
  }
]
```

---

## 👥 Contact Management Endpoints

### 1. Create Contact
**POST** `/contacts`

**Headers:**
```
Authorization: Bearer <jwt_token>
Content-Type: application/json
```

**Request Body:**
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "phone": "+1234567890",
  "company": "Acme Corp",
  "position": "Manager",
  "status": "lead",
  "notes": "Potential customer"
}
```

**Parameters:**
- `first_name` (string, required): Contact's first name
- `last_name` (string, required): Contact's last name
- `email` (string, optional): Contact's email address
- `phone` (string, optional): Contact's phone number
- `company` (string, optional): Company name
- `position` (string, optional): Job position
- `status` (string, optional): "lead", "prospect", or "customer" (default: "lead")
- `notes` (string, optional): Additional notes

**Success Response (201):**
```json
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "phone": "+1234567890",
  "company": "Acme Corp",
  "position": "Manager",
  "status": "lead",
  "notes": "Potential customer",
  "owner_id": 1,
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

---

### 2. Get All Contacts
**GET** `/contacts`

**Headers:**
```
Authorization: Bearer <jwt_token>
```

**Query Parameters:**
- `skip` (integer, optional): Number of records to skip (default: 0)
- `limit` (integer, optional): Maximum records to return (default: 100)

**Success Response (200):**
```json
[
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "phone": "+1234567890",
    "company": "Acme Corp",
    "position": "Manager",
    "status": "lead",
    "notes": "Potential customer",
    "owner_id": 1,
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
  }
]
```

---

### 3. Get Contact by ID
**GET** `/contacts/{contact_id}`

**Headers:**
```
Authorization: Bearer <jwt_token>
```

**Path Parameters:**
- `contact_id` (integer, required): Contact ID

**Success Response (200):**
```json
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "phone": "+1234567890",
  "company": "Acme Corp",
  "position": "Manager",
  "status": "lead",
  "notes": "Potential customer",
  "owner_id": 1,
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

**Error Response (404):**
```json
{
  "detail": "Contact not found"
}
```

---

### 4. Update Contact
**PUT** `/contacts/{contact_id}`

**Headers:**
```
Authorization: Bearer <jwt_token>
Content-Type: application/json
```

**Path Parameters:**
- `contact_id` (integer, required): Contact ID

**Request Body:**
```json
{
  "first_name": "John",
  "last_name": "Smith",
  "email": "john.smith@example.com",
  "phone": "+1234567890",
  "company": "New Corp",
  "position": "Director",
  "status": "prospect",
  "notes": "Updated notes"
}
```

**Parameters (all optional):**
- `first_name` (string): Contact's first name
- `last_name` (string): Contact's last name
- `email` (string): Contact's email address
- `phone` (string): Contact's phone number
- `company` (string): Company name
- `position` (string): Job position
- `status` (string): "lead", "prospect", or "customer"
- `notes` (string): Additional notes

**Success Response (200):**
```json
{
  "id": 1,
  "first_name": "John",
  "last_name": "Smith",
  "email": "john.smith@example.com",
  "phone": "+1234567890",
  "company": "New Corp",
  "position": "Director",
  "status": "prospect",
  "notes": "Updated notes",
  "owner_id": 1,
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:30:00Z"
}
```

**Error Response (404):**
```json
{
  "detail": "Contact not found"
}
```

---

### 5. Delete Contact
**DELETE** `/contacts/{contact_id}`

**Headers:**
```
Authorization: Bearer <jwt_token>
```

**Path Parameters:**
- `contact_id` (integer, required): Contact ID

**Success Response (200):**
```json
{
  "message": "Contact deleted successfully"
}
```

**Error Response (404):**
```json
{
  "detail": "Contact not found"
}
```

---

## 📞 Interaction Tracking Endpoints

### 1. Create Interaction
**POST** `/interactions`

**Headers:**
```
Authorization: Bearer <jwt_token>
Content-Type: application/json
```

**Request Body:**
```json
{
  "type": "call",
  "subject": "Follow-up call",
  "notes": "Discussed pricing and timeline",
  "contact_id": 1
}
```

**Parameters:**
- `type` (string, required): "call", "email", "meeting", or "note"
- `subject` (string, required): Interaction subject
- `notes` (string, optional): Additional notes
- `contact_id` (integer, required): Contact ID

**Success Response (201):**
```json
{
  "id": 1,
  "type": "call",
  "subject": "Follow-up call",
  "notes": "Discussed pricing and timeline",
  "contact_id": 1,
  "user_id": 1,
  "created_at": "2024-01-01T12:00:00Z"
}
```

---

### 2. Get Interactions by Contact
**GET** `/contacts/{contact_id}/interactions`

**Headers:**
```
Authorization: Bearer <jwt_token>
```

**Path Parameters:**
- `contact_id` (integer, required): Contact ID

**Success Response (200):**
```json
[
  {
    "id": 1,
    "type": "call",
    "subject": "Follow-up call",
    "notes": "Discussed pricing and timeline",
    "contact_id": 1,
    "user_id": 1,
    "created_at": "2024-01-01T12:00:00Z"
  },
  {
    "id": 2,
    "type": "email",
    "subject": "Proposal sent",
    "notes": "Sent pricing proposal",
    "contact_id": 1,
    "user_id": 1,
    "created_at": "2024-01-01T13:00:00Z"
  }
]
```

---

## ✅ Task Management Endpoints

### 1. Create Task
**POST** `/tasks`

**Headers:**
```
Authorization: Bearer <jwt_token>
Content-Type: application/json
```

**Request Body:**
```json
{
  "title": "Follow up with client",
  "description": "Call client about proposal",
  "priority": "high",
  "status": "pending",
  "due_date": "2024-01-15T10:00:00Z",
  "contact_id": 1
}
```

**Parameters:**
- `title` (string, required): Task title
- `description` (string, optional): Task description
- `priority` (string, optional): "low", "medium", "high", or "urgent" (default: "medium")
- `status` (string, optional): "pending", "in_progress", "completed", or "cancelled" (default: "pending")
- `due_date` (datetime, optional): Task due date (ISO format)
- `contact_id` (integer, optional): Associated contact ID

**Success Response (201):**
```json
{
  "id": 1,
  "title": "Follow up with client",
  "description": "Call client about proposal",
  "priority": "high",
  "status": "pending",
  "due_date": "2024-01-15T10:00:00Z",
  "contact_id": 1,
  "owner_id": 1,
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

---

### 2. Get All Tasks
**GET** `/tasks`

**Headers:**
```
Authorization: Bearer <jwt_token>
```

**Query Parameters:**
- `skip` (integer, optional): Number of records to skip (default: 0)
- `limit` (integer, optional): Maximum records to return (default: 100)

**Success Response (200):**
```json
[
  {
    "id": 1,
    "title": "Follow up with client",
    "description": "Call client about proposal",
    "priority": "high",
    "status": "pending",
    "due_date": "2024-01-15T10:00:00Z",
    "contact_id": 1,
    "owner_id": 1,
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
  }
]
```

---

### 3. Get Task by ID
**GET** `/tasks/{task_id}`

**Headers:**
```
Authorization: Bearer <jwt_token>
```

**Path Parameters:**
- `task_id` (integer, required): Task ID

**Success Response (200):**
```json
{
  "id": 1,
  "title": "Follow up with client",
  "description": "Call client about proposal",
  "priority": "high",
  "status": "pending",
  "due_date": "2024-01-15T10:00:00Z",
  "contact_id": 1,
  "owner_id": 1,
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

**Error Response (404):**
```json
{
  "detail": "Task not found"
}
```

---

### 4. Update Task
**PUT** `/tasks/{task_id}`

**Headers:**
```
Authorization: Bearer <jwt_token>
Content-Type: application/json
```

**Path Parameters:**
- `task_id` (integer, required): Task ID

**Request Body:**
```json
{
  "title": "Updated task title",
  "description": "Updated description",
  "priority": "medium",
  "status": "in_progress",
  "due_date": "2024-01-20T10:00:00Z"
}
```

**Parameters (all optional):**
- `title` (string): Task title
- `description` (string): Task description
- `priority` (string): "low", "medium", "high", or "urgent"
- `status` (string): "pending", "in_progress", "completed", or "cancelled"
- `due_date` (datetime): Task due date (ISO format)

**Success Response (200):**
```json
{
  "id": 1,
  "title": "Updated task title",
  "description": "Updated description",
  "priority": "medium",
  "status": "in_progress",
  "due_date": "2024-01-20T10:00:00Z",
  "contact_id": 1,
  "owner_id": 1,
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:30:00Z"
}
```

**Error Response (404):**
```json
{
  "detail": "Task not found"
}
```

---

### 5. Delete Task
**DELETE** `/tasks/{task_id}`

**Headers:**
```
Authorization: Bearer <jwt_token>
```

**Path Parameters:**
- `task_id` (integer, required): Task ID

**Success Response (200):**
```json
{
  "message": "Task deleted successfully"
}
```

**Error Response (404):**
```json
{
  "detail": "Task not found"
}
```

---

## 💼 Deal Management Endpoints

### 1. Create Deal
**POST** `/deals`

**Headers:**
```
Authorization: Bearer <jwt_token>
Content-Type: application/json
```

**Request Body:**
```json
{
  "title": "Software License Deal",
  "description": "Annual software license for 100 users",
  "value": 50000.00,
  "stage": "prospecting",
  "probability": 25,
  "expected_close_date": "2024-03-15T00:00:00Z",
  "contact_id": 1
}
```

**Parameters:**
- `title` (string, required): Deal title
- `description` (string, optional): Deal description
- `value` (float, optional): Deal value in currency
- `stage` (string, optional): "prospecting", "qualification", "proposal", "negotiation", "closed_won", or "closed_lost" (default: "prospecting")
- `probability` (integer, optional): Probability percentage 0-100 (default: 0)
- `expected_close_date` (datetime, optional): Expected close date (ISO format)
- `contact_id` (integer, required): Associated contact ID

**Success Response (201):**
```json
{
  "id": 1,
  "title": "Software License Deal",
  "description": "Annual software license for 100 users",
  "value": 50000.00,
  "stage": "prospecting",
  "probability": 25,
  "expected_close_date": "2024-03-15T00:00:00Z",
  "contact_id": 1,
  "owner_id": 1,
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

---

### 2. Get All Deals
**GET** `/deals`

**Headers:**
```
Authorization: Bearer <jwt_token>
```

**Query Parameters:**
- `skip` (integer, optional): Number of records to skip (default: 0)
- `limit` (integer, optional): Maximum records to return (default: 100)

**Success Response (200):**
```json
[
  {
    "id": 1,
    "title": "Software License Deal",
    "description": "Annual software license for 100 users",
    "value": 50000.00,
    "stage": "prospecting",
    "probability": 25,
    "expected_close_date": "2024-03-15T00:00:00Z",
    "contact_id": 1,
    "owner_id": 1,
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
  }
]
```

---

### 3. Get Deal by ID
**GET** `/deals/{deal_id}`

**Headers:**
```
Authorization: Bearer <jwt_token>
```

**Path Parameters:**
- `deal_id` (integer, required): Deal ID

**Success Response (200):**
```json
{
  "id": 1,
  "title": "Software License Deal",
  "description": "Annual software license for 100 users",
  "value": 50000.00,
  "stage": "prospecting",
  "probability": 25,
  "expected_close_date": "2024-03-15T00:00:00Z",
  "contact_id": 1,
  "owner_id": 1,
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

**Error Response (404):**
```json
{
  "detail": "Deal not found"
}
```

---

### 4. Update Deal
**PUT** `/deals/{deal_id}`

**Headers:**
```
Authorization: Bearer <jwt_token>
Content-Type: application/json
```

**Path Parameters:**
- `deal_id` (integer, required): Deal ID

**Request Body:**
```json
{
  "title": "Updated Deal Title",
  "description": "Updated description",
  "value": 60000.00,
  "stage": "qualification",
  "probability": 50,
  "expected_close_date": "2024-04-15T00:00:00Z"
}
```

**Parameters (all optional):**
- `title` (string): Deal title
- `description` (string): Deal description
- `value` (float): Deal value in currency
- `stage` (string): "prospecting", "qualification", "proposal", "negotiation", "closed_won", or "closed_lost"
- `probability` (integer): Probability percentage 0-100
- `expected_close_date` (datetime): Expected close date (ISO format)

**Success Response (200):**
```json
{
  "id": 1,
  "title": "Updated Deal Title",
  "description": "Updated description",
  "value": 60000.00,
  "stage": "qualification",
  "probability": 50,
  "expected_close_date": "2024-04-15T00:00:00Z",
  "contact_id": 1,
  "owner_id": 1,
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:30:00Z"
}
```

**Error Response (404):**
```json
{
  "detail": "Deal not found"
}
```

---

### 5. Delete Deal
**DELETE** `/deals/{deal_id}`

**Headers:**
```
Authorization: Bearer <jwt_token>
```

**Path Parameters:**
- `deal_id` (integer, required): Deal ID

**Success Response (200):**
```json
{
  "message": "Deal deleted successfully"
}
```

**Error Response (404):**
```json
{
  "detail": "Deal not found"
}
```

---

## 📊 Dashboard Endpoints

### 1. Get Dashboard Statistics
**GET** `/dashboard/stats`

**Headers:**
```
Authorization: Bearer <jwt_token>
```

**Success Response (200):**
```json
{
  "total_contacts": 25,
  "total_leads": 10,
  "total_prospects": 8,
  "total_customers": 7,
  "total_tasks": 15,
  "pending_tasks": 8,
  "completed_tasks": 7,
  "total_deals": 12,
  "total_deal_value": 150000.0,
  "deals_by_stage": {
    "prospecting": 3,
    "qualification": 2,
    "proposal": 2,
    "negotiation": 3,
    "closed_won": 2,
    "closed_lost": 0
  },
  "recent_interactions": [
    {
      "id": 1,
      "type": "call",
      "subject": "Follow-up call",
      "notes": "Discussed pricing",
      "contact_id": 1,
      "user_id": 1,
      "created_at": "2024-01-01T12:00:00Z"
    }
  ]
}
```

---

## 🔧 Common Error Responses

### 401 Unauthorized
```json
{
  "detail": "Could not validate credentials"
}
```

### 403 Forbidden
```json
{
  "detail": "Not enough permissions"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 422 Validation Error
```json
{
  "detail": [
    {
      "loc": ["body", "field_name"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

---

## 📝 Postman Collection Setup

### Environment Variables
Create these variables in Postman:
- `base_url`: `http://localhost:8000`
- `token`: (will be set after login)

### Pre-request Script (for authenticated endpoints)
```javascript
pm.request.headers.add({
    key: 'Authorization',
    value: 'Bearer ' + pm.environment.get('token')
});
```

### Test Script (for login endpoint)
```javascript
if (pm.response.code === 200) {
    const response = pm.response.json();
    pm.environment.set('token', response.access_token);
}
```

---

## 🚀 Complete Test Sequence

1. **Register User**
   ```
   POST {{base_url}}/register
   ```

2. **Login**
   ```
   POST {{base_url}}/token
   ```

3. **Get Profile**
   ```
   GET {{base_url}}/users/me
   ```

4. **Create Contact**
   ```
   POST {{base_url}}/contacts
   ```

5. **Get Contacts**
   ```
   GET {{base_url}}/contacts
   ```

6. **Create Task**
   ```
   POST {{base_url}}/tasks
   ```

7. **Create Deal**
   ```
   POST {{base_url}}/deals
   ```

8. **Get Dashboard**
   ```
   GET {{base_url}}/dashboard/stats
   ```

This documentation provides complete examples for testing all endpoints with Postman!

