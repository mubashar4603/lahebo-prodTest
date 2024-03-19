from utilities import getResponseHttps
from api.apiLegislation import apiLegEndpoints
from utilities import utilXL
from utilities import getToken


class fetchData:
    # legalRegister = legApiEndpoints.getLegalRegister()
    scrappedLegislation = apiLegEndpoints.getActList()

    def fetchAPIresponse(self, username, password):
        token = getToken.getAccessToken(username, password)
        responseFromRequest = getResponseHttps.request(self.scrappedLegislation,
                                                       token)  # request is utility which we use for get response from API, and getResponseHttps is file name
        # print(result)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            print("\033[92mYour API request is successfully completed: response code is \033[0m",
                  "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False
        # print(statusCode)
        req_data_list = []
        for x in myjson["records"]:
            json_data = x["name"]
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
obj.fetchAPIresponse(username="ElizabethHucker", password="Marcus3004$")
