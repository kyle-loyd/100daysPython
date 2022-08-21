import requests
import rest_client
from datetime import datetime

HOME_LAT = 41
HOME_LNG = -88


def iss_is_overhead():
    iss_position = rest_client.get_iss_position()
    latitude_check = (HOME_LAT - 5) < iss_position["latitude"] < (HOME_LAT + 5)
    longitude_check = (HOME_LNG - 5) < iss_position["longitude"] < (HOME_LNG + 5)
    return latitude_check and longitude_check




if iss_is_overhead():
    pass

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



