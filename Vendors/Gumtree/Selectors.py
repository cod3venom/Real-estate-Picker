"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 26.04.2021
 * Time: 11:27
 * Github: https://github.com/cod3venom
"""

from Kernel.Global import ctx


class Selectors:
    TITLE = ctx.Settings.GUMTREE_SELECTORS["TITLE"]
    PHONE_NUMBER = ctx.Settings.GUMTREE_SELECTORS["PHONE_NUMBER"]
    GALLERY_MAIN = ctx.Settings.GUMTREE_SELECTORS["GALLERY_MAIN"]
    GALLERY_SELECTED = ctx.Settings.GUMTREE_SELECTORS["GALLERY_SELECTED"]
    GALLERY_NEXT = ctx.Settings.GUMTREE_SELECTORS["GALLERY_NEXT"]
    GALLERY_CLOSE = ctx.Settings.GUMTREE_SELECTORS["GALLERY_CLOSE"]
    IMAGES_TOTAL = ctx.Settings.GUMTREE_SELECTORS["IMAGES_TOTAL"]
    PRICE = ctx.Settings.GUMTREE_SELECTORS["PRICE"]
    LOCATION = ctx.Settings.GUMTREE_SELECTORS["LOCATION"]
    MEASUREMENT = ctx.Settings.GUMTREE_SELECTORS["MEASUREMENT"]
    ROOMS_AMOUNT = ctx.Settings.GUMTREE_SELECTORS["ROOMS_AMOUNT"]
    CONTACT_DIGNITY = ctx.Settings.GUMTREE_SELECTORS["CONTACT_DIGNITY"]
    DESCRIPTION = ctx.Settings.GUMTREE_SELECTORS["DESCRIPTION"]
