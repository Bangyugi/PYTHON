from math import *

n = int(input())
a = []

if n < 2:
    print(-1)
else:
    if n % 2 == 0:
        a += [2] * (n // 2)
    else:
        a += [2] * ((n - 3) // 2) + [3]
    print(len(a))
    for i in a:
        print(i, end=" ")
