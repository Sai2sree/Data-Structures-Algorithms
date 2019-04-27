# Uses python3


def LastDigitOfFibSeq(n):
    F = [None]*(n+1)
    F[0] = 0
    F[1] = 1
    for i in range(2, len(F)):
        F[i] = (F[i-1] + F[i-2]) % 10
    return int(F[n] % 10)


if __name__ == "__main__":
    n = int(input())
    print(LastDigitOfFibSeq(n))
