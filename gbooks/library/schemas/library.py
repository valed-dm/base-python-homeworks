from dataclasses import dataclass
from typing import List

from library.models import Book


@dataclass
class Library:
    books_cards: List[Book] = [],
    all_authors: List[str] = [],
    all_categories: List[str] = [],
