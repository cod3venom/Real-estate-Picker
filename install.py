"""
 * Project: Real-estate-Picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 4/30/2021
 * Time: 8:24 PM
 * Github: https://github.com/cod3venom
"""
import os

with open("requirements.txt", "r") as reader:
    content = reader.read()
    if "\n" in content:
        requirements = content.split("\n")
        for requirement in requirements:
            os.system(f"python3 -m pip install {requirement}")