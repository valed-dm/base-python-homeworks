from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from api.api import fetch_to_session
from api.helpers import add_into_library, get_book


# Create your views here.
@csrf_protect
def books_view(request):
    api = fetch_to_session(request)

    return render(request, "api/books.html", {
        "books": api.books,
        "books_found": api.books_found,
        "display_start_info": api.display_start_info,
        # image size vars
        "width": 105,
        "height": 150
    })


@csrf_protect
def book_view(request):
    book = {}
    # retrieves book from django session
    if request.method == "GET":
        book = get_book(request)
    # adds book to library
    if request.method == "POST":
        book = add_into_library(request)

    return render(request, "api/book.html", {
        "book": book,
        "width": 150,
        "height": 210
    })
