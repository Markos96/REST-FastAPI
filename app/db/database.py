from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings

SQLALCHEMY_DATABASE_URL = settings.POSTGRES_URL

# Crea la conexion a la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creamos la instancia de la sesion para interactuar con la base de datos
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Creamos la estructura y los modelos de la base de datos
Base = declarative_base()


# Devuelve la sesion de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
