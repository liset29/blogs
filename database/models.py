from sqlalchemy.orm import declarative_base, Mapped, mapped_column

from sqlalchemy import ForeignKey

Base = declarative_base()


class Blogs(Base):
    __tablename__ = 'blogs'

    id: Mapped[int] = mapped_column(primary_key=True)

    user_login: Mapped[str] = mapped_column(ForeignKey('users.login'))
    name_blog: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)


class Users(Base):
    __tablename__ = 'users'

    email: Mapped[str] = mapped_column(nullable=False)
    login: Mapped[str] = mapped_column(primary_key=True)
    password: Mapped[str] = mapped_column(nullable=False)
