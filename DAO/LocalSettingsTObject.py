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
        self.BINARY_PATH = workDir + json_data["BINARY_PATH"]
        self.JS_PATH = workDir + json_data["JS_PATH"]
        self.DEFAULT_ENCODING = json_data["DEFAULT_ENCODING"]
        self.DEFAULT_TEMPLATE = workDir + json_data["DEFAULT_TEMPLATE"]

        self.MORIZON_STORAGE = workDir + json_data["MORIZON_STORAGE"]
        self.MORIZON_SELECTORS = json_data["MORIZON_SELECTORS"]

