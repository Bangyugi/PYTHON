from math import *

a, b, c = map(float, input().split())

if a == 0:
    if b == 0:
        if c == 0:
            print("VO SO NGHIEM")
        else:
            print("VO NGHIEM")
    else:
        if c == 0:
            print("{:.2f}".format(0))
        else:
            print("{:.2f}".format((-c / b)))
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("VO NGHIEM")
    elif delta > 0:
        print(
            "{:.2f}".format((-b - sqrt(delta)) / (2 * a)),
            "{:.2f}".format((-b + sqrt(delta)) / (2 * a)),
        )
