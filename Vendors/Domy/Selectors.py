"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 27.04.2021
 * Time: 14:33
 * Github: https://github.com/cod3venom
"""

from Kernel.Global import ctx


class Selectors:
    TITLE = ctx.Settings.DOMY_SELECTORS["TITLE"]
    IMAGES_TOTAL = ctx.Settings.DOMY_SELECTORS["IMAGES_TOTAL"]
    SCROLL_TO_GALLERY = ctx.Settings.DOMY_SELECTORS["SCROLL_TO_GALLERY"]
    GALLERY_SELECTED = ctx.Settings.DOMY_SELECTORS["GALLERY_SELECTED"]
    GALLERY_NEXT = ctx.Settings.DOMY_SELECTORS["GALLERY_NEXT"]
    PRICE = ctx.Settings.DOMY_SELECTORS["PRICE"]
    LOCATION = ctx.Settings.DOMY_SELECTORS["LOCATION"]
    MEASUREMENT = ctx.Settings.DOMY_SELECTORS["MEASUREMENT"]
    ROOMS_AMOUNT = ctx.Settings.DOMY_SELECTORS["ROOMS_AMOUNT"]
    PHONE_NUMBER = ctx.Settings.DOMY_SELECTORS["PHONE_NUMBER"]
    CONTACT_DIGNITY = ctx.Settings.DOMY_SELECTORS["CONTACT_DIGNITY"]
    DESCRIPTION = ctx.Settings.DOMY_SELECTORS["DESCRIPTION"]