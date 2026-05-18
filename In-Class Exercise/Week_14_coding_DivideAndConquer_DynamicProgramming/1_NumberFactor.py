# Number Factor Problem in Python

def numberFactor(n):
    if n in (0,1,2): # only one way to express these numbers
        return 1
    elif n == 3: # {1,1,1} and {3} so 2 ways to express
        return 2
    else:
        subP1 = numberFactor(n-1)
        subP2 = numberFactor(n-3)
        subP3 = numberFactor(n-4)
        return subP1 + subP2 + subP3
    

print(numberFactor(15))
    
