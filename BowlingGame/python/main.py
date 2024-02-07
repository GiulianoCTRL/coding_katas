import unittest


class Game:

    def __init__(self):
        self.rolls = []

    def roll(self, pins: int):
        if pins < 0 or pins > 10:
            raise ValueError("Pins out of range.")
        self.rolls.append(pins)

    def score(self):

        len_rolls = len(self.rolls)
        if len_rolls < 12:
            raise ValueError("Not enough rolls.")
        
        if len_rolls > 20:
            raise ValueError("Too many rolls.")

        score = 0
        index = 0
        for _frame in range(10):
            if self._is_strike(index):
                score += 10 + self.rolls[index + 1] + self.rolls[index + 2]
                index += 1
            elif self._is_spare(index):
                score += 10 + self.rolls[index + 2]
                index += 2
            else:
                score += self.rolls[index] + self.rolls[index + 1]
                index += 2
        return score

    def _is_spare(self, index: int):
        return self.rolls[index] + self.rolls[index + 1] == 10

    def _is_strike(self, index: int):
        return self.rolls[index] == 10


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_pins_appended_to_rolls(self):
        self.game.roll(5)
        self.assertEqual(self.game.rolls[-1], 5)

    def test_value_error_on_too_high_pins(self):
        self.assertRaises(ValueError, self.game.roll, 15)

    def test_value_error_on_too_low_pins(self):
        self.assertRaises(ValueError, self.game.roll, -5)

    def test_total_score_not_possible_below_12_rolls(self):
        self._roll_many([1 for _ in range(5)])
        self.assertRaises(ValueError, self.game.score)

    def test_total_score_not_possible_above_20_rolls(self):
        self._roll_many([1 for _ in range(25)])
        self.assertRaises(ValueError, self.game.score)

    def test_all_zeros_is_0_score(self):
        result = self._is_score_correct_for_same_pin_games(0, 20, 0)
        self.assertTrue(result[0], result[1])

    def test_all_strikes_is_300_score(self):
        result = self._is_score_correct_for_same_pin_games(10, 12, 300)
        self.assertTrue(result[0], result[1])

    def test_all_ones_is_20_score(self):
        result = self._is_score_correct_for_same_pin_games(1, 20, 20)
        self.assertTrue(result[0], result[1])

    def test_role_one_spare_and_5_scores_20(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(5)
        result = self._is_score_correct_for_same_pin_games(0, 17, 20)
        self.assertTrue(result[0], result[1])

    def _is_score_correct_for_same_pin_games(self, pins: int, rolls: int, score: int):
        self._roll_many([pins for _ in range(rolls)])
        result = self.game.score()
        return (
            result == score,
            f"result: {result}, expected: {score}\n rolls: {self.game.rolls}",
        )

    def _roll_many(self, rolls: list[int]):
        for pins in rolls:
            self.game.roll(pins)