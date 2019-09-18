from typing import List
from abc import ABC, abstractmethod

class SortAlgo(ABC):
    """
        Abstract class for sorting algorithm.
    """

    @abstractmethod
    def sort(self) -> List:
        pass
