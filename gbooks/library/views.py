import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from library.crud import delete_book
from library.helpers import books_to_session
from library.helpers import get_args_library
from library.helpers import get_library_book
from library.helpers import info_sort_library
from library.helpers import sort_books
from library.schemas import ArgsLibrary


@csrf_protect
def library_view(request):
    # deletes book from library
    if request.method == "GET" and "del" in request.GET:
        delete_book(request)
    # prepares library
    lib = books_to_session(request)
    # default sorting order
    r = ArgsLibrary()

    # gets custom sorting params from request
    if request.method == "POST":
        r = get_args_library(request)
    # sorting
    books_cards = sort_books(r, library_books=lib.books_cards)
    info_sort_library(request, r)

    return render(request, "library/library_books.html", {
        "books": books_cards,
        # to fill data into dropdowns authors, categories:
        "authors": lib.all_authors,
        "categories": lib.all_categories,
        "width": 105,
        "height": 150
    })


@csrf_protect
def library_book_view(request):
    book = get_library_book(request)
    # to fill data into dropdowns authors, categories
    all_authors = json.loads(request.session.get("auth"))
    all_categories = json.loads(request.session.get("cat-"))

    return render(request, "library/library_book.html", {
        "book": book,
        # to fill data into dropdowns authors, categories:
        "authors": all_authors,
        "categories": all_categories,
        "width": 150,
        "height": 210
    })
