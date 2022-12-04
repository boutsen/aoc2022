import re
f = open("inputs/day4", "r")

DATA = [ (set(range(int(a),int(b)+1)),set(range(int(c),int(d)+1))) for a, b, c,d in re.findall(r"(\d+)-(\d+),(\d+)-(\d+)", f.read())]

print(len([ (a,b) for (a,b) in DATA if a.issubset(b) or b.issubset(a)]))
print(len([ (a,b) for (a,b) in DATA if not a.isdisjoint(b) or not b.isdisjoint(a)]))