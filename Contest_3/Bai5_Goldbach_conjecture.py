from math import* 

def isPrime(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True

def solve1(n):
    for i in range(2, n//2+1):
        if isPrime(i) and isPrime(n-i):
            print(i,n-i)
        

if __name__ == '__main__':
    t = int(input())
    for i in range(0,t):
        n = int(input())
        solve1(n)
