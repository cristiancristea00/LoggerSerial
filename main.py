from __future__ import annotations

from argparse import ArgumentParser
from datetime import datetime
from typing import NoReturn, TextIO
from serial import Serial
from os import fsync


class LoggerSerial:
    def __init__(self, name: str, port: str, baudrate: int) -> None:
        self.name = name
        self.serial = Serial(port, baudrate)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def serial(self) -> Serial:
        return self.__serial

    @serial.setter
    def serial(self, serial) -> None:
        self.__serial = serial

    @property
    def log_file(self) -> TextIO:
        return self.__log_file

    @log_file.setter
    def log_file(self, value: TextIO):
        self.__log_file = value

    def __enter__(self) -> LoggerSerial:
        self.log_file = open(F'{self.name}.log', mode='a', encoding='UTF-8')
        return self

    def __exit__(self) -> None:
        self.serial.close()
        self.log_file.close()

    def __read_line(self) -> str:
        read_line = self.serial.readline().decode('UTF-8').strip()
        time = datetime.now().strftime('[%d/%m/%Y - %H:%M:%S]')
        line = F'{time} {read_line}\n'
        return line

    def __write_file(self, line: str) -> None:
        self.log_file.write(line)
        self.log_file.flush()
        fsync(self.log_file)

    def __print_line(self, line: str) -> None:
        print(line, end='')

    def run(self) -> NoReturn:
        while True:
            line = self.__read_line()
            self.__write_file(line)
            self.__print_line(line)


def main():
    with LoggerSerial('AVR128DA48', 'COM4', 460800) as logger:
        logger.run()


if __name__ == '__main__':
    main()
