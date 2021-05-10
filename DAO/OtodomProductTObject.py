"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 2021-04-27
 * Time: 22:36:52
 * Github: https://github.com/cod3venom
"""

import json
from DataOperations.StringBuilder import StringBuilder
from Kernel.Global import ctx


class OtodomProductTObject:

    def __init__(self, TITLE: str, DESCRIPTION: str, IMAGES: str, PRICE: str, LOCATION: str, MEASUREMENT: str,
                 ROOMS_AMOUNT: str, PHONE_NUMBER: str, CONTACT_DIGNITY: str):
        self.title = TITLE
        self.description = DESCRIPTION
        self.images = IMAGES
        self.price = PRICE
        self.location = LOCATION
        self.measurement = MEASUREMENT
        self.rooms_amount = ROOMS_AMOUNT
        self.phone_number = PHONE_NUMBER
        self.contact_dignity = CONTACT_DIGNITY

        ctx.Logger.Print(0, ctx.LogLevel.Success, self.__repr__())

    @classmethod
    def TO(cls, jsData: str):
        try:
            if jsData != "":
                return cls(**json.loads(jsData))
            else:
                return cls(**{'title': 'empty', 'description': 'empty', 'images': 'empty', 'price': 'empty',
                              'location': 'empty', 'measurement': 'empty', 'rooms_amount': 'empty',
                              'phone_number': 'empty', 'contact_dignity': 'empty'})
        except KeyError as KeyErr:
            pass  # print (True, 3, levels.Error)

    def __repr__(self):
        buffer = StringBuilder()
        buffer.append("<OtodomProductTObject:")
        buffer.append(" TITLE=" + str(self.title))
        buffer.append(" DESCRIPTION=" + str(self.description))
        buffer.append(" IMAGES=" + str(self.images))
        buffer.append(" PRICE=" + str(self.price))
        buffer.append(" LOCATION=" + str(self.location))
        buffer.append(" MEASUREMENT=" + str(self.measurement))
        buffer.append(" ROOMS_AMOUNT=" + str(self.rooms_amount))
        buffer.append(" PHONE_NUMBER=" + str(self.phone_number))
        buffer.append(" CONTACT_DIGNITY=" + str(self.contact_dignity))
        buffer.append(">")
        return buffer.string
