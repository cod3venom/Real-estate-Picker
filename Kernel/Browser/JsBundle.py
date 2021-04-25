"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 19:58
 * Github: https://github.com/cod3venom
"""

import glob
from Kernel.FileSystem.FileSystem import FileSystem


class JsBundle:
    jsPack = {}

    def __init__(self, js_payloads_path):
        self.__js_payloads_path = js_payloads_path
        self.load_to_memory()

    def loadFiles(self) -> list:
        return glob.glob(f"{self.__js_payloads_path}/*.js")

    def load_to_memory(self):
        files = self.loadFiles()
        for index, file in enumerate(files):
            file_name = FileSystem().getFilename(file)
            self.js_add(file_name, file)

    def js_exists(self, key):
        for k in self.jsPack.keys():
            if k == key:
                return True
        return False

    def js_add(self, key, value) -> bool:
        if not self.js_exists(key):
            self.jsPack[key] = value
            return True
        return False

    def js_remove(self, key) -> bool:
        if self.js_exists(key):
            del self.jsPack[key]
            return True
        return False

    def js_get(self, key) -> str:
        if self.js_exists(key):
            return FileSystem().readfile(self.jsPack[key])
        return ""
