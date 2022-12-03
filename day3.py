from string import ascii_letters
f = open("inputs/day3", "r")

DATA = [ rucksack.strip() for rucksack in f.readlines()]
print(sum([ ascii_letters.index((set(line[:len(line)//2]) & set(line[len(line)//2:])).pop())+1 for line in DATA]))
print(sum([ ascii_letters.index((set(DATA[x]) & set(DATA[x+1]) & set(DATA[x+2])).pop())+1 for x in range(0, len(DATA) - 1, 3)]))
