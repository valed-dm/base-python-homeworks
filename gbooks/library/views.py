import json

from django.views.generic import DetailView, ListView

from api.schemas import Book
from library.crud import delete_book
from library.helpers import book_prepare
from library.helpers import get_args_library
from library.helpers import info_sort_library
from library.helpers import library_to_view
from library.helpers import sort_books
from library.schemas import ArgsLibrary, Library
from .models import Book as DB_Book


class LibraryListView(ListView):
    model = DB_Book
    template_name = "library/library_books.html"
    context_object_name = "library"

    def get(self, request, *args, **kwargs):
        if "del" in request.GET:
            delete_book(request)
        return super().get(self, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return super().get(self, *args, *kwargs)

    def get_queryset(self):
        lib = library_to_view(self.request)
        r = ArgsLibrary()
        if self.request.method == "POST":
            r = get_args_library(self.request)
        books_cards_sorted = sort_books(r, library_books=lib.books_cards)
        lib.books_cards = books_cards_sorted
        info_sort_library(self.request, r)
        return lib

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # book image size: width, height
        context["width"] = 105
        context["height"] = 150

        return context


class BookDetailView(DetailView):
    model = DB_Book
    template_name = "library/library_book.html"
    book = Book()
    library = Library()

    def get_object(self, queryset=None):
        self.book = DB_Book.objects.get(google_book_id=self.kwargs.get("slug"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        book = book_prepare(self.book)
        self.library.all_authors = json.loads(self.request.session.get("auth"))
        self.library.all_categories = json.loads(self.request.session.get("cat-"))

        context["book"] = book
        context["library"] = self.library
        # book image size: width, height
        context["width"] = 150
        context["height"] = 210

        return context
