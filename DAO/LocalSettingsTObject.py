"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 17:24
 * Github: https://github.com/cod3venom
"""

import json
import os
from Kernel.FileSystem.FileSystem import FileSystem


class LocalSettingsTObject:

    def __init__(self, settings_file: str):
        json_data = json.loads(FileSystem().readfile(settings_file))
        workDir = os.getcwd()
        self.VERSION = json_data["VERSION"]
        self.AUTHOR = json_data["AUTHOR"]
        self.AUTHOR_MAIL = json_data["AUTHOR_MAIL"]

        self.TERMINAL_PREFIX = json_data["TERMINAL_PREFIX"].format(self.VERSION)

        self.LOG_FORMAT = json_data["LOG_FORMAT"]
        self.TEXTS_PATH: str = str(workDir + json_data["TEXTS_PATH"]).replace("/", os.sep)

        self.BINARY_PATH_LINUX = str(workDir + json_data["BINARY_PATH_LINUX"]).replace("/", os.sep)
        self.BINARY_PATH_WINDOWS = str(workDir + json_data["BINARY_PATH_WINDOWS"]).replace("/", os.sep)

        self.JS_PATH = str(workDir + json_data["JS_PATH"]).replace("/", os.sep)

        self.DEFAULT_ENCODING = json_data["DEFAULT_ENCODING"]
        self.DEFAULT_TEMPLATE = str(workDir + json_data["DEFAULT_TEMPLATE"]).replace("/", os.sep)

        self.MORIZON_STORAGE = str(workDir + json_data["MORIZON_STORAGE"]).replace("/", os.sep)
        self.GUMTREE_STORAGE = str(workDir + json_data["GUMTREE_STORAGE"]).replace("/", os.sep)
        self.OLX_STORAGE = str(workDir + json_data["OLX_STORAGE"]).replace("/", os.sep)
        self.GRATKA_STORAGE = str(workDir + json_data["GRATKA_STORAGE"]).replace("/", os.sep)
        self.DOMY_STORAGE = str(workDir + json_data["DOMY_STORAGE"]).replace("/", os.sep)
        self.DOMIPORTAL_STORAGE = str(workDir + json_data["DOMIPORTAL_STORAGE"]).replace("/", os.sep)
        self.OTODOM_STORAGE = str(workDir + json_data["OTODOM_STORAGE"]).replace("/", os.sep)

        self.MORIZON_SELECTORS = json_data["MORIZON_SELECTORS"]
        self.GUMTREE_SELECTORS = json_data["GUMTREE_SELECTORS"]
        self.OLX_SELECTORS = json_data["OLX_SELECTORS"]
        self.GRATKA_SELECTORS = json_data["GRATKA_SELECTORS"]
        self.DOMY_SELECTORS = json_data["DOMY_SELECTORS"]
        self.DOMIPORTAL_SELECTORS = json_data["DOMIPORTAL_SELECTORS"]
        self.OTODOM_SELECTORS = json_data["OTODOM_SELECTORS"]