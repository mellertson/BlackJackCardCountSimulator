import unittest
from unittest.mock import patch
import builtins
from Game import Game

class Game_TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gameCodes = [Game.NEW_GAME, Game.QUIT_GAME]
    def setUp(self):
        self.game = Game(1)
    def test_init_method(self):
        game = Game(5)
        self.assertIsInstance(game, Game, "Expected Game object to be returned.")
    def test_run_method_return_code(self):
        game = Game(1)
        rCode = game.run()
        self.assertIn(rCode, self.gameCodes, "Game.run() returned unexpected return code")
    def test_promptBet(self):
        game = Game(1)

        # simulate user input = 4.0
        with patch.object(builtins, "input", create=True, return_value="4.0"):
            actual = game.promptBet()
        self.assertEqual(actual, 4.0, "Expected 4.0 as return value from Game.promptBet()")

        # simulate user input = 5.0
        with patch.object(builtins, "input", create=True, return_value="5.0"):
            actual = game.promptBet()
        self.assertEqual(actual, 5.0, "Expected 5.0 as return value from Game.promptBet()")

        # simulate user input = ''
        with patch.object(builtins, "input", create=True, return_value=""):
            actual = game.promptBet()
        self.assertEqual(actual, 2.0, "Expected 2.0 as default return value from Game.promptBet()")

        # simulate user input = ' '
        with patch.object(builtins, "input", create=True, return_value=" "):
            actual = game.promptBet()
        self.assertEqual(actual, 2.0, "Expected 2.0 as default return value from Game.promptBet()")