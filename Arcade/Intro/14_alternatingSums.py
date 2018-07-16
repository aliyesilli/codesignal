def alternatingSums(a):
    a1 = 0
    a2 = 0
    b = []
    for i in range(0,len(a),2):
        a1 += a[i]
    b.append(a1)
    for i in range(1,len(a),2):
        a2 += a[i]
    b.append(a2)
    return b;