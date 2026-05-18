# Number Factor Problem using Dynamic Programming in Python
# Top Down Approach

def numberFactor(n, tempDict):
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    else:
        if n not in tempDict:
            subP1 = numberFactor(n-1, tempDict)
            subP2 = numberFactor(n-3, tempDict)
            subP3 = numberFactor(n-4, tempDict)
            tempDict[n] = subP1 + subP2 + subP3
        return tempDict[n]
    

print(numberFactor(5, {}))