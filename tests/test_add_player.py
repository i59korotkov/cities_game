import unittest
from game import Game


class MyTestCase(unittest.TestCase):
    def test_correct(self):
        G = Game()
        try:
            G.add_player('Igor')
        except ValueError:
            self.fail("raised ValueError unexpectedly!")

    def test_wrong(self):
        G = Game()
        with self.assertRaises(ValueError):
            G.add_player('Igor')
            G.add_player('Igor')



if __name__ == '__main__':
    unittest.main()
