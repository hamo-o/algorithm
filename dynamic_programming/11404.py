import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = float("inf")

memo = [[INF for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    memo[a-1][b-1] = min(c, memo[a-1][b-1])

for i in range(n):
    for j in range(n):
        if i == j:
            memo[i][j] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            memo[i][j] = min(memo[i][j], memo[i][k]+memo[k][j])

for i in range(n):
    for j in range(n):
        if memo[i][j] == INF:
            memo[i][j] = 0

for line in memo:
    print(" ".join(map(str, line)))
