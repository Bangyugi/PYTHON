from math import *

n = int(input())


a = []
for i in range(1, isqrt(n) + 1):
    if n % i == 0:
        a.append(i)
        if n // i != i:
            a.append(n // i)

print(len(a))
a.sort()
for i in a:
    print(i, end=" ")
