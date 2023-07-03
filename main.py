from fastapi import FastAPI
import uvicorn
from app.router import user, auth
from fastapi.security import OAuth2PasswordBearer


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


app.include_router(user.router)
app.include_router(auth.router)

if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True)
