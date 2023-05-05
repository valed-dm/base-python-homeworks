import json

from api.schemas import Book


def get_book(request):
    book = Book()
    book.title = "Sample single book view (no book data available)"
    book.description = "This sample can't be added to library"

    try:
        b_key = request.GET.get('id')
        b_serialized = request.session.get(f'{b_key}', None)
        book = json.loads(b_serialized)
    except TypeError:
        pass

    return book
