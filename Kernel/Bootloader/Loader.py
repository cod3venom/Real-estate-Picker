"""
 * Project: Real-estate-Picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 4/29/2021
 * Time: 7:06 PM
 * Github: https://github.com/cod3venom
"""
from Kernel.Config.Context import Context
from Kernel.TCP.CommandParser import CommandParser


class Loader:
    __ctx: Context

    def __init__(self, ctx: Context, ipAddress: str, port: str):
        self.__ctx = ctx
        self.__ipAddress = ipAddress
        self.__port = int(port)
        self.__commandParser = CommandParser()

    def load(self):
        self.__ctx.tcpClient.set_ipaddress(self.__ipAddress)
        self.__ctx.tcpClient.set_port(self.__port)
        self.__ctx.tcpClient.connect()

        while self.__ctx.tcpClient.isConnected:
            if not self.__ctx.tcpClient.isConnected:
                break


            message: str = self.__ctx.tcpClient.receive_messages()
            if message:

                self.__commandParser.parse_header(message)

