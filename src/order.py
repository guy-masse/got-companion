from combi import *

RAID = 0
SUPPORT = 1
DEFEND = 2
MARCH = 3
CONSOLIDATE = 4


class Order:

    def __init__(self, type, value=0, star=False):
        self._type = type
        self._value = value
        self._star = star

    def get_name(self):
        if self._type == RAID:
            return 'RAID'
        elif self._type == SUPPORT:
            return 'SUPPORT'
        elif self._type == DEFEND:
            return 'DEFEND'
        elif self._type == MARCH:
            return 'MARCH'
        elif self._type == CONSOLIDATE:
            return 'CONSOLIDATE'

    def __str__(self):
        return '%s(%d)%s' % (self.get_name(), self._value, '*' if self._star else '')

    def type(self):
        return self._type

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._type == other._type and self._value == other._value and self._star == other._star
        else:
            return False

    def __key(self):
        return (self._type, self._value, self._star)

    def __hash__(self):
        return hash(self.__key())

    @classmethod
    def _get_nb_stars(cls, orders):
        out = 0
        for order in orders:
            if order._star:
                out += 1
        return out

    @classmethod
    def orders(cls, nb_terrain, nb_stars):
        """
        :param nb_terrain: number of terrain owned by the player
        :param nb_stars:  number of starred order available
        :return: a permutation of plausible orders for the given parameters
        """
        combinations = CombSpace(ORDERS, nb_terrain)
        for combination in combinations:
            if cls._get_nb_stars(combination) <= nb_stars:
                yield combination


ORDERS = [
    Order(RAID),
    Order(RAID),
    Order(RAID, star=True),
    Order(SUPPORT, value=0),
    Order(SUPPORT, value=0),
    Order(SUPPORT, value=1, star=True),
    Order(DEFEND, value=1),
    Order(DEFEND, value=1),
    Order(DEFEND, value=2, star=True),
    Order(MARCH, value=-1),
    Order(MARCH, value=0),
    Order(MARCH, value=1, star=True),
    Order(CONSOLIDATE),
    Order(CONSOLIDATE),
    Order(CONSOLIDATE, star=True)
]
