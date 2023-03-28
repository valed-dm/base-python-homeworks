import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")


def fetch_uri_create(title: str = "", res_qty: str = "10", start_point: str = "0"):
    api_uri = "https://www.googleapis.com/books/v1/volumes?q=" \
              + title \
              + "&key=" \
              + api_key \
              + "&maxResults=" \
              + res_qty + \
              "&startIndex=" \
              + start_point

    return api_uri
