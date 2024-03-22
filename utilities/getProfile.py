from api.apiAuth import apiAuthEndPoints
from utilities import writeProperties
from utilities import getToken
import requests
from utilities import getResponseHttps
import json


def getProfileData(username, password):
    token = getToken.getAccessToken(username, password)
    payload = {}
    headers = {
        "Authorization": "Bearer " + token}
    responseFromRequest = requests.get(apiAuthEndPoints.userProfile(), headers=headers, data=payload)
    myjson = responseFromRequest.json()
    # print(myjson)
    # org_id = [organization['orgId'] for organization in myjson['organization']]
    org_id = myjson.get('orgId')
    loc_ids = [location['locId'] for location in myjson['locations']]
    dep_ids = [departments['depId'] for departments in myjson['departments']]
    # print("orgId value:", org_id)
    # print("locId values:", type(loc_ids), loc_ids)
    # print("depId values:", type(dep_ids), dep_ids)
    writeProperties.save_to_properties_file(loc_ids, dep_ids, org_id)


getProfileData("lahebotest1", "Lahebo@123")
