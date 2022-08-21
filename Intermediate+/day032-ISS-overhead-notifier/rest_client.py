import requests as req
from datetime import datetime as dt

ISS_API_URL = "http://api.open-notify.org/iss-now.json"
SUNRISE_SUNSET_API_URL = "https://api.sunrise-sunset.org/json"


def get(url, params=None):
    print(f"Making request to {url}")
    res = req.get(url=url) if params is None else req.get(url=url, params=params)
    res.raise_for_status()
    return res.json()


def get_iss_position():
    data = get(url=ISS_API_URL)
    lat = float(data["iss_position"]["latitude"])
    lng = float(data["iss_position"]["longitude"])
    return {"latitude": lat, "longitude": lng}


def get_sunrise_sunset(position):
    params = {"lat": position["latitude"], "lng": position["longitude"], "formatted": 0}
    return get(url=SUNRISE_SUNSET_API_URL, params=params)
    
    
