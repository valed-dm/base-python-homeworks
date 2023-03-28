def sort_rubric(rubric, books):
    res = books
    if rubric != "all":
        res = [book for book in books if book.rubric == rubric]
    return res


def sort_category(category, books):
    res = books
    if category != "all":
        res = [book for book in books if category in [cat.name.lower() for cat in book.categories]]
    return res


def sort_author(author, books):
    res = books
    if author != "all":
        res = [book for book in books if author in [auth.name for auth in book.authors]]
    return res


def sort_date(sort, books):
    res = books
    if sort == "newest":
        res.sort(key=lambda book: book.date, reverse=True)
    return res


def sort_books(rubric, category, author, sort, library_books):
    # for book in library_books:
    #     print(book.__dict__)
    result = sort_rubric(
        rubric,
        sort_category(
            category,
            sort_author(
                author,
                sort_date(
                    sort,
                    library_books
                )
            )
        )
    )

    return result
