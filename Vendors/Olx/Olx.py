"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 27.04.2021
 * Time: 10:31
 * Github: https://github.com/cod3venom
"""

import json
import os
import time

from DAO.OlxProductTObject import OlxProductTObject
from DataOperations.DATE import DATE
from DataOperations.LIST import LIST
from Kernel.Config.Context import Context
from Kernel.Global import browser
from Template.Template import Template
from Vendors.Olx.Selectors import Selectors


class Olx:

    def __init__(self, ctx: Context, url: str):
        self.__ctx = ctx
        self.__url = url
        self.__parsed: dict = {}
        self.__images: list = []
        self.__obj: OlxProductTObject

    def start(self):
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
        browser.ChromeDriver.navigate(self.__url, 1)
        self.__ctx.XPATH.set_source(browser.ChromeDriver.driver().page_source)
        self.__accept_regulations()
        self.__initialize_slider()
        self.__reveal_phone_number()
        self.__extract_data()

    def __accept_regulations(self):
        """
        Accept regulations, cookies,
        and preloaded modals
        :return:
        """
        time.sleep(3)
        accept_btn = browser.Element.findElementByXpath(Selectors.ACCEPT_REGULATIONS)
        browser.Element.click(accept_btn)

    def __initialize_slider(self) -> list:
        """
        Slide to carousel main div,
        then choose images in loop and
        extract actually selected image link
        with xpath, after extraction, link will
        be added into the self.__images variable
        :return:
        """
        time.sleep(3)
        #open_gallery = browser.Element.findElementByCss(Selectors.GALLERY_MAIN)
        #browser.Element.click(open_gallery)

        self.__ctx.XPATH.set_source(browser.ChromeDriver.driver().page_source)
        self.__images = self.__ctx.XPATH.extract(Selectors.GALLERY_IMAGES)
        #browser.Javascript.execute_js(code=Selectors.GALLERY_CLOSE)
        return self.__images

    def __reveal_phone_number(self):
        button = browser.Element.findElementByXpath(Selectors.PHONE_BUTTON)
        browser.Element.click(button, 1)

    def __extract_data(self):
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
        self.__parsed["ROOMS_AMOUNT"] = str(self.__ctx.XPATH.extract(Selectors.ROOMS_AMOUNT)).replace('Liczba pokoi:', '').replace('pokoje', '')
        self.__parsed["DESCRIPTION"] = LIST.list_to_str(self.__ctx.XPATH.extract(Selectors.DESCRIPTION))
        self.__parsed["PHONE_NUMBER"] = browser.Javascript.execute_js(Selectors.PHONE_NUMBER)
        self.__parsed["CONTACT_DIGNITY"] = self.__ctx.XPATH.extract(Selectors.CONTACT_DIGNITY)

        self.__export()

    def __export(self):
        """
        Prepare parsed elements for exporting.
        Text based data will be converted into .txt file,
        and images just will be downloaded in the current vendors
        storage directory.
        :return:
        """
        obj = OlxProductTObject.TO(json.dumps(self.__parsed, indent=4))
        path = self.__ctx.FileSystem.sanitize_path(f"{self.__ctx.Settings.OLX_STORAGE}{obj.phone_number}_{obj.contact_dignity}_{DATE().full_date}")
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
                self.__ctx.HTTP.download(url=image, path=f'{path}{os.sep}{str(index)}.jpg')

