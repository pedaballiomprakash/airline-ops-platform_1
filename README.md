# Airline Operations Management Platform

An AI-native full-stack platform for managing airline operations — flights, crew, aircraft, and bookings — with a FastAPI backend and React frontend.

## Tech Stack

**Backend** — FastAPI, PostgreSQL, SQLAlchemy, Alembic, JWT (python-jose), bcrypt

**Frontend** — React, Vite

## Project Structure

```
airline-ops-platform/
├── backend/
│   ├── alembic/              # database migrations
│   ├── app/
│   │   ├── core/             # config, security, dependencies
│   │   ├── database/         # engine, session, Base
│   │   ├── models/           # SQLAlchemy models (ER diagram)
│   │   ├── schemas/          # Pydantic request/response models
│   │   ├── routers/          # API endpoints
│   │   ├── services/         # business logic
│   │   └── main.py           # application entry point
│   ├── .env                  # secrets (not committed)
│   ├── .env.example          # template
│   └── requirements.txt
├── frontend/
└── venv/
```

## Prerequisites

- Python 3.11+
- PostgreSQL 16+
- Node.js 18+ (frontend)

## Setup

### 1. Clone and create the virtual environment

```bash
git clone <repository-url>
cd airline-ops-platform

python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS / Linux
```

### 2. Install dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3. Create the database

```bash
psql -U postgres -c "CREATE DATABASE airline_ops;"
```

### 4. Configure environment variables

Copy the template and fill in your values:

```bash
copy .env.example .env         # Windows
cp .env.example .env           # macOS / Linux
```

Edit `backend/.env`:

```
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/airline_ops
SECRET_KEY=your_generated_secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
PROJECT_NAME=Airline Operations Platform
API_V1_PREFIX=/api/v1
```

Generate a secret key:

```bash
python -c "import secrets; print(secrets.token_urlsafe(64))"
```

**Note:** if your PostgreSQL password contains special characters, percent-encode them in the URL — `@` becomes `%40`, `#` becomes `%23`, `/` becomes `%2F`.

### 5. Run migrations

```bash
alembic upgrade head
```

Creates all tables. Verify with `psql -U postgres -d airline_ops -c "\dt"`.

### 6. Start the server

```bash
uvicorn app.main:app --reload
```

| URL | Description |
|---|---|
| http://localhost:8000/docs | Swagger UI |
| http://localhost:8000/api/health/db | Database health check |

## API Endpoints

### Health

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Service status |
| GET | `/api/health/db` | Database connectivity |

### Authentication

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/api/v1/auth/register` | Public | Create an account |
| POST | `/api/v1/auth/login` | Public | Get a JWT access token |
| GET | `/api/v1/auth/me` | Bearer | Current user details |
| GET | `/api/v1/auth/admin-only` | Admin | Role check test endpoint |

## Authentication Flow

1. `POST /api/v1/auth/register` with email, password, and full name. Passwords are hashed with bcrypt (12 rounds) — plain text is never stored.
2. `POST /api/v1/auth/login` returns a JWT access token valid for 30 minutes.
3. Send the token on protected requests: `Authorization: Bearer <token>`
4. The token payload carries the user id and role. On each request the server verifies the signature and expiry, then confirms the user still exists and is active.

**Roles:** `user` (default) and `admin`. Requests without a valid token receive **401**; authenticated users lacking the required role receive **403**.

### Testing in Swagger

Call `/api/v1/auth/login`, copy the `access_token`, click **Authorize** at the top right, paste the token, then call protected endpoints.

## Database Schema

Eight tables mapped from the ER diagram:

| Table | Purpose |
|---|---|
| `users` | application accounts with login and roles |
| `airports` | network airports (IATA codes) |
| `aircraft` | fleet with registration and capacity |
| `crew` | pilots and cabin crew |
| `passengers` | travellers (no login) |
| `flights` | scheduled and actual flight times, status, route |
| `crew_assignments` | flights ↔ crew (many-to-many) |
| `bookings` | flights ↔ passengers, with seat and fare |

Referential integrity, status values, and business rules — arrival after departure, origin ≠ destination, one seat per flight — are enforced by database constraints in addition to API-level validation.

## Migrations

```bash
alembic revision --autogenerate -m "description"   # after changing models
alembic upgrade head                               # apply
alembic downgrade -1                               # roll back one
alembic current                                    # show current revision
```

## Security Notes

- `.env` is gitignored and must never be committed.
- Passwords are hashed with bcrypt and a per-user salt.
- JWT payloads are signed, not encrypted — no sensitive data is stored in them.
- Roles are assigned server-side; clients cannot set their own role.
