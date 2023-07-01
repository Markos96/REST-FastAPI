from fastapi import FastAPI
import uvicorn
from app.db.database import Base, engine
from app.router import user


def create_table():
    Base.metadata.create_all(bind=engine)


create_table()


app = FastAPI()

app.include_router(user.router)


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True)
