import pytest
from api.apiOrganisation import apiOrganizationEndpoints
from utilities import getToken
from utilities import getResponseHttps, readRandomProp
from utilities.customLogger import LogGen
from utilities import utilXL
from utilities import getProfile


class Test_06_Organization:
    logger = LogGen.loggen()
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
    token = readRandomProp.read_random_value_from_section('Token', 'prop_token.ini')

    @pytest.mark.smoke
    def test_organization(self):
        self.logger.info("*******************************Test_06_Organization*******************************")
        self.logger.info(
            "*******************************Verifying Organization Detail API*******************************")
        responseFromRequest = getResponseHttps.request(self.organizationDetails, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            # print("\033[92mOrganization Details API request is successfully completed: response code is \033[0m",
            #       "\033[95m" + str(statusCode) + "\033[0m")
            assert True
            self.logger.info(
                "*******************************Organization Detail API test is passed*******************************")
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.error(
                "*******************************Organization Detail API test is failed*******************************")
            assert False

    @pytest.mark.smoke
    def test_department(self):
        self.logger.info(
            "*******************************Verifying Department API*******************************")
        responseFromRequest = getResponseHttps.request(self.departments, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            # print("\033[92mDepartments of organization API request is successfully completed: response code is \033[0m",
            #       "\033[95m" + str(statusCode) + "\033[0m")
            assert True
            self.logger.info(
                "*******************************Department API test is passed*******************************")
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.error(
                "*******************************Department API test is failed*******************************")
            assert False

    @pytest.mark.smoke
    def test_location(self):
        self.logger.info(
            "*******************************Verifying Location API*******************************")
        responseFromRequest = getResponseHttps.request(self.locations, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            # print("\033[92mLocations of organization API request is successfully completed: response code is \033[0m",
            #       "\033[95m" + str(statusCode) + "\033[0m")
            self.logger.info(
                "*******************************Location API test is passed*******************************")
            assert True
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.error(
                "*******************************Location API test is failed*******************************")
            assert False

    @pytest.mark.smoke
    def test_jobFunction(self):
        self.logger.info(
            "*******************************Verifying Job Function API*******************************")
        responseFromRequest = getResponseHttps.request(self.jobFunction, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            # print(
            # "\033[92mJob Function of organization API request is successfully completed: response code is \033[0m",
            # "\033[95m" + str(statusCode) + "\033[0m")
            self.logger.info(
                "*******************************Job Function API test is passed*******************************")
            assert True
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.error(
                "*******************************Job function API test is failed*******************************")
            assert False

    @pytest.mark.smoke
    def test_userSetup(self):
        self.logger.info(
            "*******************************Verifying User Setup API*******************************")
        responseFromRequest = getResponseHttps.request(self.userSetup, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            # print(
            #     "\033[92mUser setup of organization API request is successfully completed: response code is \033[0m",
            #     "\033[95m" + str(statusCode) + "\033[0m")
            self.logger.info(
                "*******************************Location API test is passed*******************************")
            assert True
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.error(
                "*******************************Location API test is failed*******************************")
            assert False

    @pytest.mark.smoke
    def test_subscription(self):
        self.logger.info(
            "*******************************Verifying Subscription API*******************************")
        responseFromRequest = getResponseHttps.request(self.subscription, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            # print(
            #     "\033[92mSubscriptions organization API request is successfully completed: response code is \033[0m",
            #     "\033[95m" + str(statusCode) + "\033[0m")
            self.logger.info(
                "*******************************Subscription API test is passed*******************************")
            assert True
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.error(
                "*******************************Subscription API is failed*******************************")
            assert False

    def test_invoices(self):
        self.logger.info(
            "*******************************Verifying Invoices API*******************************")
        responseFromRequest = getResponseHttps.request(self.invoices, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            # print(
            #     "\033[92mInvoices of organization API request is successfully completed: response code is \033[0m",
            #     "\033[95m" + str(statusCode) + "\033[0m")
            self.logger.info(
                "*******************************Invoices API is passed*******************************")
            assert True
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.error(
                "*******************************Invoices API is failed*******************************")
            assert False

    def test_product(self):
        self.logger.info(
            "*******************************Verifying Product API*******************************")
        responseFromRequest = getResponseHttps.request(self.product, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            # print(
            #     "\033[92mProduct details of organization API request is successfully completed: response code is \033[0m",
            #     "\033[95m" + str(statusCode) + "\033[0m")
            self.logger.info(
                "*******************************Product API is passed*******************************")
            assert True
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.error(
                "*******************************Product API is failed*******************************")
            assert False

    def test_prices(self):
        self.logger.info(
            "*******************************Verifying Prices API*******************************")
        responseFromRequest = getResponseHttps.request(self.prices, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            # print(
            #     "\033[92mUser setup of organization API request is successfully completed: response code is \033[0m",
            #     "\033[95m" + str(statusCode) + "\033[0m")
            self.logger.error(
                "*******************************Prices API is passed*******************************")
            assert True
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.error(
                "*******************************Prices API is failed*******************************")
            assert False

    @pytest.mark.smoke
    def test_riskMatrix(self):
        self.logger.info(
            "*******************************Verifying Risk Matrix API*******************************")
        responseFromRequest = getResponseHttps.request(self.riskMatrix, self.token)
        myjson, statusCode = responseFromRequest
        if statusCode == 200:
            # print(
            #     "\033[92mUser setup of organization API request is successfully completed: response code is \033[0m",
            #     "\033[95m" + str(statusCode) + "\033[0m")
            self.logger.info(
                "*******************************Risk Matrix API is passed*******************************")
            assert True
        else:
            # print("\033[91mYour API request aborted (server error):\033[0m")
            self.logger.error(
                "*******************************Risk Matrix API is failed*******************************")
            assert False
