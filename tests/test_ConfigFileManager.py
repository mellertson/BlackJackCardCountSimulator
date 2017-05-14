import unittest
import os
# os.chdir('../')
# print("The current working directory is: {}".format(os.getcwd()))
from ConfigFileManager import ConfigFileManager as CF

class ConfigFileManager_TestCase(unittest.TestCase):
    def test_property_gameNumber_getter_and_setter(self):
        cf = CF()
        gameNumber = cf.gameNumber
        # verify getter returns an int
        self.assertIsInstance(gameNumber, int, "gameNumber getter should return an int")

        # increment gameNumber and save to the config file
        cf.gameNumber = gameNumber + 1
        self.assertEqual(cf.gameNumber, gameNumber+1,
                         "gameNumber setter expected {}, but got {}".format(gameNumber+1, cf.gameNumber))


