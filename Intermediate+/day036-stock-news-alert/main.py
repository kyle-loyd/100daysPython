from rest_client import get_ticker_data, send_alert
from datetime import datetime as dt, timedelta
from math import floor


def extract_data_for_date(date):
    date_string = f"{date.year}-{date.month if date.month > 10 else f'0{date.month}'}-{date.day}"
    return get_ticker_data()["Time Series (Daily)"][date_string]["4. close"]


def get_percent_difference(x, y):
    quotient = x / y
    total_percent = floor(quotient * 100)
    return abs(total_percent - 100)


def format_text_body(key, data):
    body_text = f"\nTicker: {key}"
    body_text += f"\nDifference: {data['difference']}"
    body_text += f"\nPercent Difference: {data['percent_difference']}"
    return body_text


tickers = ['AAPL']
records = {}
yesterday = dt.today() - timedelta(days=1)
day_before_yesterday = dt.today() - timedelta(days=2)
for ticker in tickers:
    yesterday_closing = float(extract_data_for_date(yesterday))
    day_before_yesterday_closing = float(extract_data_for_date(day_before_yesterday))
    difference = yesterday_closing - day_before_yesterday_closing
    percent_difference = get_percent_difference(yesterday_closing, day_before_yesterday_closing)
    records[ticker] = {
        "difference": str(difference),
        "percent_difference": f"{'+ ' if difference > 0 else '- '}{percent_difference}%"
    }
    send_alert(format_text_body(ticker, records[ticker]))

print(records)
