from math import *

a1, a2, a3, b1, b2, b3 = map(int, input().split())
n = int(input())

a = a1 + a2 + a3
b = b1 + b2 + b3

ab = ceil(a / 5) + ceil(b / 10)

if ab <= n:
    print("YES")
else:
    print("NO")
