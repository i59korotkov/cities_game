import unittest
from game import Game


class MyTestCase(unittest.TestCase):
    def test_add_correct(self):
        G = Game(['Moscow'])
        G.add_player('Igor')
        self.assertTrue(G.add_city('Igor', 'Moscow'))

    def test_add_playernotexist(self):
        G = Game(['Moscow'])
        self.assertFalse(G.add_city('Igor', 'Moscow'))

    def test_add_sitynotexist(self):
        G = Game(['Moscow'])
        G.add_player('Igor')
        self.assertFalse(G.add_city('Igor', 'MMOOSSCCOOWW'))


if __name__ == '__main__':
    unittest.main()
