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
    ACCEPT_REGULATIONS = ctx.Settings.DOMIPORTA_SELECTORS["ACCEPT_REGULATIONS"]
    TITLE = ctx.Settings.DOMIPORTA_SELECTORS["TITLE"]
    PHONE_NUMBER = ctx.Settings.DOMIPORTA_SELECTORS["PHONE_NUMBER"]
    SCROLL_TO_GALLERY = ctx.Settings.DOMIPORTA_SELECTORS["SCROLL_TO_GALLERY"]
    GALLERY_IMAGES = ctx.Settings.DOMIPORTA_SELECTORS["GALLERY_IMAGES"]
    PRICE = ctx.Settings.DOMIPORTA_SELECTORS["PRICE"]
    LOCATION = ctx.Settings.DOMIPORTA_SELECTORS["LOCATION"]
    MEASUREMENT = ctx.Settings.DOMIPORTA_SELECTORS["MEASUREMENT"]
    ROOMS_AMOUNT = ctx.Settings.DOMIPORTA_SELECTORS["ROOMS_AMOUNT"]
    DESCRIPTION = ctx.Settings.DOMIPORTA_SELECTORS["DESCRIPTION"]
