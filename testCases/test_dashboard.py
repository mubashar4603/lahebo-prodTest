from api.apiDashboard import apiDashboardEndpoints
from utilities import getToken
from utilities import getResponseHttps, readRandomProp
from utilities.customLogger import LogGen
import pytest
from utilities import utilXL
from utilities import getProfile


class Test_02_Dashboard:
    logger = LogGen.loggen()
    dashboardStats = apiDashboardEndpoints.getDashboardStats()
    username = utilXL.readData("/home/mubashar4603/PycharmProjects/lahebo-prodTest/TestData/credential.xlsx", "Sheet1",
                               2, 1)
    password = utilXL.readData("/home/mubashar4603/PycharmProjects/lahebo-prodTest/TestData/credential.xlsx", "Sheet1",
                               2, 2)
    token = readRandomProp.read_random_value_from_section('Token', 'prop_token.ini')

    @pytest.mark.smoke
    def test_dashboardStats(self):
        self.logger.info("*******************************Test_02_Dashboard*******************************")
        self.logger.info(
            "*******************************Verifying Dashboard Stats API*******************************")
        responseFromRequest = getResponseHttps.request(self.dashboardStats, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            # print("\033[92mAction Center API request is successfully completed: response code is \033[0m",
            #       "\033[95m" + str(statusCode) + "\033[0m")
            assert True
            self.logger.info("*******************************Dashboard Stats API is passed*******************************")
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.info("*******************************Dashboard Stats API is failed*******************************")
            assert False
