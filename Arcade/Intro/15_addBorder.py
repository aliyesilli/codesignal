def addBorder(picture):
    a = len(picture[0])
    for i in range(len(picture)):
        picture[i] = '*'+picture[i]+'*'
    return ['*'*(a+2)]+picture+['*'*(a+2)];