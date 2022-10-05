import unittest
from game import Game


class TestCityIsValid(unittest.TestCase):
    def test_char_case(self):
        game = Game(['Moscow', 'Perm', 'Warsaw'])

        self.assertTrue(game.__city_is_valid('Moscow', 'waRSaw'))

    def test_spaces(self):
        game = Game(['Moscow', 'Perm', 'Warsaw'])

        self.assertTrue(game.__city_is_valid('Moscow', '   Warsaw   '))

    def test_repeating(self):
        game = Game(['Moscow', 'Perm', 'Warsaw'])

        self.assertTrue(game.__city_is_valid('Warsaw', 'Warsaw'))

    def test_diff_char(self):
        game = Game(['Moscow', 'Perm', 'Warsaw'])

        self.assertFalse(game.__city_is_valid('Moscow', 'Perm'))

    def test_city_not_in_list(self):
        game = Game(['Moscow', 'Perm', 'Warsaw'])

        self.assertFalse(game.__city_is_valid('Perm', 'Madrid'))
