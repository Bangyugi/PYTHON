from math import *

a, b, k = map(int, (input().split()))

temp = ceil(k / 2)

print(temp * a - (k - temp) * b)
