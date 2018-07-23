def extractEachKth(inputArray, k):
    a = inputArray.copy()
    for i in range(len(inputArray)):
        if (i+1)%k == 0:
            a.remove(inputArray[i])
    return a
