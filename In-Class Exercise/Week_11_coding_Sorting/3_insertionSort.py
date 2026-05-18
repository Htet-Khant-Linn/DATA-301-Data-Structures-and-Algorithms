def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i-1
        while j >= 0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    print(customList)

cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
insertionSort(cList) 

# Initial List: [2, 1, 7, 6, 5, 3, 4, 9, 8]
# Pass 1 (i=1, key=1)
# j = 0
# j == 0 and 1 < 2:
#   customList[1] = customList[0] -> [2, 2, 7, 6, 5, 3, 4, 9, 8]
# j = -1
# Insert: customList[0] = key -> [1, 2, 7, 6, 5, 3, 4, 9, 8]