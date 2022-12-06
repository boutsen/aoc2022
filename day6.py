f = open("inputs/day6", "r")

DATA = f.read()

def tuning2(data,filter):
    for i in range(0,len(data)-(filter-1)):
        if( len(set(data[i:i+filter])) == filter):
            return i+filter

print(tuning2(DATA,4))
print(tuning2(DATA,14))
