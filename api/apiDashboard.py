from utilities.readProperties import ReadConfig


class apiDashboardEndpoints:
    baseUrl = ReadConfig.getBaseUrl()
    dashboardEndPoint = 'report/dashboard?'

    @staticmethod
    def getDashboardStats():
        apiUrl = apiDashboardEndpoints.baseUrl + apiDashboardEndpoints.dashboardEndPoint
        return apiUrl
