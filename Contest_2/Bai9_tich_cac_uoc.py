from math import *

n = int(input())

res = 1
for i in range(1, isqrt(n) + 1):
    if n % i == 0:
        res *= i
        if n // i != i:
            res *= n // i

print(res)
