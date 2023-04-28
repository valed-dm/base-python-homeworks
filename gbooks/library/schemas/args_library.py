from dataclasses import dataclass


@dataclass
class ArgsLibrary:
    rubric: str = "all"
    category: str = "all"
    author: str = "all"
    sort: str = "last_added"
    b_key: str = None
