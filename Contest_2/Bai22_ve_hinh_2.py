n = int(input())


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= i:
            print("*", sep="", end="")
    print()
print()


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= n - i + 1:
            print("*", sep="", end="")
    print()
print()


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j > n - i:
            print("*", sep="", end="")
        else:
            print(" ", sep="", end="")
    print()
print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j >= i:
            print("*", sep="", end="")
        else:
            print(" ", sep="", end="")
    print()
print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == 1 or j == i or i == n:
            print("*", sep="", end="")
        else:
            print(" ", sep="", end="")
    print()
print()
