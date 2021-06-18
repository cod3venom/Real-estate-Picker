"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 17:06
 * Github: https://github.com/cod3venom
"""
import os

from selenium.webdriver.chrome.options import Options
from Kernel.Bootloader.Args import Args
import Kernel.Global as global_config


class ChromiumConfig:
    def __init__(self):
        self.args = Args()
        self.args.sysArgvTOdict()
        self.ctx = global_config.ctx

    def get_options(self):
        option = Options()
        option.add_argument('--disable-dev-shm-usage')
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        option.add_argument("--disable-blink-features=AutomationControlled")
        option.add_argument('--enable-extensions')

        if self.args.keyExists('--incognito'):
            option.add_argument('--incognito')
        else:

            if self.args.keyExists('--default-profile'):
                pass
                # option.add_argument("user-data-dir=C:\\Users\\venom\\AppData\\Local\\Google\\Chrome\\User Data")
            else:
                option.add_argument(f"user-data-dir={os.getcwd() + os.sep}user_data_dir")

        if self.args.keyExists('--incognito'):
            option.add_argument("--app=" + self.args.getValueOf('--incognito'))

        if self.args.keyExists('--browser-mode'):
            if self.args.getValueOf('--browser-mode') == 'headless':
                option.headless = True
                option.add_argument('disable-gpu')
        else:
            option.add_argument('window-size=1700,1500')

        if self.args.keyExists('--adblock'):
            option.add_extension(self.ctx.Settings.ADBLOCKER_CRX)


        return option
