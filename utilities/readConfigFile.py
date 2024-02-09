import configparser

config = configparser.RawConfigParser()  # this (configparser.RawConfigParser) method is use  to read the data from
# config.ini
# file # .ini file we have # create to save the common data


config.read("D:\\Credence Class Notes\\CredenceBatches\\Credence_Automation_Jan 24\\Credkart_Pytest\\Configuration\\config.ini")


class Readconfig:

    @staticmethod
    def getUserEmail():
        UserEmail = config.get('login data', 'UserEmail') # this is gpoing to fetch data from common data section and from Useremail field
        #config.get('section', 'Field')
        return UserEmail

    @staticmethod
    def getPassword():
        Password = config.get('login data', 'Password')
        return Password




