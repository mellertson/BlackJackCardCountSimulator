from Game import Game
from ConfigFileManager import ConfigFileManager

class View:
    @classmethod
    def main(cls):
        """
        Get the game number from ConfigFileManager.
        Begin main loop.
            Instantiate Game object, passing it the game number.
            Execute Game.run() method
            If Game.run() returns 1, continue loop. Else, exit the program
        :return: none
        :rtype None:
        """
        rCode = Game.NEW_GAME
        while rCode == Game.NEW_GAME:
            cf = ConfigFileManager()
            game = Game(cf.gameNumber)
            rCode = game.run()

        return rCode