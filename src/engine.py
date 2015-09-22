import copy
from combi import *
from map import *
from order import *


class Play:
    def __init__(self, terrain, orders):
        self._terrain = terrain
        self._orders = orders

    def __str__(self):
        out = []
        for x in range(0, len(self._terrain)):
            out.append('%s:%s' % (self._terrain[x], self._orders[x]))
        return ','.join(out)

    def get_plays_of_type(self, type):
        plays = []
        for x in range(0, len(self._orders)):
            if self._orders[x].type() == type:
                plays.append((self._terrain[x], self._orders[x]))
        return plays

    def __len__(self):
        return len(self._orders)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._orders == other._orders and self._terrain == other._terrain
        else:
            return False

    def __key(self):
        return (tuple(self._terrain), self._orders)

    def __hash__(self):
        return hash(self.__key())

class Move:

    def __init__(self, clan, order, startTerrain, destTerrain):
        self._clan = clan
        self._order = order
        self._start = startTerrain
        self._destination = destTerrain


class Engine:

    def __init__(self, map):
        self._map = map

    def can_play(self, order, tile):
        if order.type() == CONSOLIDATE and tile.type() == WATER:
            return False
        return True

    def possible_plays(self, terrain, nbStar):
        possible_plays = set()

        orders = Orders(len(terrain), nbStar)
        for option in orders._options:
            # TODO Optimization : remove senseless random pick (March -1 when March 0 was not picked... and such)

            # see all possible permutation of the orders
            permutations = PermSpace(tuple(option))
            for permutation in permutations:
                issue = False

                # find out if the terrain may play this order
                for i in range(0, len(terrain)):
                    if not self.can_play(permutation[i], self._map.get_tile(terrain[i])):
                        issue = True
                if not issue:
                    possible_plays.add(Play(terrain, tuple(permutation)))

        return possible_plays

    def simulate_2_players(self, clan1, playsP1, clan2, playsP2):
        initialScore1 = self._map.score_player(clan1)
        initialScore2 = self._map.score_player(clan2)

        for play1 in playsP1:
            for play2 in playsP2:

                # Create all move sequences
                moveSequences = []


                #  Raid
                #   ex: Play1 = GS:RAID(0), Ha:DEFENSE(1), L:MARCH(0)
                #       Play2 = StSe:RAID(0), CP:RAID(0), Ri:MARCH(0)
                #
                raid1 = play1.get_plays_of_type(RAID)
                raid2 = play2.get_plays_of_type(RAID)

                #       raid1 = GS:RAID(0)
                #       raid2 = StSe:RAID(0), CP:RAID(0)

                if len(raid1) > 0 and len(raid2) > 0:
                    raid1Permutations = PermSpace(raid1)
                    raid2Permutations = PermSpace(raid2)
                    # raidPermission1 = [GS:RAID(0)]
                    # raidPermission2 = [(StSe:RAID(0), CP:RAID(0)), (CP:RAID(0), StSe:RAID(0))]
                    for raid1Permutation in raid1Permutations:
                        for raid2Permutation in raid2Permutations:
                            sequence = []
                            i = 0
                            while i < max(len(raid1Permutation), len(raid2Permutation)):
                                if i < len(raid1Permutation):
                                    sequence.append(raid1Permutation[i])
                                if i < len(raid2Permutation):
                                    sequence.append(raid2Permutation[i])
                                i += 1
                                # all possible sequence of alternative plays between 2 players, for raid commands
                                # sequence = [L/GS:RAID(0), GJ/StSe:RAID(0), GJ/CP:RAID(0); L/GS:RAID(0), GJ/CP:RAID(0), GJ/StSe:RAID(0)]
                                # this must be duplicated for each potential target of the command


                elif len(raid1) > 0:
                    raid1Permutations = PermSpace(raid1)
                    for raid1Permutation in raid1Permutations:
                        print tuple(raid1Permutation)
                elif len(raid2) > 0:
                    raid2Permutations = PermSpace(raid2)
                    for raid2Permutation in raid2Permutations:
                        print tuple(raid2Permutation)

                #  March



                # Consolidate


                print '%s <> %s' % (play1, play2)
        return

