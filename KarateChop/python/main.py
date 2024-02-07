"""
In this kata five different implementations of the prosaic binary search
algorithm are to be implemented one new implementation each day. Start date: 2024-02-07.
"""
import typing

import pytest


def binary_search1(num: int, array: list[int]) -> int:
    size = len(array)

    if size == 0:
        raise ValueError("No elements in array")

    if size == 1:
        return 0

    first_index = 0
    last_index = size - 1
    cursor = last_index // 2
    mid_element = array[cursor]

    while True:
        if first_index == last_index and mid_element != num:
            raise ValueError("Item not found.")

        elif mid_element > num:
            last_index = cursor - 1

        elif mid_element < num:
            first_index = cursor + 1
            
        if mid_element == num:
            return cursor

        cursor = (first_index + last_index) // 2
        mid_element = array[cursor]
            

def binary_search2(num: int, array: list[int]) -> int:
    return binary_search1(num, array)

def binary_search3(num: int, array: list[int]) -> int:
    return binary_search1(num, array)

def binary_search4(num: int, array: list[int]) -> int:
    return binary_search1(num, array)

def binary_search5(num: int, array: list[int]) -> int:
    return binary_search1(num, array)

    

# see if index is item in the middle, if it is return index
# if it is not check if item is smaller or larger, move to the left/right depending on result
#

@pytest.mark.parametrize("binary_search", [binary_search1, binary_search2, binary_search3, binary_search4, binary_search5])
class TestBinarySeach:


    def test_value_not_in_array(self, binary_search: typing.Callable):
        with pytest.raises(ValueError):
            binary_search(3, [])
            binary_search(3, [])
            binary_search(2, [1, 3])
            binary_search(0, [1, 3, 5])
            binary_search(2, [1, 3, 5])
            binary_search(4, [1, 3, 5])
            binary_search(6, [1, 3, 5, 7])
            binary_search(0, [1, 3, 5, 7])
            binary_search(2, [1, 3, 5, 7])
            binary_search(4, [1, 3, 5, 7])
            binary_search(6, [1, 3, 5, 7])
            binary_search(8, [1, 3, 5, 7])

    def test_value_at_index_0(self, binary_search: typing.Callable):
        assert 0 == binary_search(1, [1])
        assert 0 == binary_search(1, [1, 3, 5])
        assert 0 == binary_search(1, [1, 3, 5, 7])

    def test_value_at_index_1(self, binary_search: typing.Callable):
        assert 1 == binary_search(3, [1, 3, 5])
        assert 1 == binary_search(3, [1, 3, 5, 7])

    def test_value_at_index_2(self, binary_search: typing.Callable):
        assert 2 == binary_search(5, [1, 3, 5])
        assert 2 == binary_search(5, [1, 3, 5, 7])

    def test_value_at_index_3(self, binary_search: typing.Callable):
        assert 3 == binary_search(7, [1, 3, 5, 7])
    
