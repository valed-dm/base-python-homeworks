import json


def get_book(request):
    b_key = request.GET.get('id')
    b_serialized = request.session.get(f'{b_key}', None)
    book = json.loads(b_serialized)

    return book
