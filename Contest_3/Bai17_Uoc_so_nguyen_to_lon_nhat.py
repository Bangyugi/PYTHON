from math import* 

def solve(x):
    res=0
    for i in range(2,isqrt(x)+1):
        if x%i==0:
            res=max(res,i)
            while x%i==0:
                x//=i
    if x!=1:
        res = max(res,x)
    return res


if __name__ == '__main__':
    n= int(input())
    for i in range(0,n):
        x=int(input())
        print(solve(x))
