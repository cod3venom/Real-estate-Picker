"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 26.04.2021
 * Time: 11:27
 * Github: https://github.com/cod3venom
"""
import json
import time

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

    def __init__(self, ctx: Context, url: str):
        self.__ctx = ctx
        self.__url = url
        self.__parsed: dict = {}
        self.__images = []

    def start(self) -> str:
        browser.ChromeDriver.navigate(self.__url, 2)
        self.__ctx.XPATH.set_source(browser.ChromeDriver.driver().page_source)
        self.__initialize_slider()
        return self.__extract_data()

    def __initialize_slider(self):
        browser.Javascript.execute_js('''document.querySelector('img[data-index="0"]').click()''')
        gallery_next_button = browser.Element.findElementByXpath(Selectors.GALLERY_NEXT)
        total_images = self.__ctx.XPATH.extract(Selectors.IMAGES_TOTAL)

        if total_images is not None:
            for i in range(1, int(total_images)):
                browser.Element.click(gallery_next_button)
                time.sleep(3)
                actual_image = browser.Javascript.execute_js(code=Selectors.GALLERY_SELECTED)
                self.__images.append(actual_image)

        browser.Javascript.execute_js(code=Selectors.GALLERY_CLOSE)

    def __extract_data(self) -> str:
        self.__parsed["TITLE"] = self.__ctx.XPATH.extract(Selectors.TITLE)
        self.__parsed["IMAGES"] = self.__images
        self.__parsed["PRICE"] = self.__ctx.XPATH.extract(Selectors.PRICE)
        self.__parsed["LOCATION"] = LIST.list_to_str(self.__ctx.XPATH.extract(Selectors.LOCATION))
        self.__parsed["MEASUREMENT"] = self.__ctx.XPATH.extract(Selectors.MEASUREMENT)
        self.__parsed["ROOMS_AMOUNT"] = self.__ctx.XPATH.extract(Selectors.ROOMS_AMOUNT)
        self.__parsed["DESCRIPTION"] = LIST.list_to_str(self.__ctx.XPATH.extract(Selectors.DESCRIPTION))
        self.__parsed["PHONE_NUMBER"] = self.__ctx.XPATH.extract(Selectors.PHONE_NUMBER)
        self.__parsed["CONTACT_DIGNITY"] = LIST.list_to_str(self.__ctx.XPATH.extract(Selectors.CONTACT_DIGNITY))

        return self.__export()

    def __export(self) -> str:
        obj = GumtreeProductTObject.TO(self.__ctx.JSON.dumps(self.__parsed))
        path = self.__ctx.Settings.GUMTREE_STORAGE + self.__ctx.FileSystem.sanitize_name(f"{obj.title}_{DATE().full_date}")

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
                self.__ctx.HTTP.download(url=image, path=f'{path}//{str(index)}.jpg')
            return path
        return ""
