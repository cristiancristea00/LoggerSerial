"""
Author: Cristian Cristea - M70957

Sumary: Class that parses the arguments of the script: the name of the
device, its port and baudrate and returns them as a Namespace object.
"""

from __future__ import annotations

from argparse import ArgumentParser
from argparse import Namespace


class LoggerSerialParser:
    """
    Class that parses the arguments of the script for the LoggerSerial class.
    """

    def __init__(self) -> None:
        """
        Initializes the parser and its arguments.
        """

        self.__parser: ArgumentParser = ArgumentParser(description='Script that logs data from a serial device',
                                                       epilog='Made by Cristian Cristea - M70957 with LOVE <3', allow_abbrev=False)

        self.__parser.add_argument('-n', '--name', help='Name of the connected device',
                                   required=True, type=str, metavar='NAME')

        self.__parser.add_argument('-p', '--port', help='Port of the connected device',
                                   required=True, type=str, metavar='PORT')

        self.__parser.add_argument('-b', '--baudrate', help='Baudrate of the connected device',
                                   required=True, type=int, metavar='BAUDRATE')

    @property
    def parser(self) -> ArgumentParser:
        """
        Gets the parser.

        Returns:
            ArgumentParser: The parser
        """
        return self.__parser

    @parser.setter
    def parser(self, parser: ArgumentParser) -> None:
        """
        Sets the parser and its arguments.

        Args:
            parser (ArgumentParser): The parser

        Raises:
            TypeError: If the parser is not an ArgumentParser instance
        """

        if not isinstance(parser, ArgumentParser):

            raise TypeError('The parser must be an ArgumentParser instance')

        self.__parser = parser

    def parse(self) -> Namespace:
        """
        Parses the arguments and returns them.

        Returns:
            Namespace: The arguments
        """

        return self.parser.parse_args()
