from .schemas import ArgsBook


def get_args_book(req):
    title = req.args.get("title")
    pace = req.args.get("pace")
    category = req.args.get("category")
    sort = req.args.get("sort")

    req_args = ArgsBook(
        title=title,
        pace=pace,
        category=category,
        sort=sort
    )

    return req_args
