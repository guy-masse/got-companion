import unittest
import logging

from engine import *

# Enable DEBUG level logging for this class
logger = logging.getLogger()
#logger.setLevel(logging.DEBUG)


class TestEngine(unittest.TestCase):

    def test_Play_eq(self):
        p1 = Play(['X', 'Y', 'Z'], (ORDERS[0], ORDERS[1], ORDERS[2]))
        p2 = Play(['X', 'Y', 'Z'], (ORDERS[1], ORDERS[0], ORDERS[2]))
        self.assertTrue(p1 == p1)
        self.assertTrue(p1 == p2)

        s = set()
        s.add(p1)
        s.add(p1)

        self.assertTrue(len(s) == 1)
        s.add(p2)

        self.assertTrue(len(s) == 1)

    def test_simulate(self):
        plays1 = set()
        plays1.add(Play(['A', 'B'], (ORDERS[0], ORDERS[1])))
        plays2 = set()
        plays2.add(Play(['Y', 'Z'], (ORDERS[0], ORDERS[2])))

        map = Map()
        engine = Engine(map)

        engine.simulate_2_players(LANNISTER, plays1, GREYJOY, plays2)