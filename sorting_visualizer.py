#!/usr/bin/env python3.11.6
from modules.engine import SortingVisualizer

def main():
    sorting = SortingVisualizer()

    # Starts performance measurement.
    with sorting.utils.timer('total'):
        sorting.run()


if __name__ == '__main__':
    main()
