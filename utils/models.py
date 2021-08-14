from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence

from utils.definitions import Schema

Base = declarative_base()


class Users(Base):
    __tablename__ = Schema.Users

    id = Column(String(50), primary_key=True)
    name = Column(String(100), nullable=False)
    password = Column(String(500), nullable=False, unique=True)
    email_id = Column(String(50), nullable=False, unique=True)
    updated_at = Column(Date)
    updated_by = Column(String(100))
    deleted_at = Column(Date)
    deleted_by = Column(String(100))
