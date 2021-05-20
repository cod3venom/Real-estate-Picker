"""
 * Project: Real-estate-Picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 5/20/2021
 * Time: 11:58 AM
 * Github: https://github.com/cod3venom
"""
import json
from DataOperations.StringBuilder import StringBuilder
from Kernel.Global import ctx


class PLEstateSheetTObject:

    def __init__(self, MIASTO: str = "", DZIELNICA: str = "", ULICA: str = "", NR: str = "", LINK: str = "", CENA: str = ""):
        self.city = MIASTO
        self.district = DZIELNICA
        self.street = ULICA
        self.street_number = NR
        self.link = LINK
        self.price = CENA

        ctx.Logger.Print(0, ctx.LogLevel.Success, self.__repr__())


    @classmethod
    def TO(cls, jsData: str):
        try:
            if jsData != "":
                return cls(**json.loads(jsData))
            else:
                return cls(
                    **{'city': 'empty', 'district': 'empty', 'street': 'empty', 'street_number': 'empty', 'link': 'empty', 'price': 'empty'})
        except KeyError as KeyErr:
            pass  # print (True, 3, levels.Error)


    def __repr__(self):
        buffer = StringBuilder()
        buffer.append("<PLEstateSheetTObject:")
        buffer.append(" CITY=" + str(self.city))
        buffer.append(" DZIELNICA=" + str(self.district))
        buffer.append(" ULICA=" + str(self.street))
        buffer.append(" NR=" + str(self.street_number))
        buffer.append(" LINK=" + str(self.link))
        buffer.append(" PRICE=" + str(self.price))
        buffer.append(">")
        return buffer.string
