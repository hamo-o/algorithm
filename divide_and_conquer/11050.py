a, b = map(int, input().split())


def bino(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return bino(n-1, k-1)+bino(n-1, k)


print(bino(a, b))
