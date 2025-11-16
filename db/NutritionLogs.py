from Database import Base
from sqlalchemy import Column, Integer, Date, Time, ForeignKey


class NutritionLogs(Base):
    __tablename__ = "nutrition_logs"

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True)

    date = Column(Date)
    time = Column(Time)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
