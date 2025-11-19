# libs
from sqlalchemy import select


# project module
from db.Database import async_session
from db.models.Users import Users
from db.Constants import StatusOperation





async def get_user(email: str) -> Users:
    """
        Функция для получения пользователя
        
        Входные данные:
        
            - email: почта
        
        Выходные данные:
            
            - Users: возвращает модель Users при поиске совпадений в базе
            - None: возвращает None когда совпадений в базе данных нет
    """

    # исхрожу из того что аккаунт у нас уникальный
    async with async_session() as db:
        stml = select(Users).where(Users.email == email)
        result = await db.execute(stml)
        user = result.scalar_one_or_none()

    return user




async def add_user(email: str, password: str) -> bool:
    """
        Функция для записи пользователя в базе данных
        
        Входные данные:
        
            - email: почта
            - password: пароль
        
        Выходные данные:
            
            - True: пользователя нет в базе и мы его записали
            - False: пользователь в базе есть и записать его нельзя
    """

    async with async_session() as db:
        stml = select(Users).where(Users.email == email)
        result = await db.execute(stml)
        user = result.scalar_one_or_none()

        if user is not None:
            return StatusOperation.FAILURE

        else:
            user = Users(email=email, psswd=password)
            db.add(user)
            await db.commit()
            await db.refresh(user)
            return StatusOperation.SUCCESS



async def update_user_password(email: str, password: str) -> bool:
    """
        Функция для изменения пароля пользователя
        
        Входные данные:
        
            - email: почта
            - password: пароль
        
        Выходные данные:
            
            - True: пользователь успешно сменил пароль
            - False: пользователя в базе нет
    """
    
    async with async_session() as db:
        stml = select(Users).where(Users.email == email)
        result = await db.execute(stml)
        user: Users = result.scalar_one_or_none()


        if user is not None:
            return StatusOperation.FAILURE
        

        user.psswd = password
        await db.commit()
        
        return StatusOperation.SUCCESS
