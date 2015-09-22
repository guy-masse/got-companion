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

    def test_score(self):
        map = Map()

        map.set_armies('L', LANNISTER, 0, 1, 1)
        self.assertTrue(map.score_player(LANNISTER) == 3)

        map.set_armies('BI', LANNISTER, 1, 0, 0)
        self.assertTrue(map.score_player(LANNISTER) == 4)

        map.set_armies('IB', GREYJOY, 1, 0, 0)
        self.assertTrue(map.score_player(LANNISTER) == 4)

