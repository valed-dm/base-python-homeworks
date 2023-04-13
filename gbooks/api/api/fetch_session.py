import json

from django.core.serializers.json import DjangoJSONEncoder

from api.helpers import prepare_list
from api.helpers.get_args import get_args_book
from api.helpers.info_search import info_search
from api.schemas import API
# from .fetch_prepare import data_prepare
from .fetch_result import fetch_result


def fetch_to_session(request):
    books_cards = []
    r = get_args_book(request)
    books_found, books = fetch_result(r)

    for book in books:
        b = book
        # serializes book object
        b_dict = b.__dict__
        b_serialized = json.dumps(b_dict, cls=DjangoJSONEncoder)
        b_key = book.google_book_id
        # store serialized book object into django session
        request.session[b_key] = b_serialized
        # provides authors,categories string truncated for books.html cards
        b.authors = prepare_list(b.authors)
        b.categories = prepare_list(b.categories)
        books_cards.append(b)

    info_search(request, r, books_found, len(books))
    # triggers no search performed info to be shown for initial page appearance
    display_start_info = r.title is None

    api = API()
    api.books = books
    api.books_found = books_found
    api.display_start_info = display_start_info

    return api
