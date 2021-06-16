"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 27.04.2021
 * Time: 14:33
 * Github: https://github.com/cod3venom
"""
import json
import os
import time

from DAO.DomyProductTObject import DomyProductTObject
from DAO.PLEstateSheetTObject import PLEstateSheetTObject
from DataOperations.DATE import DATE
from DataOperations.LIST import LIST
from Kernel.Config.Context import Context
from Kernel.Global import browser
from Template.Template import Template
from Vendors.Domy.Selectors import Selectors


class Domy:

    def __init__(self, ctx: Context, url: str, sheetObj: PLEstateSheetTObject = None):
        self.__ctx = ctx
        self.__url = url
        self.__parsed: dict = {}
        self.__images: list = []
        self.__obj: DomyProductTObject
        self.sheetObj = sheetObj

    def start(self) -> str:
        """
        This is the entry point for the every vendor module,
        basically the plan is always same.
        1) Accept regulations & cookies
        2) Interact with slider and extract selected image
        3) Extract elements by xpath
        4) Convert extracted data to DAO object
        5) Create output folder
        6) Push all data into the created folder
        :return:
        """
        try:
            browser.ChromeDriver.navigate(self.__url, 1)
            self.__ctx.XPATH.set_source(browser.ChromeDriver.driver().page_source)
            self.__accept_regulations()
            self.__remove_ad_banner()
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
        button = browser.Element.findElementByXpath(Selectors.ACCEPT_REGULATIONS)
        browser.Element.click(button)


    def __remove_ad_banner(self):
        browser.Javascript.execute_js(Selectors.REMOVE_TOP_AD_BANNER)

    def __initialize_slider(self):
        """
        Slide to carousel main div,
        then choose images in loop and
        extract actually selected image link
        with xpath, after extraction, link will
        be added into the self.__images variable
        :return:
        """
        # Scroll to gallery element
        browser.Javascript.scrollToElement(Selectors.SCROLL_TO_GALLERY)
        # Gallery full screen
        browser.Javascript.execute_js(Selectors.GALLERY_FULL_SCREEN, 2)

        total_images = self.__ctx.XPATH.extract(Selectors.IMAGES_TOTAL)
        time.sleep(2)
        next_btn = browser.Element.findElementByCss(Selectors.GALLERY_NEXT)
        if total_images is not None:
            # + 1 is important to keep clicking slider arrow
            # until it will achieve the last image
            for i in range(1, int(total_images) + 1):
                self.__ctx.XPATH.set_source(browser.ChromeDriver.driver().page_source)
                image = str(self.__ctx.XPATH.extract(Selectors.GALLERY_SELECTED))
                self.__images.append(image)

                browser.Element.click(next_btn)
                time.sleep(2)


    def __extract_data(self) -> str:
        """
        Parsed chromedriver web page source code
        with predefined xpath selectors
        :return:
        """
        self.__parsed["TITLE"] = self.__ctx.XPATH.extract(Selectors.TITLE)
        self.__parsed["IMAGES"] = self.__images
        self.__parsed["PRICE"] = self.__ctx.XPATH.extract(Selectors.PRICE)
        self.__parsed["LOCATION"] = self.__ctx.XPATH.extract(Selectors.LOCATION)
        self.__parsed["MEASUREMENT"] = self.__ctx.XPATH.extract(Selectors.MEASUREMENT)
        self.__parsed["ROOMS_AMOUNT"] = self.__ctx.XPATH.extract(Selectors.ROOMS_AMOUNT)
        self.__parsed["DESCRIPTION"] = LIST.list_to_str(self.__ctx.XPATH.extract(Selectors.DESCRIPTION))
        self.__parsed["PHONE_NUMBER"] = self.__ctx.XPATH.extract(Selectors.PHONE_NUMBER)
        self.__parsed["CONTACT_DIGNITY"] = self.__ctx.XPATH.extract(Selectors.CONTACT_DIGNITY)

        return self.__export()

    def __export(self) -> str:
        """
        Prepare parsed elements for exporting.
        Text based data will be converted into .txt file,
        and images just will be downloaded in the current vendors
        storage directory.
        :return:
        """
        obj = DomyProductTObject.TO(json.dumps(self.__parsed, indent=4))
        path = self.__ctx.Settings.DOMY_STORAGE + self.__ctx.FileSystem.sanitize_name(f"{obj.phone_number}_{obj.contact_dignity}_{DATE().full_date}")

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

            template.add_vendor_abbreviation(self.__ctx.Settings.VENDOR_ABBREVIATIONS["DOMY"])
            template.save(path)

            self.__ctx.HTTP.add_referer(self.__url)
            self.__ctx.HTTP.add_cookies('')
            name_index: int = 0
            for index, image in enumerate(obj.images):
                name_index += 1
                self.__ctx.HTTP.download(url=image, path=f'{path}{os.sep}{str(name_index)}A.jpg')
            return path
        return ""