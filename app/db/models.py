from app.db.database import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String, unique=True)
    password = Column(String)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String(100), nullable=False)
    created = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    active = Column(Boolean, default=False)
    venta = relationship("Venta", backref="usuario", cascade="delete,merge")


class Venta(Base):
    __tablename__ = 'venta'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    venta = Column(Integer)
    venta_product = Column(Integer)

