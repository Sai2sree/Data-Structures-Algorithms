# Uses python3


def Fib(n):
    if n <= 1:
        return n
    F = [None]*(n+1)
    F[0] = 0
    F[1] = 1
    for i in range(2, len(F)):
        F[i] = F[i-1] + F[i-2]
    return F[n]


if __name__ == "__main__":
    n = int(input())
    print(Fib(n))
