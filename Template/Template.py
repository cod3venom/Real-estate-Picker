"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 21:48
 * Github: https://github.com/cod3venom
"""
from Kernel.Config.Context import Context
from Kernel.FileSystem.FileSystem import FileSystem


class Template:

    def __init__(self, temp_path):
        self.__template: str = FileSystem().readfile(temp_path)
        self.__blacklist = [' ']

    def add_description(self, description: str):
        self.__template = self.__template.replace('$(DESCRIPTION)', description)

    def add_rooms_amount(self, amount: str):
        self.__template = self.__template.replace('$(ROOMS_AMOUNT)', amount)

    def add_measurement(self, measurement: str):
        self.__template = self.__template.replace('$(MEASUREMENT)', measurement)

    def add_price(self, price: str):
        self.__template = self.__template.replace('$(PRICE)', price)

    def add_phone_number(self, number: str):
        self.__template = self.__template.replace('$(PHONE_NUMBER)', number)

    def add_contact_dignity(self, dignity: str):
        self.__template = self.__template.replace('$(CONTACT_DIGNITY)', dignity)

    def add_link(self, link: str):
        self.__template = self.__template.replace('$(LINK)', link)

    def add_date(self, date: str):
        self.__template = self.__template.replace('$(DATE)', date)

    def report(self):
        return self.__template

    def sanitize(self):
        for black in self.__blacklist:
            if black in self.__template:
                self.__template = self.__template.replace(black, '')

    def save(self, path):
        self.sanitize()
        return FileSystem().writeToFile(path + '/opis.txt', self.__template)
