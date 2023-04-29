from datetime import datetime

from ..schemas import Book


def check_category(item: Book, cat: str) -> bool:
    result = False
    categories = [category.lower() for category in item.categories]
    if cat in categories:
        result = True
    return result


def sorted_by_date(books: [Book]):
    return sorted(
        books,
        key=lambda book: datetime.strptime(book.date, '%Y-%m-%d'),
        reverse=True
    )


def sort_by_cat(books: [Book], cat: str = ""):
    result = books
    if cat != "all":
        result = [book for book in books if check_category(book, cat)]
    return result


def sort_by_newest(books: [Book], sort: str = ""):
    result = books
    if sort == "newest":
        result = sorted_by_date(result)
    return result


def sorting_results(books: [Book], cat: str = "", sort: str = ""):
    result = sort_by_cat(books, cat)
    result = sort_by_newest(result, sort)
    return result
