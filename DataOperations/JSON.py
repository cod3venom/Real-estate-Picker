"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 21:04
 * Github: https://github.com/cod3venom
"""
import json


class JSON:

    def __init__(self):
        pass

    def dict_to_str(self, dataset: dict) -> str:
        ret_code: str = '{'
        for key in dataset.keys():
            ret_code += f'''"{key}": "{dataset[key]}", '''
        return ret_code[:-2] + "}"

    def dumps(self, dataset: dict):
        for key in dataset.keys():
            item = dataset[key]
            if type(item) == str:
                dataset[key] = str(dataset[key]).encode('utf-8').decode('utf-8')

        return json.dumps(dataset, indent=4)
