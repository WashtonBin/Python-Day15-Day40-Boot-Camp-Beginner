import requests
from datetime import datetime
USERNAME = "YOUR_OWN_USER_NAME"
TOKEN = "YOUR_OWN_TOKEN"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
#
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN,
}

today = datetime.now()


pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many km did you cycle today?"),
}

"""create a new graph with header success"""
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

"""create a new pixel"""
# pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
#
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

"""delete pixel"""
# pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
# response = requests.put(url=pixel_update_endpoint, json=pixel_data, headers=headers)

# pixel_delete_endoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
# response = requests.delete(url=pixel_delete_endoint, headers=headers)
# print(response.text)
