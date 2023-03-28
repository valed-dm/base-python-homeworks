def get_args(req):
    title = req.args.get("title")
    pace = req.args.get("pace")
    category = req.args.get("category")
    sort = req.args.get("sort")

    return [title, pace, category, sort]
