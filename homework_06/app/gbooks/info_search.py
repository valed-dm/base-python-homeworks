from flask import flash


def info_search(r, books_found, qty):
    sorting = "sorted by 'newest'" if r.sort == "newest" else ""
    flash(f"{qty} books displayed on page.", category="success")
    flash(f"{books_found} books found upon request.", category="success")
    flash(f"API was searched for '{r.title}' with '{r.category}' category {sorting} among first {r.pace} items.")
