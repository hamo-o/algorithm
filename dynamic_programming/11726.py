n = int(input())


def memo_count():
    memo = [0]*(n+1)

    if n < 3:
        return n
    else:
        memo[1] = 1
        memo[2] = 2
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]

    return memo[n]


print(memo_count() % 10007)
