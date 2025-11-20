from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db.Constants import StatusOperation
from api.Types.user import User
from db.modules.users import get_user, add_user, update_user_password

# from Types.user import User

router = APIRouter()

@router.get("/LogIn/{email}/{password}")
async def logIn(email: str, password: str):
    """
        Функция для ответа на запрос входа пользователя

        Входные данные:

            - email: почта
            - password: пароль

        Выходные данные:

            - status_code=200: пользователь есть в базе
            - status_code=404: пользователя нет в базе
    """
    checkUser = await get_user(email)
    if checkUser == None or checkUser.psswd != password:
        return JSONResponse(content={}, status_code=404)
    return JSONResponse(content={}, status_code=200)

@router.post("/RegisterUser/")
async def registerUser(user: User):
    """
        Функция для ответа на запрос регистрации пользователя

        Входные данные:

            - user - Объект класса User

        Выходные данные:

            - status_code=200: пользователя нет в базе и мы его записали
            - "message": "User already exists", status_code=400: пользователь в базе есть и записать его нельзя
    """

    result = await add_user(user.email, user.password)
    if result == StatusOperation.FAILURE:
        return JSONResponse(content={"message": "User already exists"}, status_code=400)
    return JSONResponse(content={}, status_code=200)

@router.put("/UpdatePassword/")
async def updatePassword(user: User):
    """
        Функция для ответа на запрос изменения пароля пользователя

        Входные данные:

            - user - Объект класса User

        Выходные данные:

            - status_code=200: пароль успешно изменён
            - "message": "User doesn't exist", status_code=400: пользователя нет в базе
    """
    result = await update_user_password(user.email, user.password)
    if result == StatusOperation.FAILURE:
        return JSONResponse(content={"message": "User doesn't exist"}, status_code=400)
    return JSONResponse(content={}, status_code=200)