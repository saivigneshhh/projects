import requests
from twilio.rest import Client

# account_sid = "account id"
# auth_token = "token id"


endpoint="https://api.openweathermap.org/data/2.5/forecast"
# apiley="api key"
parameters={
    "lat":17.154289,
    "lon":82.255257,
    "appid":apiley,
    "cnt":4

}


response=requests.get(endpoint,params=parameters)
response.raise_for_status()
data=response.json()

for weather_data in data["list"]:
    condition=weather_data["weather"][0]["id"]
    if int(condition)<700:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="it's raining outside",
            from_="+mobile number",
            to="mobile number"
        )
    else:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="not raining",
            from_="+mobile number",
            to="+mobile number "
        )
print("message sent")
