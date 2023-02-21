"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio

import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data


async def get_users() -> list[dict]:
    users = await fetch_json(USERS_DATA_URL)
    return users


async def get_posts() -> list[dict]:
    posts = await fetch_json(POSTS_DATA_URL)
    return posts


async def main():
    results = await asyncio.gather(get_users(), get_posts())
    users_list, posts_list = results

    print(f"{'UID:' : <6}{'user:' : <30}{'username:' : <20}{'email:' : <50}")
    for user in users_list:
        print(f"{'%4d' % user['id'] : <6}{user['name'] : <30}{user['username'] : <20}{user['email'].lower() : <50}")
    print()

    print(f"{'PID:' : <6}{'title:' : <10}")
    for post in posts_list:
        print(f"{'%4d' % post['id'] : <6}{post['title'] : <100}")


if __name__ == '__main__':
    asyncio.run(main())
