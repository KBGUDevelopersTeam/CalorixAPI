from db.Database import Base
from sqlalchemy import Column, Integer, String, Float


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True)

    name = Column(String)
    calories = Column(Float)
    proteins = Column(Float)
    fats = Column(Float)
    carbohydrates = Column(Float)
