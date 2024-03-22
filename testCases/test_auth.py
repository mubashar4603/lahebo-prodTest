from api.apiAuth import apiAuthEndPoints
from utilities import getToken
import requests
import pytest
from utilities import utilXL
from utilities.customLogger import LogGen
from utilities import getProfile


class Test_01_Auth:
    logger = LogGen.loggen()
    registerUser = apiAuthEndPoints.registerUser()
    verifyCode = apiAuthEndPoints.verifyCode()
    userProfile = apiAuthEndPoints.userProfile()
    loginUser = apiAuthEndPoints.loginUser()
    username = utilXL.readData("/home/mubashar4603/PycharmProjects/lahebo-prodTest/TestData/credential.xlsx", "Sheet1",
                               2, 1)
    password = utilXL.readData("/home/mubashar4603/PycharmProjects/lahebo-prodTest/TestData/credential.xlsx", "Sheet1",
                               2, 2)
    token = getToken.getAccessToken(username, password)

    @pytest.mark.smoke
    def test_loginAPI(self):
        self.logger.info("*******************************Test_01_Auth*******************************")
        self.logger.info(
            "*******************************Verifying Organization Detail API*******************************")
        payload = {"username": self.username, "password": self.password}
        headers = {}
        responseFromRequest = requests.post(self.loginUser, headers=headers, data=payload)
        if responseFromRequest.status_code == 201:
            # print("\033[92mLogin User API request is successfully completed: response code is \033[0m",
            #       "\033[95m" + str(responseFromRequest.status_code) + "\033[0m")
            assert True
            self.logger.info("*******************************Login API test is passed*******************************")
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.info("*******************************Login API test is failed*******************************")
            assert False

    @pytest.mark.smoke
    def test_meAPI(self):
        self.logger.info("*******************************Verifying meAPI*******************************")
        payload = {}
        headers = {
            "Authorization": "Bearer " + self.token}
        responseFromRequest = requests.get(self.userProfile, headers=headers, data=payload)
        myjson = responseFromRequest.json()
        if responseFromRequest.status_code == 200:
            # print("\033[92mUser Profile (me) API request is successfully completed: response code is \033[0m",
            #       "\033[95m" + str(responseFromRequest.status_code) + "\033[0m")
            assert True
            self.logger.info("*******************************meAPI test is passed*******************************")
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.info("*******************************meAPI test is failed*******************************")
            assert False



