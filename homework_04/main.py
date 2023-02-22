"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from jsonplaceholder_requests import fetch_all_data
from models import Base, User, Post
from models import async_engine, Session


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_users(session: AsyncSession, users_data: list[dict]) -> list[User]:
    users = [
        User(
            id=user['id'],  # type: ignore
            name=user['name'],  # type: ignore
            username=user['username'],  # type: ignore
            email=user['email']  # type: ignore
        ) for user in users_data]
    session.add_all(users)
    await session.commit()
    return users


async def create_posts(session: AsyncSession, posts_data: list[dict]) -> list[Post]:
    posts = [
        Post(
            user_id=post['userId'],  # type: ignore
            title=post['title'],  # type: ignore
            body=post['body'],  # type: ignore
        ) for post in posts_data]
    session.add_all(posts)
    await session.commit()
    return posts


async def async_main():
    async with Session() as session:
        await create_tables()
        users_data, posts_data = await fetch_all_data()
        await create_users(session, users_data)
        await create_posts(session, posts_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
