from typing import Iterable

class SortingAlgorithms():
    def __init__(self) -> None:
        pass


    def selection_sort(self, data: Iterable[int], order: str) -> Iterable[int]:
        """Sorts a list using the selection sort algorithm.

        Args:
            `data (Iterable[int])`: The iterable you want sorted.

        Returns:
            `Iterable[int]`: The given iterable but sorted.
        """
        sorted_data = data.copy()  # Don't want to alter the original.

        for i in range(len(sorted_data)):
            min_index = i

            for j in range(i + 1, len(sorted_data)):
                match order.lower():
                    case 'asc':
                        if sorted_data[j] < sorted_data[min_index]:
                            min_index = j
                    case 'desc':
                        if sorted_data[j] > sorted_data[min_index]:
                            min_index = j

            (sorted_data[i], sorted_data[min_index]) = (sorted_data[min_index], sorted_data[i])

        return sorted_data


    def bubble_sort(self, data: Iterable[int], order: str) -> Iterable[int]:
        """Sorts a list using the bubble sort algorithm.

        Args:
            `data (Iterable[int])`: The iterable you want sorted.

        Returns:
            `Iterable[int]`: The given iterable but sorted.
        """
        sorted_data = data.copy()

        for i in range(len(sorted_data)):
            for j in range(i + 1, len(sorted_data)):
                match order.lower():
                    case 'asc':
                        if sorted_data[i] > sorted_data[j]:
                            (sorted_data[i], sorted_data[j]) = (sorted_data[j], sorted_data[i])
                    case 'desc':
                        if sorted_data[i] < sorted_data[j]:
                            (sorted_data[i], sorted_data[j]) = (sorted_data[j], sorted_data[i])


        return sorted_data


    def insertion_sort(self, data: Iterable[int], order: str) -> Iterable[int]:
        """Sorts a list using the insertion sort algorithm.

        Args:
            `data (Iterable[int])`: The iterable you want sorted.

        Returns:
            `Iterable[int]`: The given iterable but sorted.
        """
        raise NotImplementedError


    def merge_sort(self, data: Iterable[int], order: str) -> Iterable[int]:
        """Sorts a list using the mergesort algorithm.

        Args:
            `data (Iterable[int])`: The iterable you want sorted.

        Returns:
            `Iterable[int]`: The given iterable but sorted.
        """
        raise NotImplementedError


    def quick_sort(self, data: Iterable[int], order: str) -> Iterable[int]:
        """Sorts a list using the quicksort algorithm.

        Args:
            `data (Iterable[int])`: The iterable you want sorted.

        Returns:
            `Iterable[int]`: The given iterable but sorted.
        """
        raise NotImplementedError


    def heap_sort(self, data: Iterable[int], order: str) -> Iterable[int]:
        """Sorts a list using the heapsort algorithm.

        Args:
            `data (Iterable[int])`: The iterable you want sorted.

        Returns:
            `Iterable[int]`: The given iterable but sorted.
        """
        raise NotImplementedError


    def counting_sort(self, data: Iterable[int], order: str) -> Iterable[int]:
        """Sorts a list using the counting sort algorithm.

        Args:
            `data (Iterable[int])`: The iterable you want sorted.

        Returns:
            `Iterable[int]`: The given iterable but sorted.
        """
        raise NotImplementedError


    def radix_sort(self, data: Iterable[int], order: str) -> Iterable[int]:
        """Sorts a list using the radix sort algorithm.

        Args:
            `data (Iterable[int])`: The iterable you want sorted.

        Returns:
            `Iterable[int]`: The given iterable but sorted.
        """
        raise NotImplementedError


    def bucket_sort(self, data: Iterable[int], order: str) -> Iterable[int]:
        """Sorts a list using the bucketsort algorithm.

        Args:
            `data (Iterable[int])`: The iterable you want sorted.

        Returns:
            `Iterable[int]`: The given iterable but sorted.
        """
        raise NotImplementedError


    def bingo_sort(self, data: Iterable[int], order: str) -> Iterable[int]:
        """Sorts a list using the bingosort algorithm.

        Args:
            `data (Iterable[int])`: The iterable you want sorted.

        Returns:
            `Iterable[int]`: The given iterable but sorted.
        """
        raise NotImplementedError


    def shell_sort(self, data: Iterable[int], order: str) -> Iterable[int]:
        """Sorts a list using the shell sort algorithm.

        Args:
            `data (Iterable[int])`: The iterable you want sorted.

        Returns:
            `Iterable[int]`: The given iterable but sorted.

        """
        raise NotImplementedError