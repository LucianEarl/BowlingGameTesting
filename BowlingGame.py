# Bowling Game
# Original author unknown
# Testing and revisions by Lucian
# 27/11/2020

class BowlingGame(object):
    """This is an instance of the bowling game

    Args:
        object (object): necessary for the construction of the class
    """

    def __init__(self):
        """The initial constructor, where the internal variables 'throws' and 'score' are assigned
        """

        self.throws = []
        self.score = 0

    def throw(self,pins):
        """This is where each throw in the game is processed

        Args:
            pins (int): how many pins were knocked over on this particular throw
        """

        self.throws.append(pins)

    def calculate_score(self):
        """Where each throw in the list of throws is assessed to calculate the final score, 
        allowing for the complicated scoring rules of bowling.
        """

        ball = 0
        for _ in range(10):
            if self.throws[ball]==10: # a strike is awarded
                self.score +=10 + self.throws[ball+1] + self.throws[ball +2]
                ball += 1
            elif self.throws[ball] + self.throws[ball+1] == 10: # a spare is awarded
                self.score += 10 + self.throws [ball +2]
                ball +=2
            else: # a standard throw
                self.score += self.throws[ball] + self.throws[ball + 1]
                ball += 2

