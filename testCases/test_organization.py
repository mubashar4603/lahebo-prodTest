from api.apiOrganisation import apiOrganizationEndpoints
from utilities import getToken
from utilities import getResponseHttps
import requests
from utilities import utilXL
from utilities import getProfile


class Test_06_Auth:
    organizationDetails = apiOrganizationEndpoints.getOrganizationDetails()
    departments = apiOrganizationEndpoints.getDepartments()
    locations = apiOrganizationEndpoints.getLocations()
    jobFunction = apiOrganizationEndpoints.getJobFunction()
    userSetup = apiOrganizationEndpoints.getuserSetup()
    subscription = apiOrganizationEndpoints.getSubscription()
    invoices = apiOrganizationEndpoints.getInvoices()
    product = apiOrganizationEndpoints.getProducts()
    prices = apiOrganizationEndpoints.getPrices()
    riskMatrix = apiOrganizationEndpoints.getRiskMatrix()
    username = utilXL.readData("/home/mubashar4603/PycharmProjects/lahebo-prodTest/TestData/credential.xlsx", "Sheet1",
                               2, 1)
    password = utilXL.readData("/home/mubashar4603/PycharmProjects/lahebo-prodTest/TestData/credential.xlsx", "Sheet1",
                               2, 2)
    token = getToken.getAccessToken(username, password)

    def test_organization(self):
        responseFromRequest = getResponseHttps.request(self.organizationDetails, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            print("\033[92mOrganization Details API request is successfully completed: response code is \033[0m",
                  "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False

    def test_department(self):
        responseFromRequest = getResponseHttps.request(self.departments, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            print("\033[92mDepartments of organization API request is successfully completed: response code is \033[0m",
                  "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False

    def test_location(self):
        responseFromRequest = getResponseHttps.request(self.locations, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            print("\033[92mLocations of organization API request is successfully completed: response code is \033[0m",
                  "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False

    def test_jobFunction(self):
        responseFromRequest = getResponseHttps.request(self.jobFunction, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            print(
                "\033[92mJob Function of organization API request is successfully completed: response code is \033[0m",
                "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False

    def test_userSetup(self):
        responseFromRequest = getResponseHttps.request(self.userSetup, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            print(
                "\033[92mUser setup of organization API request is successfully completed: response code is \033[0m",
                "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False

    def test_subscription(self):
        responseFromRequest = getResponseHttps.request(self.subscription, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            print(
                "\033[92mSubscriptions organization API request is successfully completed: response code is \033[0m",
                "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False

    def test_invoices(self):
        responseFromRequest = getResponseHttps.request(self.invoices, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            print(
                "\033[92mInvoices of organization API request is successfully completed: response code is \033[0m",
                "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False

    def test_product(self):
        responseFromRequest = getResponseHttps.request(self.product, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            print(
                "\033[92mProduct details of organization API request is successfully completed: response code is \033[0m",
                "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False

    def test_prices(self):
        responseFromRequest = getResponseHttps.request(self.prices, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            print(
                "\033[92mUser setup of organization API request is successfully completed: response code is \033[0m",
                "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False

    def test_riskMatrix(self):
        responseFromRequest = getResponseHttps.request(self.riskMatrix, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            print(
                "\033[92mUser setup of organization API request is successfully completed: response code is \033[0m",
                "\033[95m" + str(statusCode) + "\033[0m")
            assert True
        else:
            print("\033[91mYour API request aborted (server error):\033[0m")
            assert False
