import requests as req
import os
from twilio.rest import Client

ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
ALPHA_VANTAGE_API = f"https://www.alphavantage.co/query"
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
NEWSAPI_API = "https://newsapi.org/v2/everything"
NEWSAPI_API_KEY = os.environ.get("NEWSAPI_API_KEY")


def get(url, params=None):
    print(f"Making request to {url}")
    res = req.get(url=url) if params is None else req.get(url=url, params=params)
    res.raise_for_status()
    return res.json()


def get_ticker_data():
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "AAPL",
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    ticker_data = get(url=ALPHA_VANTAGE_API, params=params)
    return ticker_data


def send_alert(body_text):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages \
        .create(
            body=body_text,
            from_="+12182748754",
            to="+19803552101"
        )


def get_ticker_news(ticker, today):
    month = today.month if today.month > 9 else f'0{today.month}'
    day = today.day if today.day > 9 else f'0{today.day}'
    params = {
        "q": ticker,
        "from": f"{today.year()}-{month}-{day}",
        "sortBy": "popularity",
        "apiKey": NEWSAPI_API_KEY
    }
    get(url=NEWSAPI_API, params=params)