import pytest

from utilities import getResponseHttps
from api.apiLegislation import apiLegEndpoints
from utilities import utilXL
from utilities import getToken


class fetchData:
    legalRegister = apiLegEndpoints.getLegalRegister()
    subscribedItem = apiLegEndpoints.getSubActList()

    def fetchAPIresponse(self, username, password):
        token = getToken.getAccessToken(username, password)
        responseFromRequest = getResponseHttps.request(self.subscribedItem,
                                                       token)  # request is utility which we use for get response from API, and getResponseHttps is file name
        # print(result)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            print("\033[92mYour API request is successfully completed: response code is \033[0m",
                  "\033[95m" + str(statusCode) + "\033[0m")
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
        # print(statusCode)
        req_data_list = []
        for x in myjson["records"]:
            json_data = x["legislation"]["legActId"]
            req_data_list.append([json_data])
        print("Total count of list:", len(req_data_list))
        print(req_data_list)
        # data which we retried from API is inserting in Excel
        if len(req_data_list) != 0:
            utilXL.data_to_excel(req_data_list, "/home/mubashar4603/Desktop/output.xlsx")
        else:
            print("Data is not in list")

    # listofAPI = ["subscribedItem", "legalRegister", "riskRegister", "issueManagement" ]

    # subscribedItem = "https://wevmqe5p4i.execute-api.ap-southeast-2.amazonaws.com/prod/legislation/organization?sortBy=createdAt-DESC&subscribed=true&isReport=true"
    # legalRegister = "https://wevmqe5p4i.execute-api.ap-southeast-2.amazonaws.com/prod/legislation/register?isReport=true&sortBy=createdAt-DESC"
    # riskRegister = "https://wevmqe5p4i.execute-api.ap-southeast-2.amazonaws.com/prod/risk?isReport=true&sortBy=createdAt-DESC"
    # issueManagement = "https://wevmqe5p4i.execute-api.ap-southeast-2.amazonaws.com/prod/issue?sortBy=createdAt-DESC&isReport=true"

    # fetchAPIresponse(legalRegister, "ElizabethHucker", "Marcus3004$")


obj = fetchData()
obj.fetchAPIresponse(username="lahebotest1", password="Lahebo@123")

# def count_filled_and_blank_lists(json_data):
#     filled_lists = 0
#     blank_lists = 0
#
#     # Parse the JSON data
#     data = json.loads(json_data)
#
#     # Iterate through each list
#     for sublist in data:
#         if sublist:  # If the list is not empty
#             filled_lists += 1
#         else:
#             blank_lists += 1
#
#     return filled_lists, blank_lists
#
# # Example JSON data
# json_data = str(req_data_list)
#
# # Count filled and blank lists
# filled, blank = count_filled_and_blank_lists(json_data)
#
# print("Number of filled lists:", filled)
# print("Number of blank lists:", blank)
