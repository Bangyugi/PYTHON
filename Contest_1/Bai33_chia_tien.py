a, b, c, n = map(int, input().split())

sum = a + b + c + n

if sum % 3 == 0 and a < sum // 3 and b < sum // 3 and c < sum // 3:
    print("YES")
else:
    print("NO")
