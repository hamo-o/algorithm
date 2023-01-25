n = int(input())


def memo_num():
    memo = [0]*(n+1)
    memo[1] = 1

    if n > 1:
        memo[2] = 2
        for i in range(3, n+1):
            memo[i] = (memo[i-2] + memo[i-1]) % 15746

    return memo[n]


print(memo_num())
