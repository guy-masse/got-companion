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

    def test_simulate_interleaving(self):
        # Play already ordered
        plays1 = Play([('KL', Armies(BARATHEON, 0, 0, 1)), ('BB', Armies(BARATHEON, 2, 0, 0)), ('NS', Armies(BARATHEON, 1, 0, 0))], (Order(MARCH, value=0), Order(SUPPORT, value=0), Order(RAID)))
        plays2 = Play([('KW', Armies(MARTELL, 0, 1, 0)), ('SB', Armies(MARTELL, 1, 0, 0)), ('ShSe', Armies(MARTELL, 1, 0, 0))], (Order(DEFEND, value=1), Order(RAID), Order(RAID)))

        map = Map()
        engine = Engine(map)

        raidSubSequences = engine.interleaving_of_plays_2_players(RAID, BARATHEON, plays1, MARTELL, plays2)

        self.assertEqual(2, len(raidSubSequences), 'Given plays provides 2 possibles interleaving of raid orders since player 2 has 2 raids')
        self.assertEqual(3, len(raidSubSequences[0]))
        self.assertEqual(3, len(raidSubSequences[1]))
        self.assertEqual(BARATHEON, raidSubSequences[0][0]._clan, 'Staring player is BARATHEON in this setup')
        self.assertEqual(MARTELL, raidSubSequences[0][1]._clan, 'Second player is MARTELL in this setup')
        self.assertEqual(MARTELL, raidSubSequences[0][2]._clan, 'Third player is MARTELL in this setup, BARATHEON only had one raid order')

        plays3 = Play([('KL', Armies(BARATHEON, 0, 0, 1)), ('BB', Armies(BARATHEON, 2, 0, 0)), ('NS', Armies(BARATHEON, 1, 0, 0))], (Order(MARCH, value=0), Order(RAID), Order(RAID)))
        raidSubSequences = engine.interleaving_of_plays_2_players(RAID, BARATHEON, plays3, MARTELL, plays2)

        self.assertEqual(4, len(raidSubSequences), 'Given plays provides 4 possibles interleaving of raid orders since both players have 2 raids')
        self.assertEqual(4, len(raidSubSequences[0]), 'each interleaving has 4 orders')
        self.assertEqual(4, len(raidSubSequences[1]), 'each interleaving has 4 orders')
        self.assertEqual(4, len(raidSubSequences[2]), 'each interleaving has 4 orders')
        self.assertEqual(4, len(raidSubSequences[3]), 'each interleaving has 4 orders')

    def test_simulate_root_sequences(self):
        # Available Plays
        plays1 = set()
        plays1.add(Play([('KL', Armies(BARATHEON, 0, 0, 1)), ('BB', Armies(BARATHEON, 2, 0, 0))], (Order(MARCH, value=0), Order(SUPPORT, value=0))))
        plays1.add(Play([('KL', Armies(BARATHEON, 0, 0, 1)), ('BB', Armies(BARATHEON, 2, 0, 0))], (Order(MARCH, value=1), Order(RAID, value=0))))
        plays2 = set()
        plays2.add(Play([('KW', Armies(MARTELL, 0, 1, 0)), ('SB', Armies(MARTELL, 1, 0, 0)), ('ShSe', Armies(MARTELL, 1, 0, 0))], (Order(DEFEND, value=1), Order(RAID), Order(RAID))))
        plays2.add(Play([('KW', Armies(MARTELL, 0, 1, 0)), ('SB', Armies(MARTELL, 1, 0, 0)), ('ShSe', Armies(MARTELL, 1, 0, 0))], (Order(DEFEND, value=2), Order(SUPPORT, value=1), Order(RAID))))
        plays2.add(Play([('KW', Armies(MARTELL, 0, 1, 0)), ('SB', Armies(MARTELL, 1, 0, 0)), ('ShSe', Armies(MARTELL, 1, 0, 0))], (Order(MARCH, value=1), Order(MARCH), Order(RAID))))

        map = Map()
        engine = Engine(map)

        rootMoveSequences = engine.simulate_2_players(BARATHEON, plays1, MARTELL, plays2)
        self.assertEqual(6, len(rootMoveSequences))
        countBaratheon = (0, 0, 0)
        countMartell = (0, 0, 0)
        for (raids, marches, consolidates) in rootMoveSequences.itervalues():
            for orders in raids:
                for order in orders:
                    if order._clan == BARATHEON:
                        countBaratheon = (countBaratheon[0] + 1, countBaratheon[1], countBaratheon[2])
                    else:
                        countMartell = (countMartell[0] + 1, countMartell[1], countMartell[2])
            for orders in marches:
                for order in orders:
                    if order._clan == BARATHEON:
                        countBaratheon = (countBaratheon[0], countBaratheon[1] + 1, countBaratheon[2])
                    else:
                        countMartell = (countMartell[0], countMartell[1] + 1, countMartell[2])
            for orders in consolidates:
                for order in orders:
                    if order._clan == BARATHEON:
                        countBaratheon = (countBaratheon[0], countBaratheon[1], countBaratheon[2] + 1)
                    else:
                        countMartell = (countMartell[0], countMartell[1], countMartell[2] + 1)

        self.assertEqual(4, countBaratheon[0])
        self.assertEqual(8, countBaratheon[1])
        self.assertEqual(0, countBaratheon[2])
        self.assertEqual(12, countMartell[0])
        self.assertEqual(8, countMartell[1])
        self.assertEqual(0, countMartell[2])
