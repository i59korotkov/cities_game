import unittest
from game import Game


class MyTestCase(unittest.TestCase):
    def test_add_correct(self):
        G = Game(['Moscow'])
        G.add_player('Igor')
        self.assertTrue(G.add_city('Igor', 'Moscow'))

    def test_add_playernotexist(self):
        G = Game(['Moscow'])
        self.assertRaises(G.add_city('Igor', 'Moscow'), ValueError)

    def test_add_sitynotexist(self):
        G = Game(['Moscow'])
        G.add_player('Igor')
        self.assertFalse(G.add_city('Igor', 'MMOOSSCCOOWW'))

    def test_add_sitydoubles(self):
        G = Game(['Mathba, Amsterdam'])
        G.add_player('Igor')
        G.add_player('Ilya')
        G.add_city('Igor', 'Amsterdam')
        G.add_city('Ilya', 'Mathba')
        self.assertFalse(G.add_city('Igor', 'Amsterdam'))

    def test_add_wrongsequence(self):
        G = Game(['Mathba, Amsterdam'])
        G.add_player('Igor')
        G.add_player('Ilya')
        G.add_city('Igor', 'Amsterdam')
        self.assertFalse(G.add_city('Igor', 'Mathba'))


if __name__ == '__main__':
    unittest.main()
