import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "PROYECTO FAST-API"
    PROJECT_VERSION: str = "1.0"

    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = os.getenv('ALGORITHM')

    POSTGRES_USER: str = os.getenv('DB_USER')
    POSTGRES_PASSWORD: str = os.getenv('DB_PASSWORD')
    POSTGRES_HOST: str = os.getenv('DB_HOST')
    POSTGRES_PORT: str = os.getenv('DB_PORT')
    POSTGRES_DB: str = os.getenv('DB_NAME')
    POSTGRES_URL: str = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'


settings = Settings()
