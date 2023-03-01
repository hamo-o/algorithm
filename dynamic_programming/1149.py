n = int(input())

colors = []
for i in range(n):
    r, g, b = map(int, input().split())
    colors.append([r, g, b])


def memo_num():
    memo = [[0, 0, 0] for _ in range(n)]
    memo[0] = colors[0]

    for i in range(1, n):
        memo[i][0] = min(memo[i-1][1], memo[i-1][2]) + colors[i][0]
        memo[i][1] = min(memo[i-1][0], memo[i-1][2]) + colors[i][1]
        memo[i][2] = min(memo[i-1][0], memo[i - 1][1]) + colors[i][2]

    return min(memo[n-1])


print(memo_num())
