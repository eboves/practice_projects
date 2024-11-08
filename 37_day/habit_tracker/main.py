import requests
USER_NAME = "elvisb"
TOKEN = "avasdfv#$asdfj246"

end_point = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


response = requests.post(end_point, json=user_params)
# print(response.text)



graph_endpoint = f"{end_point}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "programming",
    "unit": "hours",
    "type": "float",
    "color": "kuro"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

graph_response = requests.post(graph_endpoint, json=graph_config, headers=headers)
print(graph_response.text)