n = int(input())


dem = 0
while n > 0:
    dem += n % 10
    n //= 10
print(dem)
