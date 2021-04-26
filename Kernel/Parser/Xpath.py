"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 16:42
 * Github: https://github.com/cod3venom
"""
from lxml import html, etree


class Xpath:
    __source: html

    def set_source(self, source: str) -> html:
        self.__source = html.fromstring(source)
        return self.__source

    def get_source(self) -> str:
        return self.__source

    def extract(self, selector: str):

        try:
            if self.__source is not None and selector != '':
                return self.__source.xpath(selector)
            return None
        except etree.ParseError as parseError:
            print(parseError)
        except etree.XPathEvalError as xpathError:
            print(xpathError)
