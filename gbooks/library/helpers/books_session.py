import json

from django.core.serializers.json import DjangoJSONEncoder

from library.crud.get_books import get_books
from library.helpers.book_prepare import book_prepare
from library.helpers.class_serialize import class_serialize
from library.schemas import Library


def books_to_session(request):
    all_authors = []
    all_categories = []
    books_cards = []
    lib = Library(books_cards=books_cards)

    books_data = get_books()

    for book in books_data:
        book_data = book_prepare(book)
        # to fill data into dropdowns authors, categories in library_view
        # collects all authors, categories stored in db into a single sorted list
        all_authors = sorted(list({*all_authors, *book_data.authors}))
        all_categories = sorted(list({*all_categories, *book_data.categories}))

        # django session keys preparation:
        a_key = "auth"
        b_key = "lib-" + book.google_book_id
        c_key = "cat-"
        # serializes all_authors, all_categories, book_data for django session storage
        a_serialized = json.dumps(all_authors, cls=DjangoJSONEncoder)
        b_serialized = class_serialize(book_data)
        c_serialized = json.dumps(all_categories, cls=DjangoJSONEncoder)
        # store serialized book object inside django session
        request.session[a_key] = a_serialized
        request.session[b_key] = b_serialized
        request.session[c_key] = c_serialized

        books_cards.append(book_data)

    # data prepared to be returned for further usage
    lib.all_authors = all_authors
    lib.all_categories = all_categories
    lib.books_cards = books_cards

    return lib
