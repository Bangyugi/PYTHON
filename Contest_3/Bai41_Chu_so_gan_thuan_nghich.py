from math import *

if __name__ == "__main__":
    n = input()
    m = n[1 : len(n) - 1]
    rm = m[::-1]
    if m == rm and (
        (int(n[0]) / int(n[len(n) - 1]) == 2) or (int(n[0]) / int(n[len(n) - 1]) == 0.5)
    ):
        print("YES")
    else:
        print("NO")
