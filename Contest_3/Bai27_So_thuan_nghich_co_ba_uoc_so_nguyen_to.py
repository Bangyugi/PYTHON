from math import *


def check(n):
    cnt = 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            cnt += 1
            while n % i == 0:
                n //= i
    if n != 1:
        cnt += 1
    return cnt >= 3


if __name__ == "__main__":
    a, b = map(int, input().split())
    ok = False
    for i in range(a, b + 1):
        x = str(i)
        y = x[::-1]
        if x == y and check(i):
            ok = True
            print(i, end=" ")
    if ok == False:
        print(-1)
