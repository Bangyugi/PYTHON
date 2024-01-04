from math import *
n = int(input())
sum = 0
for i in range(n):
    sum+=1/factorial(i)

print("{:.4f}".format(sum))