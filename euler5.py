#Answer to eulers fifth problem

def smallestNum(n: int):
    
    for i in range(10000000000):
        for j in range(1, n):
            if i % j != 0:
                i += 1
            else:
                j += 1
    print(i)
    return i

smallestNum(10)