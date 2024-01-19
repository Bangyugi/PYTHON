from math import* 

def soChinhPhuong(n):
    can = isqrt(n)
    return can**2 == n

if __name__ == '__main__':
    n = int(input())
    print("YES" if soChinhPhuong(n) else "NO")

