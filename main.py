from fastapi import FastAPI, Depends, Query
from auth import register, authenticate_user
from database.repository import Control
from schemas import Blog

app = FastAPI(title="блог фор тимур", )


@app.post('/registration')
def registration(email: str, login: str, password: str):
    result = register(email, login, password)
    return {'message': result}


@app.post('/write_blog/')
def write_blog(blog: Blog):
    result = Control.insert_blog(blog)
    return result


@app.get("/users_info/")
def get_user_info():
    result = Control.select_inf_user()
    return {'data': result}


@app.get("/blogs/")
def get_all_blogs(external_id: int ):
    result = Control.select_blog(external_id)
    return {'blogs': result}


@app.delete('/delete_blog/')
def delete_blog(id_blog: int):
    result = Control.delete_blog(id_blog)
    return {'message': result}
