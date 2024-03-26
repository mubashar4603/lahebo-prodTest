from utilities.readProperties import ReadConfig
from utilities import readRandomProp


class apiOrganizationEndpoints:
    baseUrl = ReadConfig.getBaseUrl()
    org_id = readRandomProp.read_random_value_from_section('Organisation', "prop.ini")
    organization = f"organizations/{org_id}/users?"
    departments = f"organizations/{org_id}/departments"
    locations = f"organizations/{org_id}/locations"
    jobFunction = f"organizations/{org_id}/job-function"
    userSetup = f"organizations/{org_id}/users?take=20&sortBy=createdAt-DESC"
    subscription = "payment/subscription"
    products = "payment/products"
    prices = "payment/prices"
    invoices = "payment/invoices"
    riskMatrix = f"organizations/{org_id}/risk-matrix"

    @staticmethod
    def getOrganizationDetails():
        apiUrl = apiOrganizationEndpoints.baseUrl + apiOrganizationEndpoints.organization
        return apiUrl

    @staticmethod
    def getDepartments():
        apiUrl = apiOrganizationEndpoints.baseUrl + apiOrganizationEndpoints.departments
        return apiUrl

    @staticmethod
    def getLocations():
        apiUrl = apiOrganizationEndpoints.baseUrl + apiOrganizationEndpoints.locations
        return apiUrl

    @staticmethod
    def getJobFunction():
        apiUrl = apiOrganizationEndpoints.baseUrl + apiOrganizationEndpoints.jobFunction
        return apiUrl

    @staticmethod
    def getuserSetup():
        apiUrl = apiOrganizationEndpoints.baseUrl + apiOrganizationEndpoints.userSetup
        return apiUrl

    @staticmethod
    def getSubscription():
        apiUrl = apiOrganizationEndpoints.baseUrl + apiOrganizationEndpoints.subscription
        return apiUrl

    @staticmethod
    def getInvoices():
        apiUrl = apiOrganizationEndpoints.baseUrl + apiOrganizationEndpoints.invoices
        return apiUrl

    @staticmethod
    def getProducts():
        apiUrl = apiOrganizationEndpoints.baseUrl + apiOrganizationEndpoints.products
        return apiUrl

    @staticmethod
    def getPrices():
        apiUrl = apiOrganizationEndpoints.baseUrl + apiOrganizationEndpoints.prices
        return apiUrl

    @staticmethod
    def getRiskMatrix():
        apiUrl = apiOrganizationEndpoints.baseUrl + apiOrganizationEndpoints.riskMatrix
        return apiUrl
