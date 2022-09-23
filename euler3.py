#3 final final extra final
#600851475143

num = int(input("Enter a number\n"))
def isPrime(n: int):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    else: return False


def largePrime(num):
    for i in reversed(range(2,num)):
        if num % i == 0 and isPrime(i):
            return i

(largePrime(num))