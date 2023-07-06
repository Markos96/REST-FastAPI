from app.db.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from app.schema import User, UserUpdate
from app.db import models
from app.hashing import Hash


def add_user(user: User, db: Session = Depends(get_db)):
    try:
        usuario = user.dict()
        newUser = models.User(
            username=usuario["username"],
            password=Hash.hash_password(usuario['password']),
            name=usuario["name"],
            age=usuario["age"],
            address=usuario["address"]
        )
        db.add(newUser)
        db.commit()
        db.refresh(newUser)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    return newUser


def get_by_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return user


def get_users(db: Session = Depends(get_db)):
    try:
        users = db.query(models.User).all()

        if not users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Users not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))

    return users


def update_user(updateUser: UserUpdate, user_id: int, db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.id == user_id)

        if not user.first():
            raise HTTPException(status_code=404, detail="User not found")

        user.update(updateUser.dict(exclude_unset=True))
        db.commit()

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Error occurred" + str(e))

    return user


def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    db.delete(user)
    db.commit()

    return {'User deleted': user}
