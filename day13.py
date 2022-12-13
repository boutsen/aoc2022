f = open("inputs/day13", "r")

DATA = [tuple(map(eval, line.split("\n"))) for line in f.read().split("\n\n")]


def compare(left, right):
    n1, n2 = len(left), len(right)
    for i in range(max(n1, n2)):
        if i >= n1: return True
        elif i >= n2: return False

        (l, r) = (left[i], right[i])
        if type(l) is int and type(r) is int:
            if l < r: return True
            elif l > r: return False
        else:
            res = compare([l] if type(l) is int else l, [r] if type(r) is int else r)
            if res is not None: return res


print(sum([(i+1) for i, (l, r) in enumerate(DATA) if compare(l, r)]))


def sort(l):
    n = len(l)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if compare(l[j + 1], l[j]): l[j], l[j + 1] = l[j + 1], l[j]


L1, L2 = zip(*DATA)
PART2 = list(L1+L2+([[2]], [[6]]))
sort(PART2)
print((PART2.index([[2]])+1)*(PART2.index([[6]])+1))
