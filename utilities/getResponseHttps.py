import requests

def request(url, token):
    API_url = url
    payload = {}
    headers = {
        "Authorization": "Bearer " + token}
    response_data = requests.get(API_url, headers=headers, data=payload)
    myjson = response_data.json()
    code = response_data.status_code
    return myjson, code                           # Returning two value as a tuple
