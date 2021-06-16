"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 18:35
 * Github: https://github.com/cod3venom
"""
from Kernel.Browser.Browser import Browser
from Kernel.Config.Context import Context
from Kernel.Bootloader.Args import Args

ctx = Context()

args = Args()
args.sysArgvTOdict()

browser = Browser(ctx)
