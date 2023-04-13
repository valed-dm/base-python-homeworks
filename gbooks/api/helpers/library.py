import json

from library.crud import add_book


def add_into_library(request):
    data = request.POST
    b_key = data["add_book"]
    b_rubric = data["rubric"]
    b_remarks = data["remarks"]
    b_serialized = request.session.get(f'{b_key}', None)
    book = json.loads(b_serialized)
    book["rubric"] = b_rubric
    book['remarks'] = b_remarks

    add_book(request, book)

    return book
