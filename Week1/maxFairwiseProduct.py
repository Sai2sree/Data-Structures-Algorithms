# Uses python3


def mFP(lst, n):
    index = 0

    for i in range(1, n):
        if lst[i] > lst[index]:
            index = i
    lst[n-1], lst[index] = lst[index], lst[n-1]

    for i in range(0, n-1):
        if lst[i] > lst[index]:
            index = i
    lst[n-2], lst[index] = lst[index], lst[n-2]

    return lst[n-1]*lst[n-2]


if __name__ == "__main__":
    n = int(input())
    lst = [int(x) for x in input().split()]
    print(mFP(lst, n))
