"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 21:48
 * Github: https://github.com/cod3venom
"""
import os

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

    def add_attention(self, attention: str):
        self.__template = self.__template.replace('$(ATTENTION)', attention)

    def add_percentage(self, percentage: str):
        if percentage != "":
            if "%" not in percentage:
                percentage += "%"
        self.__template = self.__template.replace('$(PERCENTAGE)', percentage)

    def add_vendor_abbreviation(self, vendor_abbreviation: str):
        self.__template = self.__template.replace('$(VENDOR_ABBREVIATION)', vendor_abbreviation)

    def report(self):
        return self.__template

    def sanitize(self):
        for black in self.__blacklist:
            if black in self.__template:
                self.__template = self.__template.replace(black, '')
                self.__template = str(self.__template).strip()

    def save(self, path):
        self.sanitize()
        return FileSystem().writeToFile(path + os.sep + 'opis.txt', self.__template)
