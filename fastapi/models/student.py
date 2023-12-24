from database import Base
from sqlalchemy import Column, Integer, String, Date


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    subject = Column(String, unique=True, nullable=False)
    un_id = Column(Integer, nullable=False)
    verify_date = Column(Date)
