from sort_algo import SortAlgo
from typing import List
from time import time

class BubbleSort(SortAlgo):
    """
        Bubble sort algorithm class.
    """

    def sort(self, lst : List) -> List:

        start = time()
        def swap(i, j):
            lst[i], lst[j] = lst[j], lst[i]

        n = len(lst)
        swapped = True

        x = -1
        while swapped:
            swapped = False
            x += 1
            for i in range(1, n-x):
                if lst[i-1] > lst[i]:
                    swap(i-1, i)
                    swapped = True

        end = time()

        print ("execution time = ", start - end)
        return lst
