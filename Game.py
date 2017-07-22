import csv

class Game(object):
    NEW_GAME = -1
    QUIT_GAME = 0
    INPUT_RECEIVED = -3

    """Construct a new game object.
    
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
        self._count = 0
        self.trueCount = 0
        self._betAmount = 2.0
        self.bankRoll = 500.0
        self._decks = 6
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self._winOrLoss = 'W or L'
        self.gameNumber = gameNumber
        self.totalRounds = self.wins + self.losses + self.ties
        self.fileTitle = 'game-' + str(gameNumber) + '.csv'
        self.vars = {'decks': ['self.decksPrompt', 'int'],
                     'count': ['self.countPrompt', 'int'],
                     'betAmount': ['self.betAmountPrompt', 'float'],
                     'winOrLoss': ['self.winOrLossPrompt', 'str']}

        # set to True to enable debug messages
        self.debug = False
        with open(self.fileTitle, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['True Count','Count','Bet Amount',
                             'Bank Roll','Decks','Win Percentage',
                             'Loss Percentage','Tie Percentage'])
            # Write a blank line... I think
            writer.writerow(['','','','','','','',''])
            if self.debug:
                print('The file has been made!')

    """
    Properties to prompt, get and set self.decks
    """
    @property
    def decksPrompt(self):
        """String used to prompt user for # of decks"""
        return "Enter the # of decks or (Q) [{}]: ".format(self.decks)
    @property
    def decks(self):
        return self._decks
    @decks.setter
    def decks(self, value):
        try:
            self._decks = int(float(value))
        except Exception:
            pass

    """
    Properties to prompt, get and set self.count
    """
    @property
    def countPrompt(self):
        """String used to prompt user for card count"""
        return "Enter the count [{}]: ".format(self.count)
    @property
    def count(self):
        return self._count
    @count.setter
    def count(self, value):
        try:
            self._count = int(float(value))
            self.trueCount = int((self._count / self.decks) + 0.5)
        except Exception:
            pass

    """
    Properties to prompt, get and set self.count
    """
    @property
    def betAmountPrompt(self):
        """String used to prompt user for bet amount"""
        return "Enter your bet [{}]: ".format(self.betAmount)
    @property
    def betAmount(self):
        return self._betAmount
    @betAmount.setter
    def betAmount(self, value):
        try:
            self._betAmount = float(value)
        except Exception:
            pass

    """
    Properties to prompt, get and set self.decks
    """
    @property
    def winOrLossPrompt(self):
        """String used to prompt user for win or loss"""
        return "Was it a win, loss, or push? [W, L, or P]: "
    @property
    def winOrLoss(self):
        return self._winOrLoss.upper()
    @winOrLoss.setter
    def winOrLoss(self, value):
        self._winOrLoss = str(value)[0].upper()
        if self._winOrLoss == 'W':
            self.wins += 1
        elif self._winOrLoss == 'L':
            self.losses += 1
        elif self._winOrLoss == 'P':
            self.ties += 1

    """
    Methods to output round data to screen and the CSV file"""
    def printRoundHeaders(self):
        print('True Count\tCount\tBet Amount\tBank Roll\tDecks\tWin Percentage\tLoss Percentage\tTie Percentage')
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

    """
    Methods to dynamically create user prompts, and dynamically get and store user input
    """
    def getUserPrompt(self, varName):
        """Dynamically creates then outputs the user prompt for the given variable name"""
        return eval(self.vars[varName][0])
    def storeUserInput(self, varName):
        prompt = self.getUserPrompt(varName)
        response = input(prompt)
        if response.upper() == 'Q':
            return self.QUIT_GAME
        elif varName == 'winOrLoss' and response not in ['W','L','P','w','l','p']:
            self.storeUserInput(varName)
        else:
            setattr(self, varName, response)
        if self.debug:
            print("{} = {}".format(varName, getattr(self, varName)))
        return self.INPUT_RECEIVED
    def run(self):
        # print headers for true count, count, bet, bank roll, and # of decks
        # self.printRoundHeaders()

        while True:
            # FIXME: if user inputs 'qw' it stores the value into the variable, but should ask for user input again.
            # ask user for # of decks or quit command (Q)
            if self.storeUserInput('decks') == self.QUIT_GAME:
                return self.QUIT_GAME

            # ask user for the count, system calculates true count automatically
            if self.storeUserInput('count') == self.QUIT_GAME:
                return self.QUIT_GAME

            # ask user to confirm bet amount
            if self.storeUserInput('betAmount') == self.QUIT_GAME:
                return self.QUIT_GAME

            # ask user if win (W) or loss (L)
            if self.storeUserInput('winOrLoss') == self.QUIT_GAME:
                return self.QUIT_GAME
            # if command = win (W)
            if self.winOrLoss == 'W':
                # add bet amount to bank roll
                self.bankRoll += self.betAmount
            # if command == lose (L)
            elif self.winOrLoss == 'L':
                # subtract bet amount from bank roll
                self.bankRoll -= self.betAmount

            # @ end of round, print the round summary and write round summary to the CSV file
            self.printRoundSummary()
            self.saveRoundSummary()

