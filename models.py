from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Prediction(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    query = Column(String, nullable=False)
    response = Column(String, nullable=False)
    query_time = Column(DateTime, nullable=False)
    response_time = Column(DateTime, nullable=False)
