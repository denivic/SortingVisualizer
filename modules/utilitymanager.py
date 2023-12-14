# Standard modules
from time import perf_counter
from contextlib import contextmanager
from logging import setLoggerClass, getLogger

# Custom modules
from modules.logger import CustomLogger

class UtilityManager():
    def __init__(self):
        setLoggerClass(CustomLogger)
        self.logger = getLogger('__name__')
        self.logger.propagate = False  # Prevents duplicate console logs
    
    
    @contextmanager
    def timer(self, *args) -> None:
        """ 
            Contextmanager that measures runtime.
            Accepts `method`, which is an optional
            name you given to the piece you're timing.\n\n
            
            If `method = 'total'` then it is the total
            runtime of the snippet of code.
        """
        start = perf_counter()

        try:
            yield
        finally:
            runtime = f'{perf_counter() - start:.2f}'

            if 'total' in args:
                self.logger.info(f'Total execution time: {runtime} seconds')
            else:
                self.logger.info(f'Execution time for {args[0]}: {runtime} seconds')
