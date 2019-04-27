# Uses python3


def gcd(a, b):
    if b == 0:
        return a
    a1 = a % b
    return gcd(b, a1)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
