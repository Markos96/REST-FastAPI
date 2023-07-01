from fastapi import APIRouter, Depends
from app.schema import UserDetails
from typing import List
from sqlalchemy.orm import Session
from app.repository import user
from app.schema import User
from app.db.database import get_db

router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.post("/")
def create_user(users: User, db: Session = Depends(get_db)):
    return user.add_user(users, db)

#@router.get("/get", response_model=UserDetails)



#@router.get("/getAll", response_model=List[UserDetails])



#@router.patch("/")



#@router.delete("/")

