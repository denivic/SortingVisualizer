# Standard
import logging
from os import path, makedirs
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
        self.check_log_folder()
        logs.add_logging_level('STATUS', logging.DEBUG - 5)

        # Adds a custom logging level.
        self.initialize_logger(LoggerType.FILE)
        self.initialize_logger(LoggerType.CONSOLE)


    def check_log_folder(self) -> None:
        """Creates the log folder if it doesn't already exist."""
        if not path.exists(Constants.LOG_PATH):
            makedirs(Constants.LOG_PATH)


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
                consolehandler = logging.StreamHandler()
                consolehandler.setFormatter(console_formatter)
                self.addHandler(consolehandler)
            case LoggerType.FILE:
                file_formatter = logging.Formatter(fmt='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%Y-%m-%d | %H:%M')

                # Create a rotating file handler for seamless logging.
                # See:  https://tinyurl.com/RotatingFilehandler
                filehandler = handlers.RotatingFileHandler(filename=f'{Constants.LOG_PATH}\SVLOG.log',
                                                           mode='w',
                                                           encoding='utf-8',
                                                           backupCount=10,
                                                           maxBytes=256_000, # 256 KB
                                                           delay=True)
                filehandler.setFormatter(file_formatter)
                self.addHandler(filehandler)
            case _:
                self.logger.error('Invalid value for "logger_type": {logger_type}')
                return""