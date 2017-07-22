import unittest
from unittest.mock import patch
import builtins
from Game import Game


class Game_TestCase(unittest.TestCase):
    def test_game_class_exists(self):
        import Game
    def setUp(self):
        from Game import Game
        self.g = Game(5)
    def test_init(self):
        self.assertEqual(0, self.g.count)
        self.assertEqual(0, self.g.trueCount)
        self.assertEqual(2.0, self.g.betAmount)
        self.assertEqual(500.0, self.g.bankRoll)
        self.assertEqual(6, self.g.decks)
        self.assertEqual(0, self.g.wins)
        self.assertEqual(0, self.g.losses)
        self.assertEqual(0, self.g.ties)
        self.assertEqual(5, self.g.gameNumber)
    def test_run(self):
        self.assertEqual(0, self.g.QUIT_GAME)
    def test_printRoundSummary(self):
        pass
    def test_saveRoundSummary(self):
        pass

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
        """This unit test needs to be re-written because Game.run() was modified."""
        game = Game(1)
        rCode = game.run()
        self.assertIn(rCode, self.gameCodes, "Game.run() returned unexpected return code")
    def promptBet(self):
        """
        The promptBet method was deleted.
        I'm leaving this code here as a reference for how to mock user input in unit tests.
        """
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
    def test_storeUserInput_decks(self):
        # simulate user inputting a string = 'H'
        with patch.object(builtins, "input", create=True, return_value="H"):
            self.game.storeUserInput('decks')
        self.assertEqual(self.game.decks, 6, "Expected 6 (the default value) for user input 'H' for decks")

        # simulate user inputting a string = 'Hats are great!'
        with patch.object(builtins, "input", create=True, return_value="Hats are great!"):
            self.game.storeUserInput('decks')
        self.assertEqual(self.game.decks, 6, "Expected 6 (the default value) for user input 'Hats are great!' for decks")

        # simulate user inputting an empty value = ''
        with patch.object(builtins, "input", create=True, return_value=""):
            self.game.storeUserInput('decks')
        self.assertEqual(self.game.decks, 6, "Expected 6 (the default value) for user inputting an empty string for decks")

        # simulate user inputting an integer = 4
        with patch.object(builtins, "input", create=True, return_value="4"):
            self.game.storeUserInput('decks')
        self.assertEqual(self.game.decks, 4, "Expected 4 as user input for decks")

        # simulate user inputting a float = 4.0
        with patch.object(builtins, "input", create=True, return_value="4.0"):
            self.game.storeUserInput('decks')
        self.assertEqual(self.game.decks, 4, "Expected 4 as user input for decks")
    def test_storeUserInput_count(self):
        # simulate user inputting a string = 'H'
        with patch.object(builtins, "input", create=True, return_value="H"):
            self.game.storeUserInput('count')
        self.assertEqual(self.game.count, 0, "Expected 0 (the default value) for user input 'H' for count")

        # simulate user inputting a string = 'Hats are great!'
        with patch.object(builtins, "input", create=True, return_value="Hats are great!"):
            self.game.storeUserInput('count')
        self.assertEqual(self.game.count, 0, "Expected 0 (the default value) for user input 'Hats are great!' for count")

        # simulate user inputting an empty value = ''
        with patch.object(builtins, "input", create=True, return_value=""):
            self.game.storeUserInput('count')
        self.assertEqual(self.game.count, 0, "Expected 0 (the default value) for user inputting an empty string for count")

        # simulate user inputting an integer = 4
        with patch.object(builtins, "input", create=True, return_value="4"):
            self.game.storeUserInput('count')
        self.assertEqual(self.game.count, 4, "Expected 4 as user input for count")

        # simulate user inputting a float = 4.0
        with patch.object(builtins, "input", create=True, return_value="4.0"):
            self.game.storeUserInput('count')
        self.assertEqual(self.game.count, 4, "Expected 4 as user input for count")
    def test_storeUserInput_betAmount(self):
        # simulate user inputting a string = 'H'
        with patch.object(builtins, "input", create=True, return_value="H"):
            self.game.storeUserInput('betAmount')
        self.assertEqual(self.game.betAmount, 2.0, "Expected 2.0 (the default value) for user input 'H' for betAmount")

        # simulate user inputting a string = 'Hats are great!'
        with patch.object(builtins, "input", create=True, return_value="Hats are great!"):
            self.game.storeUserInput('betAmount')
        self.assertEqual(self.game.betAmount, 2.0, "Expected 2.0 (the default value) for user input 'Hats are great!' for count")

        # simulate user inputting an empty value = ''
        with patch.object(builtins, "input", create=True, return_value=""):
            self.game.storeUserInput('betAmount')
        self.assertEqual(self.game.betAmount, 2.0, "Expected 2.0 (the default value) for user inputting an empty string for count")

        # simulate user inputting an integer = 4
        with patch.object(builtins, "input", create=True, return_value="4"):
            self.game.storeUserInput('betAmount')
        self.assertEqual(self.game.betAmount, 4, "Expected 4 as user input for count")

        # simulate user inputting a float = 4.0
        with patch.object(builtins, "input", create=True, return_value="4.0"):
            self.game.storeUserInput('betAmount')
        self.assertEqual(self.game.betAmount, 4, "Expected 4 as user input for count")




