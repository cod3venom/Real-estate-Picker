"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 27.04.2021
 * Time: 22:59
 * Github: https://github.com/cod3venom
"""

import json
import os
import time

from DAO.OtodomProductTObject import OtodomProductTObject
from DataOperations.DATE import DATE
from DataOperations.LIST import LIST
from Kernel.Config.Context import Context
from Kernel.Global import browser
from Template.Template import Template
from Vendors.Otodom.Selectors import Selectors
from selenium.webdriver.remote.webelement import WebElement


class Otodom:

    def __init__(self, ctx: Context, url: str):
        self.__ctx = ctx
        self.__url = url
        self.__parsed: dict = {}
        self.__images: list = []
        self.__obj: OtodomProductTObject

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
            self.__reveal_phone_number()
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
        """
        Slide to carousel main div,
        then choose images in loop and
        extract actually selected image link
        with xpath, after extraction, link will
        be added into the self.__images variable
        :return:
        """
        browser.Javascript.scrollToElement(Selectors.SCROLL_TO_GALLERY)
        time.sleep(2)

        total_images = self.__ctx.XPATH.extract(Selectors.IMAGES_TOTAL)

        if total_images is not None:
            for i in range(1, int(total_images)):
                time.sleep(1)
                browser.Javascript.execute_js(Selectors.GALLERY_NEXT)

        time.sleep(3)
        self.__images = browser.Javascript.execute_js(Selectors.GALLERY_IMAGES)
        return self.__images

    def __reveal_phone_number(self):
        button = browser.Element.findElementByXpath(Selectors.PHONE_BUTTON)
        browser.Element.click(button, 1)

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
        self.__parsed["DESCRIPTION"] = self.__ctx.XPATH.extract(Selectors.DESCRIPTION)
        self.__parsed["PHONE_NUMBER"] = str(self.__ctx.XPATH.extract(Selectors.PHONE_NUMBER)).replace(':', '')
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
        obj = OtodomProductTObject.TO(json.dumps(self.__parsed, indent=4))
        path = self.__ctx.Settings.OTODOM_STORAGE + self.__ctx.FileSystem.sanitize_name(f"{obj.phone_number}_{obj.contact_dignity}_{DATE().full_date}")
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