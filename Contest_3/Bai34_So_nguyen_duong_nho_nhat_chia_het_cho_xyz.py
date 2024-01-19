from math import *


def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def LCM(a, b):
    return (a * b) // GCD(a, b)


if __name__ == "__main__":
    x, y, z, n = map(int, input().split())
    r1 = LCM(x, LCM(y, z))
    temp = 10 ** (n - 1)
    ans = (temp + r1 - 1) // r1 * r1
    if ans >= 10**n:
        print(-1)
    else:
        print(ans)
