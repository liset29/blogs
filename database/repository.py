from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select, delete
import config as con

from database.models import Base, Users, Blogs

engine = create_engine(f'postgresql+psycopg2://{con.USER}:{con.PASSWORD}@{con.HOST}:5432/{con.DATABASE}')

session = sessionmaker(engine)


def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


class Control:

    @staticmethod
    def select_inf_user(login):
        with session() as sess:
            query = select(Users).where(Users.login == login)
            result = sess.execute(query)
            res = result.scalar()
            return res

    @staticmethod
    def insert_users(email, login, password):
        with session() as sess:
            try:
                user = Users(email=email, login=login, password=password)
                sess.add(user)
                sess.commit()
                return 'УСПЕШНО ЗАРЕГИСТРИРОВАНЫ'
            except Exception:
                return 'пользователь с таким именем уже существует'

    @staticmethod
    def insert_blog(blog, login):
        with session() as sess:
            try:
                blog = Blogs(user_login=login, name_blog=blog.name_blog, description=blog.description)
                sess.add(blog)
                sess.commit()
                return 'блог успешно добавлен'
            except Exception:
                return 'пока хз ошибка'

    @staticmethod
    def select_blog(login):
        with session() as sess:
            query = select(Blogs.name_blog, Blogs.description).where(Blogs.user_login == login)
            result = sess.execute(query)
            res = result.fetchall()
            res = [{'название блога-' + i[0]: 'описание-' + i[1]} for i in res]
            if len(res) == 0:
                return 'нет активных blogs'
            return res

    @staticmethod
    def delete_blog(login, name_blog):
        with session() as sess:
            print(login,name_blog)
            query_blog = select(Blogs).where(Blogs.name_blog == name_blog)
            result = sess.execute(query_blog)
            result = result.fetchall()
            if len(result) == 0:
                return 'блог не найден'

            query = delete(Blogs).where(Blogs.name_blog == name_blog).where(Blogs.user_login == login)
            sess.execute(query)
            sess.commit()
            return 'блог успешно удалён'


