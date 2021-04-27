"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 17:06
 * Github: https://github.com/cod3venom
"""

from selenium.webdriver.chrome.options import Options


class ChromiumConfig:

    def get_options(self, incognito: bool = False, app_mode: str = "", headless: bool = False):
        option = Options()
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--disable-extensions')
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_argument("--disable-blink-features=AutomationControlled")

        if incognito:
            option.add_argument('--incognito')

        if len(app_mode) > 3:
            option.add_argument("--app=" + app_mode)

        if headless:
            option.headless = True
            option.add_argument('disable-gpu')
        else:
            option.add_argument('window-size=1700,1500')
            #option.add_argument('--kiosk')
        return option

