import logging
from haggis import logs
from logging import handlers
from colorama import init, Fore
from constants import Constants

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


class CustomLogger(logging.Logger):
    def __init__(self, name: str):
        self.constants = Constants()
        logging.Logger.__init__(self, name, logging.DEBUG)

        # Formatting for console/file loggers
        console_formatter = ColorFormatter('[%(levelname)s] %(asctime)s - %(message)s', datefmt='%H:%M')
        file_formatter = logging.Formatter(fmt='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%Y-%m-%d | %H:%M')

        # Adds a custom logging level.
        logs.add_logging_level('STATUS', logging.DEBUG - 5)

        # Create a rotating file handler for seamless logging. See:  https://tinyurl.com/RotatingFilehandler
        self.fileHandler = handlers.RotatingFileHandler(filename=self.constants.LOG_PATH,
                                                        mode='w',
                                                        encoding='utf-8',
                                                        backupCount=10,
                                                        maxBytes=262_144, # 256 KB
                                                        delay=True)
        self.fileHandler.setFormatter(file_formatter) 
        self.addHandler(self.fileHandler)

        # Create the console handler.
        self.consoleHandler = logging.StreamHandler()
        self.consoleHandler.setFormatter(console_formatter)
        self.addHandler(self.consoleHandler)