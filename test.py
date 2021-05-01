"""
 * Project: Real-estate-Picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 5/1/2021
 * Time: 12:38 PM
 * Github: https://github.com/cod3venom
"""
import os
import sys

commands = [
    "python3 main.py vendor=DomiPorta file=links\\DomiPorta.txt",
    "python3 main.py vendor=Domy file=links\\domy.txt",
    "python3 main.py vendor=Gratka file=links\\gratka.txt",
    "python3 main.py vendor=Gumtree file=links\\gumtree.txt",
    "python3 main.py vendor=Morizon file=links\\morizon.txt",
    "python3 main.py vendor=Olx file=links\\olx.txt",
    "python3 main.py vendor=Otodom file=links\\otodom.txt",
]

mode = sys.argv[1]

for cmd in commands:
    os.system(cmd + " " + mode)

