from __future__ import annotations

from argparse import ArgumentParser, Namespace
from singleton import Singleton


class LoggerSerialParser(metaclass=Singleton):

    def __init__(self) -> None:
        self.parser = ArgumentParser(
            description='Script that logs data from a serial device', epilog='Made by Cristian Cristea - M70957 with LOVE <3', allow_abbrev=False)

        self.parser.add_argument(
            '-n', '--name', help='Name of the device connected', required=True, type=str, metavar='NAME')

        self.parser.add_argument(
            '-p', '--port', help='Port of the device connected', required=True, type=str, metavar='PORT')

        self.parser.add_argument(
            '-b', '--baudrate', help='Baudrate of the device connected', required=True, type=int, metavar='BAUDRATE')

        self.parser._actions[0].help = 'Show this help message and exit'

    @property
    def parser(self) -> ArgumentParser:
        return self.__parser

    @parser.setter
    def parser(self, parser: ArgumentParser) -> None:
        self.__parser = parser

    def parse(self) -> Namespace:
        return self.parser.parse_args()
