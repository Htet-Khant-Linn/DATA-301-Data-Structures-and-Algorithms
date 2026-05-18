# Number Factor Problem using Dynamic Programming in Python
# Bottom Up Approach

def numberFactorBU(n):
    tempArr = [1,1,1,2]
    for i in range(4, n+1):
        tempArr.append(tempArr[i-1] + tempArr[i-3] + tempArr[i-4])
    return tempArr[n]

print(numberFactorBU(5))