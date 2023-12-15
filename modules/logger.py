# Standard
import logging
from enum import Enum
from logging import handlers

# Custom module
from modules.constants import Constants

# Third-party
from colorama import init, Fore
from haggis import logs

# Replaces ANSI escape squences with the Win32 equivalent sequences.
init(autoreset=True)

class ColorFormatter(logging.Formatter):
    COLORS = {
        'INFO': Fore.LIGHTGREEN_EX,
        'DEBUG': Fore.LIGHTMAGENTA_EX,
        'ERROR': Fore.LIGHTRED_EX,
        'STATUS': Fore.LIGHTCYAN_EX,
        'WARNING': Fore.LIGHTYELLOW_EX
    }

    def format(self, record) -> str:
        color = self.COLORS.get(record.levelname, '')

        if color:
            record.levelname = f'{color}{record.levelname:^8}{Fore.WHITE}'

        return logging.Formatter.format(self, record)


class LoggerType(Enum):
    CONSOLE = 1
    FILE = 2


class SVLogger(logging.Logger):
    def __init__(self, name: str):
        logging.Logger.__init__(self, name, logging.DEBUG)

        # Adds a custom logging level.
        logs.add_logging_level('STATUS', logging.DEBUG - 5)

        # Init
        self.initialize_logger(LoggerType.FILE)
        self.initialize_logger(LoggerType.CONSOLE)


    def initialize_logger(self, logger_type: LoggerType) -> None:
        """Initializes a logger by using one of the pre-defined
        logger types as an argument.

        Args:
            `logger_type (LoggerType)`: The type of logger to initialize.
        """
        match logger_type:
            case LoggerType.CONSOLE:
                console_formatter = ColorFormatter('[%(levelname)s] %(asctime)s - %(message)s', datefmt='%H:%M')

                # Create the console handler.
                consoleHandler = logging.StreamHandler()
                consoleHandler.setFormatter(console_formatter)
                self.addHandler(consoleHandler)
            case LoggerType.FILE:
                file_formatter = logging.Formatter(fmt='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%Y-%m-%d | %H:%M')

                # Create a rotating file handler for seamless logging.
                # See:  https://tinyurl.com/RotatingFilehandler
                fileHandler = handlers.RotatingFileHandler(filename=f'{Constants.LOG_PATH}\SVLOG.log',
                                                           mode='w',
                                                           encoding='utf-8',
                                                           backupCount=10,
                                                           maxBytes=262_144, # 256 KB
                                                           delay=True)
                fileHandler.setFormatter(file_formatter)
                self.addHandler(fileHandler)
            case _:
                self.logger.error('Invalid value for "logger_type": {logger_type}')
                return