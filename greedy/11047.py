n, k = map(int, input().split())
coins = []
cnt = 0

for i in range(n):
    coins.append(int(input()))

for i in range(n):
    cnt += k // coins[n-i-1]
    k %= coins[n-i-1]

print(cnt)
