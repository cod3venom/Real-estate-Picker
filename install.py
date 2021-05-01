"""
 * Project: Real-estate-Picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 4/30/2021
 * Time: 8:24 PM
 * Github: https://github.com/cod3venom
"""
import os
storage = [
    "Storage" + os.sep + "Otodom",
    "Storage" + os.sep + "Olx",
    "Storage" + os.sep + "Morizon",
    "Storage" + os.sep + "Gumtree",
    "Storage" + os.sep + "Gratka",
    "Storage" + os.sep + "Domi",
    "Storage" + os.sep + "DomiPorta",

]
with open("requirements.txt", "r") as reader:
    content = reader.read()
    if "\n" in content:
        requirements = content.split("\n")
        for requirement in requirements:
            os.system(f"python3 -m pip install {requirement}")


for vendor in storage:
    os.mkdir(vendor)