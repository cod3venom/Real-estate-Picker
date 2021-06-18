"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 26.04.2021
 * Time: 18:01
 * Github: https://github.com/cod3venom
"""

import datetime
import inspect
import os
import locale
from colorama import Fore

from Kernel.FileSystem.FileSystem import FileSystem


class Constants:
    EMPTY = ""
    HASHTAG = "#"
    DOLLAR = "$"
    NEWLINE = "\n"


class Levels:
    Info = "Info"
    Success = "Success"
    Warning = "Warning"
    Error = "Error"
    hackerType = "hackerType"


class Colors:
    Default = Fore.WHITE
    Success = Fore.GREEN
    Error = Fore.RED
    Warning = Fore.YELLOW
    Info = Fore.BLUE
    HackerType = Fore.LIGHTCYAN_EX


class Texts:
    file: str
    textStack: dict = {}
    constants = Constants()

    def __init__(self, file: str):

        current_lang = ""
        region_language = locale.getdefaultlocale()
        if "en_US" in region_language:
            self.file  = file + "text_EN.lang"

        if "pl_PL" in region_language:
            self.file = file + "text_PL.lang"
        else:
            self.file = file + "text_EN.lang"


    def loadTexts(self):
        if os.path.isfile(self.file):
            with open(self.file, "r", encoding="utf-8") as reader:
                content = reader.read()
                if self.constants.NEWLINE in content:
                    lines = content.split(self.constants.NEWLINE)
                    for line in lines:
                        if self.constants.HASHTAG in line:
                            spl = line.split(self.constants.HASHTAG)
                            self.textStack[spl[0]] = spl[1]

    def textFromDict(self, number: int, target: dict) -> str:
        if self.textStack is not None:
            try:
                if str(number) in target.keys():
                    return target[str(number)]
            except KeyError:
                print("Text not found")
                return self.constants.EMPTY
        return self.constants.EMPTY

    def getText(self, number: int) -> str:
        return self.textFromDict(number, self.textStack)


class Logger:
    texts_file: str
    log_format: str


    def __init__(self, texts_file: str, log_format: str, logs_dir: str, autoInit: bool = False):
        self.texts_file = texts_file
        self.log_format = log_format
        self.logs_dir = logs_dir

        self.texts = Texts(self.texts_file)
        self.__globalMessage: dict = {}
        if autoInit:
            self.texts.loadTexts()

        self.constants = Constants()
        self.level = Constants.EMPTY
        self.levels = Levels()
        self.time = Constants.EMPTY
        self.color = Constants.EMPTY
        self.caller = Constants.EMPTY
        self.colors = Colors()

    @property
    def GlobalMessage(self) -> dict:
        return self.__globalMessage

    def initColor(self):
        if self.level == self.levels.Info:
            self.color = self.colors.Info
        if self.level == self.levels.Success:
            self.color = self.colors.Success
        if self.level == self.levels.Warning:
            self.color = self.colors.Warning
        if self.level == self.levels.Error:
            self.color = self.colors.Error
        if self.level == self.levels.hackerType:
            self.color = self.colors.HackerType

    def Print(self, msg_num: int, level: Levels, message: str = "", log_to_file: bool = False):
        text = ""
        self.level = level
        self.initColor()

        self.caller = inspect.stack()[1][0].f_locals["self"].__class__.__name__ + "." + inspect.stack()[
            1].function + self.constants.HASHTAG + str(inspect.stack()[1].lineno)
        self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if msg_num > 0:
            text = self.texts.getText(msg_num)
        else:
            if message:
                text = str(message)

        text = self.log_format.format(self.colors.Success, self.colors.Warning + self.time,
                                      self.color + self.caller, "Real Estate", self.colors.Default + message)
        print(text)
        self.__globalMessage = {"Log": text}

        if log_to_file:
            self.log_to_file(text)


    def log_to_file(self, content: str):
        now = datetime.datetime.now()
        creation_date = now.strftime("%Y-%m-%d %H-%M-%S")
        file = str(f"{self.logs_dir}LOG_{creation_date}.log")
        FileSystem().writeToFile(file_path=file, content=content)