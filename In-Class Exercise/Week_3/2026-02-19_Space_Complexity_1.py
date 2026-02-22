def sum(n):     # to test space complexity use run and debug
    if n <= 0:
        return 0
    return n + sum(n-1)

print(sum(3))