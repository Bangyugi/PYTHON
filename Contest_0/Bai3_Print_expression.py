a = list(map(int, input().split()))
x, y, z, t = a

print(y, z, x, t, sep=",")
print(sum(a))
print(x - y + z * t)
