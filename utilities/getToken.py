import requests
from api.apiAuth import apiAuthEndPoints


def getAccessToken(username, password):
    url = apiAuthEndPoints.loginUser()
    payload = {"username": username, "password": password}
    headers = {}
    response_data = requests.post(url, headers=headers, data=payload)

    # myjson = response_data.json()
    # print('resss:',myjson)

    # req_data = []
    if response_data.status_code == 201:
        # Extract the bearer token from the response
        token = response_data.json()["idToken"]["jwtToken"]
        # print(token)
        return token
    else:
        # If the request failed, print the error message
        print("Error response code is not matched:", response_data.text)
        return None
