# Airline Operations Platform

A full-stack application for managing airline operations with a Python FastAPI backend and React + Vite frontend.

## Project Structure

```
airline-ops-platform/
├── backend/                    # FastAPI Python backend
│   ├── app/
│   │   ├── main.py            # FastAPI app entry point
│   │   ├── routers/           # API route handlers
│   │   │   └── flights.py
│   │   ├── models/            # SQLAlchemy ORM models
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── services/          # Business logic
│   │   └── database/          # Database configuration
│   ├── requirements.txt        # Python dependencies
│   ├── .env.example           # Environment variables template
│   └── .gitignore
├── frontend/                   # React + Vite frontend
│   ├── src/
│   │   ├── App.jsx            # Main React component
│   │   ├── main.jsx           # React entry point
│   │   ├── index.css          # Tailwind CSS styles
│   │   └── services/
│   │       └── api.js         # API client
│   ├── package.json           # Node dependencies
│   ├── vite.config.js         # Vite configuration
│   ├── tailwind.config.js     # Tailwind CSS configuration
│   ├── postcss.config.js      # PostCSS configuration
│   ├── index.html
│   └── .gitignore
└── .gitignore                 # Root .gitignore
```

## Backend Setup

### 1. Create a Python Virtual Environment

```bash
cd backend
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create .env File (Optional)

```bash
cp .env.example .env
```

The default SQLite database URL will be used if `.env` is not present.

### 4. Run the Backend

```bash
uvicorn app.main:app --reload
```

The backend will be available at `http://localhost:8000`

**API Endpoints:**
- `GET /api/health` - Health check
- `GET /api/flights` - Get all flights

## Frontend Setup

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Run the Frontend

```bash
npm run dev
```

The frontend will automatically open at `http://localhost:5173`

### 3. Build for Production

```bash
npm run build
```

## Running Both Services

### Terminal 1 - Backend

```bash
cd backend
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
uvicorn app.main:app --reload
```

### Terminal 2 - Frontend

```bash
cd frontend
npm run dev
```

The application will be available at `http://localhost:5173`

## Features

✅ FastAPI backend with CORS enabled for frontend
✅ SQLAlchemy ORM with SQLite (local dev) and PostgreSQL support
✅ React frontend with Vite for fast development
✅ Tailwind CSS for styling
✅ Flights API with sample data
✅ Loading states and error handling
✅ Responsive table UI
