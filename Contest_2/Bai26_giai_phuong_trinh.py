a,b,n = map(int,input().split())


for i in range (0,10001):
    x = n-a*i
    if x/b>=0 and x%b==0:
        print("YES")
        exit()
    
print("NO")
