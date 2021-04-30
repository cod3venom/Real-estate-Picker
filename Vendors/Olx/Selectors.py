"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 27.04.2021
 * Time: 10:32
 * Github: https://github.com/cod3venom
"""

from Kernel.Global import ctx


class Selectors:
    ACCEPT_REGULATIONS = ctx.Settings.OLX_SELECTORS["ACCEPT_REGULATIONS"]
    TITLE = ctx.Settings.OLX_SELECTORS["TITLE"]

    GALLERY_MAIN = ctx.Settings.OLX_SELECTORS["GALLERY_MAIN"]
    GALLERY_MAIN_CLICK = ctx.Settings.OLX_SELECTORS["GALLERY_MAIN_CLICK"]
    GALLERY_IMAGES = ctx.Settings.OLX_SELECTORS["GALLERY_IMAGES"]
    GALLERY_NEXT = ctx.Settings.OLX_SELECTORS["GALLERY_NEXT"]
    GALLERY_CLOSE = ctx.Settings.OLX_SELECTORS["GALLERY_CLOSE"]
    IMAGES_TOTAL = ctx.Settings.OLX_SELECTORS["IMAGES_TOTAL"]

    PRICE = ctx.Settings.OLX_SELECTORS["PRICE"]
    #LOCATION = ctx.Settings.OLX_SELECTORS["LOCATION"]
    MEASUREMENT = ctx.Settings.OLX_SELECTORS["MEASUREMENT"]
    ROOMS_AMOUNT = ctx.Settings.OLX_SELECTORS["ROOMS_AMOUNT"]
    PHONE_NUMBER = ctx.Settings.OLX_SELECTORS["PHONE_NUMBER"]
    PHONE_BUTTON = ctx.Settings.OLX_SELECTORS["PHONE_BUTTON"]
    CONTACT_DIGNITY = ctx.Settings.OLX_SELECTORS["CONTACT_DIGNITY"]
    DESCRIPTION = ctx.Settings.OLX_SELECTORS["DESCRIPTION"]
