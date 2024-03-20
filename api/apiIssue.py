from utilities.readProperties import ReadConfig


class apiIssueEndPoints:
    baseUrl = ReadConfig.getBaseUrl()
    issueEndPoint = 'issue?sortBy=createdAt-DESC&isReport=true'

    @staticmethod
    def getIssueManagement():
        apiUrl = apiIssueEndPoints.baseUrl + apiIssueEndPoints.issueEndPoint
        return apiUrl
