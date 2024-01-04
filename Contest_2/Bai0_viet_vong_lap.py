n = int(input())

for i in range(1, n + 1):
    print(i, end=" ")

print()
for i in range(n, -1, -1):
    print(i, end=" ")

print()

for i in range(0, n + 1):
    if i % 2 == 0:
        print(i, end=" ")

print()
for i in range(0, n + 1):
    if i % 2 == 1:
        print(i, end=" ")

print()

for i in range(0, n):
    if i % 4 == 0:
        print(i, end=" ")

print()
s = "a"
for i in range(0, n):
    print(chr(ord(s) + i), end=" ")

print()
for i in range(123 - n, 123):
    print(chr(i), end=" ")
