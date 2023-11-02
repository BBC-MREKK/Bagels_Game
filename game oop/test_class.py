import unittest
from unittest.mock import patch
from game import BagelsGame

class TestBagelsGame(unittest.TestCase):
    def test_getSecretNum(self):
        game = BagelsGame(3, 10)
        secret_num = game.getSecretNum()
        self.assertTrue(secret_num.isdigit())
        self.assertEqual(len(secret_num), 3)

    def test_getClues(self):
        game = BagelsGame(3, 10)
        secret_num = "123"
        guess = "124"
        self.assertEqual(game.getClues(guess, secret_num), "Pico")

        guess = "134"
        self.assertEqual(game.getClues(guess, secret_num), "Pico Fermi")

        guess = "321"
        self.assertEqual(game.getClues(guess, secret_num), "Fermi Fermi Fermi")

        guess = "456"
        self.assertEqual(game.getClues(guess, secret_num), "Bagels")

if __name__ == "__main__":
    unittest.main()