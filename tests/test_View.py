import unittest


class View_TestCase(unittest.TestCase):
    def test_view_class_exists(self):
        from View import View

    def test_main_method_exists(self):
        from View import View
        view = View()
        view.main()



