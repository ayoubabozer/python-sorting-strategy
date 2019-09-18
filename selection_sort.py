from sort_algo import SortAlgo
from typing import List
from time import time

class SelectionSort(SortAlgo):
    """
        Selection sort algorithm class
    """

    def sort(self, lst : List) -> List:

        start = time()
        for i in range(len(lst)):
            minimum = i

            for j in range(i + 1, len(lst)):
                if lst[j] < lst[minimum]:
                    minimum = j

                    lst[minimum], lst[i] = lst[i], lst[minimum]
        end = time()

        print ("execution time = ", start - end)
        return lst
