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
from Kernel.Bootloader.Args import Args
from Kernel.Global import ctx, browser
from Kernel.TCP.Vendors import Vendors, VendorHosts
from Kernel.SpreadSheet.Ods import Ods
from Kernel.SpreadSheet.SheetTypes import SheetTypes
from Vendors.DomiPorta.DomiPorta import DomiPorta
from Vendors.Domy.Domy import Domy
from Vendors.Gratka.Gratka import Gratka
from Vendors.Gumtree.Gumtree import Gumtree
from Vendors.Morizon.Morizon import Morizon
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

        self.args = Args()
        self.args.sysArgvTOdict()
        self.parser()


    def parser(self):
        if self.args.keyExists("type"):
            self.file_type = self.args.getValueOf("type")

        if self.args.keyExists("file"):
            self.file = self.args.getValueOf("file")

        if self.args.keyExists("link"):
            self.link = self.args.getValueOf("link")

        if self.args.keyExists("single"):
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
        data = ods.read(self.file).select_records(["MIASTO", "DZIELNICA", "ULICA", "NR", "LINK", "CENA"])

        for key in data:
            record = ods.dict_to_str(data[key])
            plSheetObj = PLEstateSheetTObject.TO(record)

            if plSheetObj:
                self.run_not_segregated(plSheetObj.link, plSheetObj)



    def on_exit(self):
        browser.ChromeDriver.driver().close()
        browser.ChromeDriver.driver().quit()
