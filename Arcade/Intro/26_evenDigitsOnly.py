def evenDigitsOnly(n):
    for i in range(len(str(n))):
        if int(str(n)[i])%2 == 1: return False
    return True