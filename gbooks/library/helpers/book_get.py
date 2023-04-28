import json


def get_library_book(request):
    b_library_key = "lib-" + request.GET.get('id')
    book_serialized = request.session.get(b_library_key)
    book = json.loads(book_serialized)

    return book
