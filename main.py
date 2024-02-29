from fastapi import FastAPI, Depends
from auth import register, authenticate_user
from database.repository import Control
from schemas import Blog, User

app = FastAPI(title="блог фор тимур", )


@app.post('/registration')
def registration(email: str, login: str, password: str):
    result = register(email, login, password)
    return {'message': result}


@app.post('/write_blog/')
def write_blog(blog: Blog, user: User = Depends(authenticate_user)):
    if user is None:
        return user
    login = user.login
    result = Control.insert_blog(blog, login)
    return result


@app.get("/user_info/")
def get_user_info(user: User = Depends(authenticate_user)):
    return {"message": "всё хорошо!", "user_info": user}


@app.get("/blogs/")
def get_all_blogs(user: User = Depends(authenticate_user)):
    result = Control.select_blog(user.login)
    return {'blogs': result}


@app.delete('/delete_blog')
def delete_blog(name_blog: str, user: User = Depends(authenticate_user)):
    result = Control.delete_blog(user.login,name_blog)
    return {'message': result}
