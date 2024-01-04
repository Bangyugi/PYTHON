n = int(input())


temp = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(temp, end=" ")
        temp += 1
    print()
print()

for i in range(1, n + 1):
    temp = i
    for j in range(1, n + 1):
        print(temp, end=" ")
        temp += 1
    print()
print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j > n - i:
            print(i, end="")
        else:
            print("~", end="")
    print()
print()

for i in range(1, n + 1):
    id = n - 1
    temp = i
    for j in range(1, n + 1):
        if j <= i:
            print(temp, end=" ")
            temp += id
            id -= 1

    print()
print()
