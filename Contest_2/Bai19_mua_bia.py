n = int(input())
n //= 28
dem = n
while n >= 3:
    x = n // 3
    dem += x
    n %= 3
    n += x


print(dem)
