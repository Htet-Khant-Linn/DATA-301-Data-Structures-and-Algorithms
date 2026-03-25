# def powerofTwo(n):
#     if n==0:
#         return 1
#     else:
#         power = powerofTwo(n-1)
#         return power * 2
    
def powerofTwo(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power
    
print(powerofTwo(4))