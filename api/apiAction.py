from utilities.readProperties import ReadConfig


class apiActionEndPoints:
    baseUrl = ReadConfig.getBaseUrl()
    actionEndPoint = 'actions?isReport=true&sortBy=createdAt-DESC'

    @staticmethod
    def getActionCenter():
        apiUrl = apiActionEndPoints.baseUrl + apiActionEndPoints.actionEndPoint
        return apiUrl
