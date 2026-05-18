
# l = first index of the list
# m = middle index of the list
# r = last index of the list
# m = (l + (r-1))//2 (round down)
# [2, 1, 7, 6, 5, 3, 4, 9, 8]

def merge(customList, l, m, r): # l=0, r=8, m=(0 + (8-1))//2, 7//2, 3
    n1 = m - l + 1 # number of the first subarray = 3 - 0 +1 = 4
    n2 = r - m # number of the second subarray = 8 - 3 = 5

    L = [0] * (n1) # first subarray
    R = [0] * (n2) # second subarray

    for i in range(0, n1): # copy the element into the first subarray
        L[i] = customList[l+i] # l=0, i=0, -> 0, l=0, i=1, -> 2, ... n1

    for j in range(0, n2): # copy the element into the second subarray
        R[j] = customList[m+1+j] # 3+1+0=4, 3+1+1=5, ... n2

    i = 0 # initial index of the first subarray
    j = 0 # initial index of the second subarray
    k = l # inital index the merge subarray, k=0

    while i < n1 and j < n2: # 0 < 4 and 0 < 5
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1

    while i < n1: # copy the remaining element from the left side
        customList[k] = L[i]
        i += 1
        k += 1
    while j < n2: # copy the remaining element from the right side
        customList[k] = R[j]
        j += 1
        k += 1


def mergeSort(customList, l, r):
    if l < r :
        m = (l + (r-1)) // 2
        mergeSort(customList, l, m) # sort left side
        mergeSort(customList, m+1, r) # sort right side
        merge(customList, l, m, r)
    return customList

cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
print(mergeSort(cList, 0, 8))