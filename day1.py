f = open("inputs/day1", "r")

DATA = [[int(calories) for calories in elf.split("\n")] for elf in f.read().split("\n\n")]
calories_carried = [sum(cal) for cal in DATA]

print(max(calories_carried))
print(sum(sorted(calories_carried, reverse=True)[0:3]))
