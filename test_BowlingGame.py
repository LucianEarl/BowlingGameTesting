# Bowling Game - Unit Testing
# Original Author unknown
# Revisions and additional tests by Lucian
# 27/11/2020

import unittest
from BowlingGame import BowlingGame

class BowlingGameTests(unittest.TestCase):
    """This class construct the functions needed for running the various unit tests.

    Args:
        unittest (module): imported functionality to allow for automated unit tests
    """

    def throw_many(self, game, number_of_times, pins):
        """This function allows multiple throws to be handled in sequence.

        Args:
            game (object): The particular game of bowling being tested
            number_of_times (int): How many throws were made
            pins (int): How many pins were knocked over in the throw
        """

        for _ in range(number_of_times):
            game.throw(pins)

    def test_all_gutters(self):
        """Run a unit test where every throw hits zero pins
        """

        game = BowlingGame()
        self.throw_many(game, 20 ,0 )
        game.calculate_score()
        self.assertEqual(game.score,0)

    def test_perfect_game(self):
        """Run a unit test where every throw hits every pin
        """

        game = BowlingGame()
        self.throw_many(game, 12, 10)
        game.calculate_score()
        self.assertEqual(game.score, 300)

    def test_all_ones(self):
        """Run a unit test where every throw hits one pin
        """

        game = BowlingGame()
        number_of_times = 20
        pins = 1
        self.throw_many(game, number_of_times, pins)
        game.calculate_score()
        self.assertEqual(game.score, 20)

    def test_different_throws (self):
        """Run a unit test where a variety of pins are hit
        """

        game = BowlingGame()
        game.throw(6)
        game.throw(0)
        game.throw(7)
        game.throw(0)
        game.throw(2)
        for _ in range(15):
            game.throw(0)
        game.calculate_score()
        self.assertEqual(game.score, 15)

    def test_for_spare(self):
        """Run a unit test where a spare is awarded (bonus points awarded after all 10 pins hit within two throws)
        """

        game = BowlingGame()
        game.throw(4)
        game.throw(6)
        game.throw(7)
        game.throw(0)
        for _ in range(16):
            game.throw(0)
        game.calculate_score()
        self.assertEqual(game.score, 24)

    def test_for_strike(self):
        """Run a unit test where a strike is awarded (bonus points are awarded following all 10 pins being hit)
        """

        game=BowlingGame()
        game.throw(10)
        game.throw(4)
        game.throw(2)
        self.throw_many(game, 17,0)
        game.calculate_score()
        self.assertEqual(game.score, 22)

    def test_strike_brief(self):
        """test another configuration that would grant a strike, as shown in the brief
        """

        game=BowlingGame()
        game.throw(10)
        game.throw(3)
        game.throw(6)
        self.throw_many(game, 17, 0)
        game.calculate_score()
        self.assertEqual(game.score, 28)

    def test_successive_strikes(self):
        """test for successive strikes calculating, as shown in the brief
        """

        game=BowlingGame()
        game.throw(10)
        game.throw(10)
        game.throw(4)
        game.throw(2)
        self.throw_many(game, 16, 0)
        game.calculate_score()
        self.assertEqual(game.score, 46)

    def test_sample_game(self):
        """testing an example game, with a mix of open frames, spares and strikes
        """
        game=BowlingGame()
        game.throw(10)
        game.throw(7)
        game.throw(3)
        game.throw(7)
        game.throw(2)
        game.throw(9)
        game.throw(1)
        game.throw(10)
        game.throw(10)
        game.throw(10)
        game.throw(2)
        game.throw(3)
        game.throw(6)
        game.throw(4)
        game.throw(7)
        game.throw(3)
        game.throw(3)
        game.calculate_score()
        self.assertEqual(game.score, 168)


if __name__ == "__main__":
    unittest.main(verbosity=2)