n = int(input())
res = 0
for i in range(0, n + 1):
    if i % 3 == 0:
        res += i

print(res)
