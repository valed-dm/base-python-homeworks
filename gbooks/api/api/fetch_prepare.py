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
    Book.google_book_id = item['id']

    if 'authors' in item['volumeInfo'] and item['volumeInfo']['authors']:
        Book.authors = item['volumeInfo']['authors']

    if 'categories' in item['volumeInfo'] and item['volumeInfo']['categories']:
        Book.categories = item['volumeInfo']['categories']

    if 'publishedDate' in item['volumeInfo'] and item['volumeInfo']['publishedDate']:
        Book.date = date_restore(item['volumeInfo']['publishedDate'])

    if 'description' in item['volumeInfo'] and item['volumeInfo']['description']:
        Book.description = item['volumeInfo']['description']

    if 'imageLinks' in item['volumeInfo'] and item['volumeInfo']['imageLinks']['thumbnail']:
        Book.image_src = item['volumeInfo']['imageLinks']['thumbnail']
    elif 'imageLinks' in item['volumeInfo'] and item['volumeInfo']['imageLinks']['smallThumbnail']:
        Book.image_src = item['volumeInfo']['imageLinks']['smallThumbnail']

    if item['volumeInfo']['title']:
        Book.title = item['volumeInfo']['title']

    return Book
