from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from sqlalchemy.orm import DeclarativeBase


engine = create_engine("postgresql://cyberamirka:amir@localhost/Calorix", echo=True)
session = sessionmaker(autoflush=True, bind=engine)


# базоый класс по отношению ко всем классам, необходим для взаимодействия с таблицами
class Base(DeclarativeBase): pass


def db_init():
    Base.metadata.create_all(bind=engine)


