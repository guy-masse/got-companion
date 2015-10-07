import unittest
import logging

from map import *

# Enable DEBUG level logging for this class
logger = logging.getLogger()
#logger.setLevel(logging.DEBUG)


class TestMap(unittest.TestCase):

    def test_neighbors(self):
        map = Map()

        klLandNeighbors = map.find_land_neighbor('KL')
        self.assertTrue(klLandNeighbors.__contains__('KW'))

        klWaterNeighbors = map.find_water_neighbor('KL')
        self.assertTrue(klWaterNeighbors.__contains__('BB'))
        self.assertFalse(klWaterNeighbors.__contains__('SB'))

    def test_set_armies(self):
        map = Map()

        self.assertIsNone(map.get_armies('L'))
        with self.assertRaises(MapError):
            map.set_armies('L', LANNISTER, 1, 0, 1)
        map.set_armies('L', LANNISTER, 0, 0, 1)
        self.assertIsNotNone(map.get_armies('L'))

        self.assertIsNone(map.get_armies('BB'))
        with self.assertRaises(MapError):
            map.set_armies('BB', LANNISTER, 0, 0, 1)
        map.set_armies('BB', LANNISTER, 1, 0, 0)
        self.assertIsNotNone(map.get_armies('BB'))

        map.set_armies('KL', LANNISTER, 0, 1, 1)
        map.set_armies('O', LANNISTER, 0, 0, 1)

        lannister_armies = map.get_armies_by_clan(LANNISTER)
        for k,v in lannister_armies:
            if k == 'O':
                self.assertEqual(1, v._knight)
            if k == 'KL':
                self.assertEqual(1, v._footmen)
                self.assertEqual(1, v._knight)
            if k == 'BB':
                self.assertEqual(1, v._ships)
            if k == 'L':
                self.assertEqual(1, v._knight)
                self.assertEqual(0, v._footmen)
                self.assertEqual(0, v._ships)
        self.assertEqual(4, len(lannister_armies))

    def test_radeable_neibhor(self):
        map = Map()

        map.set_armies('L', LANNISTER, 0, 1, 1)
        map.set_armies('GS', GREYJOY, 1, 0, 0)
        map.set_armies('Ri', GREYJOY, 0, 1, 1)
        greyjoyTargets = map.find_raideable_neighbors('L', LANNISTER)
        self.assertEqual(1, len(greyjoyTargets))
        self.assertEqual('Ri', greyjoyTargets[0])
        lannisterTargets = map.find_raideable_neighbors('GS', GREYJOY)
        self.assertEqual(1, len(lannisterTargets))
        self.assertEqual('L', lannisterTargets[0])

    def test_score(self):
        map = Map()

        map.set_armies('L', LANNISTER, 0, 1, 1)
        self.assertTrue(map.score_player(LANNISTER) == 3)

        map.set_armies('BI', LANNISTER, 1, 0, 0)
        self.assertTrue(map.score_player(LANNISTER) == 4)

        map.set_armies('IB', GREYJOY, 1, 0, 0)
        self.assertTrue(map.score_player(LANNISTER) == 4)

