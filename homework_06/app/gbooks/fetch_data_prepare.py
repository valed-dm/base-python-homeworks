def date_restore(date) -> str:
    if len(date) == 4:
        return str(date) + "-01-01"
    elif len(date) == 7:
        return str(date) + "-01"
    else:
        return date


def data_prepare(item):
    authors = item['volumeInfo']['authors'] \
        if 'authors' in item['volumeInfo'] \
           and item['volumeInfo']['authors'] \
        else ['no author']

    categories = item['volumeInfo']['categories'] \
        if 'categories' in item['volumeInfo'] \
           and item['volumeInfo']['categories'] \
        else ['no category']

    date = date_restore(item['volumeInfo']['publishedDate']) \
        if 'publishedDate' in item['volumeInfo'] \
           and item['volumeInfo']['publishedDate'] \
        else '1900-01-01'

    description = item['volumeInfo']['description'] \
        if 'description' in item['volumeInfo'] \
           and item['volumeInfo']['description'] \
        else 'no description'

    book_id = item['id']

    image_src = ""
    if 'imageLinks' in item['volumeInfo'] and item['volumeInfo']['imageLinks']['thumbnail']:
        image_src = item['volumeInfo']['imageLinks']['thumbnail']
    elif 'imageLinks' in item['volumeInfo'] and item['volumeInfo']['imageLinks']['smallThumbnail']:
        image_src = item['volumeInfo']['imageLinks']['smallThumbnail']

    title = item['volumeInfo']['title'] \
        if item['volumeInfo']['title'] \
        else 'no title'

    return [authors, categories, date, description, book_id, image_src, title]
