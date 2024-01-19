from math import* 

def isPrime(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True

def solve1(n):
    for i in range(2,32):
        if isPrime(i) and isPrime(2**i-1):
            if (2**i-1)*(2**(i-1)) == n:
                return True
    return False

if __name__ == '__main__':
    n = int (input())
    print("YES" if solve1(n) else "NO")
