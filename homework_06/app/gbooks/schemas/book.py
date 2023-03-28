from dataclasses import dataclass


@dataclass
class Book:
    authors: [str]
    categories: [str]
    date: str
    description: str
    google_book_id: str
    image_src: str
    title: str

    # initial mock data:

    # book_data = [
    #     ["Arthur C. Clarke", "Stanley Kubrick"],
    #     "Fiction",
    #     "01-01-2016",
    #     "A deluxe hardcover edition of the wondrous space adventure that is the basis for Stanley "
    #     "Kubrick’s Oscar-winning film—now celebrating its 50th anniversary Part of Penguin Galaxy",
    #     "1",
    #     "http://books.google.com/books/content?id=JidnEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
    #     "2001: A Space Odyssey"
    # ]
    #
    # books = []
    #
    # for num in range(1, 21):
    #     book_data[4] = str(num)
    #     books.append(Book(*book_data))
    #
    # for book in books:
    #     print(book.id, end=",")
