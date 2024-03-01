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
    def select_inf_user():
        with session() as sess:
            query = select(Users)
            result = sess.execute(query)
            res = result.scalars().all()
            lst = [{'user_id': i.user_id, 'email': i.email, 'login': i.login, 'password': i.password} for i in res]
            return lst

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
    def insert_blog(blog):
        print(blog.external_id, blog.user_login, blog.name_blog, blog.description)
        with session() as sess:
            try:

                blog = Blogs(external_id=blog.external_id, user_login=blog.user_login, name_blog=blog.name_blog,
                             description=blog.description)
                sess.add(blog)
                sess.commit()
                return 'блог успешно добавлен'
            except Exception:
                return 'пока хз ошибка'

    @staticmethod
    def select_blog(external_id):
        with session() as sess:
            query = select(Blogs).where(Blogs.external_id == external_id)
            result = sess.execute(query)
            res = result.scalars().all()
            res = [{'id': i.id, 'external_id': i.external_id, 'user_login': i.user_login, 'name_blog': i.name_blog,
                    'description': i.description} for i in res]
            if len(res) == 0:
                return 'нет активных blogs'
            return res

    @staticmethod
    def delete_blog(id_blog):
        with session() as sess:
            query_blog = select(Blogs).where(Blogs.id == id_blog)
            result = sess.execute(query_blog)
            result = result.fetchall()
            if len(result) == 0:
                return 'блог не найден'

            query = delete(Blogs).where(Blogs.id == id_blog)
            sess.execute(query)
            sess.commit()
            return 'блог успешно удалён'


