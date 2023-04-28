import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

api_key = env.str("GOOGLE_API_KEY")


def fetch_uri_create(title: str = "", res_qty: str = "10", start_point: str = "0"):
    api_uri = "https://www.googleapis.com/books/v1/volumes?q=" \
              + title \
              + "&key=" \
              + str(api_key) \
              + "&maxResults=" \
              + res_qty + \
              "&startIndex=" \
              + start_point \
              + "&country=RU"

    return api_uri
