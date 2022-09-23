#euler 7th
def isPrime(n: int):
    if n > 1:
        for i in range(2, int(n)):
            if n % i == 0:
                return 1  
        return 0
    else:
        return 1        
isPrime(1)
def nPrime(n: int):
    count = []
    for i in range(2, 200000):
        if isPrime(i) == 0:
            count.append(i)
    return count[n-1]

nPrime(10001) 