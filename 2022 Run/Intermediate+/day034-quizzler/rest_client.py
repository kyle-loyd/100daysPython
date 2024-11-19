import requests as req

QUIZ_API = "https://opentdb.com/api.php?amount=10&category=15&type=boolean"

def get(url, params=None):
    print(f"Making request to {url}")
    res = req.get(url=url) if params is None else req.get(url=url, params=params)
    res.raise_for_status()
    return res.json()
    

def get_quiz_questions():
    return get(url=QUIZ_API)["results"]
