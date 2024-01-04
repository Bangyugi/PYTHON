a, b, c = map(int, input().split())

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c and c == a:
        print(1)
    elif a == b or b == c or a == c:
        print(2)
    elif (
        (a * a + b * b == c * c) or (a * a + c * c == b * b) or (b * b + c * c == a * a)
    ):
        print(3)
    else:
        print(4)
else:
    print("INVALID")
