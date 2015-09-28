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

    def test_simulate_raids(self):
        plays1 = set()
        plays1.add(Play(['KL', 'BB', 'NS'], (Order(MARCH, value=0), Order(SUPPORT, value=0), Order(RAID))))
        plays2 = set()
        plays2.add(Play(['KW', 'SB', 'ShSe'], (Order(DEFEND, value=1), Order(RAID), Order(RAID))))

        map = Map()
        engine = Engine(map)
        map.set_armies('KL', BARATHEON, 0, 0, 1)
        map.set_armies('BB', BARATHEON, 2, 0, 0)
        map.set_armies('NS', BARATHEON, 1, 0, 0)
        map.set_armies('KW', MARTELL, 0, 1, 0)
        map.set_armies('SB', MARTELL, 1, 0, 0)
        map.set_armies('ShSe', MARTELL, 1, 0, 0)

        engine.simulate_2_players(LANNISTER, plays1, GREYJOY, plays2)

    def test_simulate_raids2(self):
        plays1 = set()
        plays1.add(Play(['KL', 'BB'], (Order(MARCH, value=0), Order(SUPPORT, value=0))))
        plays2 = set()
        plays2.add(Play(['KW', 'SB', 'ShSe'], (Order(DEFEND, value=1), Order(RAID), Order(RAID))))

        map = Map()
        engine = Engine(map)
        map.set_armies('KL', BARATHEON, 0, 0, 1)
        map.set_armies('BB', BARATHEON, 2, 0, 0)
        map.set_armies('KW', MARTELL, 0, 1, 0)
        map.set_armies('SB', MARTELL, 1, 0, 0)
        map.set_armies('ShSe', MARTELL, 1, 0, 0)

        engine.simulate_2_players(LANNISTER, plays1, GREYJOY, plays2)