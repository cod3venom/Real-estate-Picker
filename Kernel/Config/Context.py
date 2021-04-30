"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 16:17
 * Github: https://github.com/cod3venom
"""
import requests

from DAO.LocalSettingsTObject import LocalSettingsTObject
from DataOperations.JSON import JSON
from Kernel.Browser.JsBundle import JsBundle
from Kernel.Config.Constants import Constants
from Kernel.FileSystem.FileSystem import FileSystem
from Kernel.HTTP.httpClient import HttpClient
from Kernel.Logger.Logger import Levels, Logger, Texts
from Kernel.Parser.Xpath import Xpath
from Kernel.TCP.TcpClient import TcpClient


class Context:


    def __init__(self):
        self.__constants = Constants()
        self.__localSettings = LocalSettingsTObject(self.__constants.SETTINGS_FILE)

        self.__logger = Logger(texts_file=self.__localSettings.EN_US, log_format=self.__localSettings.LOG_FORMAT)
        self.__levels = Levels()

        self.__texts = Texts(file=self.__localSettings.EN_US)
        self.__texts.loadTexts()

        self.__fileSystem = FileSystem()
        self.__json = JSON()

        self.__jsBundle = JsBundle(self.__localSettings.JS_PATH)
        self.__http = HttpClient()

        self.__http.set_session(requests.Session())
        self.__xpath = Xpath()
        self.tcpClient = TcpClient()




    @property
    def Constants(self):
        return self.__constants

    @property
    def Settings(self):
        return self.__localSettings

    @property
    def Logger(self):
        return self.__logger

    @property
    def Texts(self):
        return self.__texts

    @property
    def LogLevel(self):
        return self.__levels

    @property
    def FileSystem(self):
        return self.__fileSystem

    @property
    def JSON(self):
        return self.__json

    @property
    def JsBundle(self):
        return self.__jsBundle

    @property
    def HTTP(self):
        return self.__http

    @property
    def XPATH(self):
        return self.__xpath
