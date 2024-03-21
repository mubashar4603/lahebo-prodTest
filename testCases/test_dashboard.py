from api.apiDashboard import apiDashboardEndpoints
from utilities import getToken
from utilities import getResponseHttps
import requests
from utilities import utilXL
from utilities import getProfile


class Test_02_Dashboard:
    dashboardStats = apiDashboardEndpoints.getDashboardStats()
    username = utilXL.readData("/home/mubashar4603/PycharmProjects/lahebo-prodTest/TestData/credential.xlsx", "Sheet1",
                               2, 1)
    password = utilXL.readData("/home/mubashar4603/PycharmProjects/lahebo-prodTest/TestData/credential.xlsx", "Sheet1",
                               2, 2)
    token = getToken.getAccessToken(username, password)

    def test_dashboardStats(self):
        responseFromRequest = getResponseHttps.request(self.dashboardStats, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            print("\033[92mAction Center API request is successfully completed: response code is \033[0m",
                  "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False
