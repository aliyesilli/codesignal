def circleOfNumbers(n, firstNumber):
    a = ((n-2)/2)+1
    if firstNumber-a < 0:
        return firstNumber+a
    else:
        return firstNumber-a
