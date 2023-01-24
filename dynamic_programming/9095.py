t = int(input())

memo = [0]*11
memo[1] = 1
memo[2] = 2
memo[3] = 4


def memo_count():
    if n > 3:
        for i in range(4, n+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

    return memo[n]


for i in range(t):
    n = int(input())
    print(memo_count())
