import configparser

config = configparser.RawConfigParser()
config.read("/home/mubashar4603/PycharmProjects/lahebo-prodTest/Configurations/config.ini")


class ReadConfig:

    @staticmethod
    def getBaseUrl():
        baseUrl = config.get('common info', 'baseUrl')
        return baseUrl

    @staticmethod
    def getProdUrl():
        stagUrl = config.get('common info', 'stageUrl')
        return stagUrl
