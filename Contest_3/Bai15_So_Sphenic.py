from math import isqrt


def isSphenic(n):
    cnt = 0
    for i in range(2, isqrt(n) + 1):
        if cnt == 3:
            break
        if n % i == 0:
            cnt += 1
            n //= i
            if n % i == 0:
                return False

    if n != 1:
        cnt += 1
    return cnt == 3


if __name__ == "__main__":
    n = int(input())
    print(1 if isSphenic(n) else 0)
