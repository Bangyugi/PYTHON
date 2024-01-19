from math import *


if __name__ == "__main__":
    a,b = map(int,input().split())
    cana=ceil(sqrt(a))
    canb = isqrt(b)

    cnt=0
    for i in range(cana,canb+1):
        cnt+=1
    print(cnt)
    
