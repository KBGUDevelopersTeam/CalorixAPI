from db.Database import Base
from sqlalchemy import Column, Integer, String


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True)

    email = Column(String(100))
    psswd = Column(String(50))