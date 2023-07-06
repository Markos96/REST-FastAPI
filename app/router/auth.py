from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schema import Login
from app.repository import auth

router = APIRouter(
    prefix="/login",
    tags=["Login"]
)


# 1 Main method security API
@router.post('/', status_code=status.HTTP_200_OK)
def login(usuario: Login, db: Session = Depends(get_db)):
    return auth.auth_user(usuario, db)
