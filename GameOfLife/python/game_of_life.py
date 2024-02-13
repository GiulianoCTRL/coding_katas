import re
from typing import NamedTuple
import unittest

import pytest


class Coordinates(NamedTuple):
    y: int
    x: int


class GameOfLife:

    def __init__(self, size: int):
        self._size = size
        self._max_index = self._size - 1
        self._board = self._create_game_board()

    def get_board_from_str_or_empty_board(self, board_str: str):
        board_list = self._process_board_str(board_str)

        for y in range(self._size):
            for x in range(self._size):
                char = board_list[y][x]
                if char == '.':
                    self._board[y][x] = 0
                elif char == '*':
                    self._board[y][x] = 0
                else:
                    raise ValueError(f"{char} is not a valid character!")

    def print_board(self) -> None:
        print(self._get_board_as_str())

    def _process_board_str(self, board_str: str) -> list[list[chr]]:
        if self._is_board_game_valid_string(board_str):
            return list(re.findall(rf"[\.\*]{self._size}"))
        return ['.' * self._size] * self._size



    def _is_board_game_valid_string(self, board_str: str) -> bool:
        board_len = len(board_str)
        len_no_new_lines = pow(self._size, 2)
        len_all_newlines =  len_no_new_lines + self._size
        len_without_last_newline = len_no_new_lines + self._size - 1

        if not re.match(r"^[\.\*\\n]+$", board_str):
            return False

        if board_len == len_no_new_lines:
            return True
        if board_len == len_all_newlines:
            return True
        if board_len == len_without_last_newline:
            return True

        return False

    def _get_board_as_str(self) -> str:
        board_as_str = ""
        for y in self._board:
            for x in y:
                if x == 0:
                    board_as_str += "."
                else:
                    board_as_str += "*"
            board_as_str += "\n"
        return board_as_str

    def _create_game_board(self) -> list[list[int]]:
        return [([0] * self._size) for _ in range(self._size)]

    def _get_neighbour_count(self, cell: Coordinates) -> int:
        count = 0
        if self._is_neighbour_west_alive(cell):
            count += 1
        if self._is_neighbour_northwest_alive(cell):
            count += 1
        if self._is_neighbour_north_alive(cell):
            count += 1
        if self._is_neighbour_northeast_alive(cell):
            count += 1
        if self._is_neighbour_east_alive(cell):
            count += 1
        if self._is_neighbour_southeast_alive(cell):
            count += 1
        if self._is_neighbour_south_alive(cell):
            count += 1
        if self._is_neighbour_southwest_alive(cell):
            count += 1
        return count

    def _is_neighbour_west_alive(self, cell: Coordinates) -> bool:
        neighbour_x = self._get_checked_neighbour_index_lower(cell.x)
        return bool(self._board[cell.y][neighbour_x])

    def _is_neighbour_north_alive(self, cell: Coordinates) -> bool:
        neighbour_y = self._get_checked_neighbour_index_lower(cell.y)
        return bool(self._board[neighbour_y][cell.x])

    def _is_neighbour_east_alive(self, cell: Coordinates) -> bool:
        neighbour_x = self._get_checked_neighbour_index_upper(cell.x)
        return bool(self._board[cell.y][neighbour_x])

    def _is_neighbour_south_alive(self, cell: Coordinates) -> bool:
        neighbour_y = self._get_checked_neighbour_index_upper(cell.y)
        return bool(self._board[neighbour_y][cell.x])

    def _is_neighbour_northwest_alive(self, cell: Coordinates) -> bool:
        neighbour_x = self._get_checked_neighbour_index_lower(cell.x)
        neighbour_y = self._get_checked_neighbour_index_lower(cell.y)
        return bool(self._board[neighbour_y][neighbour_x])

    def _is_neighbour_northeast_alive(self, cell: Coordinates) -> bool:
        neighbour_x = self._get_checked_neighbour_index_upper(cell.x)
        neighbour_y = self._get_checked_neighbour_index_lower(cell.y)
        return bool(self._board[neighbour_y][neighbour_x])

    def _is_neighbour_southeast_alive(self, cell: Coordinates) -> bool:
        neighbour_x = self._get_checked_neighbour_index_upper(cell.x)
        neighbour_y = self._get_checked_neighbour_index_upper(cell.y)
        return bool(self._board[neighbour_y][neighbour_x])

    def _is_neighbour_southwest_alive(self, cell: Coordinates) -> bool:
        neighbour_x = self._get_checked_neighbour_index_lower(cell.x)
        neighbour_y = self._get_checked_neighbour_index_upper(cell.y)
        return bool(self._board[neighbour_y][neighbour_x])

    def _get_checked_neighbour_index_lower(self, index_cell: int) -> int:
        if index_cell != 0:
            return index_cell - 1
        return self._max_index

    def _get_checked_neighbour_index_upper(self, index_cell: int) -> int:
        if index_cell != self._max_index:
            return index_cell + 1
        return 0
