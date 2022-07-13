import requests
from datetime import datetime as dt
# pixela_endPoint = "https://pixe.la/v1/users"
# USER_NAME = "suleiman71747478ali"
# TOKEN = "test71747478"
# GRAPH_ID = "graph1"
# # create account:
# user_params = {
#     "token": TOKEN,
#     "username": USER_NAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=pixela_endPoint, json=user_params)
# print(response.text)

# create a graph:
# graph_endPoint = f"{pixela_endPoint}/{USER_NAME}/graphs"
# graph_params = {
#     "id": "graph1",
#     "name": "Cycling graph",
#     "unit":"Km",
#     "type": "float",
#     "color": "sora"
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.post(url=graph_endPoint, json=graph_params, headers=headers)
# print(response.text)
# add a pixel to the graph:
# now = dt.now().strftime("%Y%m%d")
# pixel_params = {
#     "date":now,
#     "quantity": "7.0"
# }
# response = requests.post(url=f"https://pixe.la/v1/users/{USER_NAME}/graphs/graph1", json=pixel_params, headers=headers)
# print(response.text)
# update graph or pixel:
# update_graph_params = {
#     "unit":"int"
# }
# response = requests.put(url=f"{pixela_endPoint}/{USER_NAME}/graphs/{GRAPH_ID}", json=update_graph_params, headers=headers)
# print(response.text)
# delete a pixel or graph:
# response = requests.delete(url=f"{pixela_endPoint}/{USER_NAME}/graphs/{GRAPH_ID}/{now}", headers=headers)
# print(response.text)
# to see your graph go to -> https://pixe.la/v1/users/suleiman71747478ali/graphs/graph1.html <-:
