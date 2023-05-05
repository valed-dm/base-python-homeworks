from django.shortcuts import redirect

from library.helpers.authors_str import authors_string
from library.helpers.info_add import info_add
from library.helpers.info_exists import info_exists
from library.models import Author, Book, Category, Image
from .get_or_create import get_or_create


def add_book(request, book):
    b = book
    # truncates names to avoid doubles in db authors, categories
    book_authors = [author.strip() for author in b["authors"]]
    book_categories = [category.strip() for category in b["categories"]]
    # gets or creates authors, categories to be filled in m-2-m Book fields
    authors = get_or_create(Author, book_authors)
    categories = get_or_create(Category, book_categories)
    # still not in use at the moment but is left for the future
    authors_str = authors_string(book_authors)
    # checks if book already added to db before
    book_exists = Book.objects.all().filter(google_book_id=b["google_book_id"]).exists()
    # fills in Image table to provide data for 1-2-1 image_src field
    image_src = Image(image_src=b["image_src"])
    # primarily saves data to get image_src_id
    image_src.save()

    # prepares book data to be filled in books table
    if book_exists:
        info_exists(request, b["title"])
        return redirect("book/")
    else:
        book_to_library = Book(
            authors_str=authors_str,
            title=b["title"],
            description=b["description"],
            date=b["date"],
            google_book_id=b["google_book_id"],
            rubric="read_asap",
            remark="no remark added",
            image_src=image_src,
        )
    # primarily saves book_to_library data into db
    # for a reason that book_id is necessary to perform coming next m2m operations
    book_to_library.save()
    # m-2-m operations on book object in db are performed
    # m-2-m association tables are filled in automatically
    book_to_library.authors.set(authors)
    book_to_library.categories.set(categories)

    info_add(request, b["title"])
