from utilities.readProperties import ReadConfig


class apiAuthEndPoints:
    baseUrl = ReadConfig.getBaseUrl()
    registerEndPoint = 'auth/register'
    verify_codeEndPoint = 'auth/verify-code'
    loginEndPoint = '/auth/login'
    associate_software_tokenEndpPoint = 'auth/associate-software-token'
    verify_software_tokenEndPoint = 'auth/verify-software-token'
    meEndPoint = 'auth/me'
    mfa_codeEndpoint = 'auth/login/require-totp-code'
    require_new_passwordEndPoint = 'auth/login/require-new-password'
    resend_codeEndPoint = 'auth/resend-code'
    refresh_tokenEndPoint = 'auth/refresh-token'
    change_passwordEndPoint = 'auth/change-password'
    forgot_passwordEndPoint = 'auth/forgot-password'
    confirm_passwordEndPoint = 'auth/confirm-password'

    credentialEndPoint = 'auth/credentials'
    checkEndPoint = '/auth/check'

    @staticmethod
    def registerUser():
        apiUrl = apiAuthEndPoints.baseUrl + apiAuthEndPoints.registerEndPoint
        return apiUrl
    @staticmethod
    def verifyCode():
        apiUrl = apiAuthEndPoints.baseUrl + apiAuthEndPoints.verify_codeEndPoint
        return apiUrl
    @staticmethod
    def loginUser():
        apiUrl = apiAuthEndPoints.baseUrl + apiAuthEndPoints.loginEndPoint
        return apiUrl
    @staticmethod
    def generateMfaKey():
        apiUrl = apiAuthEndPoints.baseUrl + apiAuthEndPoints.associate_software_tokenEndpPoint
        return apiUrl
    @staticmethod
    def verifyMfaKey():
        apiUrl = apiAuthEndPoints.baseUrl + apiAuthEndPoints.verify_software_tokenEndPoint
        return apiUrl
    @staticmethod
    def userProfile():
        apiUrl = apiAuthEndPoints.baseUrl + apiAuthEndPoints.meEndPoint
        return apiUrl
    @staticmethod
    def multiFactorAuthentication():
        apiUrl = apiAuthEndPoints.baseUrl + apiAuthEndPoints.mfa_codeEndpoint
        return apiUrl
