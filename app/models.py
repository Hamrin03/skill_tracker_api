
from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    proficiency = Column(String, nullable=False)
    hours_spent = Column(Integer, default=0)
    target_hours = Column(Integer, default=10)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    