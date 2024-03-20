from api.apiAuth import apiAuthEndPoints
from utilities import getToken
import requests
from utilities import utilXL
from utilities import getProfile


class Test_01_Auth:
    registerUser = apiAuthEndPoints.registerUser()
    verifyCode = apiAuthEndPoints.verifyCode()
    userProfile = apiAuthEndPoints.userProfile()
    loginUser = apiAuthEndPoints.loginUser()
    username = utilXL.readData("/home/mubashar4603/PycharmProjects/lahebo-prodTest/TestData/credential.xlsx", "Sheet1",
                               2, 1)
    password = utilXL.readData("/home/mubashar4603/PycharmProjects/lahebo-prodTest/TestData/credential.xlsx", "Sheet1",
                               2, 2)
    token = getToken.getAccessToken(username, password)

    def test_loginAPI(self):
        payload = {"username": self.username, "password": self.password}
        headers = {}
        responseFromRequest = requests.post(self.loginUser, headers=headers, data=payload)
        if responseFromRequest.status_code == 201:
            print("\033[92mLogin User API request is successfully completed: response code is \033[0m",
                  "\033[95m" + str(responseFromRequest.status_code) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False

    def test_meAPI(self):
        payload = {}
        headers = {
            "Authorization": "Bearer " + self.token}
        responseFromRequest = requests.get(self.userProfile, headers=headers, data=payload)
        myjson = responseFromRequest.json()
        if responseFromRequest.status_code == 200:
            print("\033[92mUser Profile (me) API request is successfully completed: response code is \033[0m",
                  "\033[95m" + str(responseFromRequest.status_code) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False
    # def test_getMe(self):
    #     profile = getProfile.getProfileData(self.username, self.password)
    #     print(profile)


