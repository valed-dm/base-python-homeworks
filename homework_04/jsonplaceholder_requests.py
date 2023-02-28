"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import logging
import os

import aiohttp
import asyncio
from dotenv import load_dotenv

load_dotenv()

USERS_DATA_URL = os.environ.get("USERS_URL") if os.environ.get(
    "USERS_URL") else "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = os.environ.get("POSTS_URL") if os.environ.get(
    "POSTS_URL") else "https://jsonplaceholder.typicode.com/posts"

logging.basicConfig(
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
)

log = logging.getLogger(__name__)


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

    log.info("%s users data loaded", len(users_list))
    log.info("%s user's posts loaded", len(posts_list))

    return results


if __name__ == '__main__':
    asyncio.run(fetch_all_data())
