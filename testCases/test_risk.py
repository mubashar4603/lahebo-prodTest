from api.apiRisk import apiRiskEndPoints
from utilities import getResponseHttps
from utilities import getToken


class Test_03_Legislation:
    riskRegister = apiRiskEndPoints.getRiskRegister()
    username = "lahebotest1"
    password = "Lahebo@123"
    token = getToken.getAccessToken(username, password)

    def test_riskAPI(self):
        responseFromRequest = getResponseHttps.request(self.riskRegister, self.token)
        myjson, statusCode = responseFromRequest

        if statusCode == 200:
            print("\033[92mRisk Register API request is successfully completed: response code is \033[0m",
                  "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False
