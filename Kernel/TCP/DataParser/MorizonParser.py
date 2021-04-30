"""
 * Project: Real-estate-Picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 4/29/2021
 * Time: 9:27 PM
 * Github: https://github.com/cod3venom
"""
from DataOperations.JSON import JSON
from DataOperations.StringBuilder import StringBuilder
from Kernel.Global import ctx
from Vendors.Morizon.Morizon import Morizon


class MorizonParser:

    def __init__(self):
        self.json = JSON()


    def parse(self, data: str):
        """
        :param data:
        :return:
        """
        try:
            jsonData = self.json.loads(data)

            if jsonData:
                for link in jsonData["Links"]:
                    morizon = Morizon(ctx=ctx, url=link)
                    if morizon.start():
                        ctx.tcpClient.send_message({"Link": link})




        except Exception as ex:
            print(ex)