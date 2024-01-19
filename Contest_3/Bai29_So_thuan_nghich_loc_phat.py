from math import *


def solve1(n):
    while n > 0:
        if n%10==6:
            return True
        n //= 10
    return False

def solve2(n):
    tong=0
    while n>0:
        tong+=n%10
        n//=10
    return tong%10==8


if __name__ == "__main__":
    a,b = map(int, input().split()) 
    for i in range(a,b+1):
        x = str(i)
        y = x[::-1]
        if x==y and solve1(i) and solve2(i):
            print(i,end=" ")

