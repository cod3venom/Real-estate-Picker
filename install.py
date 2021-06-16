"""
 * Project: Real-estate-Picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 4/30/2021
 * Time: 8:24 PM
 * Github: https://github.com/cod3venom
"""
import os
import subprocess
import sys

storage = [
    "Storage" + os.sep + "Otodom",
    "Storage" + os.sep + "Olx",
    "Storage" + os.sep + "Morizon",
    "Storage" + os.sep + "Gumtree",
    "Storage" + os.sep + "Gratka",
    "Storage" + os.sep + "Domy",
    "Storage" + os.sep + "DomiPorta",

]


cities = {
    "WARSZAWA":{
        "0": "Bemowo",
        "1": "Bialoleka",
        "2": "Bielany",
        "3": "Mokotow",
        "4": "Ochota",
        "5": "Praga Poludnie",
        "6": "Praga Polnoc",
        "7": "Rembertow",
        "8": "Srodmiescie",
        "9": "Targowek",
        "10": "Ursus",
        "11": "Ursynow",
        "12": "Wawer",
        "13": "Wesola",
        "14": "Wilanow",
        "15": "Wlochy",
        "16": "Wola",
        "17": "Zoliborz",
    }
}

# with open("requirements.txt", "r") as reader:
#     content = reader.read()
#     if "\n" in content:
#         requirements = content.split("\n")
#         for requirement in requirements:
#             os.system(f"python3 -m pip install {requirement}")


for vendor in storage:
    if not os.path.exists(vendor):
        os.mkdir(vendor)


env_base_path = input("Enter path for DATABASE folder > ")

if env_base_path != "":
    if os.path.exists(env_base_path):
        if env_base_path[len(env_base_path) - 1] != '\\':
            env_base_path += '\\'
        os.system(f'setx ESTATE_BASE {env_base_path}')

        for city in cities:
            city = city.upper()
            city_path = env_base_path + city + '\\'
            if not os.path.exists(city_path):
                os.mkdir(city_path)

            for district in cities[city]:
                district_path = city_path + cities[city][district].upper()
                if not os.path.exists(district_path):
                    os.mkdir(district_path)
