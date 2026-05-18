def bubbleSort(customList):
    for i in range(len(customList)-1): # put the sorted element in the last place
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    print(customList)


# cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
cList = [5, 9, 3, 1, 2, 8, 4, 7, 6]

bubbleSort(cList)