t = int(input())

memo = [[0, 0] for _ in range(41)]
memo[0] = [1, 0]
memo[1] = [0, 1]


def memo_fibo():
    if n >= 1:
        for i in range(2, n+1):
            memo[i][0] = memo[i-1][0] + memo[i-2][0]
            memo[i][1] = memo[i-1][1] + memo[i-2][1]

    return memo[n]


for i in range(t):
    n = int(input())
    print(" ".join(map(str, memo_fibo())))
