f = open("inputs/day2", "r")

DATA = [move.strip().replace(" ", "") for move in f.readlines()]
STRAT_GUIDE_1 = {'AX': 4, 'AY': 8, 'AZ': 3, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 7, 'CY': 2, 'CZ': 6}
STRAT_GUIDE_2 = {'AX': 3, 'AY': 4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7}

print(sum([STRAT_GUIDE_1[pair] for pair in DATA]))
print(sum([STRAT_GUIDE_2[pair] for pair in DATA]))
