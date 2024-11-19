import requests as req
import os
from twilio.rest import Client
from random import randint

HOME_LAT = 41.118568
HOME_LNG = -87.859970
WEATHER_API_URL = "https://api.openweathermap.org/data/3.0/onecall"
WEATHER_API_KEY = None  #Redacted
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

weather_params = {
    "lat": HOME_LAT,
    "lon": HOME_LNG,
    "appId": WEATHER_API_KEY,
    "exclude": "current, minutely, daily"
}


def build_mock_weather():
    output = {
        "hourly": []
    }
    id_options = [600, 700, 800, 900, 1000]
    for iteration in range(0, 13):
        output["hourly"].append({"weather": [{"id": id_options[randint(0, len(id_options) - 1)]}]})
    return output


def get_weather():
    # res = req.get(url=WEATHER_API_URL, params=weather_params)
    # res.raise_for_status()
    # weather_data = res.json()
    # Mocking the API call because I'm not giving my card # away for an API I don't plan on using much
    return build_mock_weather()


def send_weather_sms():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
        body="It's going to rain.  Don't forget your umbrella!",
        from_="+12182748754",
        to="+19803552101"
    )
