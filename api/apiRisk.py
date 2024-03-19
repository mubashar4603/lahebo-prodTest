from utilities.readProperties import ReadConfig


class apiRiskEndPoints:
    baseUrl = ReadConfig.getBaseUrl()
    riskEndPoint = 'risk?isReport=true&sortBy=createdAt-DESC'

    @staticmethod
    def getRiskRegister():
        apiUrl = apiRiskEndPoints.baseUrl + apiRiskEndPoints.riskEndPoint
        return apiUrl


