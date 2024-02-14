"""Tests for Game of Life."""

# pylint: disable=protected-access
import random
import unittest

from game_of_life import Cell, GameOfLife


class TestGameBoard(unittest.TestCase):
    """Test game board related functions."""

    def test_game_board_initializes_with_correct_size(self):
        game = GameOfLife(8)
        self.assertEqual(len(game._board), 8)
        for row in game._board:
            self.assertEqual(len(row), 8)

    def test_game_board_initializes_with_0_value(self):
        game = GameOfLife(8)
        for row in game._board:
            for field in row:
                self.assertEqual(field, 0)


class TestPositiveNeighbourDetection(unittest.TestCase):
    """Test positive neighbour detection for cells."""

    def test_neighbour_west(self):
        game = GameOfLife(8)
        cell = Cell(1, 7)
        game._board[1][6] = 1
        self.assertTrue(game._is_neighbour_west_alive(cell))

    def test_neighbour_west_on_boundary(self):
        game = GameOfLife(8)
        cell = Cell(1, 0)
        game._board[1][-1] = 1
        self.assertTrue(game._is_neighbour_west_alive(cell))

    def test_neighbour_east(self):
        game = GameOfLife(8)
        cell = Cell(1, 6)
        game._board[1][7] = 1
        self.assertTrue(game._is_neighbour_east_alive(cell))

    def test_neighbour_east_on_boundary(self):
        game = GameOfLife(8)
        cell = Cell(1, 7)
        game._board[1][0] = 1
        self.assertTrue(game._is_neighbour_east_alive(cell))

    def test_neighbour_north(self):
        game = GameOfLife(8)
        cell = Cell(2, 1)
        game._board[1][1] = 1
        self.assertTrue(game._is_neighbour_north_alive(cell))

    def test_neighbour_north_on_boundary(self):
        game = GameOfLife(8)
        cell = Cell(1, 1)
        game._board[0][1] = 1
        self.assertTrue(game._is_neighbour_north_alive(cell))

    def test_neighbour_south(self):
        game = GameOfLife(8)
        cell = Cell(1, 1)
        game._board[2][1] = 1
        self.assertTrue(game._is_neighbour_south_alive(cell))

    def test_neighbour_south_on_boundary(self):
        game = GameOfLife(8)
        cell = Cell(7, 1)
        game._board[0][1] = 1
        self.assertTrue(game._is_neighbour_south_alive(cell))

    def test_neighbour_northwest(self):
        game = GameOfLife(8)
        cell = Cell(2, 2)
        game._board[1][1] = 1
        self.assertTrue(game._is_neighbour_northwest_alive(cell))

    def test_neighbour_northwest_on_boundary(self):
        game = GameOfLife(8)
        cell = Cell(0, 0)
        game._board[7][7] = 1
        self.assertTrue(game._is_neighbour_northwest_alive(cell))

    def test_neighbour_northeast(self):
        game = GameOfLife(8)
        cell = Cell(2, 2)
        game._board[1][3] = 1
        self.assertTrue(game._is_neighbour_northeast_alive(cell))

    def test_neighbour_northeast_on_boundary(self):
        game = GameOfLife(8)
        cell = Cell(0, 7)
        game._board[7][0] = 1
        self.assertTrue(game._is_neighbour_northeast_alive(cell))

    def test_neighbour_southeast(self):
        game = GameOfLife(8)
        cell = Cell(2, 2)
        game._board[3][3] = 1
        self.assertTrue(game._is_neighbour_southeast_alive(cell))

    def test_neighbour_southeast_on_boundary(self):
        game = GameOfLife(8)
        cell = Cell(7, 7)
        game._board[0][0] = 1
        self.assertTrue(game._is_neighbour_southeast_alive(cell))

    def test_neighbour_southwest(self):
        game = GameOfLife(8)
        cell = Cell(2, 2)
        game._board[3][1] = 1
        self.assertTrue(game._is_neighbour_southwest_alive(cell))

    def test_neighbour_southwest_on_boundary(self):
        game = GameOfLife(8)
        cell = Cell(7, 0)
        game._board[0][7] = 1
        self.assertTrue(game._is_neighbour_southwest_alive(cell))


