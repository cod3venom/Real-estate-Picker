"""
 * Project: Real-estate-Picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 5/20/2021
 * Time: 11:46 AM
 * Github: https://github.com/cod3venom
"""
import collections
import numpy as np
import json
import os

from DataOperations.JSON import JSON


from pyexcel_ods import get_data

class Ods:

    def __init__(self):
        self.__json = JSON()
        self.sheetJsonObj = {}
        self.sheetJsonStr = ""
        self.allColumns = []
        self.allRows = {}


    def read(self, path: str):
        if os.path.exists(path):
            all_sheets = get_data(path)
            if type(all_sheets) == collections.OrderedDict:
                self.sheetJsonStr = json.dumps(all_sheets)
                self.sheetJsonObj = json.loads(self.sheetJsonStr)

                for index, sheet in enumerate(self.sheetJsonObj):
                    data = self.sheetJsonObj[sheet]
                    for itemIndex, items in enumerate(data):
                        if itemIndex == 0:
                            self.allColumns = data[itemIndex]
                        else:
                            rows = data[itemIndex]
                            if len(rows) == len(self.allColumns):
                                jsonPack: dict = {}
                                for rowIndex, row in enumerate(rows):
                                    jsonPack[self.allColumns[rowIndex]] = row

                                self.allRows[itemIndex] = self.__json.dict_to_str(jsonPack)
        return self


    def select_records(self, keys: list):
        newRow = {}
        for index in self.allRows:
            items = json.loads(self.allRows[index])
            jsPack = {}
            for itemIndex, key in enumerate(items):
                for columnKey in keys:
                    if columnKey == key:
                        jsPack[columnKey] = items[key]
            newRow[index] = jsPack
        return newRow


    def dict_to_str(self, data: dict):
        return self.__json.dict_to_str(dataset=data)



