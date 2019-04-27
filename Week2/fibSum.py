# Uses python3


def Fib(n):
    if n <= 1:
        return n
    F = [None]*(n+1)
    F[0] = 0
    F[1] = 1
    for i in range(2, len(F)):
        F[i] = F[i-1] + F[i-2]
    print(F[n])
    return F[n]


def fibSum(n):
    print((n+2) % 60)
    return (Fib((n+2) % 60) % 10)-1


if __name__ == "__main__":
    n = int(input())
    print(fibSum(n))
