import requests
from twilio.rest import Client


api_key = "__YOUR_OWM_API_KEY__"
account_sid = "__YOUR_TWILIO_ACCOUNT_ID__"
auth_token = "__YOUR_TWILIO_AUTH_TOKEN__"
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
lat = 37.540760
lon = -77.433930

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()



will_rain = False
for hour_data in (weather_data["list"]):
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️.",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER")

    print(message.status)
