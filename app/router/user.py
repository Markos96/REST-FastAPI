from fastapi import APIRouter, Depends, status
from app.schema import UserDetails, UserUpdate
from typing import List
from sqlalchemy.orm import Session
from app.repository import user
from app.schema import User
from app.db.database import get_db
from app.token import validate_token

router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(users: User, db: Session = Depends(get_db), token: str = Depends(validate_token)):
    return user.add_user(users, db)


@router.get("/get", response_model=UserDetails, status_code=status.HTTP_200_OK)
def get_by_user_id(user_id: int, db: Session = Depends(get_db), token: str = Depends(validate_token)):
    return user.get_by_user(user_id, db)


@router.get("/getAll", response_model=List[UserDetails], status_code=status.HTTP_200_OK)
def get_all_users(db: Session = Depends(get_db), token: str = Depends(validate_token)):
    return user.get_users(db)


@router.patch("/", status_code=status.HTTP_200_OK)
def update_user(userUpdate: UserUpdate, user_id: int, db: Session = Depends(get_db), token: str = Depends(validate_token)):
    return user.update_user(userUpdate, user_id, db)


@router.delete("/", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Session = Depends(get_db), token: str = Depends(validate_token)):
    return user.delete_user(user_id, db)
