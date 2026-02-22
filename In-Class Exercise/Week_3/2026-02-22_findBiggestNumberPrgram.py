def findBiggestNumber(n):
    biggest_number = n[0]               # --------------> O(1)
    for i in range(1, len(n)):          # --------------> O(N)
        if n[i] > biggest_number:       # --------------> O(1)
            biggest_number = n[i]       # --------------> O(1)
    print(biggest_number)               # --------------> O(1)

# Time Complexity for the whole code -> O(N)
findBiggestNumber([1,2,3,44,5,66,7,8,9])

