"""
 * Project: Real-estate-Picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 4/29/2021
 * Time: 9:02 PM
 * Github: https://github.com/cod3venom
"""
from Kernel.Config.Constants import Constants
from Kernel.TCP.DataParser.MorizonParser import MorizonParser
from Kernel.TCP.Vendors import Vendors


class CommandParser:

    def __init__(self):
        self.morizonParser = MorizonParser()


    def parse_header(self, data: str):
        """
        :param data:
        :return:
        """
        if type(data) == bytes:
            data = bytes(data).decode("utf-8")

        if Constants.ARROW_RIGHT in data:
            split = data.split(Constants.ARROW_RIGHT)

            if len(split) > 0:
                header: str = split[0]
                data: str = split[1]

                if header == Vendors.Morizon:
                    self.morizonParser.parse(data=data)



