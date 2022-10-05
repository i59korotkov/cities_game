import unittest
from game import Game


class MyTestCase(unittest.TestCase):
    def test_correct(self):
        G = Game()
        self.assertRaises(ValueError, G.add_player('Igor'))

    def test_wrong(self):
        G = Game()
        with self.assertRaises(ValueError):
            G.add_player('Igor')
            G.add_player('Igor')



if __name__ == '__main__':
    unittest.main()
