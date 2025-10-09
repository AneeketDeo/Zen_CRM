# ZenCRM - Modern Customer Relationship Management

A full-stack CRM application built with React frontend and Python FastAPI backend.

## Features

### 🧑‍💼 Contact & Lead Management
- Add, edit, delete contacts and leads
- Tag contacts with status (lead, prospect, customer)
- Search and filter contacts

### 📞 Interaction Tracking
- Log calls, emails, meetings, and notes per contact
- View timeline of interactions for each contact

### 👥 User Management
- Admin and standard user roles
- Login/logout functionality
- Assign contacts/deals to users

### 📅 Task System
- Create tasks linked to contacts or deals
- Set due dates and priorities
- Track task completion status

### 📊 Dashboard & Reporting
- Overview of total leads, deals, and conversion rates
- Charts for pipeline stages and user activity
- Recent interactions timeline

## Tech Stack

### Backend
- **Python 3.8+**
- **FastAPI** - Modern, fast web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **PostgreSQL/SQLite** - Database
- **JWT** - Authentication
- **Pydantic** - Data validation

### Frontend
- **React 18**
- **React Router** - Client-side routing
- **Axios** - HTTP client
- **Tailwind CSS** - Utility-first CSS framework
- **Lucide React** - Beautiful icons
- **Recharts** - Chart library

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

#### Option 1: Quick Setup (Recommended)
```bash
cd backend
python setup.py
```

#### Option 2: Manual Setup
1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# The setup script will create .env automatically
# Or manually create .env with:
# DATABASE_URL=sqlite:///./zencrm.db
# SECRET_KEY=your-secret-key-change-this-in-production
```

5. Run the application:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The application will be available at `http://localhost:3000`

## API Documentation

Once the backend is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Database

The application uses SQLite by default for development. For production, configure PostgreSQL:

1. Install PostgreSQL
2. Create a database
3. Update the `DATABASE_URL` in your `.env` file:
```
DATABASE_URL=postgresql://username:password@localhost/zencrm
```

## Default User

After starting the application, you can register a new user through the frontend or create one directly in the database.

## Project Structure

```
ZenCRM/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # Database operations
│   ├── auth.py              # Authentication logic
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── contexts/        # React contexts
│   │   └── App.js           # Main app component
│   ├── package.json
│   └── tailwind.config.js
└── README.md
```

## Features Overview

### Dashboard
- Contact statistics (total, leads, prospects, customers)
- Task overview (total, pending, completed)
- Deal metrics (total deals, value, won deals)
- Charts showing deals by stage
- Recent interactions timeline

### Contacts
- Create, read, update, delete contacts
- Search and filter functionality
- Status management (lead, prospect, customer)
- Contact details with company and position info

### Tasks
- Task management with priorities and due dates
- Link tasks to contacts
- Status tracking (pending, in progress, completed, cancelled)
- Filter by status and search functionality

### Deals
- Sales pipeline management
- Deal stages (prospecting, qualification, proposal, negotiation, closed won/lost)
- Value and probability tracking
- Expected close dates
- Link deals to contacts

## Development

### Backend Development
- The API follows RESTful conventions
- All endpoints require authentication except registration and login
- JWT tokens are used for authentication
- CORS is configured for the React frontend

### Frontend Development
- Components are organized by feature
- Tailwind CSS is used for styling
- React Context is used for state management
- Axios is configured with interceptors for authentication

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.
"# Zen_CRM" 
"# Zen_CRM" 
