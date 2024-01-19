from math import* 

def isPrime(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True

def tongChuSo(x):
    res = 0
    while x>0:
        res+=x%10
        x//=10
    return res

def thuaSoNguyenTo(n):
    res = 0
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            while n%i==0:
                res+=tongChuSo(i)
                n//=i
    if n!=1:
        res+=tongChuSo(n)
    return res



if __name__ == '__main__':
    n = int(input())
    if (not isPrime(n) and tongChuSo(n)==thuaSoNguyenTo(n)):
        print("YES")
    else:
        print("NO")
