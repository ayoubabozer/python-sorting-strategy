from typing import List
from sort_algo import SortAlgo

class SortStrategy():
    """
        Strategy interface, using SortAlgo Composition.
    """

    def __init__(self, algo : SortAlgo) -> None:
        self.__algo = algo

    @property
    def algo(self) -> SortAlgo:
        return self.__algo

    @algo.setter
    def algo(self, algo : SortAlgo) -> None:
        self.__algo = algo

    def sort(self, lst : List) -> List:
        return self.__algo.sort(lst)
