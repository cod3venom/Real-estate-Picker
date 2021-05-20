"""
 * Project: Real-estate-Picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 5/20/2021
 * Time: 11:28 AM
 * Github: https://github.com/cod3venom
"""
import os

import xlrd


class Excel:

    def __init__(self):
        pass

    def get_content(self, path: str):
        if os.path.exists(path):
            return ""

    def read(self, path: str):
        wb = xlrd.open_workbook_xls(path)
        content = wb.read(0)
        print(content)
