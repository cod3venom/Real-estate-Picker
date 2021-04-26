"""
 * Project: RealEstate_picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 25.04.2021
 * Time: 16:09
 * Github: https://github.com/cod3venom
"""
from urllib.error import URLError

import requests as req
import requests.exceptions
from tqdm import tqdm
from colorama import Fore

from Kernel.FileSystem.FileSystem import FileSystem


class HttpClient:
    __session: req.Session
    __headers: dict = {
        "UserAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.3"}

    def __init__(self):
        pass

    def set_session(self, request):
        self.__session = request

    def get_session(self) -> requests.sessions:
        return self.__session

    def append_header(self, key: str, value):
        self.__session.headers[key] = value
        return self.__session.headers

    def get_headers(self):
        return self.__session.headers

    def post(self, url, data: dict) -> str:
        try:
            return self.get_session().post(url=url, data=data, headers=self.__headers).text
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.TooManyRedirects:
            pass
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def get(self, url: str, stream: bool = False):
        return self.get_session().get(url, headers=self.__headers, stream=stream)

    def download(self, url, path):
        try:
            binary = self.get(url=url, stream=True).content
            with open(path, 'wb') as writer:

                file_name = FileSystem().file_name_from_path(path)
                for i in tqdm(range(100), colour="BLUE", desc=f"Downloading : {file_name}"):
                    pass
                writer.write(binary)
                return path
        except Exception as ex:
            return None
