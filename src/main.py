from combi import *
from map import *
from order import *
from engine import *


if __name__ == "__main__":
    map = Map()
    engine = Engine(map)

    map.set_armies('L', LANNISTER, 0, 1, 1)
    map.set_armies('StSe', LANNISTER, 0, 1, 0)

    map.set_armies('Ri', GREYJOY, 0, 1, 1)
    map.set_armies('Ha', GREYJOY, 0, 1, 0)

    plays1 = engine.possible_plays(LANNISTER, 0)
    plays2 = engine.possible_plays(GREYJOY, 0)
    # for play in plays:
    #     print play
    # print len(plays)
    print len(plays1)
    print len(plays2)

    engine.simulate_2_players(LANNISTER, plays1, GREYJOY, plays2)
