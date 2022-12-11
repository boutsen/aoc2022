import copy
import math
import re

f = open("inputs/test", "r")

DATA = f.read().split("\n\n")
MONKEYS = []

for monkey in DATA:
    info = [x.strip() for x in monkey.splitlines()]
    items = [int(x) for x in re.findall(r"(\d+)", info[1])]
    operation = re.findall(r"(\+|\*|\/|\-) (\d+|old)", info[2])[0]
    test = int(re.findall(r"(\d+)", info[3])[0])
    test_t = int(re.findall(r"(\d+)", info[4])[0])
    test_f = int(re.findall(r"(\d+)", info[5])[0])
    MONKEYS.append([items, operation, [test, test_t, test_f], 0])


def monkey_bizz(monkeys, rounds, control):
    for _ in range(rounds):
        for i in range(len(monkeys)):
            (op, val), test = monkeys[i][1], monkeys[i][2]
            monkeys[i][3] += len(monkeys[i][0])
            while len(monkeys[i][0]) > 0:
                item = monkeys[i][0].pop(0)
                item = eval(str(item) + op + str(item)) if val == "old" else eval(str(item) + op + val)
                item = item // 3 if control is None else item % control
                monkeys[test[1] if item % test[0] == 0 else test[2]][0].append(item)

    return math.prod(sorted([x[3] for x in monkeys])[-2:])


print(monkey_bizz(copy.deepcopy(MONKEYS), 20, None))
print(monkey_bizz(copy.deepcopy(MONKEYS), 10000, math.prod([x[2][0] for x in MONKEYS])))

