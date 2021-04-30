"""
 * Project: Real-estate-Picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 4/29/2021
 * Time: 10:30 PM
 * Github: https://github.com/cod3venom
"""

import json
from DataOperations.StringBuilder import StringBuilder
from Kernel.Global import ctx


class LinksListTObject:

    def __init__(self, Links: list):
        self.links = Links

        ctx.Logger.Print(0, ctx.LogLevel.Success, self.__repr__())

    @classmethod
    def TO(cls, jsData: str):
        try:
            if jsData != "":
                return cls(**json.loads(jsData))
            else:
                return cls(**{'Links': '[]'})
        except KeyError as KeyErr:
            pass  # print (True, 3, levels.Error)

    def __repr__(self):
        buffer = StringBuilder()
        buffer.append("<LinksListTObject:")
        buffer.append(" LINK=" + str(self.links))
        buffer.append(">")
        return buffer.string
