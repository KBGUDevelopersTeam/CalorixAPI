from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


# Асинхронный движок с asyncpg драйвером
engine = create_async_engine(
    "postgresql+asyncpg://calorix_user:developers_team_password@localhost/Calorix", 
    echo=True
)

# Асинхронная сессия
SessionLocal = async_sessionmaker(
    engine, 
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=True
)


# Базовый класс для всех моделей
class Base(DeclarativeBase):
    pass



async def get_db():
    async with SessionLocal() as db:
        try:
            yield db
            await db.commit()
        except Exception as e:
            await db.rollback()
            raise



# Асинхронная инициализация базы данных
async def db_init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
