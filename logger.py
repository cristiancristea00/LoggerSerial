from logger_serial_parser import LoggerSerialParser
from logger_serial import LoggerSerial


def main():
    arguments = LoggerSerialParser().parse()
    with LoggerSerial(arguments.name, arguments.port, arguments.baudrate) as logger:
        logger.run()


if __name__ == '__main__':
    main()