class TestNegativeNeighbourDetection(unittest.TestCase):
    """Test negative neighbour detection (no false positives)."""

    def test_neighbour_not_west(self):
        game = GameOfLife(8)
        cell = Cell(1, 7)
        self.assertFalse(game._is_neighbour_west_alive(cell))

    def test_neighbour_not_west_on_boundary(self):
        game = GameOfLife(8)
        cell = Cell(1, 0)
        self.assertFalse(game._is_neighbour_west_alive(cell))

    def test_neighbour_not_east(self):
        game = GameOfLife(8)
        cell = Cell(1, 6)
        self.assertFalse(game._is_neighbour_east_alive(cell))

    def test_neighbour_not_east_on_boundary(self):
        game = GameOfLife(8)
        cell = Cell(1, 7)
        self.assertFalse(game._is_neighbour_east_alive(cell))

    def test_neighbour_not_north(self):
        game = GameOfLife(8)
        cell = Cell(2, 1)
        self.assertFalse(game._is_neighbour_north_alive(cell))

    def test_neighbour_not_north_on_boundary(self):
        game = GameOfLife(8)
        cell = Cell(1, 1)
        self.assertFalse(game._is_neighbour_north_alive(cell))

    def test_neighbour_not_south(self):
        game = GameOfLife(8)
        cell = Cell(1, 1)
        self.assertFalse(game._is_neighbour_south_alive(cell))

    def test_neighbour_not_south_on_boundary(self):
        game = GameOfLife(8)
        cell = Cell(7, 1)
        self.assertFalse(game._is_neighbour_south_alive(cell))

    def test_neighbour_not_northwest(self):
        game = GameOfLife(8)
        cell = Cell(2, 2)
        self.assertFalse(game._is_neighbour_northwest_alive(cell))

    def test_neighbour_not_northwest_on_boundary(self):
        game = GameOfLife(8)
        cell = Cell(0, 0)
        self.assertFalse(game._is_neighbour_northwest_alive(cell))

    def test_neighbour_not_northeast(self):
        game = GameOfLife(8)
        cell = Cell(2, 2)
        self.assertFalse(game._is_neighbour_northeast_alive(cell))

    def test_neighbour_not_northeast_on_boundary(self):
        game = GameOfLife(8)
        cell = Cell(0, 7)
        self.assertFalse(game._is_neighbour_northeast_alive(cell))

    def test_neighbour_not_southeast(self):
        game = GameOfLife(8)
        cell = Cell(2, 2)
        self.assertFalse(game._is_neighbour_southeast_alive(cell))

    def test_neighbour_not_southeast_on_boundary(self):
        game = GameOfLife(8)
        cell = Cell(7, 7)
        self.assertFalse(game._is_neighbour_southeast_alive(cell))

    def test_neighbour_not_southwest(self):
        game = GameOfLife(8)
        cell = Cell(2, 2)
        self.assertFalse(game._is_neighbour_southwest_alive(cell))

    def test_neighbour_not_southwest_on_boundary(self):
        game = GameOfLife(8)
        cell = Cell(7, 0)
        self.assertFalse(game._is_neighbour_southwest_alive(cell))


