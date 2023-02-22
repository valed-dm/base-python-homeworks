"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
import os

import aiohttp
from dotenv import load_dotenv

load_dotenv()

USERS_DATA_URL = os.environ.get("USERS_URL")
POSTS_DATA_URL = os.environ.get("POSTS_URL")


async def fetch_json(url: str) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data


async def fetch_users_data() -> list[dict]:
    users = await fetch_json(USERS_DATA_URL)
    return users


async def fetch_posts_data() -> list[dict]:
    posts = await fetch_json(POSTS_DATA_URL)
    return posts


async def fetch_all_data():
    results = await asyncio.gather(fetch_users_data(), fetch_posts_data())
    users_list, posts_list = results

    print(f"{'UID:' : <6}{'user:' : <30}{'username:' : <20}{'email:' : <50}")
    for user in users_list:
        print(f"{'%4d' % user['id'] : <6}{user['name'] : <30}{user['username'] : <20}{user['email'].lower() : <50}")
    print()

    print(f"{'PID:' : <6}{'title:' : <10}")
    for post in posts_list:
        print(f"{'%4d' % post['id'] : <6}{post['title'] : <100}")

    return results


if __name__ == '__main__':
    asyncio.run(fetch_all_data())
