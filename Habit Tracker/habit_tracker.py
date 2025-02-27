import requests
from datetime import datetime
from file import token,username


pixela = "https://pixe.la/v1/users"

user_param = {
    "token" : token,
    "username" : username,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

graph = f"{pixela}/{username}/graphs"

graph_param ={
    "id" : "bookgraph",
    "name" : "Book",
    "unit" : "pages",
    "type" : "int",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : token
}

post_pixel = f"{graph}/bookgraph"

today = datetime.today()

post_param = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "0",
}

response = requests.post(url=post_pixel, json=post_param, headers=headers)
print(response.text)




