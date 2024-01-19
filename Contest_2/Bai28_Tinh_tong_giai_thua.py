n = int(input())
res = 1
for i in range(n, 1, -1):
    res = 1 + i * (res)
print(res)
