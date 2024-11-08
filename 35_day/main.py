import requests

based_url = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "0b9dfc46293269b59205f326d8f698d5"

weather_params = {
    "lat": 34.39627,
    "lon": 132.45937,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(based_url, params=weather_params)
response.raise_for_status()
data = response.json()

########### THIS IS HOW I DID IT ############

# list_data = data["list"]
# code_id = list_data[0]["weather"][0]["id"]
# will_rain = False
# for i in range(0, len(list_data)):
#     if code_id < 700:
#         will_rain = True
# if will_rain:
#     print("Bring an Umbrella")


########### THIS IS HOW SHE DID IT ############
will_rain = False
for list_data in data["list"]:
    weather_code = list_data["weather"][0]["id"]
    if int(weather_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella")

# print(f"length of data {len(list_data)}")
# print(code_id)