import configparser

config = configparser.RawConfigParser()
config.read("/home/mubashar4603/PycharmProjects/Lahebo_scripting/Configurations/config.ini")


class ReadConfig:

    @staticmethod
    def getBaseUrl():
        baseUrl = config.get('common info', 'baseUrl')
        return baseUrl
