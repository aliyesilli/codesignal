def absoluteValuesSumMinimization(a):
    s = []
    for i in range(len(a)):
        b = 0
        for j in range(len(a)):
            b += abs(a[j] - a[i])
        s.append([b,a[i]])
    return sorted(s)[0][1]