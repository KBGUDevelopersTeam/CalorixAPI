from Database import Base
from sqlalchemy import Column, Integer, String, Float


class Activity(Base):
    __tablename__ = "activity"

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True)

    name = Column(String)
    ratio = Column(Float)
