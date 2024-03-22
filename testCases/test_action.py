from api.apiAction import apiActionEndPoints
from utilities import getToken
from utilities import getResponseHttps
import pytest


class Test_05_Legislation:
    actionCenter = apiActionEndPoints.getActionCenter()
    username = "lahebotest1"
    password = "Lahebo@123"
    token = getToken.getAccessToken(username, password)

    @pytest.mark.smoke
    def test_actionAPI(self):
        responseFromRequest = getResponseHttps.request(self.actionCenter, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            print("\033[92mAction Center API request is successfully completed: response code is \033[0m",
                  "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False
