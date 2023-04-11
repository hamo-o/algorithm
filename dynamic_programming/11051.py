n, k = map(int, input().split())
memo = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(k+1):
        if i == j or j == 0:
            memo[i][j] = 1
        else:
            memo[i][j] = (memo[i-1][j-1]+memo[i-1][j]) % 10007

print(memo[n][k])
