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
        if os.path.exists(path):
            if remove:
                os.system(f'rm -rf {path}')

        if not os.path.exists(path):
            os.mkdir(path)
            os.chmod(path, self.chmod_allow_everything)
            return True
        return False


    def generateRandomName(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(10))

    def download(self, binary, path):
        with open(path, 'wb') as writer:
            shutil.copyfileobj(binary, writer)
            return path
