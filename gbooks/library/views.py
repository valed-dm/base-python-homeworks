import json

from django.views.generic import DetailView, ListView

from api.schemas import Book
from library.crud import delete_book
from library.helpers import book_prepare
from library.helpers import get_args_library
from library.helpers import info_sort_library
from library.helpers import library_to_view
from library.helpers import sort_books
from library.schemas import ArgsLibrary
from .models import Book as DB_Book


class LibraryListView(ListView):
    model = DB_Book
    template_name = "library/library_books.html"

    def get(self, request, *args, **kwargs):
        if "del" in request.GET:
            delete_book(request)
        return super().get(self, *args, *kwargs)

    # POST requests are allowed
    def post(self, *args, **kwargs):
        return super().get(self, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        request = self.request
        # library view sorting params
        r = ArgsLibrary()
        if request.method == "POST":
            r = get_args_library(request)
        lib = library_to_view(request)
        # library view sorting
        books_cards = sort_books(r, library_books=lib.books_cards)
        info_sort_library(request, r)

        context["books"] = books_cards
        # data for dropdowns authors, categories:
        context["authors"] = lib.all_authors
        context["categories"] = lib.all_categories
        # book cover image size:
        context["width"] = 105
        context["height"] = 150
        return context


class BookDetailView(DetailView):
    model = DB_Book
    template_name = "library/library_book.html"
    book = Book()

    def get_object(self, queryset=None):
        self.book = DB_Book.objects.get(google_book_id=self.kwargs.get("slug"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = book_prepare(self.book)
        all_authors = json.loads(self.request.session.get("auth"))
        all_categories = json.loads(self.request.session.get("cat-"))

        context["book"] = book
        context["authors"] = all_authors
        context["categories"] = all_categories
        context["width"] = 150
        context["height"] = 210
        return context
