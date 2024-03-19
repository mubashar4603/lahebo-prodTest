from api.apiAuth import apiAuthEndPoints
import requests
from utilities.getOtp import getEmailOtp


class Test_01_Auth:
    registerUser = apiAuthEndPoints.registerUser()
    verifyCode = apiAuthEndPoints.verifyCode()

    def test_registerAPI(self):
        urlApi = self.registerUser
        payload = {"username": "test112233445566",
                   "firstName": "test01",
                   "lastName": "test01",
                   "password": "Lahebo@123",
                   "email": "randomstagtest+112233445566@gmail.com",
                   "phoneNumber": "+61203108082",
                   "orgName": "test0rg112233445566"}
        headers = {}
        response_data = requests.post(urlApi, headers=headers, data=payload)
        myjson = response_data.json()
        code = response_data.status_code
        assert 201 == response_data.status_code
        print(code, myjson)
        return myjson, code

    def test_verifyCode(self):
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
        print(code, myjson)
