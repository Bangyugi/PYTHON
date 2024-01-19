n = int(input())
numbers = list(map(int,input().split()))
res = 0
for i in numbers:
    if i%2==0:
        res+=i

print(res)