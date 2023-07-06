from app.db import models
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.hashing import Hash
from app.token import generate_access_token


# 2 Authenticated credentials
def auth_user(user, db: Session):
    usuario = user.dict()
    user = db.query(models.User).filter(models.User.username == usuario["username"]).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect username")

    if not Hash.verify_password(usuario["password"], user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")

    token = generate_access_token(usuario["username"])

    return {"token": token}


