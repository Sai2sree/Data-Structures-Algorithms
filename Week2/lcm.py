# Uses python3


def gcd(a, b):
    if b == 0:
        return a
    a1 = a % b
    return gcd(b, a1)


def lcm(a, b):
    return int((a//gcd(a, b))*b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm(a, b))
