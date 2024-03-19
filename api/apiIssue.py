from utilities.readProperties import ReadConfig


class apiIssuekEndPoints:
    baseUrl = ReadConfig.getBaseUrl()
    issueEndPoint = 'issue?sortBy=createdAt-DESC&isReport=true'

    @staticmethod
    def getIssueManagement():
        apiUrl = apiIssuekEndPoints.baseUrl + apiIssuekEndPoints.issueEndPoint
        return apiUrl
