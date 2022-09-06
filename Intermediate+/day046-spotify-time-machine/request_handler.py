import requests as req

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100"


def get_billboard_page(date_string):
    target_url = f"{BILLBOARD_BASE_URL}/{date_string}"
    return req.get(target_url).text
