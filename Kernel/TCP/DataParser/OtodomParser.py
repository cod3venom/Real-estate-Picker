"""
 * Project: Real-estate-Picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 4/30/2021
 * Time: 2:37 PM
 * Github: https://github.com/cod3venom
"""

from DataOperations.JSON import JSON
from Kernel.Global import ctx, browser
from Vendors.Otodom.Otodom import Otodom


class OtodomParser:

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
                    otodom = Otodom(ctx=ctx, url=link)
                    folderPath = otodom.start()
                    if folderPath != "":
                        ctx.tcpClient.send_message({"Folder": folderPath})

        except Exception as ex:
            print(ex)

        finally:
            ctx.tcpClient.send_message({"Action": "Finished"})
            browser.ChromeDriver.driver().close()
            browser.ChromeDriver.driver().quit()
            exit(-1)
