from fastapi import APIRouter, Depends
from schemas.user_schemas import UserCreate, UserLogin
from controllers.user_controller import UserController
from config.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth")


@router.post("/register", tags=["register users"])
async def register(user_create: UserCreate, db: Session = Depends(get_db)):
    res = UserController(db).create_user(user_create)
    return res

@router.post("/login", tags=["login users"])
async def login(user_login: UserLogin, db: Session = Depends(get_db)):
    res = UserController(db).login_user(user_login)
    return res
