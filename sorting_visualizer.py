#!/usr/bin/env python3.11.6
from modules.engine import SortingVisualizer

def main():
    # TODO: Add support for CLI commands.
    # TODO: Add the visualization part of the SortingVisualizer. https://i.imgur.com/BiN4x0j.png
    sorting = SortingVisualizer()

    # Starts performance measurement.
    with sorting.utils.timer('total'):
        data = [6, 3, 0, 5]
        sorting.logger.info(f'Data: {data}')

        # Testing selection sort in an ascending manner
        sorted_data = sorting.run(data, sorting.AlgorithmType.BUBBLE_SORT, order='asc', visualize=False)
        sorting.logger.info(f'Sorted data asc: {sorted_data}')

        # Testing selection sort in a descending manner
        sorted_data = sorting.run(data, sorting.AlgorithmType.BUBBLE_SORT, order='desc', visualize=False)
        sorting.logger.info(f'Sorted data desc: {sorted_data}')

    sorting.logger.info('Exiting application now...')

if __name__ == '__main__':
    main()
