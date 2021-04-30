"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 27.04.2021
 * Time: 22:59
 * Github: https://github.com/cod3venom
"""

from Kernel.Global import ctx


class Selectors:
    ACCEPT_REGULATIONS = ctx.Settings.OTODOM_SELECTORS["ACCEPT_REGULATIONS"]
    TITLE = ctx.Settings.OTODOM_SELECTORS["TITLE"]
    SCROLL_TO_GALLERY = ctx.Settings.OTODOM_SELECTORS["SCROLL_TO_GALLERY"]
    IMAGES_TOTAL = ctx.Settings.OTODOM_SELECTORS["IMAGES_TOTAL"]
    GALLERY_IMAGES = ctx.Settings.OTODOM_SELECTORS["GALLERY_IMAGES"]
    GALLERY_NEXT = ctx.Settings.OTODOM_SELECTORS["GALLERY_NEXT"]
    PRICE = ctx.Settings.OTODOM_SELECTORS["PRICE"]
    LOCATION = ctx.Settings.OTODOM_SELECTORS["LOCATION"]
    MEASUREMENT = ctx.Settings.OTODOM_SELECTORS["MEASUREMENT"]
    ROOMS_AMOUNT = ctx.Settings.OTODOM_SELECTORS["ROOMS_AMOUNT"]
    PHONE_NUMBER = ctx.Settings.OTODOM_SELECTORS["PHONE_NUMBER"]
    PHONE_BUTTON = ctx.Settings.OTODOM_SELECTORS["PHONE_BUTTON"]
    CONTACT_DIGNITY = ctx.Settings.OTODOM_SELECTORS["CONTACT_DIGNITY"]
    DESCRIPTION = ctx.Settings.OTODOM_SELECTORS["DESCRIPTION"]