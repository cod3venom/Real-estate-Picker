"""
 * Project: Real-estate-Picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 4/29/2021
 * Time: 6:56 PM
 * Github: https://github.com/cod3venom
"""

import socket
import sys
import threading
import time

class TcpClient:
    __bufferSize: int = 20
    __isConnected: bool = False
    __ip_address: str
    __port: int
    __sock: socket



    @property
    def isConnected(self):
        return self.__isConnected

    def set_ipaddress(self, ip_address):
        self.__ip_address = ip_address

    def set_port(self, port):
        self.__port = port

    def connect(self):
        try:
            if not self.__isConnected:
                self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.__sock.connect((self.__ip_address, self.__port))
                self.__isConnected = True

        except socket.error as socKerr:
            self.__isConnected = False
            print(socKerr)



    def receive_messages(self):
        message: str = ""
        try:
            size = self.__sock.recv(self.__bufferSize).decode('utf-8')
            message = str(self.__sock.recv(int(size)).decode('utf-8'))
            print(f"Message > {message}")

        except Exception as ex:
            self.__isConnected = False
            pass

        return message

    def send_message(self, message, header: str = '') -> bool:
        if message is not None:
            if header != '':
                message = header + message
            message = str(message)
            messageBytes = message.encode('utf-8')
            self.__sock.send(messageBytes)
            return True
        return False
