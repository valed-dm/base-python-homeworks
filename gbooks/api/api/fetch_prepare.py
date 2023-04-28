from api.schemas import Book


def date_restore(date: str) -> str:
    if len(date) == 4:
        return str(date) + "-01-01"
    elif len(date) == 5:
        return str(date[:4]) + "-01-01"
    elif len(date) == 7:
        return str(date) + "-01"
    else:
        return date[:10]


def data_prepare(item):
    book = Book()
    book.google_book_id = item['id']

    if 'authors' in item['volumeInfo'] and item['volumeInfo']['authors']:
        book.authors = item['volumeInfo']['authors']

    if 'categories' in item['volumeInfo'] and item['volumeInfo']['categories']:
        book.categories = item['volumeInfo']['categories']

    if 'publishedDate' in item['volumeInfo'] and item['volumeInfo']['publishedDate']:
        book.date = date_restore(item['volumeInfo']['publishedDate'])

    if 'description' in item['volumeInfo'] and item['volumeInfo']['description']:
        book.description = item['volumeInfo']['description']

    if 'imageLinks' in item['volumeInfo'] and item['volumeInfo']['imageLinks']['thumbnail']:
        book.image_src = item['volumeInfo']['imageLinks']['thumbnail']
    elif 'imageLinks' in item['volumeInfo'] and item['volumeInfo']['imageLinks']['smallThumbnail']:
        book.image_src = item['volumeInfo']['imageLinks']['smallThumbnail']

    if item['volumeInfo']['title']:
        book.title = item['volumeInfo']['title']

    return book
