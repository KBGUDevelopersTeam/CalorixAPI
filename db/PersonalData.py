from Database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey



class PersonalData(Base):
    __tablename__ = "personal_data"

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True)

    height = Column(Float)
    weight = Column(Float)
    gender = Column(String)
    target = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))
    activity_id = Column(Integer, ForeignKey("activity.id"))
