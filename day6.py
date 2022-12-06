f = open("inputs/day6", "r")

DATA = f.read()

def tuning(data,filter):
    for i in range(0,len(data)-(filter-1)):
        if( len(set(data[i:i+filter])) == filter):
            return i+filter

print(tuning(DATA,4))
print(tuning(DATA,14))
