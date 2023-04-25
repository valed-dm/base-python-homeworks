import json
import logging

import requests

logging.basicConfig(
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
)

log = logging.getLogger(__name__)


def fetch_data(url: str) -> dict:
    res = requests.get(url)
    response = json.loads(res.text)
    return response


def fetch_books(url) -> list:
    books = fetch_data(url)
    result = [books['totalItems'], books['items']]
    log.info("%s found upon request, %s books data loaded", result[0], len(result[1]))
    return result
