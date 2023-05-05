import json

from django.core.serializers.json import DjangoJSONEncoder

from library.crud.get_books import get_books
from library.helpers.book_prepare import book_prepare
from library.schemas import Library


def library_to_view(request):
    all_authors = []
    all_categories = []
    books_cards = []
    lib = Library(books_cards=books_cards)

    books_data = get_books()

    for book in books_data:
        book_data = book_prepare(book)
        books_cards.append(book_data)
        # to fill data into dropdowns authors, categories in library_view
        # collects all authors, categories stored in db into a single sorted list
        all_authors = sorted(list({*all_authors, *book_data.authors}))
        all_categories = sorted(list({*all_categories, *book_data.categories}))

        # django session keys preparation:
        a_key = "auth"
        c_key = "cat-"
        # serialization for django session storage
        a_serialized = json.dumps(all_authors, cls=DjangoJSONEncoder)
        c_serialized = json.dumps(all_categories, cls=DjangoJSONEncoder)
        # stores serialized data inside django session
        request.session[a_key] = a_serialized
        request.session[c_key] = c_serialized

    # data prepared to be returned for further usage
    lib.all_authors = all_authors
    lib.all_categories = all_categories
    lib.books_cards = books_cards

    return lib
