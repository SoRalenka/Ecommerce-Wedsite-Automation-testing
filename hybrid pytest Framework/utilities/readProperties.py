
import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getApplicationUsername():
        name = config.get('common info','username')
        return name

    staticmethod
    def getApplicationPassword():
        pw = config.get('common info','password')
        return pw
       