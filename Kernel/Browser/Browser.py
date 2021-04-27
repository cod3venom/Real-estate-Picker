"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 17:05
 * Github: https://github.com/cod3venom
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException, WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

import time

from urllib3.exceptions import MaxRetryError

from Kernel.Browser.Drivers.ChromiumConfig import ChromiumConfig
from Kernel.Config.Context import Context


class Browser:
    alive: bool = False

    ctx: Context

    def __init__(self, ctx: Context):
        self.ctx = ctx

        self.__chromeConfig = ChromiumConfig()
        self.__chromeDriver = ChromeDriver(parent=self,
                                           browser=webdriver.Chrome(executable_path=self.ctx.Settings.BINARY_PATH_LINUX,
                                                                    chrome_options=self.__chromeConfig.get_options(
                                                                        headless=False)))
        self.__element = Elements(self)
        self.__javascript = Javascript(self)

    def keepAlive(self):
        self.alive = True
        while self.alive:
            if not self.alive:
                break
            pass

    def stopAlive(self):
        self.alive = False

    def openNewTab(self, navigate: str = "", interval: int = 0):
        pass

    def refresh(self, interval: int = 0):
        if interval > 0:
            time.sleep(interval)

    @property
    def ChromeDriver(self):
        return self.__chromeDriver

    @property
    def Element(self):
        return self.__element

    @property
    def Javascript(self):
        return self.__javascript


class ChromeDriver:

    def __init__(self, parent: Browser, browser: webdriver.Chrome):
        self.__parent = parent
        self.__chromeDriver = browser

    def navigate(self, url: str, wait_for: int = 0):
        try:
            self.__chromeDriver.get(url)
            if wait_for > 0:
                time.sleep(wait_for)

            self.__parent.ctx.Logger.Print(0, self.__parent.ctx.LogLevel.Info, self.__parent.ctx.Texts.getText(1).format(url))
        except MaxRetryError:
            pass

    def driver(self) -> webdriver.Chrome:
        return self.__chromeDriver


class Elements:
    __parent: Browser

    def __init__(self, parent: Browser):
        self.__parent = parent

    def exists(self, target) -> bool:
        time.sleep(.4)
        try:
            self.__parent.ChromeDriver.driver().find_element_by_css_selector(target)
            return True
        except NoSuchElementException:
            return False

    def input(self, target: WebElement, value) -> WebElement:
        try:
            if type(target) == WebElement:
                target.send_keys(value)
        except ElementNotInteractableException:
            return target
        return target

    def click(self, target: WebElement, interval: int = 0) -> WebElement:
        try:
            if interval > 0:
                time.sleep(interval)
            if type(target) == WebElement:
                target.click()
                self.__parent.ctx.Logger.Print(0, self.__parent.ctx.LogLevel.Success, self.__parent.ctx.Texts.getText(2).format(str(target)))
        except ElementNotInteractableException:
            return target
        except ElementClickInterceptedException:
            return target
        except StaleElementReferenceException:
            return target
        except WebDriverException:
            return target
        return target

    def findElementByCss(self, target):
        try:
            element = self.__parent.ChromeDriver.driver().find_element_by_css_selector(target)
            if element:
                self.__parent.ctx.Logger.Print(0, self.__parent.ctx.LogLevel.Success, self.__parent.ctx.Texts.getText(3).format(str(element)))
                return element
        except NoSuchElementException:
            self.__parent.ctx.Logger.Print(0, self.__parent.ctx.LogLevel.Error, self.__parent.ctx.Texts.getText(4))
            return None

    def findElementsByCss(self, target) -> list:
        try:
            element = self.__parent.ChromeDriver.driver().find_elements_by_css_selector(target)
            if element:
                self.__parent.ctx.Logger.Print(0, self.__parent.ctx.LogLevel.Success, self.__parent.ctx.Texts.getText(3).format(str(element)))
        except NoSuchElementException:
            self.__parent.ctx.Logger.Print(0, self.__parent.ctx.LogLevel.Error, self.__parent.ctx.Texts.getText(4))
            return []

    def findElementByXpath(self, target):
        try:
            return self.__parent.ChromeDriver.driver().find_element_by_xpath(target)
        except NoSuchElementException:
            return None

    def findElementsByXpath(self, target) -> list:
        try:
            return self.__parent.ChromeDriver.driver().find_elements_by_xpath(target)
        except NoSuchElementException:
            return []

    def getElementPosition(self, target: WebElement) -> dict:
        if type(target) == WebElement:
            return target.location
        return {"x": 0, "y": 0}

    def setAttribute(self, target: WebElement, name: str, value: str = ""):
        self.__parent.ChromeDriver.driver().execute_script(f"arguments[0].setAttribute('{name}','{value}')", target)

    def getAttribute(self, target: WebElement, name: str):
        return self.__parent.ChromeDriver.driver().execute_script(f"arguments[0].getAttribute('{name}')", target)

    def clickAndInput(self, target: WebElement, value: str = "", interval: int = 0):
        self.click(target=target)
        if interval > 0:
            time.sleep(interval)
        if len(value) > 0:
            self.input(target=target, value=value)
        return target

    def hover(self, target: WebElement):
        return ActionChains(self.__parent.ChromeDriver.driver()).move_to_element(target).perform()


class Javascript:
    __parent: Browser

    def __init__(self, parent: Browser):
        self.__parent = parent

    def scroll_to_bottom(self, interval: int = 0):
        self.execute_bundleJS('ScrollBottom')


    def scroll_to_top(self, interval: int = 0):
        self.execute_bundleJS('ScrollTop')

    def scrollToElement(self, selector: str, interval: int = 0):
        return self.execute_js(self.__parent.ctx.JsBundle.js_get('ScrollTo').replace('SELECTOR;', f"{selector}"),
                               interval=1)

    def execute_bundleJS(self, codeName: str, interval: int = 0):
        if self.__parent.ChromeDriver.driver() is not None:
            code = self.__parent.ctx.JsBundle.js_get(codeName)
            flag = self.execute_js(code=code, interval=interval)
            if len(flag) > 0:
                self.__parent.ctx.Logger.Print(0, self.__parent.ctx.LogLevel.Success, self.__parent.ctx.Texts.getText(5).format(str(codeName)))
            return flag

    def execute_js(self, code: str, *args, interval: int = 0):
        print(code)
        try:
            if self.__parent.ChromeDriver.driver() is not None:
                ret_code = self.__parent.ChromeDriver.driver().execute_script(code, args)
                if interval > 0:
                    time.sleep(interval)
                return ret_code
            return {}
        except StaleElementReferenceException:
            return {}
