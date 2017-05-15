import csv

class UserPrompts:
    enterBet = "Enter"

class Game(object):
    NEW_GAME = 1
    QUIT_GAME = 0
    """Game object.

    Keeps a record of the neccesary statistics for card counting in blackjack.

    Attributes:
        count: An integer describing the ratio between low cards (2-6) and
            high cards (10-A).
        trueCount: The count divided by the number of decks in play.
        betAmount: How much you want to bet. Minimum bet in casinos is usually
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
        self.count = 0
        self.trueCount = 0
        self.betAmount = 2.0
        self.bankRoll = 500.0
        self.decks = 6
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.gameNumber = gameNumber
        self.totalRounds = self.wins + self.losses + self.ties
        self.fileTitle = 'game-' + str(gameNumber) + '.csv'
        
        with open(self.fileTitle, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['True Count','Count','Bet Amount', 
                             'Bank Roll','Decks','Win Percentage',
                             'Loss Percentage','Tie Percentage'])
            # Write a blank line... I think
            writer.writerow(['','','','','','','',''])
            print('The file has been made!')

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

    def getPercentage(self, int):
        return float(int / (self.wins + self.losses + self.ties))


    def printRoundSummary(self):
        """Print a summary of the current hands."""
        summary = ('True Count: {} | Count: {} | Bet: ${:,.2f} | Bank Roll: '
                   '${:,.2f} | Decks Remaining: {} | Wins: {:.2%} | Losses: {:.2%} '
                   '| Ties: {:.2%}').format(self.trueCount, self.count,
                                            self.betAmount, self.bankRoll,
                                            self.decks,
                                            self.getPercentage(self.wins),
                                            self.getPercentage(self.losses),
                                            self.getPercentage(self.ties))
        title = '{:*^150}'.format('Current Round Summary')
        print(title)
        print(summary)

    def saveRoundSummary(self):
        """Save the hand to a CSV file."""
        with open(self.fileTitle, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([self.trueCount, self.count, self.betAmount,
                              self.bankRoll, self.decks,
                              self.getPercentage(self.wins),
                              self.getPercentage(self.losses),
                              self.getPercentage(self.ties)])



