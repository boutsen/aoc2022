import re
f = open("inputs/day7", "r")

filesystem = {"/": 0}
working_dir = ""

for line in [ line.strip() for line in f.readlines()[1:] ]:
    if line == "$ cd ..":
        working_dir = working_dir[:working_dir.rindex('/')]
    elif '$ cd' in line:
        working_dir = working_dir + '/' + line.split(' ')[2]
        filesystem[working_dir] = 0
    elif re.match("\d+ .*",line):
        size = int(line.split(' ')[0])
        filesystem["/"] += size
        reverse_dir = working_dir
        while reverse_dir:
            filesystem[reverse_dir] += size
            reverse_dir = reverse_dir[:reverse_dir.rindex('/')] if '/' in reverse_dir else ""

print(sum([v for v in filesystem.values() if v <= 100000]))
minimum_to_free = filesystem["/"] + 30000000 - 70000000
print(min([x for x in sorted(filesystem.values()) if x - minimum_to_free > 0]))