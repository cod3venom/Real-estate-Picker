"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 19:08
 * Github: https://github.com/cod3venom
"""

from Kernel.Global import ctx


class Selectors:
    ACCEPT_REGULATIONS = ctx.Settings.MORIZON_SELECTORS["ACCEPT_REGULATIONS"]
    TITLE = ctx.Settings.MORIZON_SELECTORS["TITLE"]
    IMAGES = ctx.Settings.MORIZON_SELECTORS["IMAGES"]
    IMAGES_TOTAL = ctx.Settings.MORIZON_SELECTORS["IMAGES_TOTAL"]
    GALLERY_SHOW_NEXT = ctx.Settings.MORIZON_SELECTORS["GALLERY_SHOW_NEXT"]
    PRICE = ctx.Settings.MORIZON_SELECTORS["PRICE"]
    LOCATION = ctx.Settings.MORIZON_SELECTORS["LOCATION"]
    MEASUREMENT = ctx.Settings.MORIZON_SELECTORS["MEASUREMENT"]
    ROOMS_AMOUNT = ctx.Settings.MORIZON_SELECTORS["ROOMS_AMOUNT"]
    PHONE_NUMBER = ctx.Settings.MORIZON_SELECTORS["PHONE_NUMBER"]
    CONTACT_DIGNITY = ctx.Settings.MORIZON_SELECTORS["CONTACT_DIGNITY"]
    DESCRIPTION = ctx.Settings.MORIZON_SELECTORS["DESCRIPTION"]
