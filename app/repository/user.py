from app.db.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from app.schema import User, UserUpdate
from app.db import models


def add_user(user: User, db: Session = Depends(get_db)):
    usuario = user.dict()
    newUser = models.User(
        username=usuario["username"],
        password=usuario["password"],
        name=usuario["name"],
        age=usuario["age"],
        address=usuario["address"]
    )
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser


def get_by_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user


def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


def update_user(updateUser: UserUpdate, user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id)

    if not user.first():
        raise HTTPException(status_code=404, detail="User not found")
    user.update(updateUser.dict(exclude_unset=True))
    db.commit()
    return {"Salio todo bien"}


def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(user)
    db.commit()
    return {"user deleted"}