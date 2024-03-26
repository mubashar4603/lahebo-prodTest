from api.apiAuth import apiAuthEndPoints
import requests
import pytest
from utilities import utilXL
from utilities.customLogger import LogGen
from utilities import writeProperties, readRandomProp


class Test_01_Auth:
    logger = LogGen.loggen()
    registerUser = apiAuthEndPoints.registerUser()
    verifyCode = apiAuthEndPoints.verifyCode()
    userProfile = apiAuthEndPoints.userProfile()
    loginUser = apiAuthEndPoints.loginUser()

    username = readRandomProp.read_data_from_propFile('Usernames', 'prod_users.ini', 1)
    password = readRandomProp.read_data_from_propFile('Passwords', 'prod_users.ini', 1)

    # def __init__(self, username_value, password_value):
    #     self.username = readRandomProp.read_data_from_propFile('Usernames', 'prod_users.ini', username_value)
    #     self.password = readRandomProp.read_data_from_propFile('Passwords', 'prod_users.ini', password_value)

    @pytest.mark.smoke
    def test_loadData(self):
        self.logger.info("*******************************Loading Data From Excel*******************************")
        excelData = utilXL.read_all_dataInList('credential.xlsx', 'A', 'B')
        usernames, passwords = excelData
        writeProperties.save_to_properties_file(prop_file_path='prod_users.ini', usernames=usernames,
                                                passwords=passwords)

    assert True

    @pytest.mark.smoke
    def test_loginAPI(self):
        self.logger.info("*******************************Test_01_Auth*******************************")
        self.logger.info("*******************************Verifying Organization Detail API*******************************")
        payload = {"username": self.username, "password": self.password}
        headers = {}
        responseFromRequest = requests.post(self.loginUser, headers=headers, data=payload)
        # print(responseFromRequest.status_code)

        if responseFromRequest.status_code == 201:
            tokenAccess = responseFromRequest.json()["idToken"]["jwtToken"]
            writeProperties.save_to_properties_file(token=tokenAccess, prop_file_path="prop_token.ini")
            assert True
            self.logger.info("*******************************Login API test is passed*******************************")
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.info("*******************************Login API test is failed*******************************")
            assert False

    @pytest.mark.smoke
    def test_meAPI(self):
        token = readRandomProp.read_random_value_from_section("Token", "prop_token.ini")
        self.logger.info("*******************************Verifying meAPI*******************************")
        payload = {}
        headers = {
            "Authorization": "Bearer " + token}
        responseFromRequest = requests.get(self.userProfile, headers=headers, data=payload)
        myjson = responseFromRequest.json()
        if responseFromRequest.status_code == 200:
            org_id = myjson.get('orgId')
            loc_ids = [location['locId'] for location in myjson['locations']]
            dep_ids = [departments['depId'] for departments in myjson['departments']]
            writeProperties.save_to_properties_file(loc_ids, dep_ids, org_id, prop_file_path="prop.ini")
            assert True
            self.logger.info("*******************************meAPI test is passed*******************************")
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.info("*******************************meAPI test is failed*******************************")
            assert False



