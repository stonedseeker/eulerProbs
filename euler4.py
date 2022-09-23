#fourth euler prob made more efficient

def isPalindrome(a: int):
    a = str(a)
    l = len(a)
    flag = False
    for i in range(l):
        if a[i] == a[l - 1 - i]:
            flag = True
        else: 
            return False
    return flag

def maxthreepalindrome():
    for i in range(999,900,-1):
        for j in range(998,900,-1):
            ans = i * j
            if isPalindrome(ans):
                return ans

maxthreepalindrome()