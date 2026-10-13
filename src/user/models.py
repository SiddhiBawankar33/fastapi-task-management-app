from sqlalchemy import Column, Integer, String, DateTime, Boolean
from src.utils.db import Base

class UserModel(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    name = Column(String)
    email = Column(String, unique=True, nullable=False)
    hash_password = Column(String, nullable=False)

