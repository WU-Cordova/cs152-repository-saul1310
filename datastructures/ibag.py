from abc import ABC, abstractmethod
from typing import Optional, TypeVar, Generic, Iterable

T = TypeVar('T')  # Generic type for items in the Bag

class IBag(ABC, Generic[T]):
    """
    Interface for a Bag (MultiSet) data structure.
    """

    @abstractmethod
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
       self.__Bag =[]
    
    @abstractmethod
    def add(self, item: T) -> None:
        """
        Adds an item to the Bag.

       
        
        Args:
            item (T): The item to add.

        Returns:
            None

        Raises:
            TypeError: If the item is None.

        Examples:
            >>> Bag: Bag[int] = Bag()
            >>> Bag.add(1)
            >>> Bag.add(2)
            >>> Bag.add(1)

            >>> Bag.count(1)
            2
            >>> Bag.count(2)
            1
            >>> Bag.add(None)
            TypeError: Item cannot be None
        """
        if T == None:
            raise TypeError(" this cant be Nonetype ")
        self.Bag.append(T)

        pass

    @abstractmethod
    def remove(self, item: T) -> None:
        """
        Removes one occurrence of the item from the Bag.
        
        Args:
            item (T): The item to remove.

        Returns:
            None

        Raises:
            ValueError: If the item is not present in the Bag.

        Examples:
            >>> Bag: Bag[int] = Bag()
            >>> Bag.add(1)
            >>> Bag.add(2)
            >>> Bag.add(1)

            >>> Bag.remove(1)
            >>> Bag.count(1)
            1
            >>> Bag.remove(1)
            >>> Bag.count(1)
            0
            >>> Bag.remove(1)
            ValueError: Item not found in Bag
        """
        self.Bag.remove(T)
        pass
    
    @abstractmethod
    def count(self, item: T) -> int:
        """
        Returns the number of occurrences of the item in the Bag.
        
        Args:
            item (T): The item to count.

        Returns:
            int: The number of occurrences of the item.

        Examples:
            >>> Bag: Bag[int] = Bag()
            >>> Bag.add(1)
            >>> Bag.add(2)
            >>> Bag.add(1)

            >>> Bag.count(1)
            2
            >>> Bag.count(2)
            1
            >>> Bag.count(3)
            0
        """
        return self.Bag.count(T)
        pass
    
    @abstractmethod
    def __len__(self) -> int:
        """
        Returns the total number of items in the Bag (including duplicates).
        
        Returns:
            int: The total number of items in the Bag.

        Examples:
            >>> Bag: Bag[int] = Bag()
            >>> Bag.add(1)
            >>> Bag.add(2)
            >>> Bag.add(1)

            >>> Bag.size()
            3
        """
        return len(self.Bag)
        pass
    
    @abstractmethod
    def distinct_items(self) -> Iterable[T]:
        """
        Returns an iterable of the distinct items in the Bag.
        
        Returns:
            Iterable[T]: An iterable of the distinct items in the Bag.
        """
        return set(self.Bag)
        pass
    
    @abstractmethod
    def __contains__(self, item: T) -> bool:
        """
        Checks if the Bag contains the specified item.
        
        Args:
            item (T): The item to check for.

        Returns:
            bool: True if the item is present in the Bag, False otherwise.

        Examples:
            >>> Bag: Bag[int] = Bag()
            >>> Bag.add(1)
            >>> Bag.add(2)
            >>> Bag.add(1)

            >>> Bag.contains(1)
            True
            >>> Bag.contains(2)
            True
            >>> Bag.contains(3)
            False
        """
        return T in self.Bag
        pass
    
    @abstractmethod
    def clear(self) -> None:
        """
        Removes all items from the Bag.
        """
        self.Bag.clear()
        pass
