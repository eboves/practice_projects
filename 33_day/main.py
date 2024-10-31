import requests

MY_LAT = 27.664827
MY_LNG = -81.515755


params = {
    "lat": MY_LAT,
    "lng": MY_LNG
}

response = requests.get("https://api.sunrise-sunset.org/json", params=params)
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]