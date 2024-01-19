from math import *


def solve1(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True


def solve2(n):
    lastNumber = n % 10
    while n > 0:
        if n % 10 > lastNumber:
            return False
        n //= 10
    return True


if __name__ == "__main__":
    n = int(input())
    dem = 0
    for i in range(2, n + 1):
        if solve2(i) and solve1(i):
            print(i, end=" ")
            dem += 1
    print("\n",dem,sep="")
