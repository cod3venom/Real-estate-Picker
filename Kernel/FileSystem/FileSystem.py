"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 17:25
 * Github: https://github.com/cod3venom
"""

import os
import random
import string
import shutil

from DataOperations.DATE import DATE


class FileSystem:
    chmod_allow_everything = 0o777

    def readfile(self, file_path: str) -> str:
        if file_path is not None:
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf8') as reader:
                    return reader.read()
        return ""

    def append(self, file_path: str, content: str) -> bool:
        if file_path is not None and content is not None:
            with open(file_path, 'a', encoding='utf8') as appender:
                appender.write(content + '\n')
                return True
        return False

    def appendToFile(self, file_path: str, content: str, duplicate=True) -> bool:
        if duplicate:
            return self.append(file_path, content)
        else:
            file_content = self.readfile(file_path)
            if content not in file_content:
                return self.append(file_path, content)
        return False

    def writeToFile(self, file_path: str, content: str) -> bool:
        if file_path is not None and content is not None:
            with open(file_path, 'w', encoding='utf8') as writer:
                writer.write(content)
                return True
        return False

    def getFilename(self, path) -> str:
        if '/' in path:
            file = path.split('/')[-1]
            if '.' in file:
                return file.split('.')[0]
            else:
                pass
                # print (True, 14, Levels.Warning)
        else:
            pass
            # print (True, 13, Levels.Warning)
        return ""

    def create_dir(self, path, remove: bool = False):
        path = self.sanitize_path(path)
        if os.path.exists(path) and os.path.isdir(path):
            if remove:
                shutil.rmtree(path)

        if not os.path.exists(path):
            os.mkdir(path)
            os.chmod(path, self.chmod_allow_everything)
            return True
        return False

    def generateRandomName(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(10))

    def sanitize_path(self, path: str):
        blacklist = ["<", ">", ',', 'm²', '"', "|", "?", "\n", "+"]

        for black in blacklist:
            if black in path:
                path = path.replace(black, "")
        return path

    def file_name_from_path(self, path: str):
        on_delimiter = []
        if "\\" in path:
            on_delimiter = path.split("\\")
        if "/" in path:
            on_delimiter = path.split("/")

        if len(on_delimiter) > 0:
            return on_delimiter[len(on_delimiter) - 1]
        return ""
