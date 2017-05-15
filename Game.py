import ConfigFileManager as cfm

class UserPrompts:
    enterBet = "Enter"

class Game(object):
    NEW_GAME = 1
    QUIT_GAME = 0
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
        """
        Constructor
        :param gameNumber:
        :type gameNumber: int
        """
        self.count = 0
        self.trueCount = 0
        self.betAmount = 2.0
        self.bankRoll = 500.0
        self.decks = 6
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.gameNumber = gameNumber
    def promptBet(self):
        floatReceived = False
        prompt = "What is your bet? [Enter for ${}]: $".format(self.betAmount)
        while not floatReceived:
            response = input(prompt)
            if response.strip(' ') == '':
                return self.betAmount
            try:
                response = float(response)
                return response
            except ValueError:
                floatReceived = False

        return self.betAmount
    def printRoundHeaders(self):
        print("True Count\tBet\tBank Roll\tDecks")

    def run(self):
        # print headers for true count, count, bet, bank roll, and # of decks
        self.printRoundHeaders()

        return self.QUIT_GAME

    def printRoundSum(self):
        """Print a summary of the current hands."""
        pass

    def saveRoundSum(self):
        """Save the hand to a CSV file."""
        pass





