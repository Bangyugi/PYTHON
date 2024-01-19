from math import *


def solve(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            if n != 1:
                print(i, "^", cnt, end=" * ", sep="")
            else:
                print(i, "^", cnt, sep="")
    if n != 1:
        print(n, "^", 1 ,sep="")


if __name__ == "__main__":
    n = int(input())
    solve(n)
