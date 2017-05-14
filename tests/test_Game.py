import unittest as ut

class Game_TestCase(ut.TestCase):
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
