"""
 * Project: Real-estate-Picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 6/18/2021
 * Time: 6:47 AM
 * Github: https://github.com/cod3venom
"""
import time

from selenium.webdriver.remote.webelement import WebElement

from Kernel.Global import browser, ctx, args
import pickle as pk

from Vendors.Olx.Selectors import Selectors


class Auth:

    def __init__(self, user_control: bool = False):
        self.user_control = user_control
        self.log_in()

    def log_in(self):

        if not self.is_logged:
            if args.keyExists('--olx-email') and args.keyExists('--olx-password'):

                email = args.getValueOf('--olx-email')
                password = args.getValueOf('--olx-password')


                browser.ChromeDriver.navigate(ctx.Settings.OLX_AUTH_PAGE)
                self.accept_regulations()

                if email != '' and password != '':
                    email_input = browser.Element.findElementByCss(Selectors.OLX_USER_EMAIL_INPUT)
                    password_input = browser.Element.findElementByCss(Selectors.OLX_USER_PASSWORD_INPUT)
                    google_recaptcha = browser.Element.findElementByCss(Selectors.OLX_CAPTCHA_BUTTON)
                    login_button = browser.Element.findElementByCss(Selectors.OLX_LOGIN_BUTTON)

                    if type(email_input) == WebElement and type(password_input) == WebElement:
                        browser.Element.input(target=email_input, value=email)
                        browser.Element.input(target=password_input, value=password)

                        if not self.user_control:
                            if type(google_recaptcha) == WebElement:
                                browser.Element.click(target=google_recaptcha, interval=3)

                                if type(login_button) == WebElement:
                                    browser.Element.click(target=login_button, interval=1)
                        else:
                            browser.ChromeDriver.wait_until_title_changes(interval=10)

        time.sleep(3)
        flag = self.is_logged

        if flag:
            ctx.Logger.Print(0, ctx.LogLevel.Success, ctx.Texts.getText(15).format("Olx"))
        else:
            ctx.Logger.Print(0, ctx.LogLevel.Success, ctx.Texts.getText(14).format("Olx"))

        return flag

    @property
    def is_logged(self):
        cookies = str(browser.ChromeDriver.driver().get_cookies())
        if "access_token" in cookies:
            return True
        return False

    def accept_regulations(self):
        """
        Accept regulations, cookies,
        and preloaded modals
        :return:
        """
        time.sleep(1)
        accept_btn = browser.Element.findElementByXpath(Selectors.ACCEPT_REGULATIONS)
        browser.Element.click(accept_btn)