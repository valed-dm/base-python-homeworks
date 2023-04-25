def authors_string(authors: list) -> str:
    res = ""
    for author in authors:
        res = f"{res}, {author.title()}"

    return res[2:]
