from api.apiLegislation import apiLegEndpoints
from utilities import getResponseHttps, readRandomProp
from utilities import getToken
from utilities.customLogger import LogGen
import pytest


class Test_03_Legislation:
    logger = LogGen.loggen()
    legislationList = apiLegEndpoints.getActList()
    legislationSubscribed = apiLegEndpoints.getSubActList()
    legalRegister = apiLegEndpoints.getLegalRegister()
    legislationUpdate = apiLegEndpoints.getUpdateLegislation()
    username = "lahebotest1"
    password = "Lahebo@123"
    token = readRandomProp.read_random_value_from_section('Token', 'prop_token.ini')

    @pytest.mark.smoke
    def test_legislationAPI(self):
        self.logger.info("*******************************Test_03_Legislation*******************************")
        self.logger.info("*******************************Verifying Legislation API*******************************")
        # self.token = getToken.getAccessToken(self.username, self.password)
        responseFromRequest = getResponseHttps.request(self.legislationList, self.token)
        myjson, statusCode = responseFromRequest

        if statusCode == 200:
            # print("\033[92mLegislation List API request is successfully completed: response code is \033[0m",
            #       "\033[95m" + str(statusCode) + "\033[0m")
            assert True
            self.logger.info("*******************************Legislation API test is passed*******************************")
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.info("*******************************Legislation API test is failed*******************************")
            assert False

    @pytest.mark.smoke
    def test_subscribedAPI(self):
        self.logger.info("*******************************Verifying Subscribed API*******************************")
        # self.token = getToken.getAccessToken(self.username, self.password)
        responseFromRequest = getResponseHttps.request(self.legislationSubscribed, self.token)
        myjson, statusCode = responseFromRequest

        if statusCode == 200:
            # print("\033[92mSubscribed Legislation API request is successfully completed: response code is \033[0m",
            #       "\033[95m" + str(statusCode) + "\033[0m")
            assert True
            self.logger.info("*******************************Subscribed API test is passed*******************************")
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.info("*******************************Subscribed API test is failed*******************************")
            assert False

    @pytest.mark.smoke
    def test_legalRegisterAPI(self):
        self.logger.info("*******************************Verifying Legal Register API*******************************")
        responseFromRequest = getResponseHttps.request(self.legalRegister, self.token)
        myjson, statusCode = responseFromRequest

        if statusCode == 200:
            # print("\033[92mLegal Register API request is successfully completed: response code is \033[0m",
            #       "\033[95m" + str(statusCode) + "\033[0m")
            assert True
            self.logger.info("*******************************Legal Register API test is passed*******************************")
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.info("*******************************Legal Register API test failed*******************************")
            assert False

    @pytest.mark.smoke
    def test_updateLegislationAPI(self):
        self.logger.info("*******************************Verifying update legislation API*******************************")
        responseFromRequest = getResponseHttps.request(self.legislationUpdate, self.token)
        myjson, statusCode = responseFromRequest

        if statusCode == 200:
            # print("\033[92mLegislation Update API request is successfully completed: response code is \033[0m",
            #       "\033[95m" + str(statusCode) + "\033[0m")
            assert True
            self.logger.info("*******************************Update legislation API test is passed*******************************")
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.info("*******************************Update legislation API test is failed*******************************")
            assert False

