from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db.models.Users import Users
from db.Database import session
from api.Types.user import User
# from Types.user import User

router = APIRouter()

@router.get("/LogIn/{email}/{password}")
def logIn(email: str, password: str):
    with session() as db:
        checkUser = db.query(Users).filter(Users.email==email).first()
        if checkUser == None or checkUser.psswd != password:
            return JSONResponse(content={}, status_code=404)
        return JSONResponse(content={}, status_code=200)

@router.post("/RegisterUser/")
def registerUser(user: User):
    with session() as db:
        #Проверка, если в базе данных уже есть пользователь с полученной почтой
        #Если пользователь с такой почтой уже есть, отправляем статусный код 400
        if db.query(Users).filter(Users.email==user.email).first() != None:
            return JSONResponse(content={"message": "User already exists"}, status_code=400)
        #Иначе добавляем нового пользователя в таблицу Users
        new_user = Users(email=user.email, psswd=user.psswd)
        db.add(new_user)
        db.commit()
        return JSONResponse(content={}, status_code=200)