from pathlib import Path
from enum import Enum, StrEnum

class Constants(StrEnum):
    LOG_PATH = fr'{Path(__file__).parents[1]}\logs'


class AlgorithmType(Enum):
    SELECTION_SORT = 1
    BUBBLE_SORT = 2
    INSERTION_SORT = 3
    MERGE_SORT = 4
    QUICK_SORT = 5
    HEAP_SORT = 6
    COUNTING_SORT = 7
    RADIX_SORT = 8
    BUCKET_SORT = 9
    BINGO_SORT = 10
    SHELL_SORT = 11