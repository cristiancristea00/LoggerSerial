"""
Author: Cristian Cristea - M70957

Sumary: Class that logs data from a serial device by adding the current
date and time to each line and writing it to a log file and printing it.
"""

from __future__ import annotations

from datetime import datetime
from types import TracebackType
from typing import NoReturn
from typing import Optional
from typing import Type
from os import fsync
from io import TextIOWrapper
from serial import Serial


class LoggerSerial:
    """
    Class that logs data from a serial device.
    """

    def __init__(self, name: str, port: str, baudrate: int) -> None:
        """
        Initializes the logger by setting the name and its internal
        Serial instance.

        Args:
            name (str): The device name
            port (str): The device's serial port
            baudrate (int): The device's baudrate
        """

        self.name: str = name
        self.serial: Serial = Serial(port=port, baudrate=baudrate, timeout=1)

    @staticmethod
    def __add_timestamp(line: str) -> str:
        """
        Adds the current date and time to the line.

        Args:
            line (str): The line

        Returns:
            str: The line with the timestamp added
        """

        time = datetime.now().strftime('[%Y/%m/%d - %H:%M:%S]')
        line = F'{time} {line}\n'
        return line

    @property
    def name(self) -> str:
        """
        Gets the name of the device.

        Returns:
            str: The device name
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of the device and checks if it is a non-empty
        string.

        Args:
            name (str): The device name

        Raises:
            ValueError: If the name is not a non-empty string
        """

        if not isinstance(name, str) or not name:

            raise ValueError('The name must be a non-empty string')

        self.__name = name

    @property
    def serial(self) -> Serial:
        """
        Gets the internal Serial instance.

        Returns:
            Serial: The internal Serial instance
        """

        return self.__serial

    @serial.setter
    def serial(self, serial: Serial) -> None:
        """
        Sets the internal Serial instance and checks if it is a Serial
        instance.

        Args:
            serial (Serial): The internal Serial instance

        Raises:
            ValueError: If the serial is not a Serial instance
        """

        if not isinstance(serial, Serial):

            raise ValueError('The serial must be a Serial instance')

        self.__serial = serial

    @property
    def log_file(self) -> TextIOWrapper:
        """
        Gets the log file.

        Returns:
            TextIOWrapper: The log file
        """

        return self.__log_file

    @log_file.setter
    def log_file(self, value: TextIOWrapper) -> None:
        """
        Sets the log file and checks if it is a file object.

        Args:
            value (TextIOWrapper): The log file

        Raises:
            ValueError: If the log file is not a file object
        """

        if not isinstance(value, TextIOWrapper):

            raise ValueError('The log file must be a file object')

        self.__log_file = value

    def __enter__(self) -> LoggerSerial:
        file_time: str = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name: str = F'{self.name}_{file_time}.log'
        self.log_file = open(file_name, mode='a', encoding='UTF-8')
        return self

    def __exit__(self, exp_type: Optional[Type[BaseException]], value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> Optional[bool]:
        """
        Closes the serial port and the log file.

        Args:
            type (Optional[Type[BaseException]]): The exception type
            value (Optional[BaseException]): The exception
            traceback (Optional[TracebackType]): The traceback

        Returns:
            Optional[bool]: If the exception is None
        """

        self.serial.close()
        self.log_file.close()

        return exp_type is None

    def __read_line(self) -> str:
        """
        Reads a line from the serial port and returns it.

        Returns:
            str: The line
        """

        read_line: str = self.serial.readline().decode('UTF-8').strip()
        return read_line

    def __write_line(self, line: str) -> None:
        """
        Writes a line to the log file.

        Args:
            line (str): The line
        """

        self.log_file.write(line)
        self.log_file.flush()
        fsync(self.log_file)

    def __print_line(self, line: str) -> None:
        """
        Prints a line to the console.

        Args:
            line (str): The line
        """

        print(line, end='')

    def run(self) -> NoReturn:
        """
        Runs the logger.

        Returns:
            NoReturn
        """

        while True:
            line: str = self.__read_line()

            if not line:

                continue

            line = LoggerSerial.__add_timestamp(line)
            self.__write_line(line)
            self.__print_line(line)