class TestNeighbourCounting(unittest.TestCase):
    """Test neighbours counted correctly."""

    def test_no_neighbours(self):
        game = GameOfLife(8)
        cell = Cell(3, 3)
        self.assertEqual(game._get_neighbour_count(cell), 0)

    def test_one_neighbour(self):
        game = GameOfLife(8)
        cell = Cell(3, 3)
        game._board[2][2] = 1
        self.assertEqual(game._get_neighbour_count(cell), 1)

    def test_two_neighbours(self):
        game = GameOfLife(8)
        cell = Cell(3, 3)
        game._board[2][2] = 1
        game._board[2][3] = 1
        self.assertEqual(game._get_neighbour_count(cell), 2)

    def test_three_neighbours(self):
        game = GameOfLife(8)
        cell = Cell(3, 3)
        game._board[2][2] = 1
        game._board[2][3] = 1
        game._board[2][4] = 1
        self.assertEqual(game._get_neighbour_count(cell), 3)

    def test_four_neighbours(self):
        game = GameOfLife(8)
        cell = Cell(3, 3)
        game._board[2][2] = 1
        game._board[2][3] = 1
        game._board[2][4] = 1
        game._board[3][2] = 1
        self.assertEqual(game._get_neighbour_count(cell), 4)

    def test_five_neighbours(self):
        game = GameOfLife(8)
        cell = Cell(3, 3)
        game._board[2][2] = 1
        game._board[2][3] = 1
        game._board[2][4] = 1
        game._board[3][2] = 1
        game._board[3][4] = 1
        self.assertEqual(game._get_neighbour_count(cell), 5)

    def test_six_neighbours(self):
        game = GameOfLife(8)
        cell = Cell(3, 3)
        game._board[2][2] = 1
        game._board[2][3] = 1
        game._board[2][4] = 1
        game._board[3][2] = 1
        game._board[3][4] = 1
        game._board[4][2] = 1
        self.assertEqual(game._get_neighbour_count(cell), 6)

    def test_seven_neighbours(self):
        game = GameOfLife(8)
        cell = Cell(3, 3)
        game._board[2][2] = 1
        game._board[2][3] = 1
        game._board[2][4] = 1
        game._board[3][2] = 1
        game._board[3][4] = 1
        game._board[4][2] = 1
        game._board[4][3] = 1
        self.assertEqual(game._get_neighbour_count(cell), 7)

    def test_eight_neighbours(self):
        game = GameOfLife(8)
        cell = Cell(3, 3)
        game._board[2][2] = 1
        game._board[2][3] = 1
        game._board[2][4] = 1
        game._board[3][2] = 1
        game._board[3][4] = 1
        game._board[4][2] = 1
        game._board[4][3] = 1
        game._board[4][4] = 1
        self.assertEqual(game._get_neighbour_count(cell), 8)

    def test_eight_neighbours_on_boundary(self):
        game = GameOfLife(8)
        cell = Cell(0, 0)
        game._board[0][1] = 1
        game._board[0][7] = 1
        game._board[1][0] = 1
        game._board[1][1] = 1
        game._board[1][7] = 1
        game._board[7][0] = 1
        game._board[7][1] = 1
        game._board[7][7] = 1
        self.assertEqual(game._get_neighbour_count(cell), 8)


class TestGameBoardString(unittest.TestCase):
    """Test conversion and parsing from game board to string works."""

    def test_all_cells_dead(self):
        game = GameOfLife(8)
        expected = (("." * 8) + "\n") * 8
        self.assertEqual(expected, game._get_board_as_str())

    def test_third_row_alive(self):
        game_size = 8
        game = GameOfLife(game_size)

        dead_row = ("." * 8) + "\n"
        alive_row = ("*" * 8) + "\n"
        expected = dead_row * 2 + alive_row + dead_row * 5

        for i in range(game_size):
            game._board[2][i] = 1

        self.assertEqual(expected, game._get_board_as_str())

    def test_reading_str_without_newlines(self):
        game_size = 8
        game = GameOfLife(game_size)
        input_str = "." * (game_size * game_size)
        game.get_board_from_str_or_empty_board(input_str)
        expected = [[0] * 8] * 8
        self.assertEqual(expected, game._board)

    def test_reading_str_with_all_newlines(self):
        game_size = 8
        game = GameOfLife(game_size)
        input_str = ("." * game_size + "\n") * game_size
        game.get_board_from_str_or_empty_board(input_str)
        expected = [[0] * game_size] * game_size
        self.assertEqual(expected, game._board)

    def test_reading_str_without_last_newline(self):
        game_size = 8
        game = GameOfLife(game_size)
        input_str = ("." * game_size + "\n") * game_size
        game.get_board_from_str_or_empty_board(input_str[:-1])
        expected = [[0] * game_size] * game_size
        self.assertEqual(expected, game._board)

    def test_reading_with_random_str(self):
        """Create list of board rows and randomly set cells to alive."""
        game_size = 8
        game = GameOfLife(game_size)
        input_list = [["."] * game_size] * game_size
        expected = [[0] * game_size] * game_size

        for i in range(game_size):
            for j in range(game_size):
                if random.random() > 0.90:
                    input_list[i][j] = "*"
                    expected[i][j] = 1
                else:
                    continue
        input_str = "".join([char for line in input_list for char in line])
        game.get_board_from_str_or_empty_board(input_str)
        self.assertEqual(expected, game._board)
