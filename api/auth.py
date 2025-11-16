from fastapi import APIRouter
# from Types.user import User

router = APIRouter()

@router.get("/login")
def login():
    return "200"

