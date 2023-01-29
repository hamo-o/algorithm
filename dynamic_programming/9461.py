memo = [0] * 101

memo[1] = 1
memo[2] = 1
memo[3] = 1
memo[4] = 2
memo[5] = 2

t = int(input())
for i in range(t):
    n = int(input())

    for i in range(6, n+1):
        memo[i] = memo[i-1] + memo[i-5]

    print(memo[n])
