n = int(input())
li = list(map(int, input().split()))
memo = [0]*n
memo[0] = li[0]
temp = 0

for i in range(0, n):
    if li[i] <= 0:
        temp = max(temp+li[i], 0)
        if i > 0:
            memo[i] = max(memo[i-1], li[i])
    else:
        temp += li[i]
        memo[i] = max(memo[i-1], temp)

print(memo[n-1])
