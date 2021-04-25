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
from Kernel.Parser.Xpath import Xpath


class Context:
    __constants: Constants
    __localSettings: LocalSettingsTObject
    __fileSystem: FileSystem
    __json: JSON
    __jsBundle: JsBundle
    __http: HttpClient
    __xpath: Xpath

    def __init__(self):
        self.__constants = Constants()
        self.__localSettings = LocalSettingsTObject(self.__constants.SETTINGS_FILE)
        self.__fileSystem = FileSystem()
        self.__json = JSON()
        self.__jsBundle = JsBundle(self.__localSettings.JS_PATH)
        self.__http = HttpClient()
        self.__http.set_session(requests.Session())
        self.__xpath = Xpath()

    @property
    def Constants(self):
        return self.__constants

    @property
    def Settings(self):
        return self.__localSettings

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

