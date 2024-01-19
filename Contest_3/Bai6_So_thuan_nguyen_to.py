from math import *


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def solve1(n):
    while n > 0:
        r = n % 10
        if r != 2 and r != 3 and r != 5 and r != 7:
            return False
        n //= 10
    return True


def solve2(n):
    dem = 0
    while n > 0:
        dem += n % 10
        n //= 10
    return isPrime(dem)


if __name__ == "__main__":
    a, b = map(int, input().split())
    dem = 0
    for i in range(a, b + 1):
        if solve2(i) and solve1(i) and isPrime(i):
            dem += 1
    print(dem)
