a, b, c, d = map(int, input().split())
q = b / a
if b * q == c and c * q == d:
    print("YES")
else:
    print("NO")
