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

    def test_possible_plays(self):
        map = Map()
        engine = Engine(map)

        self.assertEqual(0, len(engine.possible_plays(TYRELL, 0)))

        map.set_armies('O', TYRELL, 0, 1, 0)
        possiblePlays = engine.possible_plays(TYRELL, 0)
        self.assertEquals(6, len(possiblePlays))
        possiblePlays = engine.possible_plays(TYRELL, 1)
        self.assertEquals(11, len(possiblePlays))
        possiblePlays = engine.possible_plays(TYRELL, 2)
        self.assertEquals(11, len(possiblePlays))
        possiblePlays = engine.possible_plays(TYRELL, 3)
        self.assertEquals(11, len(possiblePlays))

        map.remove_armies('O')
        self.assertEqual(0, len(engine.possible_plays(TYRELL, 0)))

        map.set_armies('L', LANNISTER, 0, 1, 0)
        self.assertEqual(0, len(engine.possible_plays(TYRELL, 0)))

    def test_simulate_raids(self):
        plays1 = set()
        plays1.add(Play([('KL', Armies(BARATHEON, 0, 0, 1)), ('BB', Armies(BARATHEON, 2, 0, 0)), ('NS', Armies(BARATHEON, 1, 0, 0))], (Order(MARCH, value=0), Order(SUPPORT, value=0), Order(RAID))))
        plays2 = set()
        plays2.add(Play([('KW', Armies(MARTELL, 0, 1, 0)), ('SB', Armies(MARTELL, 1, 0, 0)), ('ShSe', Armies(MARTELL, 1, 0, 0))], (Order(DEFEND, value=1), Order(RAID), Order(RAID))))

        map = Map()
        engine = Engine(map)

        engine.simulate_2_players(LANNISTER, plays1, GREYJOY, plays2)

    def test_simulate_raids2(self):
        plays1 = set()
        plays1.add(Play([('KL', Armies(BARATHEON, 0, 0, 1)), ('BB', Armies(BARATHEON, 2, 0, 0))], (Order(MARCH, value=0), Order(SUPPORT, value=0))))
        plays2 = set()
        plays2.add(Play([('KW', Armies(MARTELL, 0, 1, 0)), ('SB', Armies(MARTELL, 1, 0, 0)), ('ShSe', Armies(MARTELL, 1, 0, 0))], (Order(DEFEND, value=1), Order(RAID), Order(RAID))))

        map = Map()
        engine = Engine(map)

        engine.simulate_2_players(LANNISTER, plays1, GREYJOY, plays2)