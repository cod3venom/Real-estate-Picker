"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 21:29
 * Github: https://github.com/cod3venom
"""

from datetime import datetime


class DATE:

    @property
    def day(self):
        return datetime.now().strftime("%Y-%m-%d")

    @property
    def time(self):
        return datetime.now().strftime("%H:%M:%S")

    @property
    def full_date(self):
        return f'{self.day} {self.time}'
