def arrayMaxConsecutiveSum(inputArray, k):
    a = set()
    for i in range(len(inputArray)-k+1):
        x = 0
        for j in range(k):
            x += inputArray[i+j]
        a.add(x)
    return max(a)
