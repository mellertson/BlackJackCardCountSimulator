import unittest
from Game import Game


class View_TestCase(unittest.TestCase):
    def test_view_class_exists(self):
        from View import View

    def test_main_method(self):
        from View import View
        view = View()
        rCode = view.main()
        self.assertEqual(rCode, Game.QUIT_GAME, "Bad return code from Game.run()")



