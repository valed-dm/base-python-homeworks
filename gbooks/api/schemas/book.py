import datetime
from dataclasses import dataclass


@dataclass
class Book:
    authors: [str] = "-no author-",
    categories: [str] = "-no category-",
    date: datetime.date = "1900-01-01"
    description: str = "no description"
    google_book_id: str = ""
    image_src: str = "/static/img/no_cover.webp"
    title: str = "no title"
    rubric: str = "read_asap"
    remark: str = ""
