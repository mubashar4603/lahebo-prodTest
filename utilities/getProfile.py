from api.apiAuth import apiAuthEndPoints
from utilities import getResponseHttps
from utilities import getToken
import requests
import json


def getProfileData(username, password):
    token = getToken.getAccessToken(username, password)
    payload = {}
    headers = {
        "Authorization": "Bearer " + token}
    responseFromRequest = requests.get(apiAuthEndPoints.userProfile(), headers=headers, data=payload)
    myjson = responseFromRequest.json()
    # print(myjson)
    loc_ids = [location['locId'] for location in myjson['locations']]
    dep_ids = [departments['depId'] for departments in myjson['departments']]
    print("locId values:", type(loc_ids), loc_ids)
    print("depId values:", type(dep_ids), dep_ids)




getProfileData("lahebotest1", "Lahebo@123")