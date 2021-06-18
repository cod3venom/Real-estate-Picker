"""
 * Project: Real-estate-Picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 4/30/2021
 * Time: 4:05 PM
 * Github: https://github.com/cod3venom
"""
import sys
import atexit

from DAO.PLEstateSheetTObject import PLEstateSheetTObject
from DataOperations.LIST import LIST
from Kernel.Global import args
from Kernel.Global import ctx, browser
from Kernel.TCP.Vendors import Vendors, VendorHosts
from Kernel.SpreadSheet.Ods import Ods
from Kernel.SpreadSheet.SheetTypes import SheetTypes
from Vendors.DomiPorta.DomiPorta import DomiPorta
from Vendors.Domy.Domy import Domy
from Vendors.Gratka.Gratka import Gratka
from Vendors.Gumtree.Gumtree import Gumtree
from Vendors.Morizon.Morizon import Morizon
from Vendors.Olx.Auth import Auth as OlxAuth
from Vendors.Olx.Olx import Olx
from Vendors.Otodom.Otodom import Otodom


class ArgParser:

    def __init__(self):
        atexit.register(self.on_exit)
        self.vendor = ""
        self.file = ""
        self.file_type = ""
        self.link = ""
        self.single = False
        self.login_vendor = ""

        try:
            self.parser()
        except Exception as ex:
            ctx.Logger.Print(0, ctx.LogLevel.Info, str(ex), log_to_file=True)
            ctx.Logger.Print(10, ctx.LogLevel.Info)
            sys.exit(0)

    def parser(self):

        if args.keyExists("login"):
            self.login_vendor = args.getValueOf("login").lower()

            if self.login_vendor == "olx":
                OlxAuth(user_control=True)

        if args.keyExists("type"):
            self.file_type = args.getValueOf("type")

        if args.keyExists("file"):
            self.file = args.getValueOf("file")

        if args.keyExists("link"):
            self.link = args.getValueOf("link")

        if args.keyExists("single"):
            self.single = True


        if self.file_type == "" and self.link != "":
            self.run_not_segregated(self.link)

        elif self.file != "":
            if self.file_type == SheetTypes.TXT:
                self.run_from_txt()

            if self.file_type == SheetTypes.ODS:
                self.run_from_ods()









    def run_not_segregated(self, link, sheetObj: PLEstateSheetTObject = None):
        if Vendors.Morizon.lower() in link:
            source = Morizon(ctx=ctx, url=link, sheetObj=sheetObj).start()

        if Vendors.Otodom.lower() in link:
            source = Otodom(ctx=ctx, url=link, sheetObj=sheetObj).start()

        if Vendors.Gratka.lower() in link:
            source = Gratka(ctx=ctx, url=link, sheetObj=sheetObj).start()

        if Vendors.Gumtree.lower() in link:
            source = Gumtree(ctx=ctx, url=link, sheetObj=sheetObj).start()

        if VendorHosts.Domy in link:
            source = Domy(ctx=ctx, url=link, sheetObj=sheetObj).start()

        if Vendors.Olx.lower() in link:
            source = Olx(ctx=ctx, url=link, sheetObj=sheetObj).start()

        if Vendors.DomiPorta.lower() in link:
            source = DomiPorta(ctx=ctx, url=link, sheetObj=sheetObj).start()


    def run_from_txt(self):
        content = ctx.FileSystem.readfile(self.file)
        if content != "":
            lines = LIST.str_to_lines(content)
            for link in lines:
                self.run_not_segregated(link)
        else:
            ctx.Logger.Print(0, ctx.LogLevel.Warning, ctx.Texts.getText(11).format(self.file))
            return 0

    def run_from_ods(self):
        ods = Ods()
        data = ods.read(self.file).select_records(["MIASTO", "DZIELNICA", "ULICA", "NR", "LINK", "CENA", "UWAGI", "PROWIZJA"])

        for key in data:
            record = ods.dict_to_str(data[key])
            plSheetObj = PLEstateSheetTObject.TO(record)

            if plSheetObj:
                self.run_not_segregated(plSheetObj.link, plSheetObj)



    def on_exit(self):
        browser.ChromeDriver.kill()
