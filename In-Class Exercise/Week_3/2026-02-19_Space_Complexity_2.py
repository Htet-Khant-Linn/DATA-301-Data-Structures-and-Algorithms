# Space complexity O(1)
# Time complexity O(N)

def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        total = total + pair_sum(i, i+1)
    return total

def pair_sum(a,b):
    return a+b

print(pair_sum_sequence(3))