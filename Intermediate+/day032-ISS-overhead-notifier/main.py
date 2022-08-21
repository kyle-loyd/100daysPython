import mail
import rest_client
from datetime import datetime as dt

HOME_LAT = 41.118568
HOME_LNG = -87.859970


def iss_is_overhead():
    iss_position = rest_client.get_iss_position()
    latitude_check = (HOME_LAT - 5) < iss_position["latitude"] < (HOME_LAT + 5)
    longitude_check = (HOME_LNG - 5) < iss_position["longitude"] < (HOME_LNG + 5)
    return latitude_check and longitude_check


def is_nighttime(position):
    data = rest_client.get_sunrise_sunset(position)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_hour = dt.now().hour
    return sunset < current_hour < sunrise


if is_nighttime({"latitude": HOME_LAT, "longitude": HOME_LNG}):
    if iss_is_overhead():
        mail.send()
