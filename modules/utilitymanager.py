# Standard modules
from time import perf_counter
from contextlib import contextmanager
from logging import setLoggerClass, getLogger

# Custom modules
from modules.logger import SVLogger

class UtilityManager():
    def __init__(self):
        setLoggerClass(SVLogger)
        self.logger = getLogger('__name__')
        self.logger.propagate = False  # Prevents duplicate console logs


    @contextmanager
    def timer(self, *args) -> None:
        """
            Contextmanager that measures runtime.
            Accepts `method`, which is an optional
            name given to the piece you're timing.\n\n

            If `method = 'total'` then it is the total
            runtime of the snippet of code.
        """
        start = perf_counter()

        try:
            yield
        finally:
            runtime = f'{perf_counter() - start:.6f}'

            if len(args) > 0:
                self.logger.info(f'Execution time for {args[0]}: {runtime} seconds')
            else:
                self.logger.info(f'Total execution time: {runtime} seconds')
