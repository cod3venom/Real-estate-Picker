"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 27.04.2021
 * Time: 13:22
 * Github: https://github.com/cod3venom
"""
import json
import os
import time


from DAO.GratkaProductTObject import GratkaProductTObject
from DataOperations.DATE import DATE
from DataOperations.LIST import LIST
from Kernel.Config.Context import Context
from Kernel.Global import browser
from Template.Template import Template
from Vendors.Gratka.Selectors import Selectors


class Gratka:

    def __init__(self, ctx: Context, url: str):
        self.__ctx = ctx
        self.__url = url
        self.__parsed: dict = {}
        self.__images: list = []
        self.__obj: GratkaProductTObject

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

    def __initialize_slider(self) -> list:
        self.__ctx.XPATH.set_source(browser.ChromeDriver.driver().page_source)
        self.__images = self.__ctx.XPATH.extract(Selectors.GALLERY_IMAGES)
        return self.__images

    def __extract_data(self) -> str:
        """
        Parse chromedriver web page source code
        with predefined xpath selectors
        :return:
        """
        self.__ctx.XPATH.set_source(browser.ChromeDriver.driver().page_source)
        time.sleep(2)

        self.__parsed["TITLE"] = self.__ctx.XPATH.extract(Selectors.TITLE)
        self.__parsed["IMAGES"] = self.__images
        self.__parsed["PRICE"] = self.__ctx.XPATH.extract(Selectors.PRICE)
        self.__parsed["LOCATION"] = self.__ctx.XPATH.extract(Selectors.LOCATION)
        self.__parsed["MEASUREMENT"] = self.__ctx.XPATH.extract(Selectors.MEASUREMENT)
        self.__parsed["ROOMS_AMOUNT"] = self.__ctx.XPATH.extract(Selectors.ROOMS_AMOUNT)
        self.__parsed["DESCRIPTION"] = browser.Javascript.execute_js(Selectors.DESCRIPTION)
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
        obj = GratkaProductTObject.TO(json.dumps(self.__parsed, indent=4))
        path = self.__ctx.Settings.GRATKA_STORAGE + self.__ctx.FileSystem.sanitize_name(f"{obj.phone_number}_{obj.contact_dignity}_{DATE().full_date}")

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
            template.save(path)

            for index, image in enumerate(obj.images):
                self.__ctx.HTTP.download(url=image, path=f'{path}{os.sep}A{str(index)}.jpg')
            return path
        return ""


