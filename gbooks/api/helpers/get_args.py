from api.schemas import ArgsBook


def get_args_book(request):
    data = request.POST
    title = data.get("title")
    pace = data.get("pace")
    category = data.get("category")
    sort = data.get("sort")

    req_args = ArgsBook(
        title=title,
        pace=pace,
        category=category,
        sort=sort
    )

    return req_args
