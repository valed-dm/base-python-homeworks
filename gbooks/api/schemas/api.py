from dataclasses import dataclass


@dataclass
class API:
    books: list = [],
    books_found: str = "",
    display_start_info: bool = True,
