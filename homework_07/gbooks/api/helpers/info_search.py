from django.contrib import messages


def info_search(request, r, books_found, qty):
    if r.title is not None:
        sorting = "sorted by 'newest'" if r.sort == "newest" else ""
        messages.info(
            request,
            f"{qty} books displayed on page."
        )
        messages.info(
            request,
            f"{books_found} books found upon request."
        )
        messages.info(
            request,
            f"API was searched for '{r.title}' with '{r.category}' category {sorting} among first {r.pace} items."
        )
