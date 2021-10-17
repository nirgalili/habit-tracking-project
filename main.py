import requests
from datetime import datetime
import os


pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "nirgal"
TOKEN = os.environ["TOKEN_FOR_PIXE"]
ID = "graph1"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"



graph_config = {
    "id": ID,
    "name": "swimming_graph",
    "unit": "meters",
    "type": "float",
    "color": "sora"

}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

today = datetime(year=2021, month=10, day=15)

pixela_creation_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4500",

}

# response = requests.post(url=pixela_creation_endpoint, json=pixela_creation_config, headers=headers)
# print(response.text)

update_date = today.strftime("%Y%m%d")

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{update_date}"

update_config = {
    "quantity": "4400"
}

# response = requests.put(url=update_pixel_endpoint, json=update_config, headers=headers)
# print(response.text)

delete_time = datetime.now()
delete_time = delete_time.strftime("%Y%m%d")

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{delete_time}"



response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
