"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 22:42
 * Github: https://github.com/cod3venom
"""


class LIST:

    @staticmethod
    def list_to_str(dataset: list):
        ret_code: str = ''

        for item in dataset:
            item = str(item).replace('\n', '')
            ret_code += "%s \n" % item

        ret_code = ret_code.replace('[', '').replace(']', '').replace("'", '')
        return ret_code



    @staticmethod
    def str_to_lines(dataset: str) -> list:
        if "\n" in dataset:
            return dataset.split("\n")
        return []
