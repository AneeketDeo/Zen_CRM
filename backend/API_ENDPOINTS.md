# ZenCRM API Endpoints Documentation

## Base URL
```
http://localhost:8000
```

## Authentication
Most endpoints require authentication. Include the JWT token in the Authorization header:
```
Authorization: Bearer <your_jwt_token>
```

---

## 🔐 Authentication Endpoints

### 1. Register User
**POST** `/register`
```json
{
  "email": "user@example.com",
  "password": "password123",
  "full_name": "John Doe",
  "role": "user"
}
```

### 2. Login
**POST** `/token`
```
Content-Type: application/x-www-form-urlencoded

username: user@example.com
password: password123
```

### 3. Get Current User
**GET** `/users/me`
```
Authorization: Bearer <token>
```

### 4. Get All Users
**GET** `/users`
```
Authorization: Bearer <token>
```

---

## 👥 Contact Management Endpoints

### 1. Create Contact
**POST** `/contacts`
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

### 2. Get All Contacts
**GET** `/contacts`
```
Authorization: Bearer <token>
```

### 3. Get Contact by ID
**GET** `/contacts/{contact_id}`
```
Authorization: Bearer <token>
```

### 4. Update Contact
**PUT** `/contacts/{contact_id}`
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

### 5. Delete Contact
**DELETE** `/contacts/{contact_id}`
```
Authorization: Bearer <token>
```

---

## 📞 Interaction Tracking Endpoints

### 1. Create Interaction
**POST** `/interactions`
```json
{
  "type": "call",
  "subject": "Follow-up call",
  "notes": "Discussed pricing and timeline",
  "contact_id": 1
}
```

**Interaction Types:**
- `call`
- `email`
- `meeting`
- `note`

### 2. Get Interactions by Contact
**GET** `/contacts/{contact_id}/interactions`
```
Authorization: Bearer <token>
```

---

## ✅ Task Management Endpoints

### 1. Create Task
**POST** `/tasks`
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

**Priority Options:**
- `low`
- `medium`
- `high`
- `urgent`

**Status Options:**
- `pending`
- `in_progress`
- `completed`
- `cancelled`

### 2. Get All Tasks
**GET** `/tasks`
```
Authorization: Bearer <token>
```

### 3. Get Task by ID
**GET** `/tasks/{task_id}`
```
Authorization: Bearer <token>
```

### 4. Update Task
**PUT** `/tasks/{task_id}`
```json
{
  "title": "Updated task title",
  "description": "Updated description",
  "priority": "medium",
  "status": "in_progress",
  "due_date": "2024-01-20T10:00:00Z"
}
```

### 5. Delete Task
**DELETE** `/tasks/{task_id}`
```
Authorization: Bearer <token>
```

---

## 💼 Deal Management Endpoints

### 1. Create Deal
**POST** `/deals`
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

**Stage Options:**
- `prospecting`
- `qualification`
- `proposal`
- `negotiation`
- `closed_won`
- `closed_lost`

### 2. Get All Deals
**GET** `/deals`
```
Authorization: Bearer <token>
```

### 3. Get Deal by ID
**GET** `/deals/{deal_id}`
```
Authorization: Bearer <token>
```

### 4. Update Deal
**PUT** `/deals/{deal_id}`
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

### 5. Delete Deal
**DELETE** `/deals/{deal_id}`
```
Authorization: Bearer <token>
```

---

## 📊 Dashboard Endpoints

### 1. Get Dashboard Statistics
**GET** `/dashboard/stats`
```
Authorization: Bearer <token>
```

**Response Example:**
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
  "recent_interactions": [...]
}
```

---

## 🔧 Postman Collection Setup

### Environment Variables
Create these variables in Postman:
- `base_url`: `http://localhost:8000`
- `token`: (will be set after login)

### Authentication Flow
1. **Register/Login**: Use `/register` or `/token` endpoint
2. **Copy Token**: From response, copy the `access_token`
3. **Set Authorization**: In Postman, go to Authorization tab, select "Bearer Token", paste the token
4. **Test Endpoints**: Use the token for all authenticated endpoints

### Example Postman Setup

#### 1. Register User
```
POST {{base_url}}/register
Content-Type: application/json

{
  "email": "test@example.com",
  "password": "password123",
  "full_name": "Test User"
}
```

#### 2. Login
```
POST {{base_url}}/token
Content-Type: application/x-www-form-urlencoded

username: test@example.com
password: password123
```

#### 3. Set Token Variable
In the login response, copy the `access_token` and set it as the `token` variable.

#### 4. Test Authenticated Endpoint
```
GET {{base_url}}/users/me
Authorization: Bearer {{token}}
```

---

## 📝 Common Response Formats

### Success Response
```json
{
  "id": 1,
  "field1": "value1",
  "field2": "value2",
  "created_at": "2024-01-01T00:00:00Z"
}
```

### Error Response
```json
{
  "detail": "Error message"
}
```

### Validation Error
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

---

## 🚀 Quick Test Sequence

1. **Start Server**: `python main.py`
2. **Register User**: POST `/register`
3. **Login**: POST `/token`
4. **Get Profile**: GET `/users/me`
5. **Create Contact**: POST `/contacts`
6. **Get Contacts**: GET `/contacts`
7. **Create Task**: POST `/tasks`
8. **Create Deal**: POST `/deals`
9. **Get Dashboard**: GET `/dashboard/stats`

---

## 📚 Interactive API Documentation

Once the server is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

These provide interactive documentation where you can test endpoints directly in the browser!

