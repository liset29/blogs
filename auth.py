from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from starlette import status

from database.repository import Control

security = HTTPBasic()


def register(email, login, password):
    result = Control.insert_users(email, login, password)
    return result


def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = get_user_from_db(credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="не выполнен вход в активную страницу")
    return user


def get_user_from_db(username: str):
    name = Control.select_inf_user(username)
    try:
        if name.login == username:
            return name
    except Exception:
        return None
