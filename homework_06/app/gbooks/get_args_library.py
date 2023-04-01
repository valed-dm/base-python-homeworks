from .schemas import ArgsLibrary


def get_args_library(req):
    rubric = req.args.get("rubric")
    category = req.args.get("category")
    author = req.args.get("author")
    sort = req.args.get("sort")

    req_args = ArgsLibrary(
        rubric=rubric,
        category=category,
        author=author,
        sort=sort
    )

    return req_args
    # return [rubric, category, author, sort]
