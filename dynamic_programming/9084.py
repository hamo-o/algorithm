import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    # memo[i] = k i원을 만들 수 있는 방법의 수 k개
    memo = [0 for _ in range(10001)]
    memo[0] = 1

    for coin in coins:
        for j in range(coin, m+1):
            memo[j] += memo[j-coin]

    print(memo[m])
