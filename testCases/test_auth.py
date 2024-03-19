from api.apiAuth import apiAuthEndPoints
import requests


class Test_01_Auth:
    registerUser = apiAuthEndPoints.registerUser()
    verifyCode = apiAuthEndPoints.verifyCode()
    loginUser = apiAuthEndPoints.loginUser()

    def test_registerAPI(self):
        urlApi = self.loginUser
        payload = {"username": "lahebotest1",
                   "password": "Lahebo@123"}
        headers = {}
        response_data = requests.post(urlApi, headers=headers, data=payload)
        myjson = response_data.json()
        code = response_data.status_code
        assert 201 == response_data.status_code
        # print(code, myjson)

    def test_meAPI(self):
        code = "405381"
        print(code)
        urlApi = self.verifyCode
        payload = {"username": "test112233445566",
                   "code": "405381"}
        headers = {}
        response_data = requests.post(urlApi, headers=headers, data=payload)
        myjson = response_data.json()
        code = response_data.status_code
        # assert 201 == response_data.status_code
        # print(code, myjson)
    def test(self):
        pass
