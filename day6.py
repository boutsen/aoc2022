f = open("inputs/day6", "r")

DATA = f.read()

def check_unique(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)):
            if(str[i] == str[j]):
                return False
    return True


def tuning(data,filter):
    for set in [data[i:i+filter] for i in range(0,len(DATA)-(filter-1))]:
        if check_unique(set):
            return data.index(set)+filter


print(tuning(DATA,4))
print(tuning(DATA,14))


