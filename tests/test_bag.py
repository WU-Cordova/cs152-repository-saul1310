import pytest

from datastructures.bag import Bag


@pytest.fixture
def bag():
    """Fixture to provide a fresh Bag instance for each test."""
    return Bag()


def test_add_item_increases_count(bag: Bag[int]):
    """Test adding an item increases the count of items in the bag."""
    bag.add(1)
    assert bag.count(1) == 1


def test_add_none_raises_type_error(bag: Bag[int]):
    """Test adding None raises a TypeError."""
    with pytest.raises(TypeError):
        bag.add(None)


def test_remove_item_decreases_count(bag: Bag[int]):
    """Test removing an item decreases its count in the bag."""
    bag.add(2)
    bag.add(2)
    bag.remove(2)
    assert bag.count(2) == 1


def test_remove_nonexistent_item_raises_value_error(bag: Bag[int]):
    """Test removing an item not in the bag raises a ValueError."""
    with pytest.raises(ValueError):
        bag.remove(3)


def test_count_returns_correct_number_of_occurrences(bag: Bag[int]):
    """Test count method returns the correct number of occurrences for an item."""
    bag.add(4)
    bag.add(4)
    bag.add(5)
    assert bag.count(4) == 2
    assert bag.count(5) == 1
    assert bag.count(6) == 0


def test_len_returns_total_number_of_items(bag: Bag[int]):
    """Test len method returns the total number of items, including duplicates."""
    bag.add(6)
    bag.add(7)
    bag.add(6)
    assert len(bag) == 3


def test_distinct_items_returns_unique_items(bag: Bag[int]):
    """Test distinct_items method returns only unique items."""
    bag.add(8)
    bag.add(8)
    bag.add(9)
    assert set(bag.distinct_items()) == {8, 9}


def test_contains_checks_item_membership(bag: Bag[int]):    
    """Test contains method correctly checks if an item is in the bag."""
    bag.add(10)
    assert 10 in bag
    assert 11 not in bag


def test_clear_removes_all_items(bag: Bag[int]):
    """Test clear method removes all items from the bag."""
    bag.add(12)
    bag.add(13)
    bag.clear()
    assert len(bag) == 0
    assert 12 not in bag
    assert 13 not in bag