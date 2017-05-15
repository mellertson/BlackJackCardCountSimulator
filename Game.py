import ConfigFileManager as cfm

class Game(object):
    NEW_GAME = -1
    QUIT_GAME = -2
    INPUT_RECEIVED = -3

    """Construct a new <code>Game</code> object.
    
    Attributes:
        count: An integer describing the ratio between low cards (2-6) and
            high cards (10-A).
        trueCount: The count divided by the number of decks in play.
        betAmmount: How much you want to bet. Minimum bet in casinos is usually
            $2.00.
        bankRoll: The ammount of money left in the game. Default ammount is
            $500.00.
        decks: The number of decks that have not been played yet.
        wins: Number of times the player wins a hand.
        losses: Number of times the player loses a hand.
        ties: Number of times the player pushes a hand.
        gameNumber: How many blackjack simulations were run. Used in making the
            file name
    """
    def __init__(self, gameNumber):
        """Constructor"""
        self._count = 0
        self.trueCount = 0
        self.betAmount = 2.0
        self.bankRoll = 500.0
        self._decks = 6
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.gameNumber = gameNumber

        self.vars = {'decks': ['self.decksPrompt', 'int'],
                     'count': ['self.countPrompt', 'int']}

        # set to True to enable debug messages
        self.debug = True
    # decks prompt, getter and setter
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
    # count promprt, getter and setter
    @property
    def countPrompt(self):
        """String used to prompt user for card count"""
        return "Enter the count [{}]: ".format(self.count)
    @property
    def count(self):
        return self._count
    @count.setter
    def count(self, value):
        self._count = value
    def printRoundHeaders(self):
        print("True Count\tBet\tBank Roll\tDecks")
    def printRoundSummary(self):
        """Print a summary of the current hands."""
        print()
    def saveRoundSummary(self):
        """Save the hand to a CSV file."""
        pass

    """
    Dynamic user prompts and getting and storing user input
    """
    def getUserPrompt(self, varName):
        """Dynamically creates then outputs the user prompt for the given variable name"""
        return eval(self.vars[varName][0])
    def storeUserInput(self, varName):
        prompt = self.getUserPrompt(varName)
        response = input(prompt)
        if response.upper() == 'Q':
            return self.QUIT_GAME
        elif response.isnumeric():
            setattr(self, '_'+varName, response)
        if self.debug:
            print("{} = {}".format(varName, getattr(self, varName)))
        return self.INPUT_RECEIVED
    def run(self):
        # print headers for true count, count, bet, bank roll, and # of decks
        self.printRoundHeaders()

        while True:
            # ask user for # of decks or quit command (Q)
            if self.storeUserInput('decks') == self.QUIT_GAME:
                return self.QUIT_GAME

            # ask user for the count, system calculates true count automatically
            self.storeUserInput('count')

            # ask user to confirm bet amount

            # ask user if win (W) or loss (L)

            # if command = win (W)
                # add bet amount to bank roll
            # if command == lose (L)
                # subtract bet amount from bank roll

            # @ end of round, print the round summary
            # restart