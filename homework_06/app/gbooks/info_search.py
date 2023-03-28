from flask import flash


def info_search(args, books_found, qty):
    title, pace, category, sort = args
    sorting = "sorted by 'newest'" if sort == "newest" else ""
    flash(f"{qty} books displayed on page.", category="success")
    flash(f"{books_found} books found upon request.", category="success")
    flash(f"API was searched for '{title}' with '{category}' category {sorting} among first {pace} items.")
