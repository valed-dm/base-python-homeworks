"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import os
from datetime import datetime

from dotenv import load_dotenv
from sqlalchemy import Column, String, Text, Integer
from sqlalchemy import DateTime, func
from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import relationship

load_dotenv()

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI")
DB_ECHO = os.environ.get("DB_ECHO")

async_engine: AsyncEngine = create_async_engine(url=PG_CONN_URI, echo=DB_ECHO)
Session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


class Base:
    @classmethod
    @declared_attr
    def __tablename__(cls):
        return f"blog_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


Base = declarative_base(cls=Base)


class TimestampMixin:
    created_at = Column(DateTime, default=datetime.utcnow, server_default=func.now())


class User(TimestampMixin, Base):
    name = Column(String(30), unique=True, nullable=False)
    username = Column(String(10), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)

    posts = relationship("Post", back_populates="user")

    def __str__(self) -> str:
        return (
            f"User(id={self.id}, name={self.name!r})"
            f"User(username={self.username!r}, email={self.email!r})"
        )


class Post(TimestampMixin, Base):
    title = Column(String(100), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    user_id = Column(
        Integer, ForeignKey("blog_users.id"), nullable=False, unique=False
    )

    user = relationship("User", back_populates="posts")

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(title={self.title!r}, user_id={self.user_id})"
        )
