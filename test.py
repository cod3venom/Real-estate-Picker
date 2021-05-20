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
from Kernel.FileSystem.FileSystem import FileSystem

path = r"C:\Users\venom\Desktop\BASE\WARSZAWA\BIELANY"
fs = FileSystem()

new = fs.path_creator(direction=path, create=True)
print(new)