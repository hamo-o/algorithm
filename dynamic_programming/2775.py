t = int(input())


def memo_home(a, b):
    memo = [[0 for _ in range(b)] for _ in range(a+1)]

    for i in range(b):
        memo[0][i] = i+1

    for i in range(1, a+1):
        for j in range(b):
            if j == 0:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i][j-1] + memo[i-1][j]

    return memo[a][b-1]


for i in range(t):
    k = int(input())
    n = int(input())
    print(memo_home(k, n))






