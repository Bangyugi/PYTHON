n = input()

while len(n) >= 2:
    total = 0
    for i in n:
        total += int(i)
    n = str(total)

print(total)
