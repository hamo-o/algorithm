things = []
n, k = map(int, input().split())
for _ in range(n):
    w, v = map(int, input().split())
    things.append([w, v])

memo = [[0 for _ in range(k+1)] for _ in range(n)]

# 현재 담을 수 있는 물건의 최대 인덱스 i, 현재 가방 허용 용량 j, 최대 가치 저장값
for i in range(n):
    for j in range(1, k+1):
        if things[i][0] > j:
            memo[i][j] = memo[i-1][j]
        else:
            memo[i][j] = max(memo[i-1][j], memo[i-1][j - things[i][0]] + things[i][1])

print(memo[n-1][k])
