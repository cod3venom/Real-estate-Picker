"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 27.04.2021
 * Time: 21:33
 * Github: https://github.com/cod3venom
"""

from Kernel.Global import ctx


class Selectors:
    ACCEPT_REGULATIONS = ctx.Settings.DOMIPORTAL_SELECTORS["ACCEPT_REGULATIONS"]
    TITLE = ctx.Settings.DOMIPORTAL_SELECTORS["TITLE"]
    PHONE_NUMBER = ctx.Settings.DOMIPORTAL_SELECTORS["PHONE_NUMBER"]
    SCROLL_TO_GALLERY = ctx.Settings.DOMIPORTAL_SELECTORS["SCROLL_TO_GALLERY"]
    GALLERY_IMAGES = ctx.Settings.DOMIPORTAL_SELECTORS["GALLERY_IMAGES"]
    PRICE = ctx.Settings.DOMIPORTAL_SELECTORS["PRICE"]
    LOCATION = ctx.Settings.DOMIPORTAL_SELECTORS["LOCATION"]
    MEASUREMENT = ctx.Settings.DOMIPORTAL_SELECTORS["MEASUREMENT"]
    ROOMS_AMOUNT = ctx.Settings.DOMIPORTAL_SELECTORS["ROOMS_AMOUNT"]
    DESCRIPTION = ctx.Settings.DOMIPORTAL_SELECTORS["DESCRIPTION"]
