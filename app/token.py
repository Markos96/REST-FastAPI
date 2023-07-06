import jwt
from core.config import settings
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, status, HTTPException


# 3 Create access token
def generate_access_token(username: str):
    payload = {"username": username}

    token = jwt.encode(payload, settings.SECRET_KEY, settings.ALGORITHM)

    return token


# 4 Validate token provided
def validate_token(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    return token
