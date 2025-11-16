from Database import Base
from sqlalchemy import Column, Integer, String


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True)

    email = Column(String)
    psswd = Column(String)