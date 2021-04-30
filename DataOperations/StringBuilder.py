"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 18:27
 * Github: https://github.com/cod3venom
"""


class StringBuilder:
    def __init__(self):
        self.string = ""

    def append(self, string):
        self.string += str(string)

    def __str__(self):
        return str(self.string)

    def reset(self):
        self.string = ""
