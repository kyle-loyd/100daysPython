import rest_client

weather = rest_client.get_weather()
for index in range(0, 12):
    if weather["hourly"][index]["weather"][0]["id"] < 700:
        rest_client.send_weather_sms()
        break
