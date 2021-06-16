"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 26.04.2021
 * Time: 11:27
 * Github: https://github.com/cod3venom
"""
import json
import os
import time

from DAO.PLEstateSheetTObject import PLEstateSheetTObject
from DataOperations.DATE import DATE
from DataOperations.LIST import LIST
from Kernel.Global import browser
from Template.Template import Template
from Vendors.Gumtree.Selectors import Selectors
from DAO.GumtreeProductTObject import GumtreeProductTObject
from Kernel.Config.Context import Context


class Gumtree:
    __ctx: Context
    __url: str
    __product: GumtreeProductTObject
    __images: list

    def __init__(self, ctx: Context, url: str, sheetObj: PLEstateSheetTObject = None):
        self.__ctx = ctx
        self.__url = url
        self.__parsed: dict = {}
        self.__images = []
        self.sheetObj = sheetObj

    def start(self) -> str:
        try:
            browser.ChromeDriver.navigate(self.__url, 2)
            self.__ctx.XPATH.set_source(browser.ChromeDriver.driver().page_source)
            self.__accept_regulations()
            self.__initialize_slider()
            return self.__extract_data()
        except Exception as ex:
            print(ex)
        return ""

    def __accept_regulations(self):
        """
        Accept regulations, cookies,
        and preloaded modals
        :return:
        """
        accept_btn = browser.Element.findElementByXpath(Selectors.ACCEPT_REGULATIONS)
        browser.Element.click(accept_btn)

    def __initialize_slider(self):
        browser.Javascript.execute_js('''document.querySelector('img[data-index="0"]').click()''')
        gallery_next_button = browser.Element.findElementByXpath(Selectors.GALLERY_NEXT)
        total_images = self.__ctx.XPATH.extract(Selectors.IMAGES_TOTAL)



        if total_images is not None:
            for i in range(int(total_images)):
                actual_image = browser.Element.findElementByCss(Selectors.GALLERY_SELECTED)
                self.__images.append(actual_image.get_attribute('src'))
                browser.Element.click(gallery_next_button)
                time.sleep(2)

        browser.Javascript.execute_js(code=Selectors.GALLERY_CLOSE)

    def __extract_data(self) -> str:
        self.__parsed["TITLE"] = self.__ctx.XPATH.extract(Selectors.TITLE)
        self.__parsed["IMAGES"] = self.__images
        self.__parsed["PRICE"] = self.__ctx.XPATH.extract(Selectors.PRICE)
        self.__parsed["LOCATION"] = LIST.list_to_str(self.__ctx.XPATH.extract(Selectors.LOCATION))
        self.__parsed["MEASUREMENT"] = self.__ctx.XPATH.extract(Selectors.MEASUREMENT)
        self.__parsed["ROOMS_AMOUNT"] = self.__ctx.XPATH.extract(Selectors.ROOMS_AMOUNT)
        self.__parsed["DESCRIPTION"] = self.__ctx.XPATH.extract(Selectors.DESCRIPTION)
        self.__parsed["PHONE_NUMBER"] = self.__ctx.XPATH.extract(Selectors.PHONE_NUMBER)
        self.__parsed["CONTACT_DIGNITY"] = LIST.list_to_str(self.__ctx.XPATH.extract(Selectors.CONTACT_DIGNITY))

        return self.__export()

    def __export(self) -> str:
        obj = GumtreeProductTObject.TO(self.__ctx.JSON.dumps(self.__parsed))
        path = self.__ctx.Settings.GUMTREE_STORAGE + self.__ctx.FileSystem.sanitize_name(f"{obj.title}_{DATE().full_date}")

        if self.sheetObj:
            path = f'{self.__ctx.ESTATE_BASE}{self.sheetObj.city}{os.sep}{self.sheetObj.district}{os.sep}{self.sheetObj.street} {self.sheetObj.street_number} {self.sheetObj.price}{os.sep}'
            self.__ctx.FileSystem.path_creator(direction=path, create=True)

        self.__ctx.Logger.Print(0, self.__ctx.LogLevel.Success, self.__ctx.Texts.getText(12).format(path))

        if self.__ctx.FileSystem.create_dir(path, remove=True):
            template = Template(self.__ctx.Settings.DEFAULT_TEMPLATE)
            template.add_description(obj.description)
            template.add_measurement(obj.measurement)
            template.add_rooms_amount(obj.rooms_amount)
            template.add_price(obj.price)
            template.add_phone_number(obj.phone_number)
            template.add_contact_dignity(obj.contact_dignity)
            template.add_link(self.__url)
            template.add_date(DATE().full_date)

            if self.sheetObj:
                template.add_attention(self.sheetObj.uwagi)
                template.add_percentage(self.sheetObj.prowizja)

            template.add_vendor_abbreviation(self.__ctx.Settings.VENDOR_ABBREVIATIONS["GUMTREE"])
            template.save(path)
            name_index: int = 0
            for index, image in enumerate(obj.images):
                name_index += 1
                self.__ctx.HTTP.download(url=image, path=f'{path}{os.sep}{str(name_index)}A.jpg')
            return path
        return ""
