from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from sqlalchemy.orm import DeclarativeBase




engine = create_engine("postgresql://cyberamirka:amir@localhost/Calorix", echo=True)
session = None


# базоый класс по отношению ко всем классам, необходим для взаимодействия с таблицами
class Base(DeclarativeBase): pass





def dbinit():
    Base.metadata.create_all(bind=engine)


