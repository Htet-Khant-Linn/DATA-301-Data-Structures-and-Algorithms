import math

def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i-1
        while j >= 0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    return customList


def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList))) # Determine number of buckets = 3
    maxValue = max(customList) # Find the maximum value
    arr = [] # Create an empty list that will hold all buckets

    for i in range(numberofBuckets):
        arr.append([]) # Create 3 buckets inside the arr, [[], [], []]
    for j in customList:
        index_b = math.ceil(j*numberofBuckets/maxValue) # 1, 2, 3
        arr[index_b-1].append(j)

    for i in range(numberofBuckets):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(numberofBuckets): # 3
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList

cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]

print(bucketSort(cList))