def arrayChange(inputArray):
    a = inputArray[:]
    b = 0
    for i in range(1,len(a)):
        if a[i] <= a[i-1]:
            b += abs(a[i-1]+1-a[i])
            a[i] = a[i-1]+1
    return b;