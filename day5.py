import re
f = open("inputs/day5", "r")

STACKS = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
INSTRUCTIONS = [] #[(a,b,c) for a,b,c in re.findall("move (\d+) from (\d+) to (\d+)",f.read())]

for line in f.readlines():
    if "[" in line:
        for i in range(1,len(line),4):
            if line[i] != " ": 
                STACKS[(i // 4)+1].append(line[i])
    elif line[0] == "m":
        INSTRUCTIONS.append([(int(a),int(b),int(c)) for a,b,c in (re.findall("move (\d+) from (\d+) to (\d+)", line))][0])

def crane_operation(stack, instructions, mode = 0):
    for instruction in instructions:
        (nr_move,st1,st2) = (instruction[0],instruction[1],instruction[2])
        if mode == 0:
            for i in range(0,nr_move):
                stack[st2].insert(0,stack[st1].pop(0))
        elif mode == 1:
            for block in reversed([stack[st1].pop(0) for _ in range(0,nr_move) if len(stack[st1]) > 0]):
                stack[st2].insert(0,block)

    return ''.join([ stack[i][0] for i in range(1,len(stack)+1) if len(stack[i]) > 0])


print(crane_operation({key: value[:] for key, value in STACKS.items()},INSTRUCTIONS,0))
print(crane_operation({key: value[:] for key, value in STACKS.items()},INSTRUCTIONS,1))