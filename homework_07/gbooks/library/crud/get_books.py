from library.models import Book


def get_books():
    books_data = Book.objects. \
        select_related("image_src"). \
        prefetch_related("authors", "categories"). \
        all()

    return books_data
