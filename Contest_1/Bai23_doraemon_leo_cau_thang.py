from math import *

n, m = map(int, input().split())

x = ceil(n / 2)
y = n
if m > n:
    print(-1)
else:
    print(ceil(x / m) * m)
