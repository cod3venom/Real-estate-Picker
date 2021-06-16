"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 17:06
 * Github: https://github.com/cod3venom
"""

from selenium.webdriver.chrome.options import Options
from Kernel.Bootloader.Args import Args
import Kernel.Global as global_config


class ChromiumConfig:
    def __init__(self):
        self.args = Args()
        self.args.sysArgvTOdict()
        self.ctx = global_config.ctx

    def get_options(self, incognito: bool = False, app_mode: str = "", headless: bool = False):
        option = Options()
        option.add_argument('--disable-dev-shm-usage')
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
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

        if self.args.keyExists('--adblock'):
            option.add_extension(self.ctx.Settings.ADBLOCKER_CRX)
        else:
            option.add_argument('--disable-extensions')

        return option
