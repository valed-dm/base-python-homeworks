from library.schemas import ArgsLibrary


def get_args_library(request):
    data = request.POST
    rubric = data.get("rubric")
    category = data.get("category")
    author = data.get("author")
    sort = data.get("sort")

    req_args = ArgsLibrary(
        rubric=rubric,
        category=category,
        author=author,
        sort=sort
    )

    return req_args
