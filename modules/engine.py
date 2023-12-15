from os import path, makedirs
from typing import Iterable, Optional
from logging import getLogger, setLoggerClass


class SortingVisualizer():
    from modules.algorithms import SortingAlgorithms
    from modules.constants import Constants, AlgorithmType
    from modules.utilitymanager import UtilityManager
    from modules.logger import SVLogger


    def __init__(self):
        setLoggerClass(SortingVisualizer.SVLogger)
        self.logger = getLogger('__name__')
        self.logger.propagate = False  # Prevents duplicate console logs

        # Initialize components.
        self.algorithms = self.SortingAlgorithms()
        self.utils = self.UtilityManager()

        # Create log folder if it doesn't exist.
        if not path.exists(self.Constants.LOG_PATH):
            makedirs(self.Constants.LOG_PATH)


    def run(self, data: Iterable[int], algorithm: int, order: str, visualize: Optional[bool] = None) -> None | Iterable[int]:
        # TODO: Add proper error handling.
        if data is None:
            raise NotImplementedError

        # TODO: Add proper error handling.
        if algorithm is None:
            raise NotImplementedError

        # TODO: Add proper error handling.
        # TODO: Add support for visualization.
        if visualize is None:
            visualize = False

        try:
            match algorithm:
                case self.AlgorithmType.SELECTION_SORT:
                    return self.algorithms.selection_sort(data, order)

                case self.AlgorithmType.BUBBLE_SORT:
                    return self.algorithms.bubble_sort(data, order)

                case self.AlgorithmType.INSERTION_SORT:
                    return self.algorithms.insertion_sort(data, order)

                case self.AlgorithmType.MERGE_SORT:
                    return self.algorithms.merge_sort(data, order)

                case self.AlgorithmType.QUICK_SORT:
                    return self.algorithms.quick_sort(data, order)

                case self.AlgorithmType.HEAP_SORT:
                    return self.algorithms.heap_sort(data, order)

                case self.AlgorithmType.COUNTING_SORT:
                    return self.algorithms.counting_sort(data, order)

                case self.AlgorithmType.RADIX_SORT:
                    return self.algorithms.radix_sort(data, order)

                case self.AlgorithmType.BUCKET_SORT:
                    return self.algorithms.bucket_sort(data, order)

                case self.AlgorithmType.BINGO_SORT:
                    return self.algorithms.bingo_sort(data, order)

                case self.AlgorithmType.SHELL_SORT:
                    return self.algorithms.shell_sort(data, order)
                case _:
                    self.logger.error(f'The algorithm {algorithm} is not recognized or supported.')
        except Exception as e:
            # TODO: Add proper excepton handling
            self.logger.error(e)