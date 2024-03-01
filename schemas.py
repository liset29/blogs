from pydantic import BaseModel


class Blog(BaseModel):
    external_id:int
    user_login:str
    name_blog:str
    description:str


#
# class User(BaseModel):
#     username: str
#     password: str
