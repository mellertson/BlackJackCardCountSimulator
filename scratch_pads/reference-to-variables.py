import builtins

class Game:
    def __init__(self):
        self._decks = 6
        self.vars = {'decks': [getattr(self, 'decksPrompt'), 'int'] }
    @property
    def decksPrompt(self):
        """String used to prompt user for # of decks"""
        return "Enter the # of decks or (Q) [{}]: ".format(self.decks)
    @property
    def decks(self):
        return self._decks
    @decks.setter
    def decks(self, value):
        self._decks = value

    def storeUserInput(self, varName):
        prompt = self.vars[varName][0]
        response = input(prompt)
        if response.upper() == 'Q':
            return 'Quit'
        elif response.isnumeric():
            setattr(self, varName, response)
        print("self.decks = {}".format(self.decks))
        return 'Continue'
    def run(self):
        while self.storeUserInput('decks') == 'Continue':
            pass

if __name__ == '__main__':
    game = Game()
    game.run()
