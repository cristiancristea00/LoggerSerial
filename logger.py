"""
Author: Cristian Cristea - M70957

Sumary: Main script that runs the LoggerSerial class.
"""

from typing import NoReturn
from logger_serial_parser import LoggerSerialParser
from logger_serial import LoggerSerial


def main() -> NoReturn:
    """
    Main function that runs the LoggerSerial class.

    Returns:
        NoReturn
    """
    arguments_parser = LoggerSerialParser()
    arguments = arguments_parser.parse()
    with LoggerSerial(arguments.name, arguments.port, arguments.baudrate) as logger:
        logger.run()


if __name__ == '__main__':
    main()
