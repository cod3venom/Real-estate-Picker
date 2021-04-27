"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 27.04.2021
 * Time: 13:22
 * Github: https://github.com/cod3venom
"""

from Kernel.Global import ctx


class Selectors:
    ACCEPT_REGULATIONS = ctx.Settings.GRATKA_SELECTORS["ACCEPT_REGULATIONS"]
    TITLE = ctx.Settings.GRATKA_SELECTORS["TITLE"]
    PHONE_NUMBER = ctx.Settings.GRATKA_SELECTORS["PHONE_NUMBER"]
    GALLERY_IMAGES = ctx.Settings.GRATKA_SELECTORS["GALLERY_IMAGES"]
    PRICE = ctx.Settings.GRATKA_SELECTORS["PRICE"]
    LOCATION = ctx.Settings.GRATKA_SELECTORS["LOCATION"]
    MEASUREMENT = ctx.Settings.GRATKA_SELECTORS["MEASUREMENT"]
    ROOMS_AMOUNT = ctx.Settings.GRATKA_SELECTORS["ROOMS_AMOUNT"]
    CONTACT_DIGNITY = ctx.Settings.GRATKA_SELECTORS["CONTACT_DIGNITY"]
    DESCRIPTION = ctx.Settings.GRATKA_SELECTORS["DESCRIPTION"]
