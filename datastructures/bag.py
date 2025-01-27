from typing import Dict, Iterable
from datastructures.ibag import IBag, T

class Bag(IBag[T]):
    def __init__(self, *items: T) -> None:
        self.__bag: Dict[T, int] = {}
        for item in items: self.add(item)

    def add(self, item: T) -> None:
        if item is None: raise TypeError("Item cannot be None")
        
        self.__bag[item] = self.__bag.get(item, 0) + 1
        
    def remove(self, item: T) -> None:
        if item not in self.__bag: raise ValueError(f"{item} not in bag")
        
        self.__bag[item] -= 1
        if self.__bag[item] == 0: del self.__bag[item]

    def count(self, item: T) -> int: return self.__bag.get(item, 0)

    def __len__(self) -> int: return sum(self.__bag.values())

    def distinct_items(self) -> Iterable[T]: return self.__bag.keys()

    def __contains__(self, item) -> bool: return item in self.__bag

    def clear(self) -> None: self.__bag.clear()