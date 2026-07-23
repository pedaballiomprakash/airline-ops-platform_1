from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.deps import get_current_user, require_admin
from app.database.db import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserOut
from app.schemas.token import TokenOut
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserOut,
             status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    """Create a new account. Role is always 'user'."""
    return auth_service.register_user(db, payload)


@router.post("/login", response_model=TokenOut)
def login(payload: UserLogin, db: Session = Depends(get_db)):
    """Exchange credentials for a JWT access token."""
    return auth_service.login_user(db, payload)


@router.get("/me", response_model=UserOut)
def me(current_user: User = Depends(get_current_user)):
    """Return the authenticated user. Requires a valid token."""
    return current_user


@router.get("/admin-only", response_model=UserOut)
def admin_only(current_user: User = Depends(require_admin)):
    """Test endpoint. Requires role = admin."""
    return current_user