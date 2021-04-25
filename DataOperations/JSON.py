"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 21:04
 * Github: https://github.com/cod3venom
"""


class JSON:

    def __init__(self):
        pass

    def dict_to_str(self, dataset: dict):
        ret_code: str = '{'
        for key in dataset.keys():
            ret_code += f'''"{key}": "{dataset[key]}", '''
        return ret_code[:-2] + "}"
