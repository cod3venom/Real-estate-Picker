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
        self.TERMINAL_PREFIX = json_data["TERMINAL_PREFIX"].format(self.VERSION)

        self.LOG_FORMAT = json_data["LOG_FORMAT"]
        self.EN_US: str = str(workDir + json_data["EN_US"]).replace("/", os.sep)

        self.BINARY_PATH = str(workDir + json_data["BINARY_PATH"]).replace("/", os.sep)
        self.JS_PATH = str(workDir + json_data["JS_PATH"]).replace("/", os.sep)

        self.DEFAULT_ENCODING = json_data["DEFAULT_ENCODING"]
        self.DEFAULT_TEMPLATE = str(workDir + json_data["DEFAULT_TEMPLATE"]).replace("/", os.sep)

        self.MORIZON_STORAGE = str(workDir + json_data["MORIZON_STORAGE"]).replace("/", os.sep)
        self.GUMTREE_STORAGE = str(workDir + json_data["GUMTREE_STORAGE"]).replace("/", os.sep)

        self.MORIZON_SELECTORS = json_data["MORIZON_SELECTORS"]
        self.GUMTREE_SELECTORS = json_data["GUMTREE_SELECTORS"]
