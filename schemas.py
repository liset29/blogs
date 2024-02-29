from pydantic import BaseModel


class Blog(BaseModel):
    name_blog: str
    description: str


class User(BaseModel):
    username: str
    password: str
