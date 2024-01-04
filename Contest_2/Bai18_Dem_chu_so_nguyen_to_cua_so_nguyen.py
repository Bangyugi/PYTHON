n = int(input())


dem = 0
while n > 0:
    if n % 10 == 2 or n % 10 == 3 or n % 10 == 5 or n % 10 == 7:
        dem += 1
    n //= 10
print(dem)
