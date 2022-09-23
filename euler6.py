#euler 6

def sumOfSquare():
    sum = 0
    for i in range(101):
        i = i ** 2
        sum += i
    return sum

def squareOfSum():
    sum = 0
    for i in range(101):
        sum += i
    print(sum)
    print(sum ** 2)
    return sum ** 2

squareOfSum() #25502500

def differeceOfSquares():
    return squareOfSum() - sumOfSquare()


differeceOfSquares()