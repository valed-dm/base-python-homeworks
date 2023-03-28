def get_args_library(req):
    rubric = req.args.get("rubric")
    category = req.args.get("category")
    author = req.args.get("author")
    sort = req.args.get("sort")

    return [rubric, category, author, sort]
