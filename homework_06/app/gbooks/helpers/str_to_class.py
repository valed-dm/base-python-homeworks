from ..schemas import Book


def str_to_class(s: str) -> Book:
    if isinstance(s, str):
        book = eval(s)

        return book
