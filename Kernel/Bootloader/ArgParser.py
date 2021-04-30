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

from DataOperations.LIST import LIST
from Kernel.Bootloader.Args import Args
from Kernel.Global import ctx, browser
from Kernel.TCP.Vendors import Vendors
from Vendors.DomiPortal.DomiPortal import DomiPortal
from Vendors.Domy.Domy import Domy
from Vendors.Gratka.Gratka import Gratka
from Vendors.Gumtree.Gumtree import Gumtree
from Vendors.Morizon.Morizon import Morizon
from Vendors.Olx.Olx import Olx
from Vendors.Otodom.Otodom import Otodom


class ArgParser:

    def __init__(self):
        atexit.register(self.on_exit)
        self.args = Args()
        self.args.sysArgvTOdict()
        self.parser()

    def parser(self):
        if self.args.keyExists("vendor"):
            vendor = self.args.getValueOf("vendor")

            if self.args.keyExists("link"):
                link = self.args.getValueOf("link")
                self.run_singe_link(vendor=vendor, link=link)

            if self.args.keyExists("file"):
                file = self.args.getValueOf("file")
                self.run_multiple_links(vendor=vendor, file=file)



    def run_singe_link(self, vendor: str, link: str):
        result: str = ""
        if vendor == Vendors.Morizon:
            source = Morizon(ctx=ctx, url=link)
            result = source.start()
            return
        if vendor == Vendors.Otodom:
            source = Otodom(ctx=ctx, url=link)
            result = source.start()
            return
        if vendor == Vendors.Gratka:
            source = Gratka(ctx=ctx, url=link)
            result = source.start()
            return
        if vendor == Vendors.Gumtree:
            source = Gumtree(ctx=ctx, url=link)
            result = source.start()
            return
        if vendor == Vendors.Domy:
            source = Domy(ctx=ctx, url=link)
            result = source.start()
            return
        if vendor == Vendors.Olx:
            source = Olx(ctx=ctx, url=link)
            result = source.start()
            return

        if vendor == Vendors.DomiPortal:
            source = DomiPortal(ctx=ctx, url=link)
            result = source.start()
            return

        else:
            ctx.Logger.Print(0, ctx.LogLevel.Warning, ctx.Texts.getText(8).format(vendor))
            return 0






    def run_multiple_links(self, vendor: str, file):

        content = ctx.FileSystem.readfile(file)
        if content != "":
            lines = LIST.str_to_lines(content)
            for line in lines:
                self.run_singe_link(vendor, line)



    def on_exit(self):
        browser.ChromeDriver.driver().close()
        browser.ChromeDriver.driver().quit()

