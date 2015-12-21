from collections import namedtuple

WATER = 0
LAND = 1

CASTLE = 0
STRONGHOLD = 1

STARK = 0
GREYJOY = 1
LANNISTER = 2
BARATHEON = 3
TYRELL = 4
MARTELL = 5


Terrain = namedtuple('Terrain', ['supply', 'power', 'type', 'castle', 'fortification'])
Armies = namedtuple('Armies', ['clan', 'nb_ships', 'nb_footmen', 'nb_knights', 'nb_sieges'])


class Map:

    def __init__(self):
        self._names = { 'BI' : 'Bay of Ice',
                        'CB' : 'Castle Black',
                        'ShSe' : 'The Shivering Sea',
                        'K' : 'Karhold',
                        'StSh': 'The Stoney Shore',
                        'W' : 'Winterfell',
                        'WH' :'White Harbor',
                        'WW' : 'Widow s Watch',
                        'FF' : 'Flint s Finger',
                        'GW' : 'Greywater Watch',
                        'MC' : 'Moat Calin',
                        'NS' : 'The Narrow Sea',
                        'SuSe' : 'Sunset Sea',
                        'IB' : 'Ironman s Bay',
                        'Se' : 'Seagard',
                        'T' : 'The Twin',
                        'F' : 'The Fingers',
                        'P' : 'Pyke',
                        'MM' : 'The Mountains of the Moon',
                        'Ri' : 'Riverrun',
                        'E' : 'The Eyrie',
                        'GS' : 'The Golden Sound',
                        'L' : 'Lannisport',
                        'StSe' : 'Stoney Sept',
                        'Ha' : 'Harrenhal',
                        'CP' : 'Cracklaw Point',
                        'SB' : 'Shipbreaker Bay',
                        'SM' : 'Searoad Marches',
                        'Bl' : 'Blackwater',
                        'KL' : 'King s Landing',
                        'BB' : 'Blackwater Bay',
                        'D' : 'Dragonstone',
                        'WSS' : 'West Summer Sea',
                        'Hi' : 'Highgarden',
                        'Re' : 'The Reach',
                        'KW' : 'King s Wood',
                        'SE' : 'Storm s End',
                        'RS' : 'Redwyne Straight',
                        'O' : 'Oldtown',
                        'DM' : 'Dornish Marches',
                        'Bo' : 'The Boneway',
                        'SD' : 'Sea of Dorne',
                        'ESS' : 'East Summer Sea',
                        'A' : 'The Arbor',
                        '3T' : 'Three Towers',
                        'PP' : 'Prince s Path',
                        'St' : 'Starfall',
                        'Y' : 'Yronwood',
                        'Su' : 'Sunspear',
                        'SS' : 'Salt Shore'
                        }

        self._tiles = { 'BI' : Terrain(0, 0, WATER, None, False),
                            'CB' : Terrain(0, 1, LAND, None, False),
                            'ShSe' : Terrain(0, 0, WATER, None, False),
                            'K' : Terrain(0, 1, LAND, None, False),
                            'StSh' : Terrain(1, 0, LAND, None, False),
                            'W' : Terrain(1, 1, LAND, STRONGHOLD, True),
                            'WH' : Terrain(0, 0, LAND, CASTLE, False),
                            'WW' : Terrain(1, 0, LAND, None, False),
                            'FF' : Terrain(0, 0, LAND, CASTLE, False),
                            'GW' : Terrain(1, 0, LAND, None, False),
                            'MC' : Terrain(0, 0, LAND, CASTLE, False),
                            'NS' : Terrain(0, 0, WATER, None, False),
                            'SuSe' : Terrain(0, 0, WATER, None, False),
                            'IB' : Terrain(0, 0, WATER, None, False),
                            'Se' : Terrain(1, 1, LAND, STRONGHOLD, False),
                            'T' : Terrain(0, 1, LAND, None, False),
                            'F' : Terrain(1, 0, LAND, None, False),
                            'P' : Terrain(1, 1, LAND, STRONGHOLD, True),
                            'MM' : Terrain(1, 0, LAND, None, False),
                            'Ri' : Terrain(1, 1, LAND, STRONGHOLD, False),
                            'E' : Terrain(1, 1, LAND, CASTLE, False),
                            'GS' : Terrain(0, 0, WATER, None, False),
                            'L' : Terrain(2, 0, LAND, STRONGHOLD, True),
                            'StSe' : Terrain(0, 1, LAND, None, False),
                            'Ha' : Terrain(0, 1, LAND, CASTLE, False),
                            'CP' : Terrain(0, 0, LAND, CASTLE, False),
                            'SB' : Terrain(0, 0, WATER, None, False),
                            'SM' : Terrain(1, 0, LAND, None, False),
                            'Bl' : Terrain(2, 0, LAND, None, False),
                            'KL' : Terrain(0, 2, LAND, STRONGHOLD, False),
                            'BB' : Terrain(0, 0, WATER, None, False),
                            'D' : Terrain(1, 1, LAND, STRONGHOLD, True),
                            'WSS' : Terrain(0, 0, WATER, None, False),
                            'Hi' : Terrain(2, 0, LAND, STRONGHOLD, True),
                            'Re' : Terrain(0, 0, LAND, CASTLE, False),
                            'KW' : Terrain(1, 1, LAND, None, False),
                            'SE' : Terrain(0, 0, LAND, CASTLE, False),
                            'RS' : Terrain(0, 0, WATER, None, False),
                            'O' : Terrain(0, 0, LAND, STRONGHOLD, False),
                            'DM' : Terrain(0, 1, LAND, None, False),
                            'Bo' : Terrain(0, 1, LAND, None, False),
                            'SD' : Terrain(0, 0, WATER, None, False),
                            'ESS' : Terrain(0, 0, WATER, None, False),
                            'A' : Terrain(0, 1, LAND, None, False),
                            '3T' : Terrain(1, 0, LAND, None, False),
                            'PP' : Terrain(1, 1, LAND, None, False),
                            'St' : Terrain(1, 0, LAND, CASTLE, False),
                            'Y' : Terrain(0, 0, LAND, CASTLE, False),
                            'Su' : Terrain(1, 1, LAND, STRONGHOLD, True),
                            'SS' : Terrain(1, 0, LAND, None, False)
                          }

        self._graph = { 'BI' : ['W', 'CB', 'StSh', 'GW', 'FF'],
                        'CB' : ['W', 'K', 'BI', 'ShSe'],
                        'K' : ['CB', 'W', 'ShSe'],
                        'ShSe' : ['NS', 'CB', 'K', 'W', 'WH', 'WW'],
                        'StSh' : ['W', 'BI'],
                        'W' : ['StSh', 'CB', 'K', 'MC', 'WH', 'BI', 'ShSe'],
                        'WH' : ['W', 'MC', 'WW', 'ShSe', 'NS'],
                        'WW' : ['WH', 'ShSe', 'NS'],
                        'MC' : ['GW', 'W', 'WH', 'NS', 'T', 'Se'],
                        'FF' : ['BI', 'SuSe', 'IB', 'GW'],
                        'GW' : ['BI', 'IB', 'FF', 'Se', 'MC'],
                        'NS' : ['ShSe', 'WW', 'WH', 'MC', 'T', 'F', 'MM', 'E', 'CP', 'SB'],
                        'SuSe' : ['BI', 'IB', 'GS', 'WSS', 'FF', 'SM'],
                        'IB' : ['SuSe', 'P', 'FF', 'GW', 'Se', 'Ri'],
                        'Se' : ['IB', 'MC', 'GW', 'T', 'Ri'],
                        'T' : ['Se', 'MC', 'F', 'MM', 'NS'],
                        'F' : ['T', 'NS', 'MM'],
                        'MM' : ['T', 'F', 'E', 'NS', 'CP'],
                        'P' : ['IB'],
                        'Ri' : ['IB', 'Se', 'Ha', 'StSe', 'L', 'GS'],
                        'GS' : ['SuSe', 'IB', 'L', 'Ri','SM'],
                        'L' : ['GS', 'SM', 'Ri', 'StSe'],
                        'StSe' : ['L', 'Ri', 'Ha', 'Bl', 'SM'],
                        'Ha' : ['Ri', 'StSe', 'CP', 'Bl'],
                        'E' : ['MM', 'NS'],
                        'CP' : ['NS', 'Ha', 'Bl', 'KL', 'BB', 'SB'],
                        'SB' : ['NS', 'BB', 'D', 'KW', 'SE', 'ESS'],
                        'BB' : ['KL', 'CP', 'SB', 'KW'],
                        'SM' : ['GS', 'SuSe', 'WSS', 'Hi', 'Re', 'Bl', 'StSe', 'L'],
                        'Bl' : ['StSe', 'SM', 'Re', 'Ha', 'CP', 'KL'],
                        'KL' : ['Bl', 'CP', 'KW', 'BB', 'Re'],
                        'KW' : ['KL', 'BB', 'SB', 'SE', 'Re', 'Bo'],
                        'SE' : ['KW', 'SB', 'SD', 'Bo', 'ESS'],
                        'Hi' : ['SM', 'WSS', 'Re', 'DM', 'O', 'RS'],
                        'Re' : ['Hi', 'SM', 'Bl', 'KL', 'KW', 'Bo', 'DM'],
                        'WSS' : ['SuSe', 'RS', 'A', 'SM', 'Hi', '3T', 'S', 'ESS'],
                        'RS' : ['WSS', 'A', 'Hi', 'O', '3T'],
                        'O' : ['RS', '3T', 'Hi', 'DM'],
                        'DM' : ['O', 'Hi', 'Re', 'Bo', 'PP', '3T'],
                        'Bo' : ['DM', 'Re', 'KW', 'SE', 'SD', 'Y', 'PP'],
                        'SD' : ['Bo', 'SE', 'ESS', 'Su', 'Y'],
                        '3T' : ['O', 'RS', 'DM', 'PP', 'WSS'],
                        'PP' : ['3T', 'DM', 'Bo', 'Y', 'St'],
                        'Y' : ['PP', 'Bo', 'SD', 'Su', 'SS', 'St'],
                        'Su' : ['Y', 'SD', 'ESS', 'SS'],
                        'ESS' : ['SE', 'SD', 'Su', 'SS', 'St', 'WSS', 'SB'],
                        'St' : ['WSS', 'PP', 'Y', 'SS', 'ESS'],
                        'SS' : ['St', 'Y', 'Su', 'ESS']
                      }

        self._armies = {}

    def remove_armies(self, code):
        self._armies.pop(code)

    def set_armies(self, code, clan, nb_ships=0, nb_footmen=0, nb_knights=0, nb_sieges=0):
        # make sure the tile can accept the given army
        if nb_ships != 0 and self._tiles[code].type == LAND:
            raise MapError('Cannot place ships on a land tile')
        if nb_footmen + nb_knights != 0 and self._tiles[code].type == WATER:
            raise MapError('Cannot place footman or knights on a water tile')

        self._armies[code] = Armies(clan, nb_ships, nb_footmen, nb_knights, nb_sieges)

    def get_armies(self, code):
        if code in self._armies.keys():
            return self._armies.get(code)
        else:
            return None

    # Returns a Set of tuple (terrainCode : String, army : Armies) for all armies of the given clan
    def get_armies_by_clan(self, clan):
        armies = set()
        for k,v in self._armies.iteritems():
            if v.clan == clan:
                armies.add((k, v))
        return armies

    def find_neighbors(self, code, type):
        out = []
        neighbors = self._graph[code]
        for neighbor in neighbors:
            terrain = self._tiles[neighbor]
            if terrain.type == type:
                out.append(neighbor)

        return out

    def find_land_neighbor(self, code):
        return self.find_neighbors(code, LAND)

    def find_water_neighbor(self, code):
        return self.find_neighbors(code, WATER)

    # Return an array of the tile codes where this clan could raid an opposing army
    def find_raideable_neighbors(self, code, raidingClan):
        out = []
        tile = self._tiles[code]
        candidateTiles = []
        if tile.type == WATER:
            candidateTiles.extend(self.find_water_neighbor(code))
            candidateTiles.extend(self.find_land_neighbor(code))
        else:
            candidateTiles.extend(self.find_land_neighbor(code))
        for candidate in candidateTiles:
            army = self.get_armies(candidate)
            if army is not None and army.clan != raidingClan:
                out.append(candidate)
        return out

    def get_tile(self, code):
        return self._tiles[code]

    def score_player(self, clan):
        score = 0
        for code, army in self._armies.iteritems():
            if army.clan == clan:
                tile = self._tiles[code]
                score += 1 if tile.castle is None else tile.castle + 2
        return score


class MapError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
