from utilities.readProperties import ReadConfig


class apiLegEndpoints:
    baseUrl = ReadConfig.getBaseUrl()
    legislationListEndPoint = 'legislation/acts?'
    subscribedLegEndPoint = 'legislation/organization?sortBy=createdAt-DESC&subscribed=true&isReport=true'
    legalItemEndpoint = 'legislation/register?isReport=true&sortBy=createdAt-DESC'
    updateLegEndPoint = 'legislation/new-versions'

    @staticmethod
    def getActList():
        apiUrl = apiLegEndpoints.baseUrl + apiLegEndpoints.legislationListEndPoint
        return apiUrl

    @staticmethod
    def getSubActList():
        apiUrl = apiLegEndpoints.baseUrl + apiLegEndpoints.subscribedLegEndPoint
        return apiUrl

    @staticmethod
    def getLegalRegister():
        apiUrl = apiLegEndpoints.baseUrl + apiLegEndpoints.legalItemEndpoint
        return apiUrl

    @staticmethod
    def getUpdateLegislation():
        apiUrl = apiLegEndpoints.baseUrl + apiLegEndpoints.updateLegEndPoint
        return apiUrl



