from schemas.user_schemas import UserCreate, UserLogin
from models.models import User
from utils.auth_utils import get_hashed_password, verify_password, create_access_token


class UserController:
    def __init__(self, db):
        self.db = db

    def create_user(self, user_create: UserCreate):
        user = User(
            username=user_create.username,
            email=user_create.email,
            hashed_password=get_hashed_password(user_create.password)
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return {
            "username": user.username,
            "email": user.email,
            "message": "user has been created successfully !!!",
            "status_code": "200"
        }

    def login_user(self, user_credential: UserLogin):

        user = User(
            username=user_credential.username,
            hashed_password=get_hashed_password(user_credential.password)
        )

        if not verify_password(user_credential.password, user.hashed_password):

            return {
                "message": "Incorrect email or password",
                "status": 400
            }

        return {
            "username": user.username,
            "access_token": create_access_token(user.username),
            "message": "user logged in!!!",
            "status": "200"
        }
