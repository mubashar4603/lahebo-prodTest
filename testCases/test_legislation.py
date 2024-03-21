from api.apiLegislation import apiLegEndpoints
from utilities import getResponseHttps
from utilities import getToken


class Test_03_Legislation:
    legislationList = apiLegEndpoints.getActList()
    legislationSubscribed = apiLegEndpoints.getSubActList()
    legalRegister = apiLegEndpoints.getLegalRegister()
    legislationUpdate = apiLegEndpoints.getUpdateLegislation()
    username = "lahebotest1"
    password = "Lahebo@123"
    token = getToken.getAccessToken(username, password)

    def test_legislationAPI(self):
        # self.token = getToken.getAccessToken(self.username, self.password)
        responseFromRequest = getResponseHttps.request(self.legislationList, self.token)
        myjson, statusCode = responseFromRequest

        if statusCode == 200:
            print("\033[92mLegislation List API request is successfully completed: response code is \033[0m",
                  "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False

    def test_subscribedAPI(self):
        # self.token = getToken.getAccessToken(self.username, self.password)
        responseFromRequest = getResponseHttps.request(self.legislationSubscribed, self.token)
        myjson, statusCode = responseFromRequest

        if statusCode == 200:
            print("\033[92mSubscribed Legislation API request is successfully completed: response code is \033[0m",
                  "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False

    def test_legalRegisterAPI(self):
        responseFromRequest = getResponseHttps.request(self.legalRegister, self.token)
        myjson, statusCode = responseFromRequest

        if statusCode == 200:
            print("\033[92mLegal Register API request is successfully completed: response code is \033[0m",
                  "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False
    def test_updateLegislationAPI(self):
        responseFromRequest = getResponseHttps.request(self.legislationUpdate, self.token)
        myjson, statusCode = responseFromRequest

        if statusCode == 200:
            print("\033[92mLegislation Update API request is successfully completed: response code is \033[0m",
                  "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False

