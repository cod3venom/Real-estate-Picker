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


class TcpClient:
    __bufferSize: int = 20
    __isConnected: bool = False
    __ip_address: str
    __port: int
    __sock: socket

    __keepAliveThread: threading.Thread

    @property
    def isConnected(self):
        return self.__isConnected

    def set_ipaddress(self, ip_address):
        self.__ip_address = ip_address

    def set_port(self, port):
        self.__port = port

    def connect(self):
        try:
            self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__sock.connect((self.__ip_address, self.__port))
            self.__isConnected = True
            self.__keepAliveThread = threading.Thread(target=self.keepalive)
            self.__keepAliveThread.start()

        except Exception as ex:
            print(ex)

    def keepalive(self):
        pass
        # while self.__isConnected:
        #     if not self.__isConnected:
        #         break

    def receive_messages(self):
        message: str = ""
        try:
            size = self.__sock.recv(self.__bufferSize).decode('utf-8')
            message = self.__sock.recv(int(size)).decode('utf-8')
            print(f"MESSAGE : {str(message)}")
        except Exception:
            pass
        return message


    def send_message(self, message) -> bool:
        if message is not None:
            message = str(message)
            messageBytes = message.encode('utf-8')
            self.__sock.send(messageBytes)
            return True
        return False
