"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 18:32
 * Github: https://github.com/cod3venom
"""
from DAO.MorizonProductTObject import MorizonProductTObject
from DataOperations.DATE import DATE
from DataOperations.LIST import LIST
from Kernel.Config.Context import Context
from Kernel.FileSystem.FileSystem import FileSystem
from Kernel.Global import browser
from Template.Template import Template
from Vendors.Morizon.Selectors import Selectors


class Morizon:
    __ctx: Context
    __url: str
    __product: MorizonProductTObject

    def __init__(self, ctx: Context, url: str):
        self.__ctx = ctx
        self.__url = url
        self.__parsed: dict = {}

    def start(self):
        browser.ChromeDriver.navigate(self.__url, 2)
        self.__ctx.XPATH.set_source(browser.ChromeDriver.driver().page_source)
        self.__accept_regulations()
        # self.__initialize_slider()
        self.__extract_data()

    def __accept_regulations(self):
        accept_btn = browser.Element.findElementByXpath(Selectors.ACCEPT_REGULATIONS)

        browser.Element.click(accept_btn)
        browser.Javascript.scroll_to_bottom(interval=1)
        browser.Javascript.scroll_to_top(interval=4)

    def __initialize_slider(self):
        browser.Javascript.scrollToElement(selector='''img[id="imageBig"]''', interval=2)

        gallery_next_button = browser.Element.findElementByXpath(Selectors.GALLERY_SHOW_NEXT)
        total_images = self.__ctx.XPATH.extract(Selectors.IMAGES_TOTAL)

        if total_images is not None:
            for i in range(1, int(total_images)):
                browser.Element.click(gallery_next_button)

    def __extract_data(self):
        self.__parsed["TITLE"] = self.__ctx.XPATH.extract(Selectors.TITLE)
        self.__parsed["IMAGES"] = self.__ctx.XPATH.extract(Selectors.IMAGES)
        self.__parsed["PRICE"] = self.__ctx.XPATH.extract(Selectors.PRICE)
        self.__parsed["LOCATION"] = self.__ctx.XPATH.extract(Selectors.LOCATION)
        self.__parsed["MEASUREMENT"] = self.__ctx.XPATH.extract(Selectors.MEASUREMENT)
        self.__parsed["ROOMS_AMOUNT"] = self.__ctx.XPATH.extract(Selectors.ROOMS_AMOUNT)
        self.__parsed["DESCRIPTION"] = LIST.list_to_str(self.__ctx.XPATH.extract(Selectors.DESCRIPTION))
        self.__parsed["PHONE_NUMBER"] = self.__ctx.XPATH.extract(Selectors.PHONE_NUMBER)
        self.__parsed["CONTACT_DIGNITY"] = self.__ctx.XPATH.extract(Selectors.CONTACT_DIGNITY)

        self.__export()

    def __export(self):

        obj = MorizonProductTObject.TO(self.__ctx.JSON.dict_to_str(self.__parsed))
        path = self.__ctx.Settings.MORIZON_STORAGE + f'''{obj.location.replace("'", '')}'''

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

            for image in obj.images:
                print(image)
