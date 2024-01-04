n = int(input())

y = n // 365
m = (n % 365) // 7
d = n % 365 % 7

print(y, m, d)
